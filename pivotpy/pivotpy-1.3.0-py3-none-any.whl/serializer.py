import os
import json
import pickle
from collections import namedtuple
from contextlib import suppress

import numpy as np


def dict2tuple(name,d):
    """Converts a dictionary (nested as well) to namedtuple, accessible via index and dot notation as well as by unpacking.
    - **Parameters**
        - name: Name of the tuple.
        - d   : Dictionary, nested works as well.
    """
    return namedtuple(name,d.keys())(
           *(dict2tuple(k.upper(),v) if isinstance(v,dict) else v for k,v in d.items())
           )

class Dict2Data:
    _req_keys = ()
    _subclasses = ()
    """
    - Returns a Data object with dictionary keys as attributes of Data accessible by dot notation or by key. Once an attribute is created, it can not be changed from outside.
    - **Parmeters**
        - dict : Python dictionary (nested as well) containing any python data types.
    - **Methods**
        - to_dict  : Converts a Data object to dictionary if it could be made a dictionary, otherwise throws relevant error.
        - to_json  : Converts to json str or save to file if `outfil` given. Accepts `indent` as parameter.
        - to_pickle: Converts to bytes str or save to file if `outfile` given.
        - to_tuple : Converts to a named tuple.
    - **Example**
        > x = Dict2Data({'A':1,'B':{'C':2}})
        > x
        > Data(
        >     A = 1
        >     B = Data(
        >         C = 2
        >         )
        >     )
        > x.B.to_dict()
        > {'C': 2}
    """
    def __init__(self,d):
        if not hasattr(self.__class__,'_req_keys'):
            raise AttributeError("Derived class of `Dict2Data` should have attribute '_req_keys'")
        if isinstance(d,(self.__class__, Dict2Data)):
            d = d.to_dict() # if nested Dict2Data , must expand
        # Check if all required keys are present in main level of subclasses
        for key in self.__class__._req_keys:
            if key not in d:
                raise ValueError(f"Invalid input for {self.__class__.__name__}")
        # ===================
        for a,b in d.items(): 
            if isinstance(b,(self.__class__, Dict2Data)):
                b = b.to_dict() # expands self instance !must here.
            
            if a == 'poscar' and 'extra_info' in b:
                setattr(self,a, PoscarData(b)) # Enables custom methods for PoscarData
            elif isinstance(b,(list,tuple)):
                setattr(self,a,[Dict2Data(x) if isinstance(x,dict) else x for x in b])
            else:
                setattr(self,a,Dict2Data(b) if isinstance(b,dict) else b)
    
    @classmethod
    def validated(cls, data):
        "Validate data like it's own or from json/pickle file/string."
        if isinstance(data,cls):
            return data
        
        if isinstance(data,(str,bytes)):
            new_data = load(data)
            if not isinstance(new_data,cls):
                raise TypeError(f"Data is not of type {cls}.")
            return new_data
        
        if isinstance(data,Dict2Data) and cls is not Dict2Data: # Check for other classes strictly   
            data_keys = data.keys()
            for key in cls._req_keys:
                if key not in data_keys:
                    raise KeyError(f"Invalid data for {cls.__name__}")
            
        return cls(data) # make of that type at end
        
    def to_dict(self):
        """Converts a `Dict2Data` object (root or nested level) to a dictionary.
        """
        result = {}
        for k,v in self.__dict__.items():
            if isinstance(v,(self.__class__,Dict2Data)):
                result.update({k:Dict2Data.to_dict(v)})
            else:
                result.update({k:v})
        return result
    def to_json(self,outfile=None,indent=1):
        """Dumps a `Dict2Data` object (root or nested level) to json.
        - **Parameters**
            - outfile : Default is None and returns string. If given, writes to file.
            - indent  : Json indent. Default is 1.
        """
        return dump(self,dump_to='json',outfile=outfile,indent=indent)

    def to_pickle(self,outfile=None):
        """Dumps a `Dict2Data` or subclass object (root or nested level) to pickle.
        - **Parameters**
            - outfile : Default is None and returns string. If given, writes to file.
        """
        return dump(self,dump_to='pickle',outfile=outfile)

    def to_tuple(self):
        """Creates a namedtuple."""
        return dict2tuple('Data',self.to_dict())

    def __repr__(self):
        items= []
        for k,v in self.__dict__.items():
            if type(v) not in (str,float,int,range,bool,None,True,False) and not isinstance(v,Dict2Data):
                if isinstance(v,np.ndarray):
                    v = "<{}:shape={}>".format(v.__class__.__name__,np.shape(v))
                elif type(v) in (list,tuple):
                    v = ("<{}:len={}>".format(v.__class__.__name__,len(v)) if len(v) > 10 else v)
                else:
                    v = v.__class__
            if isinstance(v,Dict2Data):
                v = repr(v).replace("\n","\n    ")
            items.append(f"    {k} = {v}")

        return "Data(\n{}\n)".format('\n'.join(items))
    def __getstate__(self):
        pass  #This is for pickling

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise AttributeError(f"Outside assignment is restricted for already present attribute.")
        else:
            self.__dict__[name] = value
    # Dictionary-wise access
    def keys(self):
        return self.__dict__.keys()
    def __getitem__(self,key):
        return self.__dict__[key]
    def items(self):
        return self.__dict__.items()

    
class VasprunData(Dict2Data):
    _req_keys = ('kpath','bands','poscar')
    def __init__(self,d):
        super().__init__(d)
    
    def __repr__(self):
        return super().__repr__().replace("Data","VasprunData",1)
    
    @property
    def fermi(self):
        "Fermi energy based on occupancy. Returns `self.Fermi` if occupancies cannot be resolved."
        try:
            if self.sys_info.ISPIN == 1:
                return float(self.bands.evals[self.bands.occs > 0].max())
                
            else: # ISPIN 2
                energies = []
                for attr in ['SpinUp','SpinDown']:
                    energies.append(self.bands.evals[attr][self.bands.occs[attr] > 0].max())
                return float(max(energies))
        except:
            return self.Fermi
    
    @property
    def Fermi(self):
        "Fermi energy given in vasprun.xml."
        return self.bands.Fermi
    
class SpinData(Dict2Data):
    _req_keys = ('kpoints','spins','poscar')
    def __init__(self,d):
        super().__init__(d)
        with suppress(BaseException): # Silently set fermi if not present
            self.sys_info.fermi = self.fermi
    
    def __repr__(self):
        return super().__repr__().replace("Data","SpinData",1)
    
    @property
    def fermi(self):
        "Fermi energy based on occupancy. Returns `self.Fermi` if occupancies cannot be resolved."
        try:
            if self.sys_info.ISPIN == 1:
                return float(self.evals.e[self.evals.occs > 0].max())
                
            else: # ISPIN 2
                energies = []
                for a, b in [('u','SpinUp'),('d','SpinDown')]:
                    energies.append(self.evals[a][self.evals.occs[b] > 0].max())
                return float(max(energies))
        except:
            return self.Fermi
    
    @property
    def Fermi(self):
        "Fermi energy given in vasprun.xml."
        return self.evals.Fermi
    
class PoscarData(Dict2Data):
    _req_keys = ('basis','rec_basis','extra_info')
    def __init__(self,d):
        super().__init__(d)
    
    def __repr__(self):
        return super().__repr__().replace("Data","PoscarData",1)
    
    @property
    def coords(self):
        """Returns the lattice coordinates in cartesian space of the atoms in the poscar data.
        """
        from .sio import to_R3 # To avoid circular import
        return to_R3(self.basis, self.positions)
    
    def write(self,sd_list = None, outfile = None, overwrite = False):
        """Writes the poscar data to a file.
        """
        from .sio import write_poscar # To avoid circular import
        return write_poscar(self,sd_list = sd_list,outfile = outfile,overwrite = overwrite)
        

class LocpotData(Dict2Data):
    _req_keys = ('ElemName','ElemIndex','SYSTEM')
    def __init__(self,d):
        super().__init__(d)
    
    def __repr__(self):
        return super().__repr__().replace("Data","LocpotData",1)

class OutcarData(Dict2Data):
    _req_keys = ('site_pot','ion_pot','basis')
    def __init__(self,d):
        super().__init__(d)
    
    def __repr__(self):
        return super().__repr__().replace("Data","OutcarData",1)


class EncodeFromNumpy(json.JSONEncoder):
    """
    - Serializes python/Numpy objects via customizing json encoder.
    - **Usage**
        - `json.dumps(python_dict, cls=EncodeFromNumpy)` to get json string.
        - `json.dump(*args, cls=EncodeFromNumpy)` to create a file.json.
    """
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return {
                "_kind_": "ndarray",
                "_value_": obj.tolist()
            }
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj,range):
            value = list(obj)
            return {
                "_kind_" : "range",
                "_value_" : [value[0],value[-1]+1]
            }
        return super(EncodeFromNumpy, self).default(obj)



class DecodeToNumpy(json.JSONDecoder):
    """
    - Deserilizes JSON object to Python/Numpy's objects.
    - **Usage**
        - `json.loads(json_string,cls=DecodeToNumpy)` from string, use `json.load()` for file.
    """
    def __init__(self, *args, **kwargs):
        json.JSONDecoder.__init__(self, object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        if '_kind_' not in obj:
            return obj
        kind = obj['_kind_']
        if kind == 'ndarray':
            return np.array(obj['_value_'])
        elif kind == 'range':
            value = obj['_value_']
            return range(value[0],value[-1])
        return obj

    
def dump(dict_data = None, dump_to = 'pickle',outfile = None,indent=1):
    """
    - Dump an `export_vasprun` or `load_export`'s `Data` object or any dictionary to json or pickle string/file. It convert `Dict2Data` to dictionary before serializing to json/pickle, so json/pickle.loads() of converted Data would be a simple dictionary, pass that to `Dict2Data` to again make accessible via dot notation.
    - **Parameters**
        - dict_data: Any dictionary/Dict2Data(or subclass Data) object containg numpy arrays, including `export_vasprun` or `load_export` output.
        - dump_to  : Defualt is `pickle` or `json`.
        - outfile  : Defualt is None and return string. File name does not require extension.
        - indent   : Defualt is 1. Only works for json.
    """
    if dump_to not in ['pickle','json']:
        raise ValueError("`dump_to` expects 'pickle' or 'json', got '{}'".format(dump_to))
    try: 
        dict_obj = dict_data.to_dict() # Change Data object to dictionary
        dict_obj = {'_loader_':dict_data.__class__.__name__,'_data_':dict_obj} # Add class name to dictionary for reconstruction
    except: 
        dict_obj = dict_data
    if dump_to == 'pickle':
        if outfile == None:
            return pickle.dumps(dict_obj)
        outfile = os.path.splitext(outfile)[0] + '.pickle'
        with open(outfile,'wb') as f:
            pickle.dump(dict_obj,f)
    if dump_to == 'json':
        if outfile == None:
            return json.dumps(dict_obj,cls = EncodeFromNumpy,indent=indent)
        outfile = os.path.splitext(outfile)[0] + '.json'
        with open(outfile,'w') as f:
            json.dump(dict_obj,f,cls = EncodeFromNumpy,indent=indent)
    return None


def load(file_or_str):
    """
    - Loads a json/pickle dumped file or string by auto detecting it.
    - **Parameters**
        - file_or_str : Filename of pickl/json or their string. 
    """
    out = {}
    if not isinstance(file_or_str,bytes):
        try: #must try, else fails due to path length issue
            if os.path.isfile(file_or_str):
                if '.pickle' in file_or_str:
                    with open(file_or_str,'rb') as f:
                        out = pickle.load(f)

                elif '.json' in file_or_str:
                    with open(file_or_str,'r') as f:
                        out = json.load(f,cls = DecodeToNumpy)

            else: out = json.loads(file_or_str,cls = DecodeToNumpy)
            # json.loads required in else and except both as long str > 260 causes issue in start of try block
        except: out = json.loads(file_or_str,cls = DecodeToNumpy)
    elif isinstance(file_or_str,bytes):
            out = pickle.loads(file_or_str)
    

    if type(out) is dict:
        if '_loader_' in out:
            return globals()[out['_loader_']](out['_data_'])
    else:
        if hasattr(out, '_loader_'):
            return globals()[out._loader_](out._data_)
        
    return out # Retruns usual dictionaries

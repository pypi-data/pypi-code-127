# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.2
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _material
else:
    import _material

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


import opencmiss.zinc.context
import opencmiss.zinc.font
import opencmiss.zinc.graphics
import opencmiss.zinc.field
import opencmiss.zinc.differentialoperator
import opencmiss.zinc.element
import opencmiss.zinc.node
import opencmiss.zinc.fieldassignment
import opencmiss.zinc.fieldcache
import opencmiss.zinc.fieldmodule
import opencmiss.zinc.scenecoordinatesystem
import opencmiss.zinc.timesequence
import opencmiss.zinc.optimisation
import opencmiss.zinc.fieldsmoothing
import opencmiss.zinc.fieldparameters
import opencmiss.zinc.region
import opencmiss.zinc.scene
import opencmiss.zinc.scenefilter
import opencmiss.zinc.selection
import opencmiss.zinc.timekeeper
import opencmiss.zinc.timenotifier
import opencmiss.zinc.scenepicker
import opencmiss.zinc.sceneviewer
import opencmiss.zinc.light
import opencmiss.zinc.shader
import opencmiss.zinc.spectrum
import opencmiss.zinc.streamscene
import opencmiss.zinc.stream
import opencmiss.zinc.streamregion
import opencmiss.zinc.streamimage
import opencmiss.zinc.glyph
import opencmiss.zinc.tessellation
import opencmiss.zinc.logger
class Material(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Material_swiginit(self, _material.new_Material(*args))
    __swig_destroy__ = _material.delete_Material

    def isValid(self) -> "bool":
        return _material.Material_isValid(self)

    def getId(self) -> "cmzn_material_id":
        return _material.Material_getId(self)
    ATTRIBUTE_INVALID = _material.Material_ATTRIBUTE_INVALID
    ATTRIBUTE_ALPHA = _material.Material_ATTRIBUTE_ALPHA
    ATTRIBUTE_AMBIENT = _material.Material_ATTRIBUTE_AMBIENT
    ATTRIBUTE_DIFFUSE = _material.Material_ATTRIBUTE_DIFFUSE
    ATTRIBUTE_EMISSION = _material.Material_ATTRIBUTE_EMISSION
    ATTRIBUTE_SHININESS = _material.Material_ATTRIBUTE_SHININESS
    ATTRIBUTE_SPECULAR = _material.Material_ATTRIBUTE_SPECULAR
    CHANGE_FLAG_NONE = _material.Material_CHANGE_FLAG_NONE
    CHANGE_FLAG_ADD = _material.Material_CHANGE_FLAG_ADD
    CHANGE_FLAG_REMOVE = _material.Material_CHANGE_FLAG_REMOVE
    CHANGE_FLAG_IDENTIFIER = _material.Material_CHANGE_FLAG_IDENTIFIER
    CHANGE_FLAG_DEFINITION = _material.Material_CHANGE_FLAG_DEFINITION
    CHANGE_FLAG_FULL_RESULT = _material.Material_CHANGE_FLAG_FULL_RESULT
    CHANGE_FLAG_FINAL = _material.Material_CHANGE_FLAG_FINAL

    def isManaged(self) -> "bool":
        return _material.Material_isManaged(self)

    def setManaged(self, value: "bool") -> "int":
        return _material.Material_setManaged(self, value)

    def getAttributeReal(self, attribute: "OpenCMISS::Zinc::Material::Attribute") -> "double":
        return _material.Material_getAttributeReal(self, attribute)

    def setAttributeReal(self, attribute: "OpenCMISS::Zinc::Material::Attribute", value: "double") -> "int":
        return _material.Material_setAttributeReal(self, attribute, value)

    def getAttributeReal3(self, attribute: "OpenCMISS::Zinc::Material::Attribute") -> "int":
        return _material.Material_getAttributeReal3(self, attribute)

    def setAttributeReal3(self, attribute: "OpenCMISS::Zinc::Material::Attribute", valuesIn3: "double const *") -> "int":
        return _material.Material_setAttributeReal3(self, attribute, valuesIn3)

    def getName(self) -> "char *":
        return _material.Material_getName(self)

    def setName(self, name: "char const *") -> "int":
        return _material.Material_setName(self, name)

    def getTextureField(self, textureNumber: "int") -> "OpenCMISS::Zinc::Field":
        return _material.Material_getTextureField(self, textureNumber)

    def setTextureField(self, textureNumber: "int", textureField: "Field") -> "int":
        return _material.Material_setTextureField(self, textureNumber, textureField)

    def getShaderuniforms(self) -> "OpenCMISS::Zinc::Shaderuniforms":
        return _material.Material_getShaderuniforms(self)

    def setShaderuniforms(self, shaderuniforms: "Shaderuniforms") -> "int":
        return _material.Material_setShaderuniforms(self, shaderuniforms)

    def getShaderprogram(self) -> "OpenCMISS::Zinc::Shaderprogram":
        return _material.Material_getShaderprogram(self)

    def setShaderprogram(self, shaderprogram: "Shaderprogram") -> "int":
        return _material.Material_setShaderprogram(self, shaderprogram)

    def __eq__(self, other: "Material") -> "bool":
        return _material.Material___eq__(self, other)

# Register Material in _material:
_material.Material_swigregister(Material)


def __eq__(*args) -> "bool":
    return _material.__eq__(*args)
class Materialiterator(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialiterator_swiginit(self, _material.new_Materialiterator(*args))
    __swig_destroy__ = _material.delete_Materialiterator

    def isValid(self) -> "bool":
        return _material.Materialiterator_isValid(self)

    def next(self) -> "OpenCMISS::Zinc::Material":
        return _material.Materialiterator_next(self)

# Register Materialiterator in _material:
_material.Materialiterator_swigregister(Materialiterator)

class Materialmodule(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialmodule_swiginit(self, _material.new_Materialmodule(*args))
    __swig_destroy__ = _material.delete_Materialmodule

    def isValid(self) -> "bool":
        return _material.Materialmodule_isValid(self)

    def getId(self) -> "cmzn_materialmodule_id":
        return _material.Materialmodule_getId(self)

    def createMaterial(self) -> "OpenCMISS::Zinc::Material":
        return _material.Materialmodule_createMaterial(self)

    def createMaterialiterator(self) -> "OpenCMISS::Zinc::Materialiterator":
        return _material.Materialmodule_createMaterialiterator(self)

    def findMaterialByName(self, name: "char const *") -> "OpenCMISS::Zinc::Material":
        return _material.Materialmodule_findMaterialByName(self, name)

    def beginChange(self) -> "int":
        return _material.Materialmodule_beginChange(self)

    def endChange(self) -> "int":
        return _material.Materialmodule_endChange(self)

    def defineStandardMaterials(self) -> "int":
        return _material.Materialmodule_defineStandardMaterials(self)

    def getContext(self) -> "OpenCMISS::Zinc::Context":
        return _material.Materialmodule_getContext(self)

    def getDefaultMaterial(self) -> "OpenCMISS::Zinc::Material":
        return _material.Materialmodule_getDefaultMaterial(self)

    def setDefaultMaterial(self, material: "Material") -> "int":
        return _material.Materialmodule_setDefaultMaterial(self, material)

    def getDefaultSelectedMaterial(self) -> "OpenCMISS::Zinc::Material":
        return _material.Materialmodule_getDefaultSelectedMaterial(self)

    def setDefaultSelectedMaterial(self, material: "Material") -> "int":
        return _material.Materialmodule_setDefaultSelectedMaterial(self, material)

    def getDefaultSurfaceMaterial(self) -> "OpenCMISS::Zinc::Material":
        return _material.Materialmodule_getDefaultSurfaceMaterial(self)

    def setDefaultSurfaceMaterial(self, material: "Material") -> "int":
        return _material.Materialmodule_setDefaultSurfaceMaterial(self, material)

    def readDescription(self, description: "char const *") -> "int":
        return _material.Materialmodule_readDescription(self, description)

    def writeDescription(self) -> "char *":
        return _material.Materialmodule_writeDescription(self)

    def createMaterialmodulenotifier(self) -> "OpenCMISS::Zinc::Materialmodulenotifier":
        return _material.Materialmodule_createMaterialmodulenotifier(self)

# Register Materialmodule in _material:
_material.Materialmodule_swigregister(Materialmodule)

class Materialmoduleevent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialmoduleevent_swiginit(self, _material.new_Materialmoduleevent(*args))
    __swig_destroy__ = _material.delete_Materialmoduleevent

    def isValid(self) -> "bool":
        return _material.Materialmoduleevent_isValid(self)

    def getId(self) -> "cmzn_materialmoduleevent_id":
        return _material.Materialmoduleevent_getId(self)

    def getMaterialChangeFlags(self, material: "Material") -> "OpenCMISS::Zinc::Material::ChangeFlags":
        return _material.Materialmoduleevent_getMaterialChangeFlags(self, material)

    def getSummaryMaterialChangeFlags(self) -> "OpenCMISS::Zinc::Material::ChangeFlags":
        return _material.Materialmoduleevent_getSummaryMaterialChangeFlags(self)

# Register Materialmoduleevent in _material:
_material.Materialmoduleevent_swigregister(Materialmoduleevent)

class Materialmodulecallback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _material.delete_Materialmodulecallback

# Register Materialmodulecallback in _material:
_material.Materialmodulecallback_swigregister(Materialmodulecallback)

class Materialmodulenotifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _material.Materialmodulenotifier_swiginit(self, _material.new_Materialmodulenotifier(*args))
    __swig_destroy__ = _material.delete_Materialmodulenotifier

    def isValid(self) -> "bool":
        return _material.Materialmodulenotifier_isValid(self)

    def getId(self) -> "cmzn_materialmodulenotifier_id":
        return _material.Materialmodulenotifier_getId(self)

    def setCallback(self, *args) -> "int":
        return _material.Materialmodulenotifier_setCallback(self, *args)

    def clearCallback(self) -> "int":
        return _material.Materialmodulenotifier_clearCallback(self)

# Register Materialmodulenotifier in _material:
_material.Materialmodulenotifier_swigregister(Materialmodulenotifier)




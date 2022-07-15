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
    from . import _optimisation
else:
    import _optimisation

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


import opencmiss.zinc.field
import opencmiss.zinc.differentialoperator
import opencmiss.zinc.element
import opencmiss.zinc.node
import opencmiss.zinc.fieldassignment
import opencmiss.zinc.fieldcache
import opencmiss.zinc.fieldmodule
import opencmiss.zinc.scenecoordinatesystem
import opencmiss.zinc.timesequence
import opencmiss.zinc.fieldsmoothing
import opencmiss.zinc.fieldparameters
import opencmiss.zinc.region
import opencmiss.zinc.context
import opencmiss.zinc.font
import opencmiss.zinc.graphics
import opencmiss.zinc.glyph
import opencmiss.zinc.material
import opencmiss.zinc.spectrum
import opencmiss.zinc.tessellation
import opencmiss.zinc.light
import opencmiss.zinc.logger
import opencmiss.zinc.scenefilter
import opencmiss.zinc.sceneviewer
import opencmiss.zinc.scene
import opencmiss.zinc.selection
import opencmiss.zinc.timekeeper
import opencmiss.zinc.timenotifier
import opencmiss.zinc.scenepicker
import opencmiss.zinc.shader
import opencmiss.zinc.streamscene
import opencmiss.zinc.stream
import opencmiss.zinc.streamregion
import opencmiss.zinc.streamimage
class Optimisation(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _optimisation.Optimisation_swiginit(self, _optimisation.new_Optimisation(*args))
    __swig_destroy__ = _optimisation.delete_Optimisation

    def isValid(self) -> "bool":
        return _optimisation.Optimisation_isValid(self)
    METHOD_INVALID = _optimisation.Optimisation_METHOD_INVALID
    METHOD_QUASI_NEWTON = _optimisation.Optimisation_METHOD_QUASI_NEWTON
    METHOD_LEAST_SQUARES_QUASI_NEWTON = _optimisation.Optimisation_METHOD_LEAST_SQUARES_QUASI_NEWTON
    METHOD_NEWTON = _optimisation.Optimisation_METHOD_NEWTON
    ATTRIBUTE_FUNCTION_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_FUNCTION_TOLERANCE
    ATTRIBUTE_GRADIENT_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_GRADIENT_TOLERANCE
    ATTRIBUTE_STEP_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_STEP_TOLERANCE
    ATTRIBUTE_MAXIMUM_ITERATIONS = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_ITERATIONS
    ATTRIBUTE_MAXIMUM_FUNCTION_EVALUATIONS = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_FUNCTION_EVALUATIONS
    ATTRIBUTE_MAXIMUM_STEP = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_STEP
    ATTRIBUTE_MINIMUM_STEP = _optimisation.Optimisation_ATTRIBUTE_MINIMUM_STEP
    ATTRIBUTE_LINESEARCH_TOLERANCE = _optimisation.Optimisation_ATTRIBUTE_LINESEARCH_TOLERANCE
    ATTRIBUTE_MAXIMUM_BACKTRACK_ITERATIONS = _optimisation.Optimisation_ATTRIBUTE_MAXIMUM_BACKTRACK_ITERATIONS
    ATTRIBUTE_TRUST_REGION_SIZE = _optimisation.Optimisation_ATTRIBUTE_TRUST_REGION_SIZE
    ATTRIBUTE_FIELD_PARAMETERS_TIME = _optimisation.Optimisation_ATTRIBUTE_FIELD_PARAMETERS_TIME

    def getId(self) -> "cmzn_optimisation_id":
        return _optimisation.Optimisation_getId(self)

    def getConditionalField(self, dependentField: "Field") -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getConditionalField(self, dependentField)

    def setConditionalField(self, dependentField: "Field", conditionalField: "Field") -> "int":
        return _optimisation.Optimisation_setConditionalField(self, dependentField, conditionalField)

    def addFieldassignment(self, fieldassignment: "Fieldassignment") -> "int":
        return _optimisation.Optimisation_addFieldassignment(self, fieldassignment)

    def getMethod(self) -> "OpenCMISS::Zinc::Optimisation::Method":
        return _optimisation.Optimisation_getMethod(self)

    def setMethod(self, method: "OpenCMISS::Zinc::Optimisation::Method") -> "int":
        return _optimisation.Optimisation_setMethod(self, method)

    def getAttributeInteger(self, attribute: "OpenCMISS::Zinc::Optimisation::Attribute") -> "int":
        return _optimisation.Optimisation_getAttributeInteger(self, attribute)

    def setAttributeInteger(self, attribute: "OpenCMISS::Zinc::Optimisation::Attribute", value: "int") -> "int":
        return _optimisation.Optimisation_setAttributeInteger(self, attribute, value)

    def getAttributeReal(self, attribute: "OpenCMISS::Zinc::Optimisation::Attribute") -> "double":
        return _optimisation.Optimisation_getAttributeReal(self, attribute)

    def setAttributeReal(self, attribute: "OpenCMISS::Zinc::Optimisation::Attribute", value: "double") -> "int":
        return _optimisation.Optimisation_setAttributeReal(self, attribute, value)

    def getFirstDependentField(self) -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getFirstDependentField(self)

    def getNextDependentField(self, refField: "Field") -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getNextDependentField(self, refField)

    def addDependentField(self, field: "Field") -> "int":
        return _optimisation.Optimisation_addDependentField(self, field)

    def removeDependentField(self, field: "Field") -> "int":
        return _optimisation.Optimisation_removeDependentField(self, field)

    def getFirstIndependentField(self) -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getFirstIndependentField(self)

    def getNextIndependentField(self, refField: "Field") -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getNextIndependentField(self, refField)

    def addIndependentField(self, field: "Field") -> "int":
        return _optimisation.Optimisation_addIndependentField(self, field)

    def removeIndependentField(self, field: "Field") -> "int":
        return _optimisation.Optimisation_removeIndependentField(self, field)

    def getFirstObjectiveField(self) -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getFirstObjectiveField(self)

    def getNextObjectiveField(self, refField: "Field") -> "OpenCMISS::Zinc::Field":
        return _optimisation.Optimisation_getNextObjectiveField(self, refField)

    def addObjectiveField(self, field: "Field") -> "int":
        return _optimisation.Optimisation_addObjectiveField(self, field)

    def removeObjectiveField(self, field: "Field") -> "int":
        return _optimisation.Optimisation_removeObjectiveField(self, field)

    def getSolutionReport(self) -> "char *":
        return _optimisation.Optimisation_getSolutionReport(self)

    def optimise(self) -> "int":
        return _optimisation.Optimisation_optimise(self)

# Register Optimisation in _optimisation:
_optimisation.Optimisation_swigregister(Optimisation)




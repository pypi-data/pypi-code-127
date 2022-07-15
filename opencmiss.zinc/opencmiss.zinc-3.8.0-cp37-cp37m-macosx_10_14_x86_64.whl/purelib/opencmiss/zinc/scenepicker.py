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
    from . import _scenepicker
else:
    import _scenepicker

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


import opencmiss.zinc.element
import opencmiss.zinc.field
import opencmiss.zinc.differentialoperator
import opencmiss.zinc.fieldassignment
import opencmiss.zinc.node
import opencmiss.zinc.fieldcache
import opencmiss.zinc.fieldmodule
import opencmiss.zinc.scenecoordinatesystem
import opencmiss.zinc.timesequence
import opencmiss.zinc.optimisation
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
import opencmiss.zinc.shader
import opencmiss.zinc.streamscene
import opencmiss.zinc.stream
import opencmiss.zinc.streamregion
import opencmiss.zinc.streamimage
class Scenepicker(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _scenepicker.Scenepicker_swiginit(self, _scenepicker.new_Scenepicker(*args))
    __swig_destroy__ = _scenepicker.delete_Scenepicker

    def isValid(self) -> "bool":
        return _scenepicker.Scenepicker_isValid(self)

    def getId(self) -> "cmzn_scenepicker_id":
        return _scenepicker.Scenepicker_getId(self)

    def setSceneviewerRectangle(self, sceneviewer: "Sceneviewer", scenecoordinatesystem: "OpenCMISS::Zinc::Scenecoordinatesystem", x1: "double", y1: "double", x2: "double", y2: "double") -> "int":
        return _scenepicker.Scenepicker_setSceneviewerRectangle(self, sceneviewer, scenecoordinatesystem, x1, y1, x2, y2)

    def getNearestElement(self) -> "OpenCMISS::Zinc::Element":
        return _scenepicker.Scenepicker_getNearestElement(self)

    def getNearestNode(self) -> "OpenCMISS::Zinc::Node":
        return _scenepicker.Scenepicker_getNearestNode(self)

    def getNearestElementGraphics(self) -> "OpenCMISS::Zinc::Graphics":
        return _scenepicker.Scenepicker_getNearestElementGraphics(self)

    def getNearestNodeGraphics(self) -> "OpenCMISS::Zinc::Graphics":
        return _scenepicker.Scenepicker_getNearestNodeGraphics(self)

    def getNearestGraphics(self) -> "OpenCMISS::Zinc::Graphics":
        return _scenepicker.Scenepicker_getNearestGraphics(self)

    def addPickedElementsToFieldGroup(self, fieldGroup: "FieldGroup") -> "int":
        return _scenepicker.Scenepicker_addPickedElementsToFieldGroup(self, fieldGroup)

    def addPickedNodesToFieldGroup(self, fieldGroup: "FieldGroup") -> "int":
        return _scenepicker.Scenepicker_addPickedNodesToFieldGroup(self, fieldGroup)

    def getScene(self) -> "OpenCMISS::Zinc::Scene":
        return _scenepicker.Scenepicker_getScene(self)

    def setScene(self, scene: "Scene") -> "int":
        return _scenepicker.Scenepicker_setScene(self, scene)

    def getScenefilter(self) -> "OpenCMISS::Zinc::Scenefilter":
        return _scenepicker.Scenepicker_getScenefilter(self)

    def setScenefilter(self, filter: "Scenefilter") -> "int":
        return _scenepicker.Scenepicker_setScenefilter(self, filter)

    def getPickingVolumeCentre(self) -> "int":
        return _scenepicker.Scenepicker_getPickingVolumeCentre(self)

# Register Scenepicker in _scenepicker:
_scenepicker.Scenepicker_swigregister(Scenepicker)




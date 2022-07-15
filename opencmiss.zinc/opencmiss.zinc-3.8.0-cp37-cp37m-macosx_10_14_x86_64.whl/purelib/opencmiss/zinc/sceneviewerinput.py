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
    from . import _sceneviewerinput
else:
    import _sceneviewerinput

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


import opencmiss.zinc.sceneviewer
import opencmiss.zinc.light
import opencmiss.zinc.scene
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
import opencmiss.zinc.context
import opencmiss.zinc.font
import opencmiss.zinc.glyph
import opencmiss.zinc.material
import opencmiss.zinc.spectrum
import opencmiss.zinc.logger
import opencmiss.zinc.scenefilter
import opencmiss.zinc.shader
import opencmiss.zinc.tessellation
import opencmiss.zinc.timekeeper
import opencmiss.zinc.timenotifier
import opencmiss.zinc.streamregion
import opencmiss.zinc.stream
import opencmiss.zinc.streamimage
import opencmiss.zinc.selection
import opencmiss.zinc.scenepicker
import opencmiss.zinc.streamscene
class Sceneviewerinput(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BUTTON_TYPE_INVALID = _sceneviewerinput.Sceneviewerinput_BUTTON_TYPE_INVALID
    BUTTON_TYPE_LEFT = _sceneviewerinput.Sceneviewerinput_BUTTON_TYPE_LEFT
    BUTTON_TYPE_MIDDLE = _sceneviewerinput.Sceneviewerinput_BUTTON_TYPE_MIDDLE
    BUTTON_TYPE_RIGHT = _sceneviewerinput.Sceneviewerinput_BUTTON_TYPE_RIGHT
    BUTTON_TYPE_SCROLL_DOWN = _sceneviewerinput.Sceneviewerinput_BUTTON_TYPE_SCROLL_DOWN
    BUTTON_TYPE_SCROLL_UP = _sceneviewerinput.Sceneviewerinput_BUTTON_TYPE_SCROLL_UP
    EVENT_TYPE_INVALID = _sceneviewerinput.Sceneviewerinput_EVENT_TYPE_INVALID
    EVENT_TYPE_MOTION_NOTIFY = _sceneviewerinput.Sceneviewerinput_EVENT_TYPE_MOTION_NOTIFY
    EVENT_TYPE_BUTTON_PRESS = _sceneviewerinput.Sceneviewerinput_EVENT_TYPE_BUTTON_PRESS
    EVENT_TYPE_BUTTON_RELEASE = _sceneviewerinput.Sceneviewerinput_EVENT_TYPE_BUTTON_RELEASE
    EVENT_TYPE_KEY_PRESS = _sceneviewerinput.Sceneviewerinput_EVENT_TYPE_KEY_PRESS
    EVENT_TYPE_KEY_RELEASE = _sceneviewerinput.Sceneviewerinput_EVENT_TYPE_KEY_RELEASE
    MODIFIER_FLAG_NONE = _sceneviewerinput.Sceneviewerinput_MODIFIER_FLAG_NONE
    MODIFIER_FLAG_SHIFT = _sceneviewerinput.Sceneviewerinput_MODIFIER_FLAG_SHIFT
    MODIFIER_FLAG_CONTROL = _sceneviewerinput.Sceneviewerinput_MODIFIER_FLAG_CONTROL
    MODIFIER_FLAG_ALT = _sceneviewerinput.Sceneviewerinput_MODIFIER_FLAG_ALT
    MODIFIER_FLAG_BUTTON1 = _sceneviewerinput.Sceneviewerinput_MODIFIER_FLAG_BUTTON1

    def __init__(self, *args):
        _sceneviewerinput.Sceneviewerinput_swiginit(self, _sceneviewerinput.new_Sceneviewerinput(*args))
    __swig_destroy__ = _sceneviewerinput.delete_Sceneviewerinput

    def isValid(self) -> "bool":
        return _sceneviewerinput.Sceneviewerinput_isValid(self)

    def getId(self) -> "cmzn_sceneviewerinput_id":
        return _sceneviewerinput.Sceneviewerinput_getId(self)

    def setPosition(self, x: "int", y: "int") -> "int":
        return _sceneviewerinput.Sceneviewerinput_setPosition(self, x, y)

    def setButtonType(self, buttonType: "OpenCMISS::Zinc::Sceneviewerinput::ButtonType") -> "int":
        return _sceneviewerinput.Sceneviewerinput_setButtonType(self, buttonType)

    def setEventType(self, eventType: "OpenCMISS::Zinc::Sceneviewerinput::EventType") -> "int":
        return _sceneviewerinput.Sceneviewerinput_setEventType(self, eventType)

    def setModifierFlags(self, modifierFlags: "OpenCMISS::Zinc::Sceneviewerinput::ModifierFlags") -> "int":
        return _sceneviewerinput.Sceneviewerinput_setModifierFlags(self, modifierFlags)

# Register Sceneviewerinput in _sceneviewerinput:
_sceneviewerinput.Sceneviewerinput_swigregister(Sceneviewerinput)




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
    from . import _timenotifier
else:
    import _timenotifier

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


import opencmiss.zinc.timekeeper
class Timenotifierevent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _timenotifier.Timenotifierevent_swiginit(self, _timenotifier.new_Timenotifierevent(*args))
    __swig_destroy__ = _timenotifier.delete_Timenotifierevent

    def isValid(self) -> "bool":
        return _timenotifier.Timenotifierevent_isValid(self)

    def getId(self) -> "cmzn_timenotifierevent_id":
        return _timenotifier.Timenotifierevent_getId(self)

    def getTime(self) -> "double":
        return _timenotifier.Timenotifierevent_getTime(self)

# Register Timenotifierevent in _timenotifier:
_timenotifier.Timenotifierevent_swigregister(Timenotifierevent)

class Timenotifiercallback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _timenotifier.delete_Timenotifiercallback

# Register Timenotifiercallback in _timenotifier:
_timenotifier.Timenotifiercallback_swigregister(Timenotifiercallback)

class Timenotifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _timenotifier.Timenotifier_swiginit(self, _timenotifier.new_Timenotifier(*args))
    __swig_destroy__ = _timenotifier.delete_Timenotifier

    def isValid(self) -> "bool":
        return _timenotifier.Timenotifier_isValid(self)

    def getId(self) -> "cmzn_timenotifier_id":
        return _timenotifier.Timenotifier_getId(self)

    def getTime(self) -> "double":
        return _timenotifier.Timenotifier_getTime(self)

    def getNextCallbackTime(self, playDirection: "OpenCMISS::Zinc::Timekeeper::PlayDirection") -> "double":
        return _timenotifier.Timenotifier_getNextCallbackTime(self, playDirection)

    def castRegular(self) -> "OpenCMISS::Zinc::TimenotifierRegular":
        return _timenotifier.Timenotifier_castRegular(self)

    def setCallback(self, *args) -> "int":
        return _timenotifier.Timenotifier_setCallback(self, *args)

    def clearCallback(self) -> "int":
        return _timenotifier.Timenotifier_clearCallback(self)

# Register Timenotifier in _timenotifier:
_timenotifier.Timenotifier_swigregister(Timenotifier)

class TimenotifierRegular(Timenotifier):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _timenotifier.TimenotifierRegular_swiginit(self, _timenotifier.new_TimenotifierRegular(*args))

    def setFrequency(self, frequency: "double") -> "int":
        return _timenotifier.TimenotifierRegular_setFrequency(self, frequency)

    def setOffset(self, timeOffset: "double") -> "int":
        return _timenotifier.TimenotifierRegular_setOffset(self, timeOffset)
    __swig_destroy__ = _timenotifier.delete_TimenotifierRegular

# Register TimenotifierRegular in _timenotifier:
_timenotifier.TimenotifierRegular_swigregister(TimenotifierRegular)




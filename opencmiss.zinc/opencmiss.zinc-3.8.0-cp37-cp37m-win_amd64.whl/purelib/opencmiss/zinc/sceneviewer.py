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
    from . import _sceneviewer
else:
    import _sceneviewer

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
class Sceneviewerevent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _sceneviewer.Sceneviewerevent_swiginit(self, _sceneviewer.new_Sceneviewerevent(*args))
    CHANGE_FLAG_NONE = _sceneviewer.Sceneviewerevent_CHANGE_FLAG_NONE
    CHANGE_FLAG_REPAINT_REQUIRED = _sceneviewer.Sceneviewerevent_CHANGE_FLAG_REPAINT_REQUIRED
    CHANGE_FLAG_TRANSFORM = _sceneviewer.Sceneviewerevent_CHANGE_FLAG_TRANSFORM
    CHANGE_FLAG_FINAL = _sceneviewer.Sceneviewerevent_CHANGE_FLAG_FINAL
    __swig_destroy__ = _sceneviewer.delete_Sceneviewerevent

    def isValid(self) -> "bool":
        return _sceneviewer.Sceneviewerevent_isValid(self)

    def getId(self) -> "cmzn_sceneviewerevent_id":
        return _sceneviewer.Sceneviewerevent_getId(self)

    def getChangeFlags(self) -> "OpenCMISS::Zinc::Sceneviewerevent::ChangeFlags":
        return _sceneviewer.Sceneviewerevent_getChangeFlags(self)

# Register Sceneviewerevent in _sceneviewer:
_sceneviewer.Sceneviewerevent_swigregister(Sceneviewerevent)

class Sceneviewercallback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _sceneviewer.delete_Sceneviewercallback

# Register Sceneviewercallback in _sceneviewer:
_sceneviewer.Sceneviewercallback_swigregister(Sceneviewercallback)

class Sceneviewernotifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _sceneviewer.Sceneviewernotifier_swiginit(self, _sceneviewer.new_Sceneviewernotifier(*args))
    __swig_destroy__ = _sceneviewer.delete_Sceneviewernotifier

    def isValid(self) -> "bool":
        return _sceneviewer.Sceneviewernotifier_isValid(self)

    def getId(self) -> "cmzn_sceneviewernotifier_id":
        return _sceneviewer.Sceneviewernotifier_getId(self)

    def setCallback(self, *args) -> "int":
        return _sceneviewer.Sceneviewernotifier_setCallback(self, *args)

    def clearCallback(self) -> "int":
        return _sceneviewer.Sceneviewernotifier_clearCallback(self)

# Register Sceneviewernotifier in _sceneviewer:
_sceneviewer.Sceneviewernotifier_swigregister(Sceneviewernotifier)

class Sceneviewer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    BUFFERING_MODE_INVALID = _sceneviewer.Sceneviewer_BUFFERING_MODE_INVALID
    BUFFERING_MODE_DEFAULT = _sceneviewer.Sceneviewer_BUFFERING_MODE_DEFAULT
    BUFFERING_MODE_SINGLE = _sceneviewer.Sceneviewer_BUFFERING_MODE_SINGLE
    BUFFERING_MODE_DOUBLE = _sceneviewer.Sceneviewer_BUFFERING_MODE_DOUBLE
    BUFFERING_MODE_RENDER_OFFSCREEN_AND_COPY = _sceneviewer.Sceneviewer_BUFFERING_MODE_RENDER_OFFSCREEN_AND_COPY
    BUFFERING_MODE_RENDER_OFFSCREEN_AND_BLEND = _sceneviewer.Sceneviewer_BUFFERING_MODE_RENDER_OFFSCREEN_AND_BLEND
    INTERACT_MODE_INVALID = _sceneviewer.Sceneviewer_INTERACT_MODE_INVALID
    INTERACT_MODE_STANDARD = _sceneviewer.Sceneviewer_INTERACT_MODE_STANDARD
    INTERACT_MODE_2D = _sceneviewer.Sceneviewer_INTERACT_MODE_2D
    PROJECTION_MODE_INVALID = _sceneviewer.Sceneviewer_PROJECTION_MODE_INVALID
    PROJECTION_MODE_PARALLEL = _sceneviewer.Sceneviewer_PROJECTION_MODE_PARALLEL
    PROJECTION_MODE_PERSPECTIVE = _sceneviewer.Sceneviewer_PROJECTION_MODE_PERSPECTIVE
    STEREO_MODE_INVALID = _sceneviewer.Sceneviewer_STEREO_MODE_INVALID
    STEREO_MODE_DEFAULT = _sceneviewer.Sceneviewer_STEREO_MODE_DEFAULT
    STEREO_MODE_MONO = _sceneviewer.Sceneviewer_STEREO_MODE_MONO
    STEREO_MODE_STEREO = _sceneviewer.Sceneviewer_STEREO_MODE_STEREO
    TRANSPARENCY_MODE_INVALID = _sceneviewer.Sceneviewer_TRANSPARENCY_MODE_INVALID
    TRANSPARENCY_MODE_FAST = _sceneviewer.Sceneviewer_TRANSPARENCY_MODE_FAST
    TRANSPARENCY_MODE_SLOW = _sceneviewer.Sceneviewer_TRANSPARENCY_MODE_SLOW
    TRANSPARENCY_MODE_ORDER_INDEPENDENT = _sceneviewer.Sceneviewer_TRANSPARENCY_MODE_ORDER_INDEPENDENT
    VIEWPORT_MODE_INVALID = _sceneviewer.Sceneviewer_VIEWPORT_MODE_INVALID
    VIEWPORT_MODE_ABSOLUTE = _sceneviewer.Sceneviewer_VIEWPORT_MODE_ABSOLUTE
    VIEWPORT_MODE_RELATIVE = _sceneviewer.Sceneviewer_VIEWPORT_MODE_RELATIVE
    VIEWPORT_MODE_DISTORTING_RELATIVE = _sceneviewer.Sceneviewer_VIEWPORT_MODE_DISTORTING_RELATIVE

    def __init__(self, *args):
        _sceneviewer.Sceneviewer_swiginit(self, _sceneviewer.new_Sceneviewer(*args))
    __swig_destroy__ = _sceneviewer.delete_Sceneviewer

    def isValid(self) -> "bool":
        return _sceneviewer.Sceneviewer_isValid(self)

    def getId(self) -> "cmzn_sceneviewer_id":
        return _sceneviewer.Sceneviewer_getId(self)

    def beginChange(self) -> "int":
        return _sceneviewer.Sceneviewer_beginChange(self)

    def endChange(self) -> "int":
        return _sceneviewer.Sceneviewer_endChange(self)

    def renderScene(self) -> "int":
        return _sceneviewer.Sceneviewer_renderScene(self)

    def getRenderTimeout(self) -> "double":
        return _sceneviewer.Sceneviewer_getRenderTimeout(self)

    def setRenderTimeout(self, timeout: "double") -> "int":
        return _sceneviewer.Sceneviewer_setRenderTimeout(self, timeout)

    def setScene(self, scene: "Scene") -> "int":
        return _sceneviewer.Sceneviewer_setScene(self, scene)

    def getScene(self) -> "OpenCMISS::Zinc::Scene":
        return _sceneviewer.Sceneviewer_getScene(self)

    def setScenefilter(self, scenefilter: "Scenefilter") -> "int":
        return _sceneviewer.Sceneviewer_setScenefilter(self, scenefilter)

    def getScenefilter(self) -> "OpenCMISS::Zinc::Scenefilter":
        return _sceneviewer.Sceneviewer_getScenefilter(self)

    def setViewportSize(self, width: "int", height: "int") -> "int":
        return _sceneviewer.Sceneviewer_setViewportSize(self, width, height)

    def createSceneviewerinput(self) -> "OpenCMISS::Zinc::Sceneviewerinput":
        return _sceneviewer.Sceneviewer_createSceneviewerinput(self)

    def processSceneviewerinput(self, input: "OpenCMISS::Zinc::Sceneviewerinput const &") -> "int":
        return _sceneviewer.Sceneviewer_processSceneviewerinput(self, input)

    def getAntialiasSampling(self) -> "int":
        return _sceneviewer.Sceneviewer_getAntialiasSampling(self)

    def setAntialiasSampling(self, numberOfSamples: "int") -> "int":
        return _sceneviewer.Sceneviewer_setAntialiasSampling(self, numberOfSamples)

    def getBackgroundColourAlpha(self) -> "double":
        return _sceneviewer.Sceneviewer_getBackgroundColourAlpha(self)

    def setBackgroundColourAlpha(self, alpha: "double const") -> "int":
        return _sceneviewer.Sceneviewer_setBackgroundColourAlpha(self, alpha)

    def setBackgroundColourComponentRGB(self, red: "double", green: "double", blue: "double") -> "int":
        return _sceneviewer.Sceneviewer_setBackgroundColourComponentRGB(self, red, green, blue)

    def setBackgroundColourComponentRGBA(self, red: "double", green: "double", blue: "double", alpha: "double") -> "int":
        return _sceneviewer.Sceneviewer_setBackgroundColourComponentRGBA(self, red, green, blue, alpha)

    def getBackgroundColourRGB(self) -> "int":
        return _sceneviewer.Sceneviewer_getBackgroundColourRGB(self)

    def setBackgroundColourRGB(self, valuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_setBackgroundColourRGB(self, valuesIn3)

    def getBackgroundColourRGBA(self) -> "int":
        return _sceneviewer.Sceneviewer_getBackgroundColourRGBA(self)

    def setBackgroundColourRGBA(self, valuesIn4: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_setBackgroundColourRGBA(self, valuesIn4)

    def getEyePosition(self) -> "int":
        return _sceneviewer.Sceneviewer_getEyePosition(self)

    def setEyePosition(self, eyeValuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_setEyePosition(self, eyeValuesIn3)

    def getInteractMode(self) -> "OpenCMISS::Zinc::Sceneviewer::InteractMode":
        return _sceneviewer.Sceneviewer_getInteractMode(self)

    def setInteractMode(self, interactMode: "OpenCMISS::Zinc::Sceneviewer::InteractMode") -> "int":
        return _sceneviewer.Sceneviewer_setInteractMode(self, interactMode)

    def getLookatPosition(self) -> "int":
        return _sceneviewer.Sceneviewer_getLookatPosition(self)

    def setLookatPosition(self, lookatValuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_setLookatPosition(self, lookatValuesIn3)

    def getPerturbLinesFlag(self) -> "bool":
        return _sceneviewer.Sceneviewer_getPerturbLinesFlag(self)

    def setPerturbLinesFlag(self, value: "bool") -> "int":
        return _sceneviewer.Sceneviewer_setPerturbLinesFlag(self, value)

    @staticmethod
    def ProjectionModeEnumFromString(name: "char const *") -> "OpenCMISS::Zinc::Sceneviewer::ProjectionMode":
        return _sceneviewer.Sceneviewer_ProjectionModeEnumFromString(name)

    @staticmethod
    def ProjectionModeEnumToString(mode: "OpenCMISS::Zinc::Sceneviewer::ProjectionMode") -> "char *":
        return _sceneviewer.Sceneviewer_ProjectionModeEnumToString(mode)

    def getProjectionMode(self) -> "OpenCMISS::Zinc::Sceneviewer::ProjectionMode":
        return _sceneviewer.Sceneviewer_getProjectionMode(self)

    def setProjectionMode(self, projectionMode: "OpenCMISS::Zinc::Sceneviewer::ProjectionMode") -> "int":
        return _sceneviewer.Sceneviewer_setProjectionMode(self, projectionMode)

    def getTranslationRate(self) -> "double":
        return _sceneviewer.Sceneviewer_getTranslationRate(self)

    def setTranslationRate(self, translationRate: "double") -> "int":
        return _sceneviewer.Sceneviewer_setTranslationRate(self, translationRate)

    def getTumbleRate(self) -> "double":
        return _sceneviewer.Sceneviewer_getTumbleRate(self)

    def setTumbleRate(self, tumbleRate: "double") -> "int":
        return _sceneviewer.Sceneviewer_setTumbleRate(self, tumbleRate)

    def getZoomRate(self) -> "double":
        return _sceneviewer.Sceneviewer_getZoomRate(self)

    def setZoomRate(self, zoomRate: "double") -> "int":
        return _sceneviewer.Sceneviewer_setZoomRate(self, zoomRate)

    def getUpVector(self) -> "int":
        return _sceneviewer.Sceneviewer_getUpVector(self)

    def setUpVector(self, upVectorValuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_setUpVector(self, upVectorValuesIn3)

    def getLookatParameters(self) -> "int":
        return _sceneviewer.Sceneviewer_getLookatParameters(self)

    def setLookatParametersNonSkew(self, eyeValuesIn3: "double const *", lookatValuesIn3: "double const *", upVectorValuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_setLookatParametersNonSkew(self, eyeValuesIn3, lookatValuesIn3, upVectorValuesIn3)

    def getViewingVolume(self) -> "int":
        return _sceneviewer.Sceneviewer_getViewingVolume(self)

    def setViewingVolume(self, left: "double", right: "double", bottom: "double", top: "double", near_plane: "double", far_plane: "double") -> "int":
        return _sceneviewer.Sceneviewer_setViewingVolume(self, left, right, bottom, top, near_plane, far_plane)

    def viewAll(self) -> "int":
        return _sceneviewer.Sceneviewer_viewAll(self)

    @staticmethod
    def TransparencyModeEnumFromString(name: "char const *") -> "OpenCMISS::Zinc::Sceneviewer::TransparencyMode":
        return _sceneviewer.Sceneviewer_TransparencyModeEnumFromString(name)

    @staticmethod
    def TransparencyModeEnumToString(mode: "OpenCMISS::Zinc::Sceneviewer::TransparencyMode") -> "char *":
        return _sceneviewer.Sceneviewer_TransparencyModeEnumToString(mode)

    def getTransparencyMode(self) -> "OpenCMISS::Zinc::Sceneviewer::TransparencyMode":
        return _sceneviewer.Sceneviewer_getTransparencyMode(self)

    def setTransparencyMode(self, transparencyMode: "OpenCMISS::Zinc::Sceneviewer::TransparencyMode") -> "int":
        return _sceneviewer.Sceneviewer_setTransparencyMode(self, transparencyMode)

    def getTransparencyLayers(self) -> "int":
        return _sceneviewer.Sceneviewer_getTransparencyLayers(self)

    def setTransparencyLayers(self, layers: "int") -> "int":
        return _sceneviewer.Sceneviewer_setTransparencyLayers(self, layers)

    def getViewAngle(self) -> "double":
        return _sceneviewer.Sceneviewer_getViewAngle(self)

    def setViewAngle(self, viewAngle: "double") -> "int":
        return _sceneviewer.Sceneviewer_setViewAngle(self, viewAngle)

    def getViewportMode(self) -> "OpenCMISS::Zinc::Sceneviewer::ViewportMode":
        return _sceneviewer.Sceneviewer_getViewportMode(self)

    def setViewportMode(self, viewportMode: "OpenCMISS::Zinc::Sceneviewer::ViewportMode") -> "int":
        return _sceneviewer.Sceneviewer_setViewportMode(self, viewportMode)

    def getFarClippingPlane(self) -> "double":
        return _sceneviewer.Sceneviewer_getFarClippingPlane(self)

    def getNearClippingPlane(self) -> "double":
        return _sceneviewer.Sceneviewer_getNearClippingPlane(self)

    def setFarClippingPlane(self, farClippingPlane: "double") -> "int":
        return _sceneviewer.Sceneviewer_setFarClippingPlane(self, farClippingPlane)

    def setNearClippingPlane(self, nearClippingPlane: "double") -> "int":
        return _sceneviewer.Sceneviewer_setNearClippingPlane(self, nearClippingPlane)

    def writeImageToFile(self, file_name: "char const *", force_onscreen: "int", preferred_width: "int", preferred_height: "int", preferred_antialias: "int", preferred_transparency_layers: "int") -> "int":
        return _sceneviewer.Sceneviewer_writeImageToFile(self, file_name, force_onscreen, preferred_width, preferred_height, preferred_antialias, preferred_transparency_layers)

    def addLight(self, light: "Light") -> "int":
        return _sceneviewer.Sceneviewer_addLight(self, light)

    def hasLight(self, light: "Light") -> "bool":
        return _sceneviewer.Sceneviewer_hasLight(self, light)

    def removeLight(self, light: "Light") -> "int":
        return _sceneviewer.Sceneviewer_removeLight(self, light)

    def isLightingLocalViewer(self) -> "bool":
        return _sceneviewer.Sceneviewer_isLightingLocalViewer(self)

    def setLightingLocalViewer(self, value: "bool") -> "int":
        return _sceneviewer.Sceneviewer_setLightingLocalViewer(self, value)

    def isLightingTwoSided(self) -> "bool":
        return _sceneviewer.Sceneviewer_isLightingTwoSided(self)

    def setLightingTwoSided(self, value: "bool") -> "int":
        return _sceneviewer.Sceneviewer_setLightingTwoSided(self, value)

    def transformCoordinates(self, inCoordinateSystem: "OpenCMISS::Zinc::Scenecoordinatesystem", outCoordinateSystem: "OpenCMISS::Zinc::Scenecoordinatesystem", localScene: "Scene", valuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewer_transformCoordinates(self, inCoordinateSystem, outCoordinateSystem, localScene, valuesIn3)

    def readDescription(self, description: "char const *") -> "int":
        return _sceneviewer.Sceneviewer_readDescription(self, description)

    def writeDescription(self) -> "char *":
        return _sceneviewer.Sceneviewer_writeDescription(self)

    def createSceneviewernotifier(self) -> "OpenCMISS::Zinc::Sceneviewernotifier":
        return _sceneviewer.Sceneviewer_createSceneviewernotifier(self)

# Register Sceneviewer in _sceneviewer:
_sceneviewer.Sceneviewer_swigregister(Sceneviewer)

def Sceneviewer_ProjectionModeEnumFromString(name: "char const *") -> "OpenCMISS::Zinc::Sceneviewer::ProjectionMode":
    return _sceneviewer.Sceneviewer_ProjectionModeEnumFromString(name)

def Sceneviewer_ProjectionModeEnumToString(mode: "OpenCMISS::Zinc::Sceneviewer::ProjectionMode") -> "char *":
    return _sceneviewer.Sceneviewer_ProjectionModeEnumToString(mode)

def Sceneviewer_TransparencyModeEnumFromString(name: "char const *") -> "OpenCMISS::Zinc::Sceneviewer::TransparencyMode":
    return _sceneviewer.Sceneviewer_TransparencyModeEnumFromString(name)

def Sceneviewer_TransparencyModeEnumToString(mode: "OpenCMISS::Zinc::Sceneviewer::TransparencyMode") -> "char *":
    return _sceneviewer.Sceneviewer_TransparencyModeEnumToString(mode)

class Sceneviewermodule(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _sceneviewer.Sceneviewermodule_swiginit(self, _sceneviewer.new_Sceneviewermodule(*args))
    __swig_destroy__ = _sceneviewer.delete_Sceneviewermodule

    def isValid(self) -> "bool":
        return _sceneviewer.Sceneviewermodule_isValid(self)

    def getId(self) -> "cmzn_sceneviewermodule_id":
        return _sceneviewer.Sceneviewermodule_getId(self)

    def createSceneviewer(self, buffering_mode: "OpenCMISS::Zinc::Sceneviewer::BufferingMode", stereo_mode: "OpenCMISS::Zinc::Sceneviewer::StereoMode") -> "OpenCMISS::Zinc::Sceneviewer":
        return _sceneviewer.Sceneviewermodule_createSceneviewer(self, buffering_mode, stereo_mode)

    def getDefaultBackgroundColourAlpha(self) -> "double":
        return _sceneviewer.Sceneviewermodule_getDefaultBackgroundColourAlpha(self)

    def setDefaultBackgroundColourAlpha(self, alpha: "double const") -> "int":
        return _sceneviewer.Sceneviewermodule_setDefaultBackgroundColourAlpha(self, alpha)

    def getDefaultBackgroundColourRGB(self) -> "int":
        return _sceneviewer.Sceneviewermodule_getDefaultBackgroundColourRGB(self)

    def setDefaultBackgroundColourRGB(self, valuesIn3: "double const *") -> "int":
        return _sceneviewer.Sceneviewermodule_setDefaultBackgroundColourRGB(self, valuesIn3)

    def getDefaultBackgroundColourRGBA(self) -> "int":
        return _sceneviewer.Sceneviewermodule_getDefaultBackgroundColourRGBA(self)

    def setDefaultBackgroundColourRGBA(self, valuesIn4: "double const *") -> "int":
        return _sceneviewer.Sceneviewermodule_setDefaultBackgroundColourRGBA(self, valuesIn4)

# Register Sceneviewermodule in _sceneviewer:
_sceneviewer.Sceneviewermodule_swigregister(Sceneviewermodule)




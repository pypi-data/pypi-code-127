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
    from . import _fieldmodule
else:
    import _fieldmodule

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


import opencmiss.zinc.scenecoordinatesystem
import opencmiss.zinc.timesequence
import opencmiss.zinc.optimisation
import opencmiss.zinc.field
import opencmiss.zinc.differentialoperator
import opencmiss.zinc.element
import opencmiss.zinc.node
import opencmiss.zinc.fieldassignment
import opencmiss.zinc.fieldcache
import opencmiss.zinc.fieldparameters
import opencmiss.zinc.fieldsmoothing
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
class Fieldmodule(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _fieldmodule.Fieldmodule_swiginit(self, _fieldmodule.new_Fieldmodule(*args))
    __swig_destroy__ = _fieldmodule.delete_Fieldmodule

    def isValid(self) -> "bool":
        return _fieldmodule.Fieldmodule_isValid(self)

    def getId(self) -> "cmzn_fieldmodule_id":
        return _fieldmodule.Fieldmodule_getId(self)

    def beginChange(self) -> "int":
        return _fieldmodule.Fieldmodule_beginChange(self)

    def endChange(self) -> "int":
        return _fieldmodule.Fieldmodule_endChange(self)

    def defineAllFaces(self) -> "int":
        return _fieldmodule.Fieldmodule_defineAllFaces(self)

    def findFieldByName(self, fieldName: "char const *") -> "OpenCMISS::Zinc::Field":
        return _fieldmodule.Fieldmodule_findFieldByName(self, fieldName)

    def createFieldcache(self) -> "OpenCMISS::Zinc::Fieldcache":
        return _fieldmodule.Fieldmodule_createFieldcache(self)

    def createFielditerator(self) -> "OpenCMISS::Zinc::Fielditerator":
        return _fieldmodule.Fieldmodule_createFielditerator(self)

    def createFieldmodulenotifier(self) -> "OpenCMISS::Zinc::Fieldmodulenotifier":
        return _fieldmodule.Fieldmodule_createFieldmodulenotifier(self)

    def createFieldsmoothing(self) -> "OpenCMISS::Zinc::Fieldsmoothing":
        return _fieldmodule.Fieldmodule_createFieldsmoothing(self)

    def createElementbasis(self, dimension: "int", functionType: "OpenCMISS::Zinc::Elementbasis::FunctionType") -> "OpenCMISS::Zinc::Elementbasis":
        return _fieldmodule.Fieldmodule_createElementbasis(self, dimension, functionType)

    def findNodesetByFieldDomainType(self, domainType: "OpenCMISS::Zinc::Field::DomainType") -> "OpenCMISS::Zinc::Nodeset":
        return _fieldmodule.Fieldmodule_findNodesetByFieldDomainType(self, domainType)

    def findNodesetByName(self, nodeset_name: "char const *") -> "OpenCMISS::Zinc::Nodeset":
        return _fieldmodule.Fieldmodule_findNodesetByName(self, nodeset_name)

    def findMeshByDimension(self, dimension: "int") -> "OpenCMISS::Zinc::Mesh":
        return _fieldmodule.Fieldmodule_findMeshByDimension(self, dimension)

    def findMeshByName(self, meshName: "char const *") -> "OpenCMISS::Zinc::Mesh":
        return _fieldmodule.Fieldmodule_findMeshByName(self, meshName)

    def writeDescription(self) -> "char *":
        return _fieldmodule.Fieldmodule_writeDescription(self)

    def readDescription(self, description: "char const *") -> "int":
        return _fieldmodule.Fieldmodule_readDescription(self, description)

    def getMatchingTimesequence(self, timesCount: "int") -> "OpenCMISS::Zinc::Timesequence":
        return _fieldmodule.Fieldmodule_getMatchingTimesequence(self, timesCount)

    def getRegion(self) -> "OpenCMISS::Zinc::Region":
        return _fieldmodule.Fieldmodule_getRegion(self)

    def createOptimisation(self) -> "OpenCMISS::Zinc::Optimisation":
        return _fieldmodule.Fieldmodule_createOptimisation(self)

    def createFieldAlias(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldAlias":
        return _fieldmodule.Fieldmodule_createFieldAlias(self, sourceField)

    def createFieldApply(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldApply":
        return _fieldmodule.Fieldmodule_createFieldApply(self, sourceField)

    def createFieldArgumentReal(self, numberOfComponents: "int") -> "OpenCMISS::Zinc::FieldArgumentReal":
        return _fieldmodule.Fieldmodule_createFieldArgumentReal(self, numberOfComponents)

    def createFieldAdd(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldAdd":
        return _fieldmodule.Fieldmodule_createFieldAdd(self, sourceField1, sourceField2)

    def createFieldPower(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldPower":
        return _fieldmodule.Fieldmodule_createFieldPower(self, sourceField1, sourceField2)

    def createFieldMultiply(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldMultiply":
        return _fieldmodule.Fieldmodule_createFieldMultiply(self, sourceField1, sourceField2)

    def createFieldDivide(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldDivide":
        return _fieldmodule.Fieldmodule_createFieldDivide(self, sourceField1, sourceField2)

    def createFieldSubtract(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldSubtract":
        return _fieldmodule.Fieldmodule_createFieldSubtract(self, sourceField1, sourceField2)

    def createFieldSumComponents(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldSumComponents":
        return _fieldmodule.Fieldmodule_createFieldSumComponents(self, sourceField)

    def createFieldLog(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldLog":
        return _fieldmodule.Fieldmodule_createFieldLog(self, sourceField)

    def createFieldSqrt(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldSqrt":
        return _fieldmodule.Fieldmodule_createFieldSqrt(self, sourceField)

    def createFieldExp(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldExp":
        return _fieldmodule.Fieldmodule_createFieldExp(self, sourceField)

    def createFieldAbs(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldAbs":
        return _fieldmodule.Fieldmodule_createFieldAbs(self, sourceField)

    def createFieldIdentity(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldIdentity":
        return _fieldmodule.Fieldmodule_createFieldIdentity(self, sourceField)

    def createFieldComponent(self, sourceField: "Field", sourceComponentIndexesCount: "int") -> "OpenCMISS::Zinc::FieldComponent":
        return _fieldmodule.Fieldmodule_createFieldComponent(self, sourceField, sourceComponentIndexesCount)

    def createFieldConcatenate(self, fieldsCount: "int") -> "OpenCMISS::Zinc::FieldConcatenate":
        return _fieldmodule.Fieldmodule_createFieldConcatenate(self, fieldsCount)

    def createFieldIf(self, sourceField1: "Field", sourceField2: "Field", sourceField3: "Field") -> "OpenCMISS::Zinc::FieldIf":
        return _fieldmodule.Fieldmodule_createFieldIf(self, sourceField1, sourceField2, sourceField3)

    def createFieldConstant(self, valuesCount: "int") -> "OpenCMISS::Zinc::FieldConstant":
        return _fieldmodule.Fieldmodule_createFieldConstant(self, valuesCount)

    def createFieldStringConstant(self, stringConstant: "char const *") -> "OpenCMISS::Zinc::FieldStringConstant":
        return _fieldmodule.Fieldmodule_createFieldStringConstant(self, stringConstant)

    def createFieldCoordinateTransformation(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldCoordinateTransformation":
        return _fieldmodule.Fieldmodule_createFieldCoordinateTransformation(self, sourceField)

    def createFieldVectorCoordinateTransformation(self, vectorField: "Field", coordinateField: "Field") -> "OpenCMISS::Zinc::FieldVectorCoordinateTransformation":
        return _fieldmodule.Fieldmodule_createFieldVectorCoordinateTransformation(self, vectorField, coordinateField)

    def createFieldFibreAxes(self, fibreField: "Field", coordinateField: "Field") -> "OpenCMISS::Zinc::FieldFibreAxes":
        return _fieldmodule.Fieldmodule_createFieldFibreAxes(self, fibreField, coordinateField)

    def createFieldFiniteElement(self, numberOfComponents: "int") -> "OpenCMISS::Zinc::FieldFiniteElement":
        return _fieldmodule.Fieldmodule_createFieldFiniteElement(self, numberOfComponents)

    def createFieldEmbedded(self, sourceField: "Field", embeddedLocationField: "Field") -> "OpenCMISS::Zinc::FieldEmbedded":
        return _fieldmodule.Fieldmodule_createFieldEmbedded(self, sourceField, embeddedLocationField)

    def createFieldEdgeDiscontinuity(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldEdgeDiscontinuity":
        return _fieldmodule.Fieldmodule_createFieldEdgeDiscontinuity(self, sourceField)

    def createFieldFindMeshLocation(self, sourceField: "Field", meshField: "Field", mesh: "Mesh") -> "OpenCMISS::Zinc::FieldFindMeshLocation":
        return _fieldmodule.Fieldmodule_createFieldFindMeshLocation(self, sourceField, meshField, mesh)

    def createFieldNodeValue(self, sourceField: "Field", nodeValueLabel: "OpenCMISS::Zinc::Node::ValueLabel", versionNumber: "int") -> "OpenCMISS::Zinc::FieldNodeValue":
        return _fieldmodule.Fieldmodule_createFieldNodeValue(self, sourceField, nodeValueLabel, versionNumber)

    def createFieldStoredMeshLocation(self, mesh: "Mesh") -> "OpenCMISS::Zinc::FieldStoredMeshLocation":
        return _fieldmodule.Fieldmodule_createFieldStoredMeshLocation(self, mesh)

    def createFieldStoredString(self) -> "OpenCMISS::Zinc::FieldStoredString":
        return _fieldmodule.Fieldmodule_createFieldStoredString(self)

    def createFieldIsExterior(self) -> "OpenCMISS::Zinc::FieldIsExterior":
        return _fieldmodule.Fieldmodule_createFieldIsExterior(self)

    def createFieldIsOnFace(self, face: "OpenCMISS::Zinc::Element::FaceType") -> "OpenCMISS::Zinc::FieldIsOnFace":
        return _fieldmodule.Fieldmodule_createFieldIsOnFace(self, face)

    def createFieldGroup(self) -> "OpenCMISS::Zinc::FieldGroup":
        return _fieldmodule.Fieldmodule_createFieldGroup(self)

    def createFieldImage(self) -> "OpenCMISS::Zinc::FieldImage":
        return _fieldmodule.Fieldmodule_createFieldImage(self)

    def createFieldImageFromSource(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldImage":
        return _fieldmodule.Fieldmodule_createFieldImageFromSource(self, sourceField)

    def createFieldAnd(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldAnd":
        return _fieldmodule.Fieldmodule_createFieldAnd(self, sourceField1, sourceField2)

    def createFieldEqualTo(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldEqualTo":
        return _fieldmodule.Fieldmodule_createFieldEqualTo(self, sourceField1, sourceField2)

    def createFieldGreaterThan(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldGreaterThan":
        return _fieldmodule.Fieldmodule_createFieldGreaterThan(self, sourceField1, sourceField2)

    def createFieldIsDefined(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldIsDefined":
        return _fieldmodule.Fieldmodule_createFieldIsDefined(self, sourceField)

    def createFieldLessThan(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldLessThan":
        return _fieldmodule.Fieldmodule_createFieldLessThan(self, sourceField1, sourceField2)

    def createFieldOr(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldOr":
        return _fieldmodule.Fieldmodule_createFieldOr(self, sourceField1, sourceField2)

    def createFieldNot(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldNot":
        return _fieldmodule.Fieldmodule_createFieldNot(self, sourceField)

    def createFieldXor(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldXor":
        return _fieldmodule.Fieldmodule_createFieldXor(self, sourceField1, sourceField2)

    def createFieldDeterminant(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldDeterminant":
        return _fieldmodule.Fieldmodule_createFieldDeterminant(self, sourceField)

    def createFieldEigenvalues(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldEigenvalues":
        return _fieldmodule.Fieldmodule_createFieldEigenvalues(self, sourceField)

    def createFieldEigenvectors(self, eigenValuesField: "FieldEigenvalues") -> "OpenCMISS::Zinc::FieldEigenvectors":
        return _fieldmodule.Fieldmodule_createFieldEigenvectors(self, eigenValuesField)

    def createFieldMatrixInvert(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldMatrixInvert":
        return _fieldmodule.Fieldmodule_createFieldMatrixInvert(self, sourceField)

    def createFieldMatrixMultiply(self, numberOfRows: "int", sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldMatrixMultiply":
        return _fieldmodule.Fieldmodule_createFieldMatrixMultiply(self, numberOfRows, sourceField1, sourceField2)

    def createFieldProjection(self, sourceField: "Field", projectionMatrixField: "Field") -> "OpenCMISS::Zinc::FieldProjection":
        return _fieldmodule.Fieldmodule_createFieldProjection(self, sourceField, projectionMatrixField)

    def createFieldTranspose(self, sourceNumberOfRows: "int", sourceField: "Field") -> "OpenCMISS::Zinc::FieldTranspose":
        return _fieldmodule.Fieldmodule_createFieldTranspose(self, sourceNumberOfRows, sourceField)

    def createFieldMeshIntegral(self, integrandField: "Field", coordinateField: "Field", mesh: "Mesh") -> "OpenCMISS::Zinc::FieldMeshIntegral":
        return _fieldmodule.Fieldmodule_createFieldMeshIntegral(self, integrandField, coordinateField, mesh)

    def createFieldMeshIntegralSquares(self, integrandField: "Field", coordinateField: "Field", mesh: "Mesh") -> "OpenCMISS::Zinc::FieldMeshIntegralSquares":
        return _fieldmodule.Fieldmodule_createFieldMeshIntegralSquares(self, integrandField, coordinateField, mesh)

    def createFieldNodesetSum(self, sourceField: "Field", nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodesetSum":
        return _fieldmodule.Fieldmodule_createFieldNodesetSum(self, sourceField, nodeset)

    def createFieldNodesetMean(self, sourceField: "Field", nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodesetMean":
        return _fieldmodule.Fieldmodule_createFieldNodesetMean(self, sourceField, nodeset)

    def createFieldNodesetSumSquares(self, sourceField: "Field", nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodesetSumSquares":
        return _fieldmodule.Fieldmodule_createFieldNodesetSumSquares(self, sourceField, nodeset)

    def createFieldNodesetMeanSquares(self, sourceField: "Field", nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodesetMeanSquares":
        return _fieldmodule.Fieldmodule_createFieldNodesetMeanSquares(self, sourceField, nodeset)

    def createFieldNodesetMinimum(self, sourceField: "Field", nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodesetMinimum":
        return _fieldmodule.Fieldmodule_createFieldNodesetMinimum(self, sourceField, nodeset)

    def createFieldNodesetMaximum(self, sourceField: "Field", nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodesetMaximum":
        return _fieldmodule.Fieldmodule_createFieldNodesetMaximum(self, sourceField, nodeset)

    def createFieldNodeGroup(self, nodeset: "Nodeset") -> "OpenCMISS::Zinc::FieldNodeGroup":
        return _fieldmodule.Fieldmodule_createFieldNodeGroup(self, nodeset)

    def createFieldElementGroup(self, mesh: "Mesh") -> "OpenCMISS::Zinc::FieldElementGroup":
        return _fieldmodule.Fieldmodule_createFieldElementGroup(self, mesh)

    def createFieldTimeLookup(self, sourceField: "Field", timeField: "Field") -> "OpenCMISS::Zinc::FieldTimeLookup":
        return _fieldmodule.Fieldmodule_createFieldTimeLookup(self, sourceField, timeField)

    def createFieldTimeValue(self, timeKeeper: "Timekeeper") -> "OpenCMISS::Zinc::FieldTimeValue":
        return _fieldmodule.Fieldmodule_createFieldTimeValue(self, timeKeeper)

    def createFieldDerivative(self, sourceField: "Field", xi_index: "int") -> "OpenCMISS::Zinc::FieldDerivative":
        return _fieldmodule.Fieldmodule_createFieldDerivative(self, sourceField, xi_index)

    def createFieldCurl(self, vectorField: "Field", coordinateField: "Field") -> "OpenCMISS::Zinc::FieldCurl":
        return _fieldmodule.Fieldmodule_createFieldCurl(self, vectorField, coordinateField)

    def createFieldDivergence(self, vectorField: "Field", coordinateField: "Field") -> "OpenCMISS::Zinc::FieldDivergence":
        return _fieldmodule.Fieldmodule_createFieldDivergence(self, vectorField, coordinateField)

    def createFieldGradient(self, sourceField: "Field", coordinateField: "Field") -> "OpenCMISS::Zinc::FieldGradient":
        return _fieldmodule.Fieldmodule_createFieldGradient(self, sourceField, coordinateField)

    def createFieldSin(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldSin":
        return _fieldmodule.Fieldmodule_createFieldSin(self, sourceField)

    def createFieldCos(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldCos":
        return _fieldmodule.Fieldmodule_createFieldCos(self, sourceField)

    def createFieldTan(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldTan":
        return _fieldmodule.Fieldmodule_createFieldTan(self, sourceField)

    def createFieldAsin(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldAsin":
        return _fieldmodule.Fieldmodule_createFieldAsin(self, sourceField)

    def createFieldAcos(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldAcos":
        return _fieldmodule.Fieldmodule_createFieldAcos(self, sourceField)

    def createFieldAtan(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldAtan":
        return _fieldmodule.Fieldmodule_createFieldAtan(self, sourceField)

    def createFieldAtan2(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldAtan2":
        return _fieldmodule.Fieldmodule_createFieldAtan2(self, sourceField1, sourceField2)

    def createFieldCrossProduct(self, *args) -> "OpenCMISS::Zinc::FieldCrossProduct":
        return _fieldmodule.Fieldmodule_createFieldCrossProduct(self, *args)

    def createFieldDotProduct(self, sourceField1: "Field", sourceField2: "Field") -> "OpenCMISS::Zinc::FieldDotProduct":
        return _fieldmodule.Fieldmodule_createFieldDotProduct(self, sourceField1, sourceField2)

    def createFieldMagnitude(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldMagnitude":
        return _fieldmodule.Fieldmodule_createFieldMagnitude(self, sourceField)

    def createFieldNodeLookup(self, sourceField: "Field", lookupNode: "Node") -> "OpenCMISS::Zinc::FieldNodeLookup":
        return _fieldmodule.Fieldmodule_createFieldNodeLookup(self, sourceField, lookupNode)

    def createFieldNormalise(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldNormalise":
        return _fieldmodule.Fieldmodule_createFieldNormalise(self, sourceField)

    def createFieldImagefilterBinaryDilate(self, sourceField: "Field", radius: "int", dilate_value: "double") -> "OpenCMISS::Zinc::FieldImagefilterBinaryDilate":
        return _fieldmodule.Fieldmodule_createFieldImagefilterBinaryDilate(self, sourceField, radius, dilate_value)

    def createFieldImagefilterBinaryErode(self, sourceField: "Field", radius: "int", erode_value: "double") -> "OpenCMISS::Zinc::FieldImagefilterBinaryErode":
        return _fieldmodule.Fieldmodule_createFieldImagefilterBinaryErode(self, sourceField, radius, erode_value)

    def createFieldImagefilterBinaryThreshold(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldImagefilterBinaryThreshold":
        return _fieldmodule.Fieldmodule_createFieldImagefilterBinaryThreshold(self, sourceField)

    def createFieldImagefilterCannyEdgeDetection(self, sourceField: "Field", variance: "double", maximumError: "double", upperThreshold: "double", lowerThreshold: "double") -> "OpenCMISS::Zinc::FieldImagefilterCannyEdgeDetection":
        return _fieldmodule.Fieldmodule_createFieldImagefilterCannyEdgeDetection(self, sourceField, variance, maximumError, upperThreshold, lowerThreshold)

    def createFieldImagefilterConnectedThreshold(self, sourceField: "Field", lowerThreshold: "double", upperThreshold: "double", replaceValue: "double", dimension: "int", seedPointsCount: "int") -> "OpenCMISS::Zinc::FieldImagefilterConnectedThreshold":
        return _fieldmodule.Fieldmodule_createFieldImagefilterConnectedThreshold(self, sourceField, lowerThreshold, upperThreshold, replaceValue, dimension, seedPointsCount)

    def createFieldImagefilterCurvatureAnisotropicDiffusion(self, sourceField: "Field", timeStep: "double", conductance: "double", numIterations: "int") -> "OpenCMISS::Zinc::FieldImagefilterCurvatureAnisotropicDiffusion":
        return _fieldmodule.Fieldmodule_createFieldImagefilterCurvatureAnisotropicDiffusion(self, sourceField, timeStep, conductance, numIterations)

    def createFieldImagefilterDiscreteGaussian(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldImagefilterDiscreteGaussian":
        return _fieldmodule.Fieldmodule_createFieldImagefilterDiscreteGaussian(self, sourceField)

    def createFieldImagefilterHistogram(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldImagefilterHistogram":
        return _fieldmodule.Fieldmodule_createFieldImagefilterHistogram(self, sourceField)

    def createFieldImagefilterMean(self, sourceField: "Field", radiusSizesCount: "int") -> "OpenCMISS::Zinc::FieldImagefilterMean":
        return _fieldmodule.Fieldmodule_createFieldImagefilterMean(self, sourceField, radiusSizesCount)

    def createFieldImagefilterGradientMagnitudeRecursiveGaussian(self, sourceField: "Field", sigma: "double") -> "OpenCMISS::Zinc::FieldImagefilterGradientMagnitudeRecursiveGaussian":
        return _fieldmodule.Fieldmodule_createFieldImagefilterGradientMagnitudeRecursiveGaussian(self, sourceField, sigma)

    def createFieldImagefilterRescaleIntensity(self, sourceField: "Field", outputMin: "double", outputMax: "double") -> "OpenCMISS::Zinc::FieldImagefilterRescaleIntensity":
        return _fieldmodule.Fieldmodule_createFieldImagefilterRescaleIntensity(self, sourceField, outputMin, outputMax)

    def createFieldImagefilterSigmoid(self, sourceField: "Field", min: "double", max: "double", alpha: "double", beta: "double") -> "OpenCMISS::Zinc::FieldImagefilterSigmoid":
        return _fieldmodule.Fieldmodule_createFieldImagefilterSigmoid(self, sourceField, min, max, alpha, beta)

    def createFieldImagefilterThreshold(self, sourceField: "Field") -> "OpenCMISS::Zinc::FieldImagefilterThreshold":
        return _fieldmodule.Fieldmodule_createFieldImagefilterThreshold(self, sourceField)

    def createFieldSceneviewerProjection(self, sceneviewer: "Sceneviewer", fromCoordinateSystem: "OpenCMISS::Zinc::Scenecoordinatesystem", toCoordinateSystem: "OpenCMISS::Zinc::Scenecoordinatesystem") -> "OpenCMISS::Zinc::FieldSceneviewerProjection":
        return _fieldmodule.Fieldmodule_createFieldSceneviewerProjection(self, sceneviewer, fromCoordinateSystem, toCoordinateSystem)

# Register Fieldmodule in _fieldmodule:
_fieldmodule.Fieldmodule_swigregister(Fieldmodule)


def __eq__(*args) -> "bool":
    return _fieldmodule.__eq__(*args)
class Fieldmoduleevent(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _fieldmodule.Fieldmoduleevent_swiginit(self, _fieldmodule.new_Fieldmoduleevent(*args))
    __swig_destroy__ = _fieldmodule.delete_Fieldmoduleevent

    def isValid(self) -> "bool":
        return _fieldmodule.Fieldmoduleevent_isValid(self)

    def getId(self) -> "cmzn_fieldmoduleevent_id":
        return _fieldmodule.Fieldmoduleevent_getId(self)

    def getFieldChangeFlags(self, field: "Field") -> "OpenCMISS::Zinc::Field::ChangeFlags":
        return _fieldmodule.Fieldmoduleevent_getFieldChangeFlags(self, field)

    def getMeshchanges(self, mesh: "Mesh") -> "OpenCMISS::Zinc::Meshchanges":
        return _fieldmodule.Fieldmoduleevent_getMeshchanges(self, mesh)

    def getNodesetchanges(self, nodeset: "Nodeset") -> "OpenCMISS::Zinc::Nodesetchanges":
        return _fieldmodule.Fieldmoduleevent_getNodesetchanges(self, nodeset)

    def getSummaryFieldChangeFlags(self) -> "OpenCMISS::Zinc::Field::ChangeFlags":
        return _fieldmodule.Fieldmoduleevent_getSummaryFieldChangeFlags(self)

# Register Fieldmoduleevent in _fieldmodule:
_fieldmodule.Fieldmoduleevent_swigregister(Fieldmoduleevent)

class Fieldmodulecallback(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _fieldmodule.delete_Fieldmodulecallback

# Register Fieldmodulecallback in _fieldmodule:
_fieldmodule.Fieldmodulecallback_swigregister(Fieldmodulecallback)

class Fieldmodulenotifier(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _fieldmodule.Fieldmodulenotifier_swiginit(self, _fieldmodule.new_Fieldmodulenotifier(*args))
    __swig_destroy__ = _fieldmodule.delete_Fieldmodulenotifier

    def isValid(self) -> "bool":
        return _fieldmodule.Fieldmodulenotifier_isValid(self)

    def getId(self) -> "cmzn_fieldmodulenotifier_id":
        return _fieldmodule.Fieldmodulenotifier_getId(self)

    def setCallback(self, *args) -> "int":
        return _fieldmodule.Fieldmodulenotifier_setCallback(self, *args)

    def clearCallback(self) -> "int":
        return _fieldmodule.Fieldmodulenotifier_clearCallback(self)

# Register Fieldmodulenotifier in _fieldmodule:
_fieldmodule.Fieldmodulenotifier_swigregister(Fieldmodulenotifier)




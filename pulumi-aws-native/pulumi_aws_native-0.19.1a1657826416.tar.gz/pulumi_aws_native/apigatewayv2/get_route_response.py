# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRouteResponseResult',
    'AwaitableGetRouteResponseResult',
    'get_route_response',
    'get_route_response_output',
]

@pulumi.output_type
class GetRouteResponseResult:
    def __init__(__self__, id=None, model_selection_expression=None, response_models=None, response_parameters=None, route_response_key=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_selection_expression and not isinstance(model_selection_expression, str):
            raise TypeError("Expected argument 'model_selection_expression' to be a str")
        pulumi.set(__self__, "model_selection_expression", model_selection_expression)
        if response_models and not isinstance(response_models, dict):
            raise TypeError("Expected argument 'response_models' to be a dict")
        pulumi.set(__self__, "response_models", response_models)
        if response_parameters and not isinstance(response_parameters, dict):
            raise TypeError("Expected argument 'response_parameters' to be a dict")
        pulumi.set(__self__, "response_parameters", response_parameters)
        if route_response_key and not isinstance(route_response_key, str):
            raise TypeError("Expected argument 'route_response_key' to be a str")
        pulumi.set(__self__, "route_response_key", route_response_key)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[str]:
        return pulumi.get(self, "model_selection_expression")

    @property
    @pulumi.getter(name="responseModels")
    def response_models(self) -> Optional[Any]:
        return pulumi.get(self, "response_models")

    @property
    @pulumi.getter(name="responseParameters")
    def response_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "response_parameters")

    @property
    @pulumi.getter(name="routeResponseKey")
    def route_response_key(self) -> Optional[str]:
        return pulumi.get(self, "route_response_key")


class AwaitableGetRouteResponseResult(GetRouteResponseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteResponseResult(
            id=self.id,
            model_selection_expression=self.model_selection_expression,
            response_models=self.response_models,
            response_parameters=self.response_parameters,
            route_response_key=self.route_response_key)


def get_route_response(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteResponseResult:
    """
    Resource Type definition for AWS::ApiGatewayV2::RouteResponse
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getRouteResponse', __args__, opts=opts, typ=GetRouteResponseResult).value

    return AwaitableGetRouteResponseResult(
        id=__ret__.id,
        model_selection_expression=__ret__.model_selection_expression,
        response_models=__ret__.response_models,
        response_parameters=__ret__.response_parameters,
        route_response_key=__ret__.route_response_key)


@_utilities.lift_output_func(get_route_response)
def get_route_response_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteResponseResult]:
    """
    Resource Type definition for AWS::ApiGatewayV2::RouteResponse
    """
    ...

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
    'GetRouteResult',
    'AwaitableGetRouteResult',
    'get_route',
    'get_route_output',
]

@pulumi.output_type
class GetRouteResult:
    def __init__(__self__, api_key_required=None, authorization_scopes=None, authorization_type=None, authorizer_id=None, id=None, model_selection_expression=None, operation_name=None, request_models=None, request_parameters=None, route_key=None, route_response_selection_expression=None, target=None):
        if api_key_required and not isinstance(api_key_required, bool):
            raise TypeError("Expected argument 'api_key_required' to be a bool")
        pulumi.set(__self__, "api_key_required", api_key_required)
        if authorization_scopes and not isinstance(authorization_scopes, list):
            raise TypeError("Expected argument 'authorization_scopes' to be a list")
        pulumi.set(__self__, "authorization_scopes", authorization_scopes)
        if authorization_type and not isinstance(authorization_type, str):
            raise TypeError("Expected argument 'authorization_type' to be a str")
        pulumi.set(__self__, "authorization_type", authorization_type)
        if authorizer_id and not isinstance(authorizer_id, str):
            raise TypeError("Expected argument 'authorizer_id' to be a str")
        pulumi.set(__self__, "authorizer_id", authorizer_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if model_selection_expression and not isinstance(model_selection_expression, str):
            raise TypeError("Expected argument 'model_selection_expression' to be a str")
        pulumi.set(__self__, "model_selection_expression", model_selection_expression)
        if operation_name and not isinstance(operation_name, str):
            raise TypeError("Expected argument 'operation_name' to be a str")
        pulumi.set(__self__, "operation_name", operation_name)
        if request_models and not isinstance(request_models, dict):
            raise TypeError("Expected argument 'request_models' to be a dict")
        pulumi.set(__self__, "request_models", request_models)
        if request_parameters and not isinstance(request_parameters, dict):
            raise TypeError("Expected argument 'request_parameters' to be a dict")
        pulumi.set(__self__, "request_parameters", request_parameters)
        if route_key and not isinstance(route_key, str):
            raise TypeError("Expected argument 'route_key' to be a str")
        pulumi.set(__self__, "route_key", route_key)
        if route_response_selection_expression and not isinstance(route_response_selection_expression, str):
            raise TypeError("Expected argument 'route_response_selection_expression' to be a str")
        pulumi.set(__self__, "route_response_selection_expression", route_response_selection_expression)
        if target and not isinstance(target, str):
            raise TypeError("Expected argument 'target' to be a str")
        pulumi.set(__self__, "target", target)

    @property
    @pulumi.getter(name="apiKeyRequired")
    def api_key_required(self) -> Optional[bool]:
        return pulumi.get(self, "api_key_required")

    @property
    @pulumi.getter(name="authorizationScopes")
    def authorization_scopes(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "authorization_scopes")

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[str]:
        return pulumi.get(self, "authorization_type")

    @property
    @pulumi.getter(name="authorizerId")
    def authorizer_id(self) -> Optional[str]:
        return pulumi.get(self, "authorizer_id")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="modelSelectionExpression")
    def model_selection_expression(self) -> Optional[str]:
        return pulumi.get(self, "model_selection_expression")

    @property
    @pulumi.getter(name="operationName")
    def operation_name(self) -> Optional[str]:
        return pulumi.get(self, "operation_name")

    @property
    @pulumi.getter(name="requestModels")
    def request_models(self) -> Optional[Any]:
        return pulumi.get(self, "request_models")

    @property
    @pulumi.getter(name="requestParameters")
    def request_parameters(self) -> Optional[Any]:
        return pulumi.get(self, "request_parameters")

    @property
    @pulumi.getter(name="routeKey")
    def route_key(self) -> Optional[str]:
        return pulumi.get(self, "route_key")

    @property
    @pulumi.getter(name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> Optional[str]:
        return pulumi.get(self, "route_response_selection_expression")

    @property
    @pulumi.getter
    def target(self) -> Optional[str]:
        return pulumi.get(self, "target")


class AwaitableGetRouteResult(GetRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouteResult(
            api_key_required=self.api_key_required,
            authorization_scopes=self.authorization_scopes,
            authorization_type=self.authorization_type,
            authorizer_id=self.authorizer_id,
            id=self.id,
            model_selection_expression=self.model_selection_expression,
            operation_name=self.operation_name,
            request_models=self.request_models,
            request_parameters=self.request_parameters,
            route_key=self.route_key,
            route_response_selection_expression=self.route_response_selection_expression,
            target=self.target)


def get_route(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouteResult:
    """
    Resource Type definition for AWS::ApiGatewayV2::Route
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:apigatewayv2:getRoute', __args__, opts=opts, typ=GetRouteResult).value

    return AwaitableGetRouteResult(
        api_key_required=__ret__.api_key_required,
        authorization_scopes=__ret__.authorization_scopes,
        authorization_type=__ret__.authorization_type,
        authorizer_id=__ret__.authorizer_id,
        id=__ret__.id,
        model_selection_expression=__ret__.model_selection_expression,
        operation_name=__ret__.operation_name,
        request_models=__ret__.request_models,
        request_parameters=__ret__.request_parameters,
        route_key=__ret__.route_key,
        route_response_selection_expression=__ret__.route_response_selection_expression,
        target=__ret__.target)


@_utilities.lift_output_func(get_route)
def get_route_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouteResult]:
    """
    Resource Type definition for AWS::ApiGatewayV2::Route
    """
    ...

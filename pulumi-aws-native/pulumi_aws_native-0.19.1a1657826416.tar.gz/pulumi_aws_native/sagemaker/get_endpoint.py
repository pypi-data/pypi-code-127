# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetEndpointResult',
    'AwaitableGetEndpointResult',
    'get_endpoint',
    'get_endpoint_output',
]

@pulumi.output_type
class GetEndpointResult:
    def __init__(__self__, deployment_config=None, endpoint_config_name=None, exclude_retained_variant_properties=None, id=None, retain_all_variant_properties=None, retain_deployment_config=None, tags=None):
        if deployment_config and not isinstance(deployment_config, dict):
            raise TypeError("Expected argument 'deployment_config' to be a dict")
        pulumi.set(__self__, "deployment_config", deployment_config)
        if endpoint_config_name and not isinstance(endpoint_config_name, str):
            raise TypeError("Expected argument 'endpoint_config_name' to be a str")
        pulumi.set(__self__, "endpoint_config_name", endpoint_config_name)
        if exclude_retained_variant_properties and not isinstance(exclude_retained_variant_properties, list):
            raise TypeError("Expected argument 'exclude_retained_variant_properties' to be a list")
        pulumi.set(__self__, "exclude_retained_variant_properties", exclude_retained_variant_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if retain_all_variant_properties and not isinstance(retain_all_variant_properties, bool):
            raise TypeError("Expected argument 'retain_all_variant_properties' to be a bool")
        pulumi.set(__self__, "retain_all_variant_properties", retain_all_variant_properties)
        if retain_deployment_config and not isinstance(retain_deployment_config, bool):
            raise TypeError("Expected argument 'retain_deployment_config' to be a bool")
        pulumi.set(__self__, "retain_deployment_config", retain_deployment_config)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="deploymentConfig")
    def deployment_config(self) -> Optional['outputs.EndpointDeploymentConfig']:
        return pulumi.get(self, "deployment_config")

    @property
    @pulumi.getter(name="endpointConfigName")
    def endpoint_config_name(self) -> Optional[str]:
        return pulumi.get(self, "endpoint_config_name")

    @property
    @pulumi.getter(name="excludeRetainedVariantProperties")
    def exclude_retained_variant_properties(self) -> Optional[Sequence['outputs.EndpointVariantProperty']]:
        return pulumi.get(self, "exclude_retained_variant_properties")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="retainAllVariantProperties")
    def retain_all_variant_properties(self) -> Optional[bool]:
        return pulumi.get(self, "retain_all_variant_properties")

    @property
    @pulumi.getter(name="retainDeploymentConfig")
    def retain_deployment_config(self) -> Optional[bool]:
        return pulumi.get(self, "retain_deployment_config")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.EndpointTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetEndpointResult(GetEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEndpointResult(
            deployment_config=self.deployment_config,
            endpoint_config_name=self.endpoint_config_name,
            exclude_retained_variant_properties=self.exclude_retained_variant_properties,
            id=self.id,
            retain_all_variant_properties=self.retain_all_variant_properties,
            retain_deployment_config=self.retain_deployment_config,
            tags=self.tags)


def get_endpoint(id: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEndpointResult:
    """
    Resource Type definition for AWS::SageMaker::Endpoint
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:sagemaker:getEndpoint', __args__, opts=opts, typ=GetEndpointResult).value

    return AwaitableGetEndpointResult(
        deployment_config=__ret__.deployment_config,
        endpoint_config_name=__ret__.endpoint_config_name,
        exclude_retained_variant_properties=__ret__.exclude_retained_variant_properties,
        id=__ret__.id,
        retain_all_variant_properties=__ret__.retain_all_variant_properties,
        retain_deployment_config=__ret__.retain_deployment_config,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_endpoint)
def get_endpoint_output(id: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEndpointResult]:
    """
    Resource Type definition for AWS::SageMaker::Endpoint
    """
    ...

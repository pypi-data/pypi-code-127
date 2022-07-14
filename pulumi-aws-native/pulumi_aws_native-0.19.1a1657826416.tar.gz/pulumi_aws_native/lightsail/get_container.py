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
    'GetContainerResult',
    'AwaitableGetContainerResult',
    'get_container',
    'get_container_output',
]

@pulumi.output_type
class GetContainerResult:
    def __init__(__self__, container_arn=None, container_service_deployment=None, is_disabled=None, power=None, public_domain_names=None, scale=None, tags=None, url=None):
        if container_arn and not isinstance(container_arn, str):
            raise TypeError("Expected argument 'container_arn' to be a str")
        pulumi.set(__self__, "container_arn", container_arn)
        if container_service_deployment and not isinstance(container_service_deployment, dict):
            raise TypeError("Expected argument 'container_service_deployment' to be a dict")
        pulumi.set(__self__, "container_service_deployment", container_service_deployment)
        if is_disabled and not isinstance(is_disabled, bool):
            raise TypeError("Expected argument 'is_disabled' to be a bool")
        pulumi.set(__self__, "is_disabled", is_disabled)
        if power and not isinstance(power, str):
            raise TypeError("Expected argument 'power' to be a str")
        pulumi.set(__self__, "power", power)
        if public_domain_names and not isinstance(public_domain_names, list):
            raise TypeError("Expected argument 'public_domain_names' to be a list")
        pulumi.set(__self__, "public_domain_names", public_domain_names)
        if scale and not isinstance(scale, int):
            raise TypeError("Expected argument 'scale' to be a int")
        pulumi.set(__self__, "scale", scale)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if url and not isinstance(url, str):
            raise TypeError("Expected argument 'url' to be a str")
        pulumi.set(__self__, "url", url)

    @property
    @pulumi.getter(name="containerArn")
    def container_arn(self) -> Optional[str]:
        return pulumi.get(self, "container_arn")

    @property
    @pulumi.getter(name="containerServiceDeployment")
    def container_service_deployment(self) -> Optional['outputs.ContainerServiceDeployment']:
        """
        Describes a container deployment configuration of an Amazon Lightsail container service.
        """
        return pulumi.get(self, "container_service_deployment")

    @property
    @pulumi.getter(name="isDisabled")
    def is_disabled(self) -> Optional[bool]:
        """
        A Boolean value to indicate whether the container service is disabled.
        """
        return pulumi.get(self, "is_disabled")

    @property
    @pulumi.getter
    def power(self) -> Optional[str]:
        """
        The power specification for the container service.
        """
        return pulumi.get(self, "power")

    @property
    @pulumi.getter(name="publicDomainNames")
    def public_domain_names(self) -> Optional[Sequence['outputs.ContainerPublicDomainName']]:
        """
        The public domain names to use with the container service, such as example.com and www.example.com.
        """
        return pulumi.get(self, "public_domain_names")

    @property
    @pulumi.getter
    def scale(self) -> Optional[int]:
        """
        The scale specification for the container service.
        """
        return pulumi.get(self, "scale")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ContainerTag']]:
        """
        An array of key-value pairs to apply to this resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def url(self) -> Optional[str]:
        """
        The publicly accessible URL of the container service.
        """
        return pulumi.get(self, "url")


class AwaitableGetContainerResult(GetContainerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerResult(
            container_arn=self.container_arn,
            container_service_deployment=self.container_service_deployment,
            is_disabled=self.is_disabled,
            power=self.power,
            public_domain_names=self.public_domain_names,
            scale=self.scale,
            tags=self.tags,
            url=self.url)


def get_container(service_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerResult:
    """
    Resource Type definition for AWS::Lightsail::Container


    :param str service_name: The name for the container service.
    """
    __args__ = dict()
    __args__['serviceName'] = service_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:lightsail:getContainer', __args__, opts=opts, typ=GetContainerResult).value

    return AwaitableGetContainerResult(
        container_arn=__ret__.container_arn,
        container_service_deployment=__ret__.container_service_deployment,
        is_disabled=__ret__.is_disabled,
        power=__ret__.power,
        public_domain_names=__ret__.public_domain_names,
        scale=__ret__.scale,
        tags=__ret__.tags,
        url=__ret__.url)


@_utilities.lift_output_func(get_container)
def get_container_output(service_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerResult]:
    """
    Resource Type definition for AWS::Lightsail::Container


    :param str service_name: The name for the container service.
    """
    ...

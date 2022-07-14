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
    'GetResourceShareResult',
    'AwaitableGetResourceShareResult',
    'get_resource_share',
    'get_resource_share_output',
]

@pulumi.output_type
class GetResourceShareResult:
    def __init__(__self__, allow_external_principals=None, arn=None, id=None, name=None, permission_arns=None, principals=None, resource_arns=None, tags=None):
        if allow_external_principals and not isinstance(allow_external_principals, bool):
            raise TypeError("Expected argument 'allow_external_principals' to be a bool")
        pulumi.set(__self__, "allow_external_principals", allow_external_principals)
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if permission_arns and not isinstance(permission_arns, list):
            raise TypeError("Expected argument 'permission_arns' to be a list")
        pulumi.set(__self__, "permission_arns", permission_arns)
        if principals and not isinstance(principals, list):
            raise TypeError("Expected argument 'principals' to be a list")
        pulumi.set(__self__, "principals", principals)
        if resource_arns and not isinstance(resource_arns, list):
            raise TypeError("Expected argument 'resource_arns' to be a list")
        pulumi.set(__self__, "resource_arns", resource_arns)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="allowExternalPrincipals")
    def allow_external_principals(self) -> Optional[bool]:
        return pulumi.get(self, "allow_external_principals")

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="permissionArns")
    def permission_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "permission_arns")

    @property
    @pulumi.getter
    def principals(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "principals")

    @property
    @pulumi.getter(name="resourceArns")
    def resource_arns(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "resource_arns")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ResourceShareTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetResourceShareResult(GetResourceShareResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceShareResult(
            allow_external_principals=self.allow_external_principals,
            arn=self.arn,
            id=self.id,
            name=self.name,
            permission_arns=self.permission_arns,
            principals=self.principals,
            resource_arns=self.resource_arns,
            tags=self.tags)


def get_resource_share(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceShareResult:
    """
    Resource Type definition for AWS::RAM::ResourceShare
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ram:getResourceShare', __args__, opts=opts, typ=GetResourceShareResult).value

    return AwaitableGetResourceShareResult(
        allow_external_principals=__ret__.allow_external_principals,
        arn=__ret__.arn,
        id=__ret__.id,
        name=__ret__.name,
        permission_arns=__ret__.permission_arns,
        principals=__ret__.principals,
        resource_arns=__ret__.resource_arns,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_resource_share)
def get_resource_share_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceShareResult]:
    """
    Resource Type definition for AWS::RAM::ResourceShare
    """
    ...

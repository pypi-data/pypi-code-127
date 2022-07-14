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
    'GetSecurityGroupResult',
    'AwaitableGetSecurityGroupResult',
    'get_security_group',
    'get_security_group_output',
]

@pulumi.output_type
class GetSecurityGroupResult:
    def __init__(__self__, description=None, id=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SecurityGroupTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetSecurityGroupResult(GetSecurityGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSecurityGroupResult(
            description=self.description,
            id=self.id,
            tags=self.tags)


def get_security_group(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSecurityGroupResult:
    """
    Resource Type definition for AWS::ElastiCache::SecurityGroup
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:elasticache:getSecurityGroup', __args__, opts=opts, typ=GetSecurityGroupResult).value

    return AwaitableGetSecurityGroupResult(
        description=__ret__.description,
        id=__ret__.id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_security_group)
def get_security_group_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSecurityGroupResult]:
    """
    Resource Type definition for AWS::ElastiCache::SecurityGroup
    """
    ...

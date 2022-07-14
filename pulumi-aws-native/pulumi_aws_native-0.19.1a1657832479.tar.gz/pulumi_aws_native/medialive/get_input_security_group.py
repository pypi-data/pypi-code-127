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
    'GetInputSecurityGroupResult',
    'AwaitableGetInputSecurityGroupResult',
    'get_input_security_group',
    'get_input_security_group_output',
]

@pulumi.output_type
class GetInputSecurityGroupResult:
    def __init__(__self__, arn=None, id=None, tags=None, whitelist_rules=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if whitelist_rules and not isinstance(whitelist_rules, list):
            raise TypeError("Expected argument 'whitelist_rules' to be a list")
        pulumi.set(__self__, "whitelist_rules", whitelist_rules)

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
    def tags(self) -> Optional[Any]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="whitelistRules")
    def whitelist_rules(self) -> Optional[Sequence['outputs.InputSecurityGroupInputWhitelistRuleCidr']]:
        return pulumi.get(self, "whitelist_rules")


class AwaitableGetInputSecurityGroupResult(GetInputSecurityGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInputSecurityGroupResult(
            arn=self.arn,
            id=self.id,
            tags=self.tags,
            whitelist_rules=self.whitelist_rules)


def get_input_security_group(id: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInputSecurityGroupResult:
    """
    Resource Type definition for AWS::MediaLive::InputSecurityGroup
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:medialive:getInputSecurityGroup', __args__, opts=opts, typ=GetInputSecurityGroupResult).value

    return AwaitableGetInputSecurityGroupResult(
        arn=__ret__.arn,
        id=__ret__.id,
        tags=__ret__.tags,
        whitelist_rules=__ret__.whitelist_rules)


@_utilities.lift_output_func(get_input_security_group)
def get_input_security_group_output(id: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInputSecurityGroupResult]:
    """
    Resource Type definition for AWS::MediaLive::InputSecurityGroup
    """
    ...

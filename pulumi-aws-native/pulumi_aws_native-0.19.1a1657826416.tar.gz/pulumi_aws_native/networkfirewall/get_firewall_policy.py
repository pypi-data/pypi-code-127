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
from ._enums import *

__all__ = [
    'GetFirewallPolicyResult',
    'AwaitableGetFirewallPolicyResult',
    'get_firewall_policy',
    'get_firewall_policy_output',
]

@pulumi.output_type
class GetFirewallPolicyResult:
    def __init__(__self__, description=None, firewall_policy=None, firewall_policy_arn=None, firewall_policy_id=None, tags=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if firewall_policy and not isinstance(firewall_policy, dict):
            raise TypeError("Expected argument 'firewall_policy' to be a dict")
        pulumi.set(__self__, "firewall_policy", firewall_policy)
        if firewall_policy_arn and not isinstance(firewall_policy_arn, str):
            raise TypeError("Expected argument 'firewall_policy_arn' to be a str")
        pulumi.set(__self__, "firewall_policy_arn", firewall_policy_arn)
        if firewall_policy_id and not isinstance(firewall_policy_id, str):
            raise TypeError("Expected argument 'firewall_policy_id' to be a str")
        pulumi.set(__self__, "firewall_policy_id", firewall_policy_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="firewallPolicy")
    def firewall_policy(self) -> Optional['outputs.FirewallPolicy']:
        return pulumi.get(self, "firewall_policy")

    @property
    @pulumi.getter(name="firewallPolicyArn")
    def firewall_policy_arn(self) -> Optional[str]:
        return pulumi.get(self, "firewall_policy_arn")

    @property
    @pulumi.getter(name="firewallPolicyId")
    def firewall_policy_id(self) -> Optional[str]:
        return pulumi.get(self, "firewall_policy_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.FirewallPolicyTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetFirewallPolicyResult(GetFirewallPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFirewallPolicyResult(
            description=self.description,
            firewall_policy=self.firewall_policy,
            firewall_policy_arn=self.firewall_policy_arn,
            firewall_policy_id=self.firewall_policy_id,
            tags=self.tags)


def get_firewall_policy(firewall_policy_arn: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFirewallPolicyResult:
    """
    Resource type definition for AWS::NetworkFirewall::FirewallPolicy
    """
    __args__ = dict()
    __args__['firewallPolicyArn'] = firewall_policy_arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:networkfirewall:getFirewallPolicy', __args__, opts=opts, typ=GetFirewallPolicyResult).value

    return AwaitableGetFirewallPolicyResult(
        description=__ret__.description,
        firewall_policy=__ret__.firewall_policy,
        firewall_policy_arn=__ret__.firewall_policy_arn,
        firewall_policy_id=__ret__.firewall_policy_id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_firewall_policy)
def get_firewall_policy_output(firewall_policy_arn: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFirewallPolicyResult]:
    """
    Resource type definition for AWS::NetworkFirewall::FirewallPolicy
    """
    ...

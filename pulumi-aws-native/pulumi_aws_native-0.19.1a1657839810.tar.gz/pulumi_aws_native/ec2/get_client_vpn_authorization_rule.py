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
    'GetClientVpnAuthorizationRuleResult',
    'AwaitableGetClientVpnAuthorizationRuleResult',
    'get_client_vpn_authorization_rule',
    'get_client_vpn_authorization_rule_output',
]

@pulumi.output_type
class GetClientVpnAuthorizationRuleResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetClientVpnAuthorizationRuleResult(GetClientVpnAuthorizationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientVpnAuthorizationRuleResult(
            id=self.id)


def get_client_vpn_authorization_rule(id: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientVpnAuthorizationRuleResult:
    """
    Resource Type definition for AWS::EC2::ClientVpnAuthorizationRule
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getClientVpnAuthorizationRule', __args__, opts=opts, typ=GetClientVpnAuthorizationRuleResult).value

    return AwaitableGetClientVpnAuthorizationRuleResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_client_vpn_authorization_rule)
def get_client_vpn_authorization_rule_output(id: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientVpnAuthorizationRuleResult]:
    """
    Resource Type definition for AWS::EC2::ClientVpnAuthorizationRule
    """
    ...

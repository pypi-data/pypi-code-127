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
    'GetListenerRuleResult',
    'AwaitableGetListenerRuleResult',
    'get_listener_rule',
    'get_listener_rule_output',
]

@pulumi.output_type
class GetListenerRuleResult:
    def __init__(__self__, actions=None, conditions=None, is_default=None, priority=None, rule_arn=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if conditions and not isinstance(conditions, list):
            raise TypeError("Expected argument 'conditions' to be a list")
        pulumi.set(__self__, "conditions", conditions)
        if is_default and not isinstance(is_default, bool):
            raise TypeError("Expected argument 'is_default' to be a bool")
        pulumi.set(__self__, "is_default", is_default)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if rule_arn and not isinstance(rule_arn, str):
            raise TypeError("Expected argument 'rule_arn' to be a str")
        pulumi.set(__self__, "rule_arn", rule_arn)

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.ListenerRuleAction']]:
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> Optional[Sequence['outputs.ListenerRuleRuleCondition']]:
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="isDefault")
    def is_default(self) -> Optional[bool]:
        return pulumi.get(self, "is_default")

    @property
    @pulumi.getter
    def priority(self) -> Optional[int]:
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="ruleArn")
    def rule_arn(self) -> Optional[str]:
        return pulumi.get(self, "rule_arn")


class AwaitableGetListenerRuleResult(GetListenerRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetListenerRuleResult(
            actions=self.actions,
            conditions=self.conditions,
            is_default=self.is_default,
            priority=self.priority,
            rule_arn=self.rule_arn)


def get_listener_rule(rule_arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetListenerRuleResult:
    """
    Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerRule
    """
    __args__ = dict()
    __args__['ruleArn'] = rule_arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:elasticloadbalancingv2:getListenerRule', __args__, opts=opts, typ=GetListenerRuleResult).value

    return AwaitableGetListenerRuleResult(
        actions=__ret__.actions,
        conditions=__ret__.conditions,
        is_default=__ret__.is_default,
        priority=__ret__.priority,
        rule_arn=__ret__.rule_arn)


@_utilities.lift_output_func(get_listener_rule)
def get_listener_rule_output(rule_arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetListenerRuleResult]:
    """
    Resource Type definition for AWS::ElasticLoadBalancingV2::ListenerRule
    """
    ...

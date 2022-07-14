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
    'GetTopicRuleResult',
    'AwaitableGetTopicRuleResult',
    'get_topic_rule',
    'get_topic_rule_output',
]

@pulumi.output_type
class GetTopicRuleResult:
    def __init__(__self__, arn=None, tags=None, topic_rule_payload=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if topic_rule_payload and not isinstance(topic_rule_payload, dict):
            raise TypeError("Expected argument 'topic_rule_payload' to be a dict")
        pulumi.set(__self__, "topic_rule_payload", topic_rule_payload)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TopicRuleTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="topicRulePayload")
    def topic_rule_payload(self) -> Optional['outputs.TopicRulePayload']:
        return pulumi.get(self, "topic_rule_payload")


class AwaitableGetTopicRuleResult(GetTopicRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicRuleResult(
            arn=self.arn,
            tags=self.tags,
            topic_rule_payload=self.topic_rule_payload)


def get_topic_rule(rule_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicRuleResult:
    """
    Resource Type definition for AWS::IoT::TopicRule
    """
    __args__ = dict()
    __args__['ruleName'] = rule_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getTopicRule', __args__, opts=opts, typ=GetTopicRuleResult).value

    return AwaitableGetTopicRuleResult(
        arn=__ret__.arn,
        tags=__ret__.tags,
        topic_rule_payload=__ret__.topic_rule_payload)


@_utilities.lift_output_func(get_topic_rule)
def get_topic_rule_output(rule_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicRuleResult]:
    """
    Resource Type definition for AWS::IoT::TopicRule
    """
    ...

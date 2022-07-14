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
    'GetFilterResult',
    'AwaitableGetFilterResult',
    'get_filter',
    'get_filter_output',
]

@pulumi.output_type
class GetFilterResult:
    def __init__(__self__, action=None, description=None, finding_criteria=None, id=None, rank=None):
        if action and not isinstance(action, str):
            raise TypeError("Expected argument 'action' to be a str")
        pulumi.set(__self__, "action", action)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if finding_criteria and not isinstance(finding_criteria, dict):
            raise TypeError("Expected argument 'finding_criteria' to be a dict")
        pulumi.set(__self__, "finding_criteria", finding_criteria)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if rank and not isinstance(rank, int):
            raise TypeError("Expected argument 'rank' to be a int")
        pulumi.set(__self__, "rank", rank)

    @property
    @pulumi.getter
    def action(self) -> Optional[str]:
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="findingCriteria")
    def finding_criteria(self) -> Optional['outputs.FilterFindingCriteria']:
        return pulumi.get(self, "finding_criteria")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def rank(self) -> Optional[int]:
        return pulumi.get(self, "rank")


class AwaitableGetFilterResult(GetFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFilterResult(
            action=self.action,
            description=self.description,
            finding_criteria=self.finding_criteria,
            id=self.id,
            rank=self.rank)


def get_filter(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFilterResult:
    """
    Resource Type definition for AWS::GuardDuty::Filter
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:guardduty:getFilter', __args__, opts=opts, typ=GetFilterResult).value

    return AwaitableGetFilterResult(
        action=__ret__.action,
        description=__ret__.description,
        finding_criteria=__ret__.finding_criteria,
        id=__ret__.id,
        rank=__ret__.rank)


@_utilities.lift_output_func(get_filter)
def get_filter_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFilterResult]:
    """
    Resource Type definition for AWS::GuardDuty::Filter
    """
    ...

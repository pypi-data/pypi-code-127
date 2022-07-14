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
    'GetFilterResult',
    'AwaitableGetFilterResult',
    'get_filter',
    'get_filter_output',
]

@pulumi.output_type
class GetFilterResult:
    def __init__(__self__, arn=None, description=None, filter_action=None, filter_criteria=None, name=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if filter_action and not isinstance(filter_action, str):
            raise TypeError("Expected argument 'filter_action' to be a str")
        pulumi.set(__self__, "filter_action", filter_action)
        if filter_criteria and not isinstance(filter_criteria, dict):
            raise TypeError("Expected argument 'filter_criteria' to be a dict")
        pulumi.set(__self__, "filter_criteria", filter_criteria)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Findings filter ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Findings filter description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="filterAction")
    def filter_action(self) -> Optional['FilterAction']:
        """
        Findings filter action.
        """
        return pulumi.get(self, "filter_action")

    @property
    @pulumi.getter(name="filterCriteria")
    def filter_criteria(self) -> Optional['outputs.FilterCriteria']:
        """
        Findings filter criteria.
        """
        return pulumi.get(self, "filter_criteria")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Findings filter name.
        """
        return pulumi.get(self, "name")


class AwaitableGetFilterResult(GetFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFilterResult(
            arn=self.arn,
            description=self.description,
            filter_action=self.filter_action,
            filter_criteria=self.filter_criteria,
            name=self.name)


def get_filter(arn: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFilterResult:
    """
    Inspector Filter resource schema


    :param str arn: Findings filter ARN.
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:inspectorv2:getFilter', __args__, opts=opts, typ=GetFilterResult).value

    return AwaitableGetFilterResult(
        arn=__ret__.arn,
        description=__ret__.description,
        filter_action=__ret__.filter_action,
        filter_criteria=__ret__.filter_criteria,
        name=__ret__.name)


@_utilities.lift_output_func(get_filter)
def get_filter_output(arn: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFilterResult]:
    """
    Inspector Filter resource schema


    :param str arn: Findings filter ARN.
    """
    ...

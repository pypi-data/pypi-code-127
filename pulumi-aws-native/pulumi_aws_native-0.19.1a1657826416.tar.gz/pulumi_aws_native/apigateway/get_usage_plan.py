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
    'GetUsagePlanResult',
    'AwaitableGetUsagePlanResult',
    'get_usage_plan',
    'get_usage_plan_output',
]

@pulumi.output_type
class GetUsagePlanResult:
    def __init__(__self__, api_stages=None, description=None, id=None, quota=None, tags=None, throttle=None, usage_plan_name=None):
        if api_stages and not isinstance(api_stages, list):
            raise TypeError("Expected argument 'api_stages' to be a list")
        pulumi.set(__self__, "api_stages", api_stages)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if quota and not isinstance(quota, dict):
            raise TypeError("Expected argument 'quota' to be a dict")
        pulumi.set(__self__, "quota", quota)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if throttle and not isinstance(throttle, dict):
            raise TypeError("Expected argument 'throttle' to be a dict")
        pulumi.set(__self__, "throttle", throttle)
        if usage_plan_name and not isinstance(usage_plan_name, str):
            raise TypeError("Expected argument 'usage_plan_name' to be a str")
        pulumi.set(__self__, "usage_plan_name", usage_plan_name)

    @property
    @pulumi.getter(name="apiStages")
    def api_stages(self) -> Optional[Sequence['outputs.UsagePlanApiStage']]:
        """
        The API stages to associate with this usage plan.
        """
        return pulumi.get(self, "api_stages")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the usage plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def quota(self) -> Optional['outputs.UsagePlanQuotaSettings']:
        """
        Configures the number of requests that users can make within a given interval.
        """
        return pulumi.get(self, "quota")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.UsagePlanTag']]:
        """
        An array of arbitrary tags (key-value pairs) to associate with the usage plan.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def throttle(self) -> Optional['outputs.UsagePlanThrottleSettings']:
        """
        Configures the overall request rate (average requests per second) and burst capacity.
        """
        return pulumi.get(self, "throttle")

    @property
    @pulumi.getter(name="usagePlanName")
    def usage_plan_name(self) -> Optional[str]:
        """
        A name for the usage plan.
        """
        return pulumi.get(self, "usage_plan_name")


class AwaitableGetUsagePlanResult(GetUsagePlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUsagePlanResult(
            api_stages=self.api_stages,
            description=self.description,
            id=self.id,
            quota=self.quota,
            tags=self.tags,
            throttle=self.throttle,
            usage_plan_name=self.usage_plan_name)


def get_usage_plan(id: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUsagePlanResult:
    """
    Resource Type definition for AWS::ApiGateway::UsagePlan


    :param str id: The provider-assigned unique ID for this managed resource.
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:apigateway:getUsagePlan', __args__, opts=opts, typ=GetUsagePlanResult).value

    return AwaitableGetUsagePlanResult(
        api_stages=__ret__.api_stages,
        description=__ret__.description,
        id=__ret__.id,
        quota=__ret__.quota,
        tags=__ret__.tags,
        throttle=__ret__.throttle,
        usage_plan_name=__ret__.usage_plan_name)


@_utilities.lift_output_func(get_usage_plan)
def get_usage_plan_output(id: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUsagePlanResult]:
    """
    Resource Type definition for AWS::ApiGateway::UsagePlan


    :param str id: The provider-assigned unique ID for this managed resource.
    """
    ...

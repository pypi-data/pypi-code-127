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
    'GetGatewayResult',
    'AwaitableGetGatewayResult',
    'get_gateway',
    'get_gateway_output',
]

@pulumi.output_type
class GetGatewayResult:
    def __init__(__self__, gateway_capability_summaries=None, gateway_id=None, gateway_name=None, tags=None):
        if gateway_capability_summaries and not isinstance(gateway_capability_summaries, list):
            raise TypeError("Expected argument 'gateway_capability_summaries' to be a list")
        pulumi.set(__self__, "gateway_capability_summaries", gateway_capability_summaries)
        if gateway_id and not isinstance(gateway_id, str):
            raise TypeError("Expected argument 'gateway_id' to be a str")
        pulumi.set(__self__, "gateway_id", gateway_id)
        if gateway_name and not isinstance(gateway_name, str):
            raise TypeError("Expected argument 'gateway_name' to be a str")
        pulumi.set(__self__, "gateway_name", gateway_name)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="gatewayCapabilitySummaries")
    def gateway_capability_summaries(self) -> Optional[Sequence['outputs.GatewayCapabilitySummary']]:
        """
        A list of gateway capability summaries that each contain a namespace and status.
        """
        return pulumi.get(self, "gateway_capability_summaries")

    @property
    @pulumi.getter(name="gatewayId")
    def gateway_id(self) -> Optional[str]:
        """
        The ID of the gateway device.
        """
        return pulumi.get(self, "gateway_id")

    @property
    @pulumi.getter(name="gatewayName")
    def gateway_name(self) -> Optional[str]:
        """
        A unique, friendly name for the gateway.
        """
        return pulumi.get(self, "gateway_name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.GatewayTag']]:
        """
        A list of key-value pairs that contain metadata for the gateway.
        """
        return pulumi.get(self, "tags")


class AwaitableGetGatewayResult(GetGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayResult(
            gateway_capability_summaries=self.gateway_capability_summaries,
            gateway_id=self.gateway_id,
            gateway_name=self.gateway_name,
            tags=self.tags)


def get_gateway(gateway_id: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayResult:
    """
    Resource schema for AWS::IoTSiteWise::Gateway


    :param str gateway_id: The ID of the gateway device.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:iotsitewise:getGateway', __args__, opts=opts, typ=GetGatewayResult).value

    return AwaitableGetGatewayResult(
        gateway_capability_summaries=__ret__.gateway_capability_summaries,
        gateway_id=__ret__.gateway_id,
        gateway_name=__ret__.gateway_name,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_gateway)
def get_gateway_output(gateway_id: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGatewayResult]:
    """
    Resource schema for AWS::IoTSiteWise::Gateway


    :param str gateway_id: The ID of the gateway device.
    """
    ...

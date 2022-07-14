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
    'GetConfigurationSetEventDestinationResult',
    'AwaitableGetConfigurationSetEventDestinationResult',
    'get_configuration_set_event_destination',
    'get_configuration_set_event_destination_output',
]

@pulumi.output_type
class GetConfigurationSetEventDestinationResult:
    def __init__(__self__, event_destination=None, id=None):
        if event_destination and not isinstance(event_destination, dict):
            raise TypeError("Expected argument 'event_destination' to be a dict")
        pulumi.set(__self__, "event_destination", event_destination)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter(name="eventDestination")
    def event_destination(self) -> Optional['outputs.ConfigurationSetEventDestinationEventDestination']:
        return pulumi.get(self, "event_destination")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetConfigurationSetEventDestinationResult(GetConfigurationSetEventDestinationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetConfigurationSetEventDestinationResult(
            event_destination=self.event_destination,
            id=self.id)


def get_configuration_set_event_destination(id: Optional[str] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetConfigurationSetEventDestinationResult:
    """
    Resource Type definition for AWS::PinpointEmail::ConfigurationSetEventDestination
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:pinpointemail:getConfigurationSetEventDestination', __args__, opts=opts, typ=GetConfigurationSetEventDestinationResult).value

    return AwaitableGetConfigurationSetEventDestinationResult(
        event_destination=__ret__.event_destination,
        id=__ret__.id)


@_utilities.lift_output_func(get_configuration_set_event_destination)
def get_configuration_set_event_destination_output(id: Optional[pulumi.Input[str]] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetConfigurationSetEventDestinationResult]:
    """
    Resource Type definition for AWS::PinpointEmail::ConfigurationSetEventDestination
    """
    ...

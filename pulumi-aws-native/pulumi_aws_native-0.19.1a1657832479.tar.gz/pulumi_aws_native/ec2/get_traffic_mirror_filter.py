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
    'GetTrafficMirrorFilterResult',
    'AwaitableGetTrafficMirrorFilterResult',
    'get_traffic_mirror_filter',
    'get_traffic_mirror_filter_output',
]

@pulumi.output_type
class GetTrafficMirrorFilterResult:
    def __init__(__self__, id=None, network_services=None, tags=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if network_services and not isinstance(network_services, list):
            raise TypeError("Expected argument 'network_services' to be a list")
        pulumi.set(__self__, "network_services", network_services)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="networkServices")
    def network_services(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "network_services")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.TrafficMirrorFilterTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetTrafficMirrorFilterResult(GetTrafficMirrorFilterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrafficMirrorFilterResult(
            id=self.id,
            network_services=self.network_services,
            tags=self.tags)


def get_traffic_mirror_filter(id: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrafficMirrorFilterResult:
    """
    Resource Type definition for AWS::EC2::TrafficMirrorFilter
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getTrafficMirrorFilter', __args__, opts=opts, typ=GetTrafficMirrorFilterResult).value

    return AwaitableGetTrafficMirrorFilterResult(
        id=__ret__.id,
        network_services=__ret__.network_services,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_traffic_mirror_filter)
def get_traffic_mirror_filter_output(id: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrafficMirrorFilterResult]:
    """
    Resource Type definition for AWS::EC2::TrafficMirrorFilter
    """
    ...

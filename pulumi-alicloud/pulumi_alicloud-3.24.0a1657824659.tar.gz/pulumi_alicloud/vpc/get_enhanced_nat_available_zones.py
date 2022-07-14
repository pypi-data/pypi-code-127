# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetEnhancedNatAvailableZonesResult',
    'AwaitableGetEnhancedNatAvailableZonesResult',
    'get_enhanced_nat_available_zones',
    'get_enhanced_nat_available_zones_output',
]

@pulumi.output_type
class GetEnhancedNatAvailableZonesResult:
    """
    A collection of values returned by getEnhancedNatAvailableZones.
    """
    def __init__(__self__, id=None, ids=None, output_file=None, zones=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def zones(self) -> Sequence['outputs.GetEnhancedNatAvailableZonesZoneResult']:
        return pulumi.get(self, "zones")


class AwaitableGetEnhancedNatAvailableZonesResult(GetEnhancedNatAvailableZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnhancedNatAvailableZonesResult(
            id=self.id,
            ids=self.ids,
            output_file=self.output_file,
            zones=self.zones)


def get_enhanced_nat_available_zones(output_file: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnhancedNatAvailableZonesResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['outputFile'] = output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:vpc/getEnhancedNatAvailableZones:getEnhancedNatAvailableZones', __args__, opts=opts, typ=GetEnhancedNatAvailableZonesResult).value

    return AwaitableGetEnhancedNatAvailableZonesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        output_file=__ret__.output_file,
        zones=__ret__.zones)


@_utilities.lift_output_func(get_enhanced_nat_available_zones)
def get_enhanced_nat_available_zones_output(output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnhancedNatAvailableZonesResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...

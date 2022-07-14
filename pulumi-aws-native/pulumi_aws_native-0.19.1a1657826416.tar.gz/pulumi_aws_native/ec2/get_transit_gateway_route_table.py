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
    'GetTransitGatewayRouteTableResult',
    'AwaitableGetTransitGatewayRouteTableResult',
    'get_transit_gateway_route_table',
    'get_transit_gateway_route_table_output',
]

@pulumi.output_type
class GetTransitGatewayRouteTableResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetTransitGatewayRouteTableResult(GetTransitGatewayRouteTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitGatewayRouteTableResult(
            id=self.id)


def get_transit_gateway_route_table(id: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitGatewayRouteTableResult:
    """
    Resource Type definition for AWS::EC2::TransitGatewayRouteTable
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getTransitGatewayRouteTable', __args__, opts=opts, typ=GetTransitGatewayRouteTableResult).value

    return AwaitableGetTransitGatewayRouteTableResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_transit_gateway_route_table)
def get_transit_gateway_route_table_output(id: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransitGatewayRouteTableResult]:
    """
    Resource Type definition for AWS::EC2::TransitGatewayRouteTable
    """
    ...

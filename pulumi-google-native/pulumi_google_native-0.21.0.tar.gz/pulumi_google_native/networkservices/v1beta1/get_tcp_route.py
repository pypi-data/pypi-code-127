# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetTcpRouteResult',
    'AwaitableGetTcpRouteResult',
    'get_tcp_route',
    'get_tcp_route_output',
]

@pulumi.output_type
class GetTcpRouteResult:
    def __init__(__self__, create_time=None, description=None, gateways=None, labels=None, meshes=None, name=None, rules=None, self_link=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if gateways and not isinstance(gateways, list):
            raise TypeError("Expected argument 'gateways' to be a list")
        pulumi.set(__self__, "gateways", gateways)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if meshes and not isinstance(meshes, list):
            raise TypeError("Expected argument 'meshes' to be a list")
        pulumi.set(__self__, "meshes", meshes)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rules and not isinstance(rules, list):
            raise TypeError("Expected argument 'rules' to be a list")
        pulumi.set(__self__, "rules", rules)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The timestamp when the resource was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        Optional. A free-text description of the resource. Max length 1024 characters.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def gateways(self) -> Sequence[str]:
        """
        Optional. Gateways defines a list of gateways this TcpRoute is attached to, as one of the routing rules to route the requests served by the gateway. Each gateway reference should match the pattern: `projects/*/locations/global/gateways/`
        """
        return pulumi.get(self, "gateways")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        """
        Optional. Set of label tags associated with the TcpRoute resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def meshes(self) -> Sequence[str]:
        """
        Optional. Meshes defines a list of meshes this TcpRoute is attached to, as one of the routing rules to route the requests served by the mesh. Each mesh reference should match the pattern: `projects/*/locations/global/meshes/` The attached Mesh should be of a type SIDECAR
        """
        return pulumi.get(self, "meshes")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the TcpRoute resource. It matches pattern `projects/*/locations/global/tcpRoutes/tcp_route_name>`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> Sequence['outputs.TcpRouteRouteRuleResponse']:
        """
        Rules that define how traffic is routed and handled. At least one RouteRule must be supplied. If there are multiple rules then the action taken will be the first rule to match.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL of this resource
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The timestamp when the resource was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetTcpRouteResult(GetTcpRouteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTcpRouteResult(
            create_time=self.create_time,
            description=self.description,
            gateways=self.gateways,
            labels=self.labels,
            meshes=self.meshes,
            name=self.name,
            rules=self.rules,
            self_link=self.self_link,
            update_time=self.update_time)


def get_tcp_route(location: Optional[str] = None,
                  project: Optional[str] = None,
                  tcp_route_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTcpRouteResult:
    """
    Gets details of a single TcpRoute.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['project'] = project
    __args__['tcpRouteId'] = tcp_route_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:networkservices/v1beta1:getTcpRoute', __args__, opts=opts, typ=GetTcpRouteResult).value

    return AwaitableGetTcpRouteResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        gateways=__ret__.gateways,
        labels=__ret__.labels,
        meshes=__ret__.meshes,
        name=__ret__.name,
        rules=__ret__.rules,
        self_link=__ret__.self_link,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_tcp_route)
def get_tcp_route_output(location: Optional[pulumi.Input[str]] = None,
                         project: Optional[pulumi.Input[Optional[str]]] = None,
                         tcp_route_id: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTcpRouteResult]:
    """
    Gets details of a single TcpRoute.
    """
    ...

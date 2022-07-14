# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetGatewayResult',
    'AwaitableGetGatewayResult',
    'get_gateway',
    'get_gateway_output',
]

@pulumi.output_type
class GetGatewayResult:
    def __init__(__self__, create_time=None, description=None, labels=None, name=None, ports=None, scope=None, self_link=None, server_tls_policy=None, type=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if ports and not isinstance(ports, list):
            raise TypeError("Expected argument 'ports' to be a list")
        pulumi.set(__self__, "ports", ports)
        if scope and not isinstance(scope, str):
            raise TypeError("Expected argument 'scope' to be a str")
        pulumi.set(__self__, "scope", scope)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if server_tls_policy and not isinstance(server_tls_policy, str):
            raise TypeError("Expected argument 'server_tls_policy' to be a str")
        pulumi.set(__self__, "server_tls_policy", server_tls_policy)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
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
    def labels(self) -> Mapping[str, str]:
        """
        Optional. Set of label tags associated with the Gateway resource.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the Gateway resource. It matches pattern `projects/*/locations/*/gateways/`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def ports(self) -> Sequence[int]:
        """
        One or more ports that the Gateway must receive traffic on. The proxy binds to the ports specified. Gateway listen on 0.0.0.0 on the ports specified below.
        """
        return pulumi.get(self, "ports")

    @property
    @pulumi.getter
    def scope(self) -> str:
        """
        Immutable. Scope determines how configuration across multiple Gateway instances are merged. The configuration for multiple Gateway instances with the same scope will be merged as presented as a single coniguration to the proxy/load balancer. Max length 64 characters. Scope should start with a letter and can only have letters, numbers, hyphens.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL of this resource
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="serverTlsPolicy")
    def server_tls_policy(self) -> str:
        """
        Optional. A fully-qualified ServerTLSPolicy URL reference. Specifies how TLS traffic is terminated. If empty, TLS termination is disabled.
        """
        return pulumi.get(self, "server_tls_policy")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Immutable. The type of the customer managed gateway.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The timestamp when the resource was updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetGatewayResult(GetGatewayResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGatewayResult(
            create_time=self.create_time,
            description=self.description,
            labels=self.labels,
            name=self.name,
            ports=self.ports,
            scope=self.scope,
            self_link=self.self_link,
            server_tls_policy=self.server_tls_policy,
            type=self.type,
            update_time=self.update_time)


def get_gateway(gateway_id: Optional[str] = None,
                location: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGatewayResult:
    """
    Gets details of a single Gateway.
    """
    __args__ = dict()
    __args__['gatewayId'] = gateway_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:networkservices/v1:getGateway', __args__, opts=opts, typ=GetGatewayResult).value

    return AwaitableGetGatewayResult(
        create_time=__ret__.create_time,
        description=__ret__.description,
        labels=__ret__.labels,
        name=__ret__.name,
        ports=__ret__.ports,
        scope=__ret__.scope,
        self_link=__ret__.self_link,
        server_tls_policy=__ret__.server_tls_policy,
        type=__ret__.type,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_gateway)
def get_gateway_output(gateway_id: Optional[pulumi.Input[str]] = None,
                       location: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGatewayResult]:
    """
    Gets details of a single Gateway.
    """
    ...

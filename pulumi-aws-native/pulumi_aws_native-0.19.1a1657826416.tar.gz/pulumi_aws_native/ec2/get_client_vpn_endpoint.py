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
    'GetClientVpnEndpointResult',
    'AwaitableGetClientVpnEndpointResult',
    'get_client_vpn_endpoint',
    'get_client_vpn_endpoint_output',
]

@pulumi.output_type
class GetClientVpnEndpointResult:
    def __init__(__self__, client_connect_options=None, client_login_banner_options=None, connection_log_options=None, description=None, dns_servers=None, id=None, security_group_ids=None, self_service_portal=None, server_certificate_arn=None, session_timeout_hours=None, split_tunnel=None, vpc_id=None, vpn_port=None):
        if client_connect_options and not isinstance(client_connect_options, dict):
            raise TypeError("Expected argument 'client_connect_options' to be a dict")
        pulumi.set(__self__, "client_connect_options", client_connect_options)
        if client_login_banner_options and not isinstance(client_login_banner_options, dict):
            raise TypeError("Expected argument 'client_login_banner_options' to be a dict")
        pulumi.set(__self__, "client_login_banner_options", client_login_banner_options)
        if connection_log_options and not isinstance(connection_log_options, dict):
            raise TypeError("Expected argument 'connection_log_options' to be a dict")
        pulumi.set(__self__, "connection_log_options", connection_log_options)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if dns_servers and not isinstance(dns_servers, list):
            raise TypeError("Expected argument 'dns_servers' to be a list")
        pulumi.set(__self__, "dns_servers", dns_servers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if security_group_ids and not isinstance(security_group_ids, list):
            raise TypeError("Expected argument 'security_group_ids' to be a list")
        pulumi.set(__self__, "security_group_ids", security_group_ids)
        if self_service_portal and not isinstance(self_service_portal, str):
            raise TypeError("Expected argument 'self_service_portal' to be a str")
        pulumi.set(__self__, "self_service_portal", self_service_portal)
        if server_certificate_arn and not isinstance(server_certificate_arn, str):
            raise TypeError("Expected argument 'server_certificate_arn' to be a str")
        pulumi.set(__self__, "server_certificate_arn", server_certificate_arn)
        if session_timeout_hours and not isinstance(session_timeout_hours, int):
            raise TypeError("Expected argument 'session_timeout_hours' to be a int")
        pulumi.set(__self__, "session_timeout_hours", session_timeout_hours)
        if split_tunnel and not isinstance(split_tunnel, bool):
            raise TypeError("Expected argument 'split_tunnel' to be a bool")
        pulumi.set(__self__, "split_tunnel", split_tunnel)
        if vpc_id and not isinstance(vpc_id, str):
            raise TypeError("Expected argument 'vpc_id' to be a str")
        pulumi.set(__self__, "vpc_id", vpc_id)
        if vpn_port and not isinstance(vpn_port, int):
            raise TypeError("Expected argument 'vpn_port' to be a int")
        pulumi.set(__self__, "vpn_port", vpn_port)

    @property
    @pulumi.getter(name="clientConnectOptions")
    def client_connect_options(self) -> Optional['outputs.ClientVpnEndpointClientConnectOptions']:
        return pulumi.get(self, "client_connect_options")

    @property
    @pulumi.getter(name="clientLoginBannerOptions")
    def client_login_banner_options(self) -> Optional['outputs.ClientVpnEndpointClientLoginBannerOptions']:
        return pulumi.get(self, "client_login_banner_options")

    @property
    @pulumi.getter(name="connectionLogOptions")
    def connection_log_options(self) -> Optional['outputs.ClientVpnEndpointConnectionLogOptions']:
        return pulumi.get(self, "connection_log_options")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsServers")
    def dns_servers(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "dns_servers")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="securityGroupIds")
    def security_group_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "security_group_ids")

    @property
    @pulumi.getter(name="selfServicePortal")
    def self_service_portal(self) -> Optional[str]:
        return pulumi.get(self, "self_service_portal")

    @property
    @pulumi.getter(name="serverCertificateArn")
    def server_certificate_arn(self) -> Optional[str]:
        return pulumi.get(self, "server_certificate_arn")

    @property
    @pulumi.getter(name="sessionTimeoutHours")
    def session_timeout_hours(self) -> Optional[int]:
        return pulumi.get(self, "session_timeout_hours")

    @property
    @pulumi.getter(name="splitTunnel")
    def split_tunnel(self) -> Optional[bool]:
        return pulumi.get(self, "split_tunnel")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> Optional[str]:
        return pulumi.get(self, "vpc_id")

    @property
    @pulumi.getter(name="vpnPort")
    def vpn_port(self) -> Optional[int]:
        return pulumi.get(self, "vpn_port")


class AwaitableGetClientVpnEndpointResult(GetClientVpnEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClientVpnEndpointResult(
            client_connect_options=self.client_connect_options,
            client_login_banner_options=self.client_login_banner_options,
            connection_log_options=self.connection_log_options,
            description=self.description,
            dns_servers=self.dns_servers,
            id=self.id,
            security_group_ids=self.security_group_ids,
            self_service_portal=self.self_service_portal,
            server_certificate_arn=self.server_certificate_arn,
            session_timeout_hours=self.session_timeout_hours,
            split_tunnel=self.split_tunnel,
            vpc_id=self.vpc_id,
            vpn_port=self.vpn_port)


def get_client_vpn_endpoint(id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClientVpnEndpointResult:
    """
    Resource Type definition for AWS::EC2::ClientVpnEndpoint
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getClientVpnEndpoint', __args__, opts=opts, typ=GetClientVpnEndpointResult).value

    return AwaitableGetClientVpnEndpointResult(
        client_connect_options=__ret__.client_connect_options,
        client_login_banner_options=__ret__.client_login_banner_options,
        connection_log_options=__ret__.connection_log_options,
        description=__ret__.description,
        dns_servers=__ret__.dns_servers,
        id=__ret__.id,
        security_group_ids=__ret__.security_group_ids,
        self_service_portal=__ret__.self_service_portal,
        server_certificate_arn=__ret__.server_certificate_arn,
        session_timeout_hours=__ret__.session_timeout_hours,
        split_tunnel=__ret__.split_tunnel,
        vpc_id=__ret__.vpc_id,
        vpn_port=__ret__.vpn_port)


@_utilities.lift_output_func(get_client_vpn_endpoint)
def get_client_vpn_endpoint_output(id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClientVpnEndpointResult]:
    """
    Resource Type definition for AWS::EC2::ClientVpnEndpoint
    """
    ...

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
    'GetRouterResult',
    'AwaitableGetRouterResult',
    'get_router',
    'get_router_output',
]

@pulumi.output_type
class GetRouterResult:
    def __init__(__self__, bgp=None, bgp_peers=None, creation_timestamp=None, description=None, encrypted_interconnect_router=None, interfaces=None, kind=None, md5_authentication_keys=None, name=None, nats=None, network=None, region=None, self_link=None, self_link_with_id=None):
        if bgp and not isinstance(bgp, dict):
            raise TypeError("Expected argument 'bgp' to be a dict")
        pulumi.set(__self__, "bgp", bgp)
        if bgp_peers and not isinstance(bgp_peers, list):
            raise TypeError("Expected argument 'bgp_peers' to be a list")
        pulumi.set(__self__, "bgp_peers", bgp_peers)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if encrypted_interconnect_router and not isinstance(encrypted_interconnect_router, bool):
            raise TypeError("Expected argument 'encrypted_interconnect_router' to be a bool")
        pulumi.set(__self__, "encrypted_interconnect_router", encrypted_interconnect_router)
        if interfaces and not isinstance(interfaces, list):
            raise TypeError("Expected argument 'interfaces' to be a list")
        pulumi.set(__self__, "interfaces", interfaces)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if md5_authentication_keys and not isinstance(md5_authentication_keys, list):
            raise TypeError("Expected argument 'md5_authentication_keys' to be a list")
        pulumi.set(__self__, "md5_authentication_keys", md5_authentication_keys)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if nats and not isinstance(nats, list):
            raise TypeError("Expected argument 'nats' to be a list")
        pulumi.set(__self__, "nats", nats)
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        pulumi.set(__self__, "network", network)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if self_link_with_id and not isinstance(self_link_with_id, str):
            raise TypeError("Expected argument 'self_link_with_id' to be a str")
        pulumi.set(__self__, "self_link_with_id", self_link_with_id)

    @property
    @pulumi.getter
    def bgp(self) -> 'outputs.RouterBgpResponse':
        """
        BGP information specific to this router.
        """
        return pulumi.get(self, "bgp")

    @property
    @pulumi.getter(name="bgpPeers")
    def bgp_peers(self) -> Sequence['outputs.RouterBgpPeerResponse']:
        """
        BGP information that must be configured into the routing stack to establish BGP peering. This information must specify the peer ASN and either the interface name, IP address, or peer IP address. Please refer to RFC4273.
        """
        return pulumi.get(self, "bgp_peers")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="encryptedInterconnectRouter")
    def encrypted_interconnect_router(self) -> bool:
        """
        Indicates if a router is dedicated for use with encrypted VLAN attachments (interconnectAttachments). Not currently available publicly. 
        """
        return pulumi.get(self, "encrypted_interconnect_router")

    @property
    @pulumi.getter
    def interfaces(self) -> Sequence['outputs.RouterInterfaceResponse']:
        """
        Router interfaces. Each interface requires either one linked resource, (for example, linkedVpnTunnel), or IP address and IP address range (for example, ipRange), or both.
        """
        return pulumi.get(self, "interfaces")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of resource. Always compute#router for routers.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="md5AuthenticationKeys")
    def md5_authentication_keys(self) -> Sequence['outputs.RouterMd5AuthenticationKeyResponse']:
        """
        Keys used for MD5 authentication.
        """
        return pulumi.get(self, "md5_authentication_keys")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def nats(self) -> Sequence['outputs.RouterNatResponse']:
        """
        A list of NAT services created in this router.
        """
        return pulumi.get(self, "nats")

    @property
    @pulumi.getter
    def network(self) -> str:
        """
        URI of the network to which this router belongs.
        """
        return pulumi.get(self, "network")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        URI of the region where the router resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="selfLinkWithId")
    def self_link_with_id(self) -> str:
        """
        Server-defined URL for this resource with the resource id.
        """
        return pulumi.get(self, "self_link_with_id")


class AwaitableGetRouterResult(GetRouterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRouterResult(
            bgp=self.bgp,
            bgp_peers=self.bgp_peers,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            encrypted_interconnect_router=self.encrypted_interconnect_router,
            interfaces=self.interfaces,
            kind=self.kind,
            md5_authentication_keys=self.md5_authentication_keys,
            name=self.name,
            nats=self.nats,
            network=self.network,
            region=self.region,
            self_link=self.self_link,
            self_link_with_id=self.self_link_with_id)


def get_router(project: Optional[str] = None,
               region: Optional[str] = None,
               router: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRouterResult:
    """
    Returns the specified Router resource. Gets a list of available routers by making a list() request.
    """
    __args__ = dict()
    __args__['project'] = project
    __args__['region'] = region
    __args__['router'] = router
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/alpha:getRouter', __args__, opts=opts, typ=GetRouterResult).value

    return AwaitableGetRouterResult(
        bgp=__ret__.bgp,
        bgp_peers=__ret__.bgp_peers,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        encrypted_interconnect_router=__ret__.encrypted_interconnect_router,
        interfaces=__ret__.interfaces,
        kind=__ret__.kind,
        md5_authentication_keys=__ret__.md5_authentication_keys,
        name=__ret__.name,
        nats=__ret__.nats,
        network=__ret__.network,
        region=__ret__.region,
        self_link=__ret__.self_link,
        self_link_with_id=__ret__.self_link_with_id)


@_utilities.lift_output_func(get_router)
def get_router_output(project: Optional[pulumi.Input[Optional[str]]] = None,
                      region: Optional[pulumi.Input[str]] = None,
                      router: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRouterResult]:
    """
    Returns the specified Router resource. Gets a list of available routers by making a list() request.
    """
    ...

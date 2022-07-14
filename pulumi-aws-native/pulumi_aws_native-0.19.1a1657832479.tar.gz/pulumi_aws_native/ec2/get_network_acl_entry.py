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
    'GetNetworkAclEntryResult',
    'AwaitableGetNetworkAclEntryResult',
    'get_network_acl_entry',
    'get_network_acl_entry_output',
]

@pulumi.output_type
class GetNetworkAclEntryResult:
    def __init__(__self__, cidr_block=None, icmp=None, id=None, ipv6_cidr_block=None, port_range=None, protocol=None, rule_action=None):
        if cidr_block and not isinstance(cidr_block, str):
            raise TypeError("Expected argument 'cidr_block' to be a str")
        pulumi.set(__self__, "cidr_block", cidr_block)
        if icmp and not isinstance(icmp, dict):
            raise TypeError("Expected argument 'icmp' to be a dict")
        pulumi.set(__self__, "icmp", icmp)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ipv6_cidr_block and not isinstance(ipv6_cidr_block, str):
            raise TypeError("Expected argument 'ipv6_cidr_block' to be a str")
        pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        if port_range and not isinstance(port_range, dict):
            raise TypeError("Expected argument 'port_range' to be a dict")
        pulumi.set(__self__, "port_range", port_range)
        if protocol and not isinstance(protocol, int):
            raise TypeError("Expected argument 'protocol' to be a int")
        pulumi.set(__self__, "protocol", protocol)
        if rule_action and not isinstance(rule_action, str):
            raise TypeError("Expected argument 'rule_action' to be a str")
        pulumi.set(__self__, "rule_action", rule_action)

    @property
    @pulumi.getter(name="cidrBlock")
    def cidr_block(self) -> Optional[str]:
        """
        The IPv4 CIDR range to allow or deny, in CIDR notation (for example, 172.16.0.0/24). Requirement is conditional: You must specify the CidrBlock or Ipv6CidrBlock property
        """
        return pulumi.get(self, "cidr_block")

    @property
    @pulumi.getter
    def icmp(self) -> Optional['outputs.NetworkAclEntryIcmp']:
        """
        The Internet Control Message Protocol (ICMP) code and type. Requirement is conditional: Required if specifying 1 (ICMP) for the protocol parameter
        """
        return pulumi.get(self, "icmp")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> Optional[str]:
        """
        The IPv6 network range to allow or deny, in CIDR notation (for example 2001:db8:1234:1a00::/64)
        """
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional['outputs.NetworkAclEntryPortRange']:
        """
        The IPv4 network range to allow or deny, in CIDR notation (for example 172.16.0.0/24). We modify the specified CIDR block to its canonical form; for example, if you specify 100.68.0.18/18, we modify it to 100.68.0.0/18
        """
        return pulumi.get(self, "port_range")

    @property
    @pulumi.getter
    def protocol(self) -> Optional[int]:
        """
        The protocol number. A value of "-1" means all protocols. If you specify "-1" or a protocol number other than "6" (TCP), "17" (UDP), or "1" (ICMP), traffic on all ports is allowed, regardless of any ports or ICMP types or codes that you specify. If you specify protocol "58" (ICMPv6) and specify an IPv4 CIDR block, traffic for all ICMP types and codes allowed, regardless of any that you specify. If you specify protocol "58" (ICMPv6) and specify an IPv6 CIDR block, you must specify an ICMP type and code
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="ruleAction")
    def rule_action(self) -> Optional[str]:
        """
        Indicates whether to allow or deny the traffic that matches the rule
        """
        return pulumi.get(self, "rule_action")


class AwaitableGetNetworkAclEntryResult(GetNetworkAclEntryResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkAclEntryResult(
            cidr_block=self.cidr_block,
            icmp=self.icmp,
            id=self.id,
            ipv6_cidr_block=self.ipv6_cidr_block,
            port_range=self.port_range,
            protocol=self.protocol,
            rule_action=self.rule_action)


def get_network_acl_entry(id: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkAclEntryResult:
    """
    Resource Type definition for AWS::EC2::NetworkAclEntry
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ec2:getNetworkAclEntry', __args__, opts=opts, typ=GetNetworkAclEntryResult).value

    return AwaitableGetNetworkAclEntryResult(
        cidr_block=__ret__.cidr_block,
        icmp=__ret__.icmp,
        id=__ret__.id,
        ipv6_cidr_block=__ret__.ipv6_cidr_block,
        port_range=__ret__.port_range,
        protocol=__ret__.protocol,
        rule_action=__ret__.rule_action)


@_utilities.lift_output_func(get_network_acl_entry)
def get_network_acl_entry_output(id: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNetworkAclEntryResult]:
    """
    Resource Type definition for AWS::EC2::NetworkAclEntry
    """
    ...

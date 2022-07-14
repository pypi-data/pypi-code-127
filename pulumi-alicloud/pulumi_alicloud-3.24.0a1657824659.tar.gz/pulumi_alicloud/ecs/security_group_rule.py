# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SecurityGroupRuleArgs', 'SecurityGroupRule']

@pulumi.input_type
class SecurityGroupRuleArgs:
    def __init__(__self__, *,
                 ip_protocol: pulumi.Input[str],
                 security_group_id: pulumi.Input[str],
                 type: pulumi.Input[str],
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_ip: Optional[pulumi.Input[str]] = None,
                 nic_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[str]] = None,
                 prefix_list_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 source_group_owner_account: Optional[pulumi.Input[str]] = None,
                 source_security_group_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SecurityGroupRule resource.
        :param pulumi.Input[str] ip_protocol: The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        :param pulumi.Input[str] security_group_id: The security group to apply this rule to.
        :param pulumi.Input[str] type: The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        :param pulumi.Input[str] cidr_ip: The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        :param pulumi.Input[str] description: The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        :param pulumi.Input[str] ipv6_cidr_ip: Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        :param pulumi.Input[str] nic_type: Network type, can be either `internet` or `intranet`, the default value is `internet`.
        :param pulumi.Input[str] policy: Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        :param pulumi.Input[str] port_range: The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
               For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        :param pulumi.Input[str] prefix_list_id: The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        :param pulumi.Input[int] priority: Authorization policy priority, with parameter values: `1-100`, default value: 1.
        :param pulumi.Input[str] source_group_owner_account: The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        :param pulumi.Input[str] source_security_group_id: The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        """
        pulumi.set(__self__, "ip_protocol", ip_protocol)
        pulumi.set(__self__, "security_group_id", security_group_id)
        pulumi.set(__self__, "type", type)
        if cidr_ip is not None:
            pulumi.set(__self__, "cidr_ip", cidr_ip)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ipv6_cidr_ip is not None:
            pulumi.set(__self__, "ipv6_cidr_ip", ipv6_cidr_ip)
        if nic_type is not None:
            pulumi.set(__self__, "nic_type", nic_type)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if port_range is not None:
            pulumi.set(__self__, "port_range", port_range)
        if prefix_list_id is not None:
            pulumi.set(__self__, "prefix_list_id", prefix_list_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if source_group_owner_account is not None:
            pulumi.set(__self__, "source_group_owner_account", source_group_owner_account)
        if source_security_group_id is not None:
            pulumi.set(__self__, "source_security_group_id", source_security_group_id)

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Input[str]:
        """
        The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        """
        return pulumi.get(self, "ip_protocol")

    @ip_protocol.setter
    def ip_protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "ip_protocol", value)

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Input[str]:
        """
        The security group to apply this rule to.
        """
        return pulumi.get(self, "security_group_id")

    @security_group_id.setter
    def security_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "security_group_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="cidrIp")
    def cidr_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        """
        return pulumi.get(self, "cidr_ip")

    @cidr_ip.setter
    def cidr_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_ip", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ipv6CidrIp")
    def ipv6_cidr_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        """
        return pulumi.get(self, "ipv6_cidr_ip")

    @ipv6_cidr_ip.setter
    def ipv6_cidr_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr_ip", value)

    @property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[pulumi.Input[str]]:
        """
        Network type, can be either `internet` or `intranet`, the default value is `internet`.
        """
        return pulumi.get(self, "nic_type")

    @nic_type.setter
    def nic_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nic_type", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input[str]]:
        """
        The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
        For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        """
        return pulumi.get(self, "port_range")

    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_range", value)

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        """
        return pulumi.get(self, "prefix_list_id")

    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Authorization policy priority, with parameter values: `1-100`, default value: 1.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="sourceGroupOwnerAccount")
    def source_group_owner_account(self) -> Optional[pulumi.Input[str]]:
        """
        The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        """
        return pulumi.get(self, "source_group_owner_account")

    @source_group_owner_account.setter
    def source_group_owner_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_group_owner_account", value)

    @property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        """
        return pulumi.get(self, "source_security_group_id")

    @source_security_group_id.setter
    def source_security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_security_group_id", value)


@pulumi.input_type
class _SecurityGroupRuleState:
    def __init__(__self__, *,
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_ip: Optional[pulumi.Input[str]] = None,
                 nic_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[str]] = None,
                 prefix_list_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 source_group_owner_account: Optional[pulumi.Input[str]] = None,
                 source_security_group_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SecurityGroupRule resources.
        :param pulumi.Input[str] cidr_ip: The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        :param pulumi.Input[str] description: The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        :param pulumi.Input[str] ip_protocol: The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        :param pulumi.Input[str] ipv6_cidr_ip: Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        :param pulumi.Input[str] nic_type: Network type, can be either `internet` or `intranet`, the default value is `internet`.
        :param pulumi.Input[str] policy: Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        :param pulumi.Input[str] port_range: The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
               For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        :param pulumi.Input[str] prefix_list_id: The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        :param pulumi.Input[int] priority: Authorization policy priority, with parameter values: `1-100`, default value: 1.
        :param pulumi.Input[str] security_group_id: The security group to apply this rule to.
        :param pulumi.Input[str] source_group_owner_account: The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        :param pulumi.Input[str] source_security_group_id: The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        :param pulumi.Input[str] type: The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        """
        if cidr_ip is not None:
            pulumi.set(__self__, "cidr_ip", cidr_ip)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if ip_protocol is not None:
            pulumi.set(__self__, "ip_protocol", ip_protocol)
        if ipv6_cidr_ip is not None:
            pulumi.set(__self__, "ipv6_cidr_ip", ipv6_cidr_ip)
        if nic_type is not None:
            pulumi.set(__self__, "nic_type", nic_type)
        if policy is not None:
            pulumi.set(__self__, "policy", policy)
        if port_range is not None:
            pulumi.set(__self__, "port_range", port_range)
        if prefix_list_id is not None:
            pulumi.set(__self__, "prefix_list_id", prefix_list_id)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if security_group_id is not None:
            pulumi.set(__self__, "security_group_id", security_group_id)
        if source_group_owner_account is not None:
            pulumi.set(__self__, "source_group_owner_account", source_group_owner_account)
        if source_security_group_id is not None:
            pulumi.set(__self__, "source_security_group_id", source_security_group_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="cidrIp")
    def cidr_ip(self) -> Optional[pulumi.Input[str]]:
        """
        The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        """
        return pulumi.get(self, "cidr_ip")

    @cidr_ip.setter
    def cidr_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cidr_ip", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        """
        return pulumi.get(self, "ip_protocol")

    @ip_protocol.setter
    def ip_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_protocol", value)

    @property
    @pulumi.getter(name="ipv6CidrIp")
    def ipv6_cidr_ip(self) -> Optional[pulumi.Input[str]]:
        """
        Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        """
        return pulumi.get(self, "ipv6_cidr_ip")

    @ipv6_cidr_ip.setter
    def ipv6_cidr_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_cidr_ip", value)

    @property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> Optional[pulumi.Input[str]]:
        """
        Network type, can be either `internet` or `intranet`, the default value is `internet`.
        """
        return pulumi.get(self, "nic_type")

    @nic_type.setter
    def nic_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nic_type", value)

    @property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        """
        return pulumi.get(self, "policy")

    @policy.setter
    def policy(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy", value)

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> Optional[pulumi.Input[str]]:
        """
        The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
        For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        """
        return pulumi.get(self, "port_range")

    @port_range.setter
    def port_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "port_range", value)

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        """
        return pulumi.get(self, "prefix_list_id")

    @prefix_list_id.setter
    def prefix_list_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "prefix_list_id", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Authorization policy priority, with parameter values: `1-100`, default value: 1.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The security group to apply this rule to.
        """
        return pulumi.get(self, "security_group_id")

    @security_group_id.setter
    def security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "security_group_id", value)

    @property
    @pulumi.getter(name="sourceGroupOwnerAccount")
    def source_group_owner_account(self) -> Optional[pulumi.Input[str]]:
        """
        The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        """
        return pulumi.get(self, "source_group_owner_account")

    @source_group_owner_account.setter
    def source_group_owner_account(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_group_owner_account", value)

    @property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        """
        return pulumi.get(self, "source_security_group_id")

    @source_security_group_id.setter
    def source_security_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_security_group_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class SecurityGroupRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_ip: Optional[pulumi.Input[str]] = None,
                 nic_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[str]] = None,
                 prefix_list_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 source_group_owner_account: Optional[pulumi.Input[str]] = None,
                 source_security_group_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a SecurityGroupRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_ip: The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        :param pulumi.Input[str] description: The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        :param pulumi.Input[str] ip_protocol: The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        :param pulumi.Input[str] ipv6_cidr_ip: Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        :param pulumi.Input[str] nic_type: Network type, can be either `internet` or `intranet`, the default value is `internet`.
        :param pulumi.Input[str] policy: Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        :param pulumi.Input[str] port_range: The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
               For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        :param pulumi.Input[str] prefix_list_id: The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        :param pulumi.Input[int] priority: Authorization policy priority, with parameter values: `1-100`, default value: 1.
        :param pulumi.Input[str] security_group_id: The security group to apply this rule to.
        :param pulumi.Input[str] source_group_owner_account: The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        :param pulumi.Input[str] source_security_group_id: The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        :param pulumi.Input[str] type: The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SecurityGroupRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a SecurityGroupRule resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param SecurityGroupRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SecurityGroupRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cidr_ip: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 ip_protocol: Optional[pulumi.Input[str]] = None,
                 ipv6_cidr_ip: Optional[pulumi.Input[str]] = None,
                 nic_type: Optional[pulumi.Input[str]] = None,
                 policy: Optional[pulumi.Input[str]] = None,
                 port_range: Optional[pulumi.Input[str]] = None,
                 prefix_list_id: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 security_group_id: Optional[pulumi.Input[str]] = None,
                 source_group_owner_account: Optional[pulumi.Input[str]] = None,
                 source_security_group_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SecurityGroupRuleArgs.__new__(SecurityGroupRuleArgs)

            __props__.__dict__["cidr_ip"] = cidr_ip
            __props__.__dict__["description"] = description
            if ip_protocol is None and not opts.urn:
                raise TypeError("Missing required property 'ip_protocol'")
            __props__.__dict__["ip_protocol"] = ip_protocol
            __props__.__dict__["ipv6_cidr_ip"] = ipv6_cidr_ip
            __props__.__dict__["nic_type"] = nic_type
            __props__.__dict__["policy"] = policy
            __props__.__dict__["port_range"] = port_range
            __props__.__dict__["prefix_list_id"] = prefix_list_id
            __props__.__dict__["priority"] = priority
            if security_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'security_group_id'")
            __props__.__dict__["security_group_id"] = security_group_id
            __props__.__dict__["source_group_owner_account"] = source_group_owner_account
            __props__.__dict__["source_security_group_id"] = source_security_group_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
        super(SecurityGroupRule, __self__).__init__(
            'alicloud:ecs/securityGroupRule:SecurityGroupRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cidr_ip: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ip_protocol: Optional[pulumi.Input[str]] = None,
            ipv6_cidr_ip: Optional[pulumi.Input[str]] = None,
            nic_type: Optional[pulumi.Input[str]] = None,
            policy: Optional[pulumi.Input[str]] = None,
            port_range: Optional[pulumi.Input[str]] = None,
            prefix_list_id: Optional[pulumi.Input[str]] = None,
            priority: Optional[pulumi.Input[int]] = None,
            security_group_id: Optional[pulumi.Input[str]] = None,
            source_group_owner_account: Optional[pulumi.Input[str]] = None,
            source_security_group_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'SecurityGroupRule':
        """
        Get an existing SecurityGroupRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr_ip: The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        :param pulumi.Input[str] description: The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        :param pulumi.Input[str] ip_protocol: The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        :param pulumi.Input[str] ipv6_cidr_ip: Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        :param pulumi.Input[str] nic_type: Network type, can be either `internet` or `intranet`, the default value is `internet`.
        :param pulumi.Input[str] policy: Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        :param pulumi.Input[str] port_range: The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
               For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        :param pulumi.Input[str] prefix_list_id: The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        :param pulumi.Input[int] priority: Authorization policy priority, with parameter values: `1-100`, default value: 1.
        :param pulumi.Input[str] security_group_id: The security group to apply this rule to.
        :param pulumi.Input[str] source_group_owner_account: The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        :param pulumi.Input[str] source_security_group_id: The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        :param pulumi.Input[str] type: The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SecurityGroupRuleState.__new__(_SecurityGroupRuleState)

        __props__.__dict__["cidr_ip"] = cidr_ip
        __props__.__dict__["description"] = description
        __props__.__dict__["ip_protocol"] = ip_protocol
        __props__.__dict__["ipv6_cidr_ip"] = ipv6_cidr_ip
        __props__.__dict__["nic_type"] = nic_type
        __props__.__dict__["policy"] = policy
        __props__.__dict__["port_range"] = port_range
        __props__.__dict__["prefix_list_id"] = prefix_list_id
        __props__.__dict__["priority"] = priority
        __props__.__dict__["security_group_id"] = security_group_id
        __props__.__dict__["source_group_owner_account"] = source_group_owner_account
        __props__.__dict__["source_security_group_id"] = source_security_group_id
        __props__.__dict__["type"] = type
        return SecurityGroupRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cidrIp")
    def cidr_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The target IP address range. The default value is 0.0.0.0/0 (which means no restriction will be applied). Other supported formats include 10.159.6.18/12. Only IPv4 is supported.
        """
        return pulumi.get(self, "cidr_ip")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the security group rule. The description can be up to 1 to 512 characters in length. Defaults to null.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipProtocol")
    def ip_protocol(self) -> pulumi.Output[str]:
        """
        The protocol. Can be `tcp`, `udp`, `icmp`, `gre` or `all`.
        """
        return pulumi.get(self, "ip_protocol")

    @property
    @pulumi.getter(name="ipv6CidrIp")
    def ipv6_cidr_ip(self) -> pulumi.Output[Optional[str]]:
        """
        Source IPv6 CIDR address block that requires access. Supports IP address ranges in CIDR format and IPv6 format. **NOTE:** This parameter cannot be set at the same time as the `cidr_ip` parameter.
        """
        return pulumi.get(self, "ipv6_cidr_ip")

    @property
    @pulumi.getter(name="nicType")
    def nic_type(self) -> pulumi.Output[str]:
        """
        Network type, can be either `internet` or `intranet`, the default value is `internet`.
        """
        return pulumi.get(self, "nic_type")

    @property
    @pulumi.getter
    def policy(self) -> pulumi.Output[Optional[str]]:
        """
        Authorization policy, can be either `accept` or `drop`, the default value is `accept`.
        """
        return pulumi.get(self, "policy")

    @property
    @pulumi.getter(name="portRange")
    def port_range(self) -> pulumi.Output[Optional[str]]:
        """
        The range of port numbers relevant to the IP protocol. Default to "-1/-1". When the protocol is tcp or udp, each side port number range from 1 to 65535 and '-1/-1' will be invalid.
        For example, `1/200` means that the range of the port numbers is 1-200. Other protocols' 'port_range' can only be "-1/-1", and other values will be invalid.
        """
        return pulumi.get(self, "port_range")

    @property
    @pulumi.getter(name="prefixListId")
    def prefix_list_id(self) -> pulumi.Output[str]:
        """
        The ID of the source/destination prefix list to which you want to control access. **NOTE:** If you specify `cidr_ip`,`source_security_group_id`,`ipv6_cidr_ip` parameter, this parameter is ignored.
        """
        return pulumi.get(self, "prefix_list_id")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Authorization policy priority, with parameter values: `1-100`, default value: 1.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="securityGroupId")
    def security_group_id(self) -> pulumi.Output[str]:
        """
        The security group to apply this rule to.
        """
        return pulumi.get(self, "security_group_id")

    @property
    @pulumi.getter(name="sourceGroupOwnerAccount")
    def source_group_owner_account(self) -> pulumi.Output[Optional[str]]:
        """
        The Alibaba Cloud user account Id of the target security group when security groups are authorized across accounts.  This parameter is invalid if `cidr_ip` has already been set.
        """
        return pulumi.get(self, "source_group_owner_account")

    @property
    @pulumi.getter(name="sourceSecurityGroupId")
    def source_security_group_id(self) -> pulumi.Output[Optional[str]]:
        """
        The target security group ID within the same region. If this field is specified, the `nic_type` can only select `intranet`.
        """
        return pulumi.get(self, "source_security_group_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of rule being created. Valid options are `ingress` (inbound) or `egress` (outbound).
        """
        return pulumi.get(self, "type")


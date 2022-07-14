# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SubnetCidrBlockArgs', 'SubnetCidrBlock']

@pulumi.input_type
class SubnetCidrBlockArgs:
    def __init__(__self__, *,
                 ipv6_cidr_block: pulumi.Input[str],
                 subnet_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a SubnetCidrBlock resource.
        """
        pulumi.set(__self__, "ipv6_cidr_block", ipv6_cidr_block)
        pulumi.set(__self__, "subnet_id", subnet_id)

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ipv6_cidr_block")

    @ipv6_cidr_block.setter
    def ipv6_cidr_block(self, value: pulumi.Input[str]):
        pulumi.set(self, "ipv6_cidr_block", value)

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "subnet_id")

    @subnet_id.setter
    def subnet_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "subnet_id", value)


warnings.warn("""SubnetCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class SubnetCidrBlock(pulumi.CustomResource):
    warnings.warn("""SubnetCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::SubnetCidrBlock

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubnetCidrBlockArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::SubnetCidrBlock

        :param str resource_name: The name of the resource.
        :param SubnetCidrBlockArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubnetCidrBlockArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ipv6_cidr_block: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SubnetCidrBlock is deprecated: SubnetCidrBlock is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        if opts is None:
            opts = pulumi.ResourceOptions()
        else:
            opts = copy.copy(opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubnetCidrBlockArgs.__new__(SubnetCidrBlockArgs)

            if ipv6_cidr_block is None and not opts.urn:
                raise TypeError("Missing required property 'ipv6_cidr_block'")
            __props__.__dict__["ipv6_cidr_block"] = ipv6_cidr_block
            if subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'subnet_id'")
            __props__.__dict__["subnet_id"] = subnet_id
        super(SubnetCidrBlock, __self__).__init__(
            'aws-native:ec2:SubnetCidrBlock',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SubnetCidrBlock':
        """
        Get an existing SubnetCidrBlock resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubnetCidrBlockArgs.__new__(SubnetCidrBlockArgs)

        __props__.__dict__["ipv6_cidr_block"] = None
        __props__.__dict__["subnet_id"] = None
        return SubnetCidrBlock(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipv6CidrBlock")
    def ipv6_cidr_block(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ipv6_cidr_block")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "subnet_id")


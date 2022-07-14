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
from ._inputs import *

__all__ = ['InternetGatewayArgs', 'InternetGateway']

@pulumi.input_type
class InternetGatewayArgs:
    def __init__(__self__, *,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['InternetGatewayTagArgs']]]] = None):
        """
        The set of arguments for constructing a InternetGateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['InternetGatewayTagArgs']]] tags: Any tags to assign to the internet gateway.
        """
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['InternetGatewayTagArgs']]]]:
        """
        Any tags to assign to the internet gateway.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['InternetGatewayTagArgs']]]]):
        pulumi.set(self, "tags", value)


class InternetGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InternetGatewayTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::EC2::InternetGateway

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InternetGatewayTagArgs']]]] tags: Any tags to assign to the internet gateway.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[InternetGatewayArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::EC2::InternetGateway

        :param str resource_name: The name of the resource.
        :param InternetGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InternetGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['InternetGatewayTagArgs']]]]] = None,
                 __props__=None):
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
            __props__ = InternetGatewayArgs.__new__(InternetGatewayArgs)

            __props__.__dict__["tags"] = tags
            __props__.__dict__["internet_gateway_id"] = None
        super(InternetGateway, __self__).__init__(
            'aws-native:ec2:InternetGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InternetGateway':
        """
        Get an existing InternetGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InternetGatewayArgs.__new__(InternetGatewayArgs)

        __props__.__dict__["internet_gateway_id"] = None
        __props__.__dict__["tags"] = None
        return InternetGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="internetGatewayId")
    def internet_gateway_id(self) -> pulumi.Output[str]:
        """
        ID of internet gateway.
        """
        return pulumi.get(self, "internet_gateway_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.InternetGatewayTag']]]:
        """
        Any tags to assign to the internet gateway.
        """
        return pulumi.get(self, "tags")


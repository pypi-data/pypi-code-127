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

__all__ = ['GlobalNetworkArgs', 'GlobalNetwork']

@pulumi.input_type
class GlobalNetworkArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalNetworkTagArgs']]]] = None):
        """
        The set of arguments for constructing a GlobalNetwork resource.
        :param pulumi.Input[str] description: The description of the global network.
        :param pulumi.Input[Sequence[pulumi.Input['GlobalNetworkTagArgs']]] tags: The tags for the global network.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the global network.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GlobalNetworkTagArgs']]]]:
        """
        The tags for the global network.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GlobalNetworkTagArgs']]]]):
        pulumi.set(self, "tags", value)


class GlobalNetwork(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalNetworkTagArgs']]]]] = None,
                 __props__=None):
        """
        The AWS::NetworkManager::GlobalNetwork type specifies a global network of the user's account

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the global network.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalNetworkTagArgs']]]] tags: The tags for the global network.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[GlobalNetworkArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The AWS::NetworkManager::GlobalNetwork type specifies a global network of the user's account

        :param str resource_name: The name of the resource.
        :param GlobalNetworkArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalNetworkArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GlobalNetworkTagArgs']]]]] = None,
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
            __props__ = GlobalNetworkArgs.__new__(GlobalNetworkArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(GlobalNetwork, __self__).__init__(
            'aws-native:networkmanager:GlobalNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GlobalNetwork':
        """
        Get an existing GlobalNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GlobalNetworkArgs.__new__(GlobalNetworkArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["tags"] = None
        return GlobalNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the global network.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the global network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.GlobalNetworkTag']]]:
        """
        The tags for the global network.
        """
        return pulumi.get(self, "tags")


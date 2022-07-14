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

__all__ = ['ParameterGroupArgs', 'ParameterGroup']

@pulumi.input_type
class ParameterGroupArgs:
    def __init__(__self__, *,
                 cache_parameter_group_family: pulumi.Input[str],
                 description: pulumi.Input[str],
                 properties: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]]] = None):
        """
        The set of arguments for constructing a ParameterGroup resource.
        """
        pulumi.set(__self__, "cache_parameter_group_family", cache_parameter_group_family)
        pulumi.set(__self__, "description", description)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cacheParameterGroupFamily")
    def cache_parameter_group_family(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cache_parameter_group_family")

    @cache_parameter_group_family.setter
    def cache_parameter_group_family(self, value: pulumi.Input[str]):
        pulumi.set(self, "cache_parameter_group_family", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[Any]:
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[Any]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ParameterGroupTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""ParameterGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class ParameterGroup(pulumi.CustomResource):
    warnings.warn("""ParameterGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_parameter_group_family: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterGroupTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::ElastiCache::ParameterGroup

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ParameterGroupArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::ElastiCache::ParameterGroup

        :param str resource_name: The name of the resource.
        :param ParameterGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ParameterGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cache_parameter_group_family: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 properties: Optional[Any] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ParameterGroupTagArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ParameterGroup is deprecated: ParameterGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = ParameterGroupArgs.__new__(ParameterGroupArgs)

            if cache_parameter_group_family is None and not opts.urn:
                raise TypeError("Missing required property 'cache_parameter_group_family'")
            __props__.__dict__["cache_parameter_group_family"] = cache_parameter_group_family
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["properties"] = properties
            __props__.__dict__["tags"] = tags
        super(ParameterGroup, __self__).__init__(
            'aws-native:elasticache:ParameterGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ParameterGroup':
        """
        Get an existing ParameterGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ParameterGroupArgs.__new__(ParameterGroupArgs)

        __props__.__dict__["cache_parameter_group_family"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["tags"] = None
        return ParameterGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cacheParameterGroupFamily")
    def cache_parameter_group_family(self) -> pulumi.Output[str]:
        return pulumi.get(self, "cache_parameter_group_family")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output[Optional[Any]]:
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ParameterGroupTag']]]:
        return pulumi.get(self, "tags")


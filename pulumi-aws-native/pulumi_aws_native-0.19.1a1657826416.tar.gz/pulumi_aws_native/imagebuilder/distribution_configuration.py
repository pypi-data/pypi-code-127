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
from ._enums import *
from ._inputs import *

__all__ = ['DistributionConfigurationArgs', 'DistributionConfiguration']

@pulumi.input_type
class DistributionConfigurationArgs:
    def __init__(__self__, *,
                 distributions: pulumi.Input[Sequence[pulumi.Input['DistributionConfigurationDistributionArgs']]],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None):
        """
        The set of arguments for constructing a DistributionConfiguration resource.
        :param pulumi.Input[Sequence[pulumi.Input['DistributionConfigurationDistributionArgs']]] distributions: The distributions of the distribution configuration.
        :param pulumi.Input[str] description: The description of the distribution configuration.
        :param pulumi.Input[str] name: The name of the distribution configuration.
        :param Any tags: The tags associated with the component.
        """
        pulumi.set(__self__, "distributions", distributions)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def distributions(self) -> pulumi.Input[Sequence[pulumi.Input['DistributionConfigurationDistributionArgs']]]:
        """
        The distributions of the distribution configuration.
        """
        return pulumi.get(self, "distributions")

    @distributions.setter
    def distributions(self, value: pulumi.Input[Sequence[pulumi.Input['DistributionConfigurationDistributionArgs']]]):
        pulumi.set(self, "distributions", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the distribution configuration.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the distribution configuration.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Any]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[Any]):
        pulumi.set(self, "tags", value)


class DistributionConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distributions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionConfigurationDistributionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
                 __props__=None):
        """
        Resource schema for AWS::ImageBuilder::DistributionConfiguration

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The description of the distribution configuration.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionConfigurationDistributionArgs']]]] distributions: The distributions of the distribution configuration.
        :param pulumi.Input[str] name: The name of the distribution configuration.
        :param Any tags: The tags associated with the component.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DistributionConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::ImageBuilder::DistributionConfiguration

        :param str resource_name: The name of the resource.
        :param DistributionConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DistributionConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 distributions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DistributionConfigurationDistributionArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[Any] = None,
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
            __props__ = DistributionConfigurationArgs.__new__(DistributionConfigurationArgs)

            __props__.__dict__["description"] = description
            if distributions is None and not opts.urn:
                raise TypeError("Missing required property 'distributions'")
            __props__.__dict__["distributions"] = distributions
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["arn"] = None
        super(DistributionConfiguration, __self__).__init__(
            'aws-native:imagebuilder:DistributionConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DistributionConfiguration':
        """
        Get an existing DistributionConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DistributionConfigurationArgs.__new__(DistributionConfigurationArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["distributions"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return DistributionConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        The Amazon Resource Name (ARN) of the distribution configuration.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the distribution configuration.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def distributions(self) -> pulumi.Output[Sequence['outputs.DistributionConfigurationDistribution']]:
        """
        The distributions of the distribution configuration.
        """
        return pulumi.get(self, "distributions")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the distribution configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Any]]:
        """
        The tags associated with the component.
        """
        return pulumi.get(self, "tags")


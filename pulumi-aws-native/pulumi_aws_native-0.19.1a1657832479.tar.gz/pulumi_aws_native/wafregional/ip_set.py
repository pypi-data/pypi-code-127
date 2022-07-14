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

__all__ = ['IPSetArgs', 'IPSet']

@pulumi.input_type
class IPSetArgs:
    def __init__(__self__, *,
                 i_p_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input['IPSetDescriptorArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IPSet resource.
        """
        if i_p_set_descriptors is not None:
            pulumi.set(__self__, "i_p_set_descriptors", i_p_set_descriptors)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="iPSetDescriptors")
    def i_p_set_descriptors(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['IPSetDescriptorArgs']]]]:
        return pulumi.get(self, "i_p_set_descriptors")

    @i_p_set_descriptors.setter
    def i_p_set_descriptors(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['IPSetDescriptorArgs']]]]):
        pulumi.set(self, "i_p_set_descriptors", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""IPSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class IPSet(pulumi.CustomResource):
    warnings.warn("""IPSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 i_p_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IPSetDescriptorArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAFRegional::IPSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[IPSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAFRegional::IPSet

        :param str resource_name: The name of the resource.
        :param IPSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IPSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 i_p_set_descriptors: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['IPSetDescriptorArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""IPSet is deprecated: IPSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = IPSetArgs.__new__(IPSetArgs)

            __props__.__dict__["i_p_set_descriptors"] = i_p_set_descriptors
            __props__.__dict__["name"] = name
        super(IPSet, __self__).__init__(
            'aws-native:wafregional:IPSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IPSet':
        """
        Get an existing IPSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IPSetArgs.__new__(IPSetArgs)

        __props__.__dict__["i_p_set_descriptors"] = None
        __props__.__dict__["name"] = None
        return IPSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="iPSetDescriptors")
    def i_p_set_descriptors(self) -> pulumi.Output[Optional[Sequence['outputs.IPSetDescriptor']]]:
        return pulumi.get(self, "i_p_set_descriptors")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")


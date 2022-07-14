# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['RegexPatternSetArgs', 'RegexPatternSet']

@pulumi.input_type
class RegexPatternSetArgs:
    def __init__(__self__, *,
                 regex_pattern_strings: pulumi.Input[Sequence[pulumi.Input[str]]],
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a RegexPatternSet resource.
        """
        pulumi.set(__self__, "regex_pattern_strings", regex_pattern_strings)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="regexPatternStrings")
    def regex_pattern_strings(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "regex_pattern_strings")

    @regex_pattern_strings.setter
    def regex_pattern_strings(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "regex_pattern_strings", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""RegexPatternSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class RegexPatternSet(pulumi.CustomResource):
    warnings.warn("""RegexPatternSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAFRegional::RegexPatternSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegexPatternSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAFRegional::RegexPatternSet

        :param str resource_name: The name of the resource.
        :param RegexPatternSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegexPatternSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 regex_pattern_strings: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        pulumi.log.warn("""RegexPatternSet is deprecated: RegexPatternSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = RegexPatternSetArgs.__new__(RegexPatternSetArgs)

            __props__.__dict__["name"] = name
            if regex_pattern_strings is None and not opts.urn:
                raise TypeError("Missing required property 'regex_pattern_strings'")
            __props__.__dict__["regex_pattern_strings"] = regex_pattern_strings
        super(RegexPatternSet, __self__).__init__(
            'aws-native:wafregional:RegexPatternSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegexPatternSet':
        """
        Get an existing RegexPatternSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegexPatternSetArgs.__new__(RegexPatternSetArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["regex_pattern_strings"] = None
        return RegexPatternSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regexPatternStrings")
    def regex_pattern_strings(self) -> pulumi.Output[Sequence[str]]:
        return pulumi.get(self, "regex_pattern_strings")


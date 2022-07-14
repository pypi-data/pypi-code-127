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

__all__ = ['RulesetArgs', 'Ruleset']

@pulumi.input_type
class RulesetArgs:
    def __init__(__self__, *,
                 rules: pulumi.Input[Sequence[pulumi.Input['RulesetRuleArgs']]],
                 target_arn: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['RulesetTagArgs']]]] = None):
        """
        The set of arguments for constructing a Ruleset resource.
        :param pulumi.Input[Sequence[pulumi.Input['RulesetRuleArgs']]] rules: List of the data quality rules in the ruleset
        :param pulumi.Input[str] target_arn: Arn of the target resource (dataset) to apply the ruleset to
        :param pulumi.Input[str] description: Description of the Ruleset
        :param pulumi.Input[str] name: Name of the Ruleset
        """
        pulumi.set(__self__, "rules", rules)
        pulumi.set(__self__, "target_arn", target_arn)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Input[Sequence[pulumi.Input['RulesetRuleArgs']]]:
        """
        List of the data quality rules in the ruleset
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: pulumi.Input[Sequence[pulumi.Input['RulesetRuleArgs']]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Input[str]:
        """
        Arn of the target resource (dataset) to apply the ruleset to
        """
        return pulumi.get(self, "target_arn")

    @target_arn.setter
    def target_arn(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_arn", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Ruleset
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Ruleset
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RulesetTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RulesetTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Ruleset(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesetRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesetTagArgs']]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataBrew::Ruleset.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the Ruleset
        :param pulumi.Input[str] name: Name of the Ruleset
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesetRuleArgs']]]] rules: List of the data quality rules in the ruleset
        :param pulumi.Input[str] target_arn: Arn of the target resource (dataset) to apply the ruleset to
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RulesetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataBrew::Ruleset.

        :param str resource_name: The name of the resource.
        :param RulesetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RulesetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesetRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RulesetTagArgs']]]]] = None,
                 target_arn: Optional[pulumi.Input[str]] = None,
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
            __props__ = RulesetArgs.__new__(RulesetArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            if rules is None and not opts.urn:
                raise TypeError("Missing required property 'rules'")
            __props__.__dict__["rules"] = rules
            __props__.__dict__["tags"] = tags
            if target_arn is None and not opts.urn:
                raise TypeError("Missing required property 'target_arn'")
            __props__.__dict__["target_arn"] = target_arn
        super(Ruleset, __self__).__init__(
            'aws-native:databrew:Ruleset',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Ruleset':
        """
        Get an existing Ruleset resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RulesetArgs.__new__(RulesetArgs)

        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_arn"] = None
        return Ruleset(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the Ruleset
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Ruleset
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.RulesetRule']]:
        """
        List of the data quality rules in the ruleset
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.RulesetTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetArn")
    def target_arn(self) -> pulumi.Output[str]:
        """
        Arn of the target resource (dataset) to apply the ruleset to
        """
        return pulumi.get(self, "target_arn")


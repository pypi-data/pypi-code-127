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

__all__ = ['PricingRuleArgs', 'PricingRule']

@pulumi.input_type
class PricingRuleArgs:
    def __init__(__self__, *,
                 modifier_percentage: pulumi.Input[float],
                 scope: pulumi.Input['PricingRuleScope'],
                 type: pulumi.Input['PricingRuleType'],
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['PricingRuleTagArgs']]]] = None):
        """
        The set of arguments for constructing a PricingRule resource.
        :param pulumi.Input[float] modifier_percentage: Pricing rule modifier percentage
        :param pulumi.Input['PricingRuleScope'] scope: A term used to categorize the granularity of a Pricing Rule.
        :param pulumi.Input['PricingRuleType'] type: One of MARKUP or DISCOUNT that describes the direction of the rate that is applied to a pricing plan.
        :param pulumi.Input[str] description: Pricing rule description
        :param pulumi.Input[str] name: Pricing rule name
        :param pulumi.Input[str] service: The service which a pricing rule is applied on
        """
        pulumi.set(__self__, "modifier_percentage", modifier_percentage)
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if service is not None:
            pulumi.set(__self__, "service", service)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="modifierPercentage")
    def modifier_percentage(self) -> pulumi.Input[float]:
        """
        Pricing rule modifier percentage
        """
        return pulumi.get(self, "modifier_percentage")

    @modifier_percentage.setter
    def modifier_percentage(self, value: pulumi.Input[float]):
        pulumi.set(self, "modifier_percentage", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input['PricingRuleScope']:
        """
        A term used to categorize the granularity of a Pricing Rule.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input['PricingRuleScope']):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input['PricingRuleType']:
        """
        One of MARKUP or DISCOUNT that describes the direction of the rate that is applied to a pricing plan.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input['PricingRuleType']):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Pricing rule description
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Pricing rule name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[str]]:
        """
        The service which a pricing rule is applied on
        """
        return pulumi.get(self, "service")

    @service.setter
    def service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PricingRuleTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PricingRuleTagArgs']]]]):
        pulumi.set(self, "tags", value)


warnings.warn("""PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class PricingRule(pulumi.CustomResource):
    warnings.warn("""PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 modifier_percentage: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['PricingRuleScope']] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PricingRuleTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['PricingRuleType']] = None,
                 __props__=None):
        """
        A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Pricing rule description
        :param pulumi.Input[float] modifier_percentage: Pricing rule modifier percentage
        :param pulumi.Input[str] name: Pricing rule name
        :param pulumi.Input['PricingRuleScope'] scope: A term used to categorize the granularity of a Pricing Rule.
        :param pulumi.Input[str] service: The service which a pricing rule is applied on
        :param pulumi.Input['PricingRuleType'] type: One of MARKUP or DISCOUNT that describes the direction of the rate that is applied to a pricing plan.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PricingRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.

        :param str resource_name: The name of the resource.
        :param PricingRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PricingRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 modifier_percentage: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input['PricingRuleScope']] = None,
                 service: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PricingRuleTagArgs']]]]] = None,
                 type: Optional[pulumi.Input['PricingRuleType']] = None,
                 __props__=None):
        pulumi.log.warn("""PricingRule is deprecated: PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PricingRuleArgs.__new__(PricingRuleArgs)

            __props__.__dict__["description"] = description
            if modifier_percentage is None and not opts.urn:
                raise TypeError("Missing required property 'modifier_percentage'")
            __props__.__dict__["modifier_percentage"] = modifier_percentage
            __props__.__dict__["name"] = name
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            __props__.__dict__["service"] = service
            __props__.__dict__["tags"] = tags
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["arn"] = None
            __props__.__dict__["associated_pricing_plan_count"] = None
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["last_modified_time"] = None
        super(PricingRule, __self__).__init__(
            'aws-native:billingconductor:PricingRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'PricingRule':
        """
        Get an existing PricingRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PricingRuleArgs.__new__(PricingRuleArgs)

        __props__.__dict__["arn"] = None
        __props__.__dict__["associated_pricing_plan_count"] = None
        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["modifier_percentage"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["scope"] = None
        __props__.__dict__["service"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return PricingRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arn(self) -> pulumi.Output[str]:
        """
        Pricing rule ARN
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="associatedPricingPlanCount")
    def associated_pricing_plan_count(self) -> pulumi.Output[int]:
        """
        The number of pricing plans associated with pricing rule
        """
        return pulumi.get(self, "associated_pricing_plan_count")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[int]:
        """
        Creation timestamp in UNIX epoch time format
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Pricing rule description
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[int]:
        """
        Latest modified timestamp in UNIX epoch time format
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter(name="modifierPercentage")
    def modifier_percentage(self) -> pulumi.Output[float]:
        """
        Pricing rule modifier percentage
        """
        return pulumi.get(self, "modifier_percentage")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Pricing rule name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output['PricingRuleScope']:
        """
        A term used to categorize the granularity of a Pricing Rule.
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def service(self) -> pulumi.Output[Optional[str]]:
        """
        The service which a pricing rule is applied on
        """
        return pulumi.get(self, "service")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.PricingRuleTag']]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output['PricingRuleType']:
        """
        One of MARKUP or DISCOUNT that describes the direction of the rate that is applied to a pricing plan.
        """
        return pulumi.get(self, "type")


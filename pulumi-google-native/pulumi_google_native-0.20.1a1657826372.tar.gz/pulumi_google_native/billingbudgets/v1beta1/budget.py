# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['BudgetArgs', 'Budget']

@pulumi.input_type
class BudgetArgs:
    def __init__(__self__, *,
                 amount: pulumi.Input['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs'],
                 billing_account_id: pulumi.Input[str],
                 all_updates_rule: Optional[pulumi.Input['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs']] = None,
                 budget_filter: Optional[pulumi.Input['GoogleCloudBillingBudgetsV1beta1FilterArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 threshold_rules: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]]] = None):
        """
        The set of arguments for constructing a Budget resource.
        :param pulumi.Input['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs'] amount: Budgeted amount.
        :param pulumi.Input['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs'] all_updates_rule: Optional. Rules to apply to notifications sent based on budget spend and thresholds.
        :param pulumi.Input['GoogleCloudBillingBudgetsV1beta1FilterArgs'] budget_filter: Optional. Filters that define which resources are used to compute the actual spend against the budget amount, such as projects, services, and the budget's time period, as well as other filters.
        :param pulumi.Input[str] display_name: User data for display name in UI. Validation: <= 60 chars.
        :param pulumi.Input[str] etag: Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
        :param pulumi.Input[Sequence[pulumi.Input['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]] threshold_rules: Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications.
        """
        pulumi.set(__self__, "amount", amount)
        pulumi.set(__self__, "billing_account_id", billing_account_id)
        if all_updates_rule is not None:
            pulumi.set(__self__, "all_updates_rule", all_updates_rule)
        if budget_filter is not None:
            pulumi.set(__self__, "budget_filter", budget_filter)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if threshold_rules is not None:
            pulumi.set(__self__, "threshold_rules", threshold_rules)

    @property
    @pulumi.getter
    def amount(self) -> pulumi.Input['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs']:
        """
        Budgeted amount.
        """
        return pulumi.get(self, "amount")

    @amount.setter
    def amount(self, value: pulumi.Input['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs']):
        pulumi.set(self, "amount", value)

    @property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "billing_account_id")

    @billing_account_id.setter
    def billing_account_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "billing_account_id", value)

    @property
    @pulumi.getter(name="allUpdatesRule")
    def all_updates_rule(self) -> Optional[pulumi.Input['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs']]:
        """
        Optional. Rules to apply to notifications sent based on budget spend and thresholds.
        """
        return pulumi.get(self, "all_updates_rule")

    @all_updates_rule.setter
    def all_updates_rule(self, value: Optional[pulumi.Input['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs']]):
        pulumi.set(self, "all_updates_rule", value)

    @property
    @pulumi.getter(name="budgetFilter")
    def budget_filter(self) -> Optional[pulumi.Input['GoogleCloudBillingBudgetsV1beta1FilterArgs']]:
        """
        Optional. Filters that define which resources are used to compute the actual spend against the budget amount, such as projects, services, and the budget's time period, as well as other filters.
        """
        return pulumi.get(self, "budget_filter")

    @budget_filter.setter
    def budget_filter(self, value: Optional[pulumi.Input['GoogleCloudBillingBudgetsV1beta1FilterArgs']]):
        pulumi.set(self, "budget_filter", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        User data for display name in UI. Validation: <= 60 chars.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]]]:
        """
        Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications.
        """
        return pulumi.get(self, "threshold_rules")

    @threshold_rules.setter
    def threshold_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]]]):
        pulumi.set(self, "threshold_rules", value)


class Budget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 all_updates_rule: Optional[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs']]] = None,
                 amount: Optional[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs']]] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 budget_filter: Optional[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1FilterArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 threshold_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]]]] = None,
                 __props__=None):
        """
        Creates a new budget. See [Quotas and limits](https://cloud.google.com/billing/quotas) for more information on the limits of the number of budgets you can create.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs']] all_updates_rule: Optional. Rules to apply to notifications sent based on budget spend and thresholds.
        :param pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs']] amount: Budgeted amount.
        :param pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1FilterArgs']] budget_filter: Optional. Filters that define which resources are used to compute the actual spend against the budget amount, such as projects, services, and the budget's time period, as well as other filters.
        :param pulumi.Input[str] display_name: User data for display name in UI. Validation: <= 60 chars.
        :param pulumi.Input[str] etag: Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]]] threshold_rules: Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BudgetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new budget. See [Quotas and limits](https://cloud.google.com/billing/quotas) for more information on the limits of the number of budgets you can create.
        Auto-naming is currently not supported for this resource.

        :param str resource_name: The name of the resource.
        :param BudgetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BudgetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 all_updates_rule: Optional[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleArgs']]] = None,
                 amount: Optional[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1BudgetAmountArgs']]] = None,
                 billing_account_id: Optional[pulumi.Input[str]] = None,
                 budget_filter: Optional[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1FilterArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 threshold_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['GoogleCloudBillingBudgetsV1beta1ThresholdRuleArgs']]]]] = None,
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
            __props__ = BudgetArgs.__new__(BudgetArgs)

            __props__.__dict__["all_updates_rule"] = all_updates_rule
            if amount is None and not opts.urn:
                raise TypeError("Missing required property 'amount'")
            __props__.__dict__["amount"] = amount
            if billing_account_id is None and not opts.urn:
                raise TypeError("Missing required property 'billing_account_id'")
            __props__.__dict__["billing_account_id"] = billing_account_id
            __props__.__dict__["budget_filter"] = budget_filter
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["etag"] = etag
            __props__.__dict__["threshold_rules"] = threshold_rules
            __props__.__dict__["name"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["billing_account_id"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Budget, __self__).__init__(
            'google-native:billingbudgets/v1beta1:Budget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Budget':
        """
        Get an existing Budget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BudgetArgs.__new__(BudgetArgs)

        __props__.__dict__["all_updates_rule"] = None
        __props__.__dict__["amount"] = None
        __props__.__dict__["billing_account_id"] = None
        __props__.__dict__["budget_filter"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["threshold_rules"] = None
        return Budget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allUpdatesRule")
    def all_updates_rule(self) -> pulumi.Output['outputs.GoogleCloudBillingBudgetsV1beta1AllUpdatesRuleResponse']:
        """
        Optional. Rules to apply to notifications sent based on budget spend and thresholds.
        """
        return pulumi.get(self, "all_updates_rule")

    @property
    @pulumi.getter
    def amount(self) -> pulumi.Output['outputs.GoogleCloudBillingBudgetsV1beta1BudgetAmountResponse']:
        """
        Budgeted amount.
        """
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter(name="billingAccountId")
    def billing_account_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "billing_account_id")

    @property
    @pulumi.getter(name="budgetFilter")
    def budget_filter(self) -> pulumi.Output['outputs.GoogleCloudBillingBudgetsV1beta1FilterResponse']:
        """
        Optional. Filters that define which resources are used to compute the actual spend against the budget amount, such as projects, services, and the budget's time period, as well as other filters.
        """
        return pulumi.get(self, "budget_filter")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        User data for display name in UI. Validation: <= 60 chars.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        Optional. Etag to validate that the object is unchanged for a read-modify-write operation. An empty etag will cause an update to overwrite other changes.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name of the budget. The resource name implies the scope of a budget. Values are of the form `billingAccounts/{billingAccountId}/budgets/{budgetId}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="thresholdRules")
    def threshold_rules(self) -> pulumi.Output[Sequence['outputs.GoogleCloudBillingBudgetsV1beta1ThresholdRuleResponse']]:
        """
        Optional. Rules that trigger alerts (notifications of thresholds being crossed) when spend exceeds the specified percentages of the budget. Optional for `pubsubTopic` notifications. Required if using email notifications.
        """
        return pulumi.get(self, "threshold_rules")


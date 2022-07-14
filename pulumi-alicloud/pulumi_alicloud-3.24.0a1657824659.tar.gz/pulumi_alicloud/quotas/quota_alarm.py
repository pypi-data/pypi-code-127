# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = ['QuotaAlarmArgs', 'QuotaAlarm']

@pulumi.input_type
class QuotaAlarmArgs:
    def __init__(__self__, *,
                 product_code: pulumi.Input[str],
                 quota_action_code: pulumi.Input[str],
                 quota_alarm_name: pulumi.Input[str],
                 quota_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_percent: Optional[pulumi.Input[float]] = None,
                 web_hook: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a QuotaAlarm resource.
        :param pulumi.Input[str] product_code: The Product Code.
        :param pulumi.Input[str] quota_action_code: The Quota Action Code.
        :param pulumi.Input[str] quota_alarm_name: The name of Quota Alarm.
        :param pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]] quota_dimensions: The Quota Dimensions.
        :param pulumi.Input[float] threshold: The threshold of Quota Alarm.
        :param pulumi.Input[float] threshold_percent: The threshold percent of Quota Alarm.
        :param pulumi.Input[str] web_hook: The WebHook of Quota Alarm.
        """
        pulumi.set(__self__, "product_code", product_code)
        pulumi.set(__self__, "quota_action_code", quota_action_code)
        pulumi.set(__self__, "quota_alarm_name", quota_alarm_name)
        if quota_dimensions is not None:
            pulumi.set(__self__, "quota_dimensions", quota_dimensions)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if threshold_percent is not None:
            pulumi.set(__self__, "threshold_percent", threshold_percent)
        if web_hook is not None:
            pulumi.set(__self__, "web_hook", web_hook)

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Input[str]:
        """
        The Product Code.
        """
        return pulumi.get(self, "product_code")

    @product_code.setter
    def product_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "product_code", value)

    @property
    @pulumi.getter(name="quotaActionCode")
    def quota_action_code(self) -> pulumi.Input[str]:
        """
        The Quota Action Code.
        """
        return pulumi.get(self, "quota_action_code")

    @quota_action_code.setter
    def quota_action_code(self, value: pulumi.Input[str]):
        pulumi.set(self, "quota_action_code", value)

    @property
    @pulumi.getter(name="quotaAlarmName")
    def quota_alarm_name(self) -> pulumi.Input[str]:
        """
        The name of Quota Alarm.
        """
        return pulumi.get(self, "quota_alarm_name")

    @quota_alarm_name.setter
    def quota_alarm_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "quota_alarm_name", value)

    @property
    @pulumi.getter(name="quotaDimensions")
    def quota_dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]]]:
        """
        The Quota Dimensions.
        """
        return pulumi.get(self, "quota_dimensions")

    @quota_dimensions.setter
    def quota_dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]]]):
        pulumi.set(self, "quota_dimensions", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[float]]:
        """
        The threshold of Quota Alarm.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="thresholdPercent")
    def threshold_percent(self) -> Optional[pulumi.Input[float]]:
        """
        The threshold percent of Quota Alarm.
        """
        return pulumi.get(self, "threshold_percent")

    @threshold_percent.setter
    def threshold_percent(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold_percent", value)

    @property
    @pulumi.getter(name="webHook")
    def web_hook(self) -> Optional[pulumi.Input[str]]:
        """
        The WebHook of Quota Alarm.
        """
        return pulumi.get(self, "web_hook")

    @web_hook.setter
    def web_hook(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_hook", value)


@pulumi.input_type
class _QuotaAlarmState:
    def __init__(__self__, *,
                 product_code: Optional[pulumi.Input[str]] = None,
                 quota_action_code: Optional[pulumi.Input[str]] = None,
                 quota_alarm_name: Optional[pulumi.Input[str]] = None,
                 quota_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_percent: Optional[pulumi.Input[float]] = None,
                 web_hook: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering QuotaAlarm resources.
        :param pulumi.Input[str] product_code: The Product Code.
        :param pulumi.Input[str] quota_action_code: The Quota Action Code.
        :param pulumi.Input[str] quota_alarm_name: The name of Quota Alarm.
        :param pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]] quota_dimensions: The Quota Dimensions.
        :param pulumi.Input[float] threshold: The threshold of Quota Alarm.
        :param pulumi.Input[float] threshold_percent: The threshold percent of Quota Alarm.
        :param pulumi.Input[str] web_hook: The WebHook of Quota Alarm.
        """
        if product_code is not None:
            pulumi.set(__self__, "product_code", product_code)
        if quota_action_code is not None:
            pulumi.set(__self__, "quota_action_code", quota_action_code)
        if quota_alarm_name is not None:
            pulumi.set(__self__, "quota_alarm_name", quota_alarm_name)
        if quota_dimensions is not None:
            pulumi.set(__self__, "quota_dimensions", quota_dimensions)
        if threshold is not None:
            pulumi.set(__self__, "threshold", threshold)
        if threshold_percent is not None:
            pulumi.set(__self__, "threshold_percent", threshold_percent)
        if web_hook is not None:
            pulumi.set(__self__, "web_hook", web_hook)

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> Optional[pulumi.Input[str]]:
        """
        The Product Code.
        """
        return pulumi.get(self, "product_code")

    @product_code.setter
    def product_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product_code", value)

    @property
    @pulumi.getter(name="quotaActionCode")
    def quota_action_code(self) -> Optional[pulumi.Input[str]]:
        """
        The Quota Action Code.
        """
        return pulumi.get(self, "quota_action_code")

    @quota_action_code.setter
    def quota_action_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quota_action_code", value)

    @property
    @pulumi.getter(name="quotaAlarmName")
    def quota_alarm_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of Quota Alarm.
        """
        return pulumi.get(self, "quota_alarm_name")

    @quota_alarm_name.setter
    def quota_alarm_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "quota_alarm_name", value)

    @property
    @pulumi.getter(name="quotaDimensions")
    def quota_dimensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]]]:
        """
        The Quota Dimensions.
        """
        return pulumi.get(self, "quota_dimensions")

    @quota_dimensions.setter
    def quota_dimensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['QuotaAlarmQuotaDimensionArgs']]]]):
        pulumi.set(self, "quota_dimensions", value)

    @property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[float]]:
        """
        The threshold of Quota Alarm.
        """
        return pulumi.get(self, "threshold")

    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold", value)

    @property
    @pulumi.getter(name="thresholdPercent")
    def threshold_percent(self) -> Optional[pulumi.Input[float]]:
        """
        The threshold percent of Quota Alarm.
        """
        return pulumi.get(self, "threshold_percent")

    @threshold_percent.setter
    def threshold_percent(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "threshold_percent", value)

    @property
    @pulumi.getter(name="webHook")
    def web_hook(self) -> Optional[pulumi.Input[str]]:
        """
        The WebHook of Quota Alarm.
        """
        return pulumi.get(self, "web_hook")

    @web_hook.setter
    def web_hook(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "web_hook", value)


class QuotaAlarm(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 product_code: Optional[pulumi.Input[str]] = None,
                 quota_action_code: Optional[pulumi.Input[str]] = None,
                 quota_alarm_name: Optional[pulumi.Input[str]] = None,
                 quota_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QuotaAlarmQuotaDimensionArgs']]]]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_percent: Optional[pulumi.Input[float]] = None,
                 web_hook: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Quotas Quota Alarm resource.

        For information about Quotas Quota Alarm and how to use it, see [What is Quota Alarm](https://help.aliyun.com/document_detail/184343.html).

        > **NOTE:** Available in v1.116.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.quotas.QuotaAlarm("example",
            product_code="ecs",
            quota_action_code="q_prepaid-instance-count-per-once-purchase",
            quota_alarm_name="tf-testAcc",
            quota_dimensions=[alicloud.quotas.QuotaAlarmQuotaDimensionArgs(
                key="regionId",
                value="cn-hangzhou",
            )],
            threshold=100)
        ```

        ## Import

        Quotas Quota Alarm can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:quotas/quotaAlarm:QuotaAlarm example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] product_code: The Product Code.
        :param pulumi.Input[str] quota_action_code: The Quota Action Code.
        :param pulumi.Input[str] quota_alarm_name: The name of Quota Alarm.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QuotaAlarmQuotaDimensionArgs']]]] quota_dimensions: The Quota Dimensions.
        :param pulumi.Input[float] threshold: The threshold of Quota Alarm.
        :param pulumi.Input[float] threshold_percent: The threshold percent of Quota Alarm.
        :param pulumi.Input[str] web_hook: The WebHook of Quota Alarm.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: QuotaAlarmArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Quotas Quota Alarm resource.

        For information about Quotas Quota Alarm and how to use it, see [What is Quota Alarm](https://help.aliyun.com/document_detail/184343.html).

        > **NOTE:** Available in v1.116.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example = alicloud.quotas.QuotaAlarm("example",
            product_code="ecs",
            quota_action_code="q_prepaid-instance-count-per-once-purchase",
            quota_alarm_name="tf-testAcc",
            quota_dimensions=[alicloud.quotas.QuotaAlarmQuotaDimensionArgs(
                key="regionId",
                value="cn-hangzhou",
            )],
            threshold=100)
        ```

        ## Import

        Quotas Quota Alarm can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:quotas/quotaAlarm:QuotaAlarm example <id>
        ```

        :param str resource_name: The name of the resource.
        :param QuotaAlarmArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(QuotaAlarmArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 product_code: Optional[pulumi.Input[str]] = None,
                 quota_action_code: Optional[pulumi.Input[str]] = None,
                 quota_alarm_name: Optional[pulumi.Input[str]] = None,
                 quota_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QuotaAlarmQuotaDimensionArgs']]]]] = None,
                 threshold: Optional[pulumi.Input[float]] = None,
                 threshold_percent: Optional[pulumi.Input[float]] = None,
                 web_hook: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = QuotaAlarmArgs.__new__(QuotaAlarmArgs)

            if product_code is None and not opts.urn:
                raise TypeError("Missing required property 'product_code'")
            __props__.__dict__["product_code"] = product_code
            if quota_action_code is None and not opts.urn:
                raise TypeError("Missing required property 'quota_action_code'")
            __props__.__dict__["quota_action_code"] = quota_action_code
            if quota_alarm_name is None and not opts.urn:
                raise TypeError("Missing required property 'quota_alarm_name'")
            __props__.__dict__["quota_alarm_name"] = quota_alarm_name
            __props__.__dict__["quota_dimensions"] = quota_dimensions
            __props__.__dict__["threshold"] = threshold
            __props__.__dict__["threshold_percent"] = threshold_percent
            __props__.__dict__["web_hook"] = web_hook
        super(QuotaAlarm, __self__).__init__(
            'alicloud:quotas/quotaAlarm:QuotaAlarm',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            product_code: Optional[pulumi.Input[str]] = None,
            quota_action_code: Optional[pulumi.Input[str]] = None,
            quota_alarm_name: Optional[pulumi.Input[str]] = None,
            quota_dimensions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QuotaAlarmQuotaDimensionArgs']]]]] = None,
            threshold: Optional[pulumi.Input[float]] = None,
            threshold_percent: Optional[pulumi.Input[float]] = None,
            web_hook: Optional[pulumi.Input[str]] = None) -> 'QuotaAlarm':
        """
        Get an existing QuotaAlarm resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] product_code: The Product Code.
        :param pulumi.Input[str] quota_action_code: The Quota Action Code.
        :param pulumi.Input[str] quota_alarm_name: The name of Quota Alarm.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['QuotaAlarmQuotaDimensionArgs']]]] quota_dimensions: The Quota Dimensions.
        :param pulumi.Input[float] threshold: The threshold of Quota Alarm.
        :param pulumi.Input[float] threshold_percent: The threshold percent of Quota Alarm.
        :param pulumi.Input[str] web_hook: The WebHook of Quota Alarm.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _QuotaAlarmState.__new__(_QuotaAlarmState)

        __props__.__dict__["product_code"] = product_code
        __props__.__dict__["quota_action_code"] = quota_action_code
        __props__.__dict__["quota_alarm_name"] = quota_alarm_name
        __props__.__dict__["quota_dimensions"] = quota_dimensions
        __props__.__dict__["threshold"] = threshold
        __props__.__dict__["threshold_percent"] = threshold_percent
        __props__.__dict__["web_hook"] = web_hook
        return QuotaAlarm(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="productCode")
    def product_code(self) -> pulumi.Output[str]:
        """
        The Product Code.
        """
        return pulumi.get(self, "product_code")

    @property
    @pulumi.getter(name="quotaActionCode")
    def quota_action_code(self) -> pulumi.Output[str]:
        """
        The Quota Action Code.
        """
        return pulumi.get(self, "quota_action_code")

    @property
    @pulumi.getter(name="quotaAlarmName")
    def quota_alarm_name(self) -> pulumi.Output[str]:
        """
        The name of Quota Alarm.
        """
        return pulumi.get(self, "quota_alarm_name")

    @property
    @pulumi.getter(name="quotaDimensions")
    def quota_dimensions(self) -> pulumi.Output[Optional[Sequence['outputs.QuotaAlarmQuotaDimension']]]:
        """
        The Quota Dimensions.
        """
        return pulumi.get(self, "quota_dimensions")

    @property
    @pulumi.getter
    def threshold(self) -> pulumi.Output[Optional[float]]:
        """
        The threshold of Quota Alarm.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter(name="thresholdPercent")
    def threshold_percent(self) -> pulumi.Output[Optional[float]]:
        """
        The threshold percent of Quota Alarm.
        """
        return pulumi.get(self, "threshold_percent")

    @property
    @pulumi.getter(name="webHook")
    def web_hook(self) -> pulumi.Output[Optional[str]]:
        """
        The WebHook of Quota Alarm.
        """
        return pulumi.get(self, "web_hook")


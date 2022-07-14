# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['SuspendProcessArgs', 'SuspendProcess']

@pulumi.input_type
class SuspendProcessArgs:
    def __init__(__self__, *,
                 process: pulumi.Input[str],
                 scaling_group_id: pulumi.Input[str]):
        """
        The set of arguments for constructing a SuspendProcess resource.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        pulumi.set(__self__, "process", process)
        pulumi.set(__self__, "scaling_group_id", scaling_group_id)

    @property
    @pulumi.getter
    def process(self) -> pulumi.Input[str]:
        """
        Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        """
        return pulumi.get(self, "process")

    @process.setter
    def process(self, value: pulumi.Input[str]):
        pulumi.set(self, "process", value)

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Input[str]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")

    @scaling_group_id.setter
    def scaling_group_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "scaling_group_id", value)


@pulumi.input_type
class _SuspendProcessState:
    def __init__(__self__, *,
                 process: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SuspendProcess resources.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        if process is not None:
            pulumi.set(__self__, "process", process)
        if scaling_group_id is not None:
            pulumi.set(__self__, "scaling_group_id", scaling_group_id)

    @property
    @pulumi.getter
    def process(self) -> Optional[pulumi.Input[str]]:
        """
        Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        """
        return pulumi.get(self, "process")

    @process.setter
    def process(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "process", value)

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")

    @scaling_group_id.setter
    def scaling_group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scaling_group_id", value)


class SuspendProcess(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 process: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Suspend/Resume processes to a specified scaling group.

        For information about scaling group suspend process, see [SuspendProcesses](https://www.alibabacloud.com/help/en/auto-scaling/latest/suspendprocesses).

        > NOTE: Available in v1.166.0+

        ## Import

        ### Timeouts The `timeouts` block allows you to specify [timeouts](https://www.terraform.io/docs/configuration-0-11/resources.html#timeouts) for certain actions* `create` - (Defaults to 1 mins) Used when create the process. * `delete` - (Defaults to 1 mins) Used when delete the process.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SuspendProcessArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Suspend/Resume processes to a specified scaling group.

        For information about scaling group suspend process, see [SuspendProcesses](https://www.alibabacloud.com/help/en/auto-scaling/latest/suspendprocesses).

        > NOTE: Available in v1.166.0+

        ## Import

        ### Timeouts The `timeouts` block allows you to specify [timeouts](https://www.terraform.io/docs/configuration-0-11/resources.html#timeouts) for certain actions* `create` - (Defaults to 1 mins) Used when create the process. * `delete` - (Defaults to 1 mins) Used when delete the process.

        :param str resource_name: The name of the resource.
        :param SuspendProcessArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SuspendProcessArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 process: Optional[pulumi.Input[str]] = None,
                 scaling_group_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = SuspendProcessArgs.__new__(SuspendProcessArgs)

            if process is None and not opts.urn:
                raise TypeError("Missing required property 'process'")
            __props__.__dict__["process"] = process
            if scaling_group_id is None and not opts.urn:
                raise TypeError("Missing required property 'scaling_group_id'")
            __props__.__dict__["scaling_group_id"] = scaling_group_id
        super(SuspendProcess, __self__).__init__(
            'alicloud:ess/suspendProcess:SuspendProcess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            process: Optional[pulumi.Input[str]] = None,
            scaling_group_id: Optional[pulumi.Input[str]] = None) -> 'SuspendProcess':
        """
        Get an existing SuspendProcess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] process: Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        :param pulumi.Input[str] scaling_group_id: ID of the scaling group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SuspendProcessState.__new__(_SuspendProcessState)

        __props__.__dict__["process"] = process
        __props__.__dict__["scaling_group_id"] = scaling_group_id
        return SuspendProcess(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def process(self) -> pulumi.Output[str]:
        """
        Activity type N that you want to suspend. Valid values are: `SCALE_OUT`,`SCALE_IN`,`HealthCheck`,`AlarmNotification` and `ScheduledAction`.
        """
        return pulumi.get(self, "process")

    @property
    @pulumi.getter(name="scalingGroupId")
    def scaling_group_id(self) -> pulumi.Output[str]:
        """
        ID of the scaling group.
        """
        return pulumi.get(self, "scaling_group_id")


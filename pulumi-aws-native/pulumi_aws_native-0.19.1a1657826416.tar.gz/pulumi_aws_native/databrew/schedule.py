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

__all__ = ['ScheduleArgs', 'Schedule']

@pulumi.input_type
class ScheduleArgs:
    def __init__(__self__, *,
                 cron_expression: pulumi.Input[str],
                 job_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input['ScheduleTagArgs']]]] = None):
        """
        The set of arguments for constructing a Schedule resource.
        :param pulumi.Input[str] cron_expression: Schedule cron
        :param pulumi.Input[str] name: Schedule Name
        """
        pulumi.set(__self__, "cron_expression", cron_expression)
        if job_names is not None:
            pulumi.set(__self__, "job_names", job_names)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> pulumi.Input[str]:
        """
        Schedule cron
        """
        return pulumi.get(self, "cron_expression")

    @cron_expression.setter
    def cron_expression(self, value: pulumi.Input[str]):
        pulumi.set(self, "cron_expression", value)

    @property
    @pulumi.getter(name="jobNames")
    def job_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "job_names")

    @job_names.setter
    def job_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "job_names", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Schedule Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ScheduleTagArgs']]]]:
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ScheduleTagArgs']]]]):
        pulumi.set(self, "tags", value)


class Schedule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_expression: Optional[pulumi.Input[str]] = None,
                 job_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleTagArgs']]]]] = None,
                 __props__=None):
        """
        Resource schema for AWS::DataBrew::Schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cron_expression: Schedule cron
        :param pulumi.Input[str] name: Schedule Name
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource schema for AWS::DataBrew::Schedule.

        :param str resource_name: The name of the resource.
        :param ScheduleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cron_expression: Optional[pulumi.Input[str]] = None,
                 job_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ScheduleTagArgs']]]]] = None,
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
            __props__ = ScheduleArgs.__new__(ScheduleArgs)

            if cron_expression is None and not opts.urn:
                raise TypeError("Missing required property 'cron_expression'")
            __props__.__dict__["cron_expression"] = cron_expression
            __props__.__dict__["job_names"] = job_names
            __props__.__dict__["name"] = name
            __props__.__dict__["tags"] = tags
        super(Schedule, __self__).__init__(
            'aws-native:databrew:Schedule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Schedule':
        """
        Get an existing Schedule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleArgs.__new__(ScheduleArgs)

        __props__.__dict__["cron_expression"] = None
        __props__.__dict__["job_names"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        return Schedule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> pulumi.Output[str]:
        """
        Schedule cron
        """
        return pulumi.get(self, "cron_expression")

    @property
    @pulumi.getter(name="jobNames")
    def job_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        return pulumi.get(self, "job_names")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Schedule Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence['outputs.ScheduleTag']]]:
        return pulumi.get(self, "tags")


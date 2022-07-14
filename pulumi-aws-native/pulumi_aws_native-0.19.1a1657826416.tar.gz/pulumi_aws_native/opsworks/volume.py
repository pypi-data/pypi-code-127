# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['VolumeArgs', 'Volume']

@pulumi.input_type
class VolumeArgs:
    def __init__(__self__, *,
                 ec2_volume_id: pulumi.Input[str],
                 stack_id: pulumi.Input[str],
                 mount_point: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Volume resource.
        """
        pulumi.set(__self__, "ec2_volume_id", ec2_volume_id)
        pulumi.set(__self__, "stack_id", stack_id)
        if mount_point is not None:
            pulumi.set(__self__, "mount_point", mount_point)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="ec2VolumeId")
    def ec2_volume_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ec2_volume_id")

    @ec2_volume_id.setter
    def ec2_volume_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "ec2_volume_id", value)

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "stack_id")

    @stack_id.setter
    def stack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "stack_id", value)

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "mount_point")

    @mount_point.setter
    def mount_point(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mount_point", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Volume(pulumi.CustomResource):
    warnings.warn("""Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ec2_volume_id: Optional[pulumi.Input[str]] = None,
                 mount_point: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::OpsWorks::Volume

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::OpsWorks::Volume

        :param str resource_name: The name of the resource.
        :param VolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ec2_volume_id: Optional[pulumi.Input[str]] = None,
                 mount_point: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 stack_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Volume is deprecated: Volume is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = VolumeArgs.__new__(VolumeArgs)

            if ec2_volume_id is None and not opts.urn:
                raise TypeError("Missing required property 'ec2_volume_id'")
            __props__.__dict__["ec2_volume_id"] = ec2_volume_id
            __props__.__dict__["mount_point"] = mount_point
            __props__.__dict__["name"] = name
            if stack_id is None and not opts.urn:
                raise TypeError("Missing required property 'stack_id'")
            __props__.__dict__["stack_id"] = stack_id
        super(Volume, __self__).__init__(
            'aws-native:opsworks:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VolumeArgs.__new__(VolumeArgs)

        __props__.__dict__["ec2_volume_id"] = None
        __props__.__dict__["mount_point"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["stack_id"] = None
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ec2VolumeId")
    def ec2_volume_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "ec2_volume_id")

    @property
    @pulumi.getter(name="mountPoint")
    def mount_point(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "mount_point")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="stackId")
    def stack_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "stack_id")


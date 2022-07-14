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

__all__ = ['ResourceDataSyncArgs', 'ResourceDataSync']

@pulumi.input_type
class ResourceDataSyncArgs:
    def __init__(__self__, *,
                 sync_name: pulumi.Input[str],
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 bucket_region: Optional[pulumi.Input[str]] = None,
                 k_ms_key_arn: Optional[pulumi.Input[str]] = None,
                 s3_destination: Optional[pulumi.Input['ResourceDataSyncS3DestinationArgs']] = None,
                 sync_format: Optional[pulumi.Input[str]] = None,
                 sync_source: Optional[pulumi.Input['ResourceDataSyncSyncSourceArgs']] = None,
                 sync_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ResourceDataSync resource.
        """
        pulumi.set(__self__, "sync_name", sync_name)
        if bucket_name is not None:
            pulumi.set(__self__, "bucket_name", bucket_name)
        if bucket_prefix is not None:
            pulumi.set(__self__, "bucket_prefix", bucket_prefix)
        if bucket_region is not None:
            pulumi.set(__self__, "bucket_region", bucket_region)
        if k_ms_key_arn is not None:
            pulumi.set(__self__, "k_ms_key_arn", k_ms_key_arn)
        if s3_destination is not None:
            pulumi.set(__self__, "s3_destination", s3_destination)
        if sync_format is not None:
            pulumi.set(__self__, "sync_format", sync_format)
        if sync_source is not None:
            pulumi.set(__self__, "sync_source", sync_source)
        if sync_type is not None:
            pulumi.set(__self__, "sync_type", sync_type)

    @property
    @pulumi.getter(name="syncName")
    def sync_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "sync_name")

    @sync_name.setter
    def sync_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "sync_name", value)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bucket_name")

    @bucket_name.setter
    def bucket_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_name", value)

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bucket_prefix")

    @bucket_prefix.setter
    def bucket_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_prefix", value)

    @property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "bucket_region")

    @bucket_region.setter
    def bucket_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "bucket_region", value)

    @property
    @pulumi.getter(name="kMSKeyArn")
    def k_ms_key_arn(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "k_ms_key_arn")

    @k_ms_key_arn.setter
    def k_ms_key_arn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "k_ms_key_arn", value)

    @property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> Optional[pulumi.Input['ResourceDataSyncS3DestinationArgs']]:
        return pulumi.get(self, "s3_destination")

    @s3_destination.setter
    def s3_destination(self, value: Optional[pulumi.Input['ResourceDataSyncS3DestinationArgs']]):
        pulumi.set(self, "s3_destination", value)

    @property
    @pulumi.getter(name="syncFormat")
    def sync_format(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sync_format")

    @sync_format.setter
    def sync_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_format", value)

    @property
    @pulumi.getter(name="syncSource")
    def sync_source(self) -> Optional[pulumi.Input['ResourceDataSyncSyncSourceArgs']]:
        return pulumi.get(self, "sync_source")

    @sync_source.setter
    def sync_source(self, value: Optional[pulumi.Input['ResourceDataSyncSyncSourceArgs']]):
        pulumi.set(self, "sync_source", value)

    @property
    @pulumi.getter(name="syncType")
    def sync_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "sync_type")

    @sync_type.setter
    def sync_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sync_type", value)


class ResourceDataSync(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 bucket_region: Optional[pulumi.Input[str]] = None,
                 k_ms_key_arn: Optional[pulumi.Input[str]] = None,
                 s3_destination: Optional[pulumi.Input[pulumi.InputType['ResourceDataSyncS3DestinationArgs']]] = None,
                 sync_format: Optional[pulumi.Input[str]] = None,
                 sync_name: Optional[pulumi.Input[str]] = None,
                 sync_source: Optional[pulumi.Input[pulumi.InputType['ResourceDataSyncSyncSourceArgs']]] = None,
                 sync_type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::SSM::ResourceDataSync

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ResourceDataSyncArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::SSM::ResourceDataSync

        :param str resource_name: The name of the resource.
        :param ResourceDataSyncArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ResourceDataSyncArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket_name: Optional[pulumi.Input[str]] = None,
                 bucket_prefix: Optional[pulumi.Input[str]] = None,
                 bucket_region: Optional[pulumi.Input[str]] = None,
                 k_ms_key_arn: Optional[pulumi.Input[str]] = None,
                 s3_destination: Optional[pulumi.Input[pulumi.InputType['ResourceDataSyncS3DestinationArgs']]] = None,
                 sync_format: Optional[pulumi.Input[str]] = None,
                 sync_name: Optional[pulumi.Input[str]] = None,
                 sync_source: Optional[pulumi.Input[pulumi.InputType['ResourceDataSyncSyncSourceArgs']]] = None,
                 sync_type: Optional[pulumi.Input[str]] = None,
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
            __props__ = ResourceDataSyncArgs.__new__(ResourceDataSyncArgs)

            __props__.__dict__["bucket_name"] = bucket_name
            __props__.__dict__["bucket_prefix"] = bucket_prefix
            __props__.__dict__["bucket_region"] = bucket_region
            __props__.__dict__["k_ms_key_arn"] = k_ms_key_arn
            __props__.__dict__["s3_destination"] = s3_destination
            __props__.__dict__["sync_format"] = sync_format
            if sync_name is None and not opts.urn:
                raise TypeError("Missing required property 'sync_name'")
            __props__.__dict__["sync_name"] = sync_name
            __props__.__dict__["sync_source"] = sync_source
            __props__.__dict__["sync_type"] = sync_type
        super(ResourceDataSync, __self__).__init__(
            'aws-native:ssm:ResourceDataSync',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ResourceDataSync':
        """
        Get an existing ResourceDataSync resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ResourceDataSyncArgs.__new__(ResourceDataSyncArgs)

        __props__.__dict__["bucket_name"] = None
        __props__.__dict__["bucket_prefix"] = None
        __props__.__dict__["bucket_region"] = None
        __props__.__dict__["k_ms_key_arn"] = None
        __props__.__dict__["s3_destination"] = None
        __props__.__dict__["sync_format"] = None
        __props__.__dict__["sync_name"] = None
        __props__.__dict__["sync_source"] = None
        __props__.__dict__["sync_type"] = None
        return ResourceDataSync(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bucketName")
    def bucket_name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "bucket_name")

    @property
    @pulumi.getter(name="bucketPrefix")
    def bucket_prefix(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "bucket_prefix")

    @property
    @pulumi.getter(name="bucketRegion")
    def bucket_region(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "bucket_region")

    @property
    @pulumi.getter(name="kMSKeyArn")
    def k_ms_key_arn(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "k_ms_key_arn")

    @property
    @pulumi.getter(name="s3Destination")
    def s3_destination(self) -> pulumi.Output[Optional['outputs.ResourceDataSyncS3Destination']]:
        return pulumi.get(self, "s3_destination")

    @property
    @pulumi.getter(name="syncFormat")
    def sync_format(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sync_format")

    @property
    @pulumi.getter(name="syncName")
    def sync_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "sync_name")

    @property
    @pulumi.getter(name="syncSource")
    def sync_source(self) -> pulumi.Output[Optional['outputs.ResourceDataSyncSyncSource']]:
        return pulumi.get(self, "sync_source")

    @property
    @pulumi.getter(name="syncType")
    def sync_type(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "sync_type")


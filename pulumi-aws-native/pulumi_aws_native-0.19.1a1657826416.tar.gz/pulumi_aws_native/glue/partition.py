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

__all__ = ['PartitionArgs', 'Partition']

@pulumi.input_type
class PartitionArgs:
    def __init__(__self__, *,
                 catalog_id: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 partition_input: pulumi.Input['PartitionInputArgs'],
                 table_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a Partition resource.
        """
        pulumi.set(__self__, "catalog_id", catalog_id)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "partition_input", partition_input)
        pulumi.set(__self__, "table_name", table_name)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "catalog_id")

    @catalog_id.setter
    def catalog_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "catalog_id", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="partitionInput")
    def partition_input(self) -> pulumi.Input['PartitionInputArgs']:
        return pulumi.get(self, "partition_input")

    @partition_input.setter
    def partition_input(self, value: pulumi.Input['PartitionInputArgs']):
        pulumi.set(self, "partition_input", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[str]:
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_name", value)


warnings.warn("""Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class Partition(pulumi.CustomResource):
    warnings.warn("""Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 partition_input: Optional[pulumi.Input[pulumi.InputType['PartitionInputArgs']]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::Glue::Partition

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PartitionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::Glue::Partition

        :param str resource_name: The name of the resource.
        :param PartitionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PartitionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 catalog_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 partition_input: Optional[pulumi.Input[pulumi.InputType['PartitionInputArgs']]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Partition is deprecated: Partition is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = PartitionArgs.__new__(PartitionArgs)

            if catalog_id is None and not opts.urn:
                raise TypeError("Missing required property 'catalog_id'")
            __props__.__dict__["catalog_id"] = catalog_id
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if partition_input is None and not opts.urn:
                raise TypeError("Missing required property 'partition_input'")
            __props__.__dict__["partition_input"] = partition_input
            if table_name is None and not opts.urn:
                raise TypeError("Missing required property 'table_name'")
            __props__.__dict__["table_name"] = table_name
        super(Partition, __self__).__init__(
            'aws-native:glue:Partition',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Partition':
        """
        Get an existing Partition resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PartitionArgs.__new__(PartitionArgs)

        __props__.__dict__["catalog_id"] = None
        __props__.__dict__["database_name"] = None
        __props__.__dict__["partition_input"] = None
        __props__.__dict__["table_name"] = None
        return Partition(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogId")
    def catalog_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "catalog_id")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="partitionInput")
    def partition_input(self) -> pulumi.Output['outputs.PartitionInput']:
        return pulumi.get(self, "partition_input")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "table_name")


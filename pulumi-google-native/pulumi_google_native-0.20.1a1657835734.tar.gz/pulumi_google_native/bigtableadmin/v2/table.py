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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 instance_id: pulumi.Input[str],
                 table_id: pulumi.Input[str],
                 column_families: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 granularity: Optional[pulumi.Input['TableGranularity']] = None,
                 initial_splits: Optional[pulumi.Input[Sequence[pulumi.Input['SplitArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] table_id: The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`. Maximum 50 characters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] column_families: The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `FULL`
        :param pulumi.Input['TableGranularity'] granularity: Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.
        :param pulumi.Input[Sequence[pulumi.Input['SplitArgs']]] initial_splits: The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions). Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`. Example: * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]` * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]` * Key assignment: - Tablet 1 `[, apple) => {"a"}.` - Tablet 2 `[apple, customer_1) => {"apple", "custom"}.` - Tablet 3 `[customer_1, customer_2) => {"customer_1"}.` - Tablet 4 `[customer_2, other) => {"customer_2"}.` - Tablet 5 `[other, ) => {"other", "zz"}.`
        :param pulumi.Input[str] name: The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`
        """
        pulumi.set(__self__, "instance_id", instance_id)
        pulumi.set(__self__, "table_id", table_id)
        if column_families is not None:
            pulumi.set(__self__, "column_families", column_families)
        if granularity is not None:
            pulumi.set(__self__, "granularity", granularity)
        if initial_splits is not None:
            pulumi.set(__self__, "initial_splits", initial_splits)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if project is not None:
            pulumi.set(__self__, "project", project)

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Input[str]:
        return pulumi.get(self, "instance_id")

    @instance_id.setter
    def instance_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_id", value)

    @property
    @pulumi.getter(name="tableId")
    def table_id(self) -> pulumi.Input[str]:
        """
        The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`. Maximum 50 characters.
        """
        return pulumi.get(self, "table_id")

    @table_id.setter
    def table_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_id", value)

    @property
    @pulumi.getter(name="columnFamilies")
    def column_families(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `FULL`
        """
        return pulumi.get(self, "column_families")

    @column_families.setter
    def column_families(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "column_families", value)

    @property
    @pulumi.getter
    def granularity(self) -> Optional[pulumi.Input['TableGranularity']]:
        """
        Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.
        """
        return pulumi.get(self, "granularity")

    @granularity.setter
    def granularity(self, value: Optional[pulumi.Input['TableGranularity']]):
        pulumi.set(self, "granularity", value)

    @property
    @pulumi.getter(name="initialSplits")
    def initial_splits(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SplitArgs']]]]:
        """
        The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions). Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`. Example: * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]` * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]` * Key assignment: - Tablet 1 `[, apple) => {"a"}.` - Tablet 2 `[apple, customer_1) => {"apple", "custom"}.` - Tablet 3 `[customer_1, customer_2) => {"customer_1"}.` - Tablet 4 `[customer_2, other) => {"customer_2"}.` - Tablet 5 `[other, ) => {"other", "zz"}.`
        """
        return pulumi.get(self, "initial_splits")

    @initial_splits.setter
    def initial_splits(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SplitArgs']]]]):
        pulumi.set(self, "initial_splits", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 column_families: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 granularity: Optional[pulumi.Input['TableGranularity']] = None,
                 initial_splits: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SplitArgs']]]]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 table_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] column_families: The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `FULL`
        :param pulumi.Input['TableGranularity'] granularity: Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SplitArgs']]]] initial_splits: The optional list of row keys that will be used to initially split the table into several tablets (tablets are similar to HBase regions). Given two split keys, `s1` and `s2`, three tablets will be created, spanning the key ranges: `[, s1), [s1, s2), [s2, )`. Example: * Row keys := `["a", "apple", "custom", "customer_1", "customer_2",` `"other", "zz"]` * initial_split_keys := `["apple", "customer_1", "customer_2", "other"]` * Key assignment: - Tablet 1 `[, apple) => {"a"}.` - Tablet 2 `[apple, customer_1) => {"apple", "custom"}.` - Tablet 3 `[customer_1, customer_2) => {"customer_1"}.` - Tablet 4 `[customer_2, other) => {"customer_2"}.` - Tablet 5 `[other, ) => {"other", "zz"}.`
        :param pulumi.Input[str] name: The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`
        :param pulumi.Input[str] table_id: The name by which the new table should be referred to within the parent instance, e.g., `foobar` rather than `{parent}/tables/foobar`. Maximum 50 characters.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a new table in the specified instance. The table can be created with a full set of initial column families, specified in the request.

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 column_families: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 granularity: Optional[pulumi.Input['TableGranularity']] = None,
                 initial_splits: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SplitArgs']]]]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 table_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = TableArgs.__new__(TableArgs)

            __props__.__dict__["column_families"] = column_families
            __props__.__dict__["granularity"] = granularity
            __props__.__dict__["initial_splits"] = initial_splits
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__.__dict__["instance_id"] = instance_id
            __props__.__dict__["name"] = name
            __props__.__dict__["project"] = project
            if table_id is None and not opts.urn:
                raise TypeError("Missing required property 'table_id'")
            __props__.__dict__["table_id"] = table_id
            __props__.__dict__["cluster_states"] = None
            __props__.__dict__["restore_info"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["instance_id", "project"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(Table, __self__).__init__(
            'google-native:bigtableadmin/v2:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = TableArgs.__new__(TableArgs)

        __props__.__dict__["cluster_states"] = None
        __props__.__dict__["column_families"] = None
        __props__.__dict__["granularity"] = None
        __props__.__dict__["instance_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["restore_info"] = None
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterStates")
    def cluster_states(self) -> pulumi.Output[Mapping[str, str]]:
        """
        Map from cluster ID to per-cluster table state. If it could not be determined whether or not the table has data in a particular cluster (for example, if its zone is unavailable), then there will be an entry for the cluster with UNKNOWN `replication_status`. Views: `REPLICATION_VIEW`, `ENCRYPTION_VIEW`, `FULL`
        """
        return pulumi.get(self, "cluster_states")

    @property
    @pulumi.getter(name="columnFamilies")
    def column_families(self) -> pulumi.Output[Mapping[str, str]]:
        """
        The column families configured for this table, mapped by column family ID. Views: `SCHEMA_VIEW`, `FULL`
        """
        return pulumi.get(self, "column_families")

    @property
    @pulumi.getter
    def granularity(self) -> pulumi.Output[str]:
        """
        Immutable. The granularity (i.e. `MILLIS`) at which timestamps are stored in this table. Timestamps not matching the granularity will be rejected. If unspecified at creation time, the value will be set to `MILLIS`. Views: `SCHEMA_VIEW`, `FULL`.
        """
        return pulumi.get(self, "granularity")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The unique name of the table. Values are of the form `projects/{project}/instances/{instance}/tables/_a-zA-Z0-9*`. Views: `NAME_ONLY`, `SCHEMA_VIEW`, `REPLICATION_VIEW`, `FULL`
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="restoreInfo")
    def restore_info(self) -> pulumi.Output['outputs.RestoreInfoResponse']:
        """
        If this table was restored from another data source (e.g. a backup), this field will be populated with information about the restore.
        """
        return pulumi.get(self, "restore_info")


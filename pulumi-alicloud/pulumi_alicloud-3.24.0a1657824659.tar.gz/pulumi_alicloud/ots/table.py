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

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 instance_name: pulumi.Input[str],
                 max_version: pulumi.Input[int],
                 primary_keys: pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]],
                 table_name: pulumi.Input[str],
                 time_to_live: pulumi.Input[int],
                 deviation_cell_version_in_sec: Optional[pulumi.Input[str]] = None,
                 enable_sse: Optional[pulumi.Input[bool]] = None,
                 sse_key_type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] instance_name: The name of the OTS instance in which table will located.
        :param pulumi.Input[int] max_version: The maximum number of versions stored in this table. The valid value is 1-2147483647.
        :param pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]] primary_keys: The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        :param pulumi.Input[str] table_name: The table name of the OTS instance. If changed, a new table would be created.
        :param pulumi.Input[int] time_to_live: The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        :param pulumi.Input[str] deviation_cell_version_in_sec: The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        :param pulumi.Input[bool] enable_sse: Whether enable OTS server side encryption. Default value is false.
        :param pulumi.Input[str] sse_key_type: The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        """
        pulumi.set(__self__, "instance_name", instance_name)
        pulumi.set(__self__, "max_version", max_version)
        pulumi.set(__self__, "primary_keys", primary_keys)
        pulumi.set(__self__, "table_name", table_name)
        pulumi.set(__self__, "time_to_live", time_to_live)
        if deviation_cell_version_in_sec is not None:
            pulumi.set(__self__, "deviation_cell_version_in_sec", deviation_cell_version_in_sec)
        if enable_sse is not None:
            pulumi.set(__self__, "enable_sse", enable_sse)
        if sse_key_type is not None:
            pulumi.set(__self__, "sse_key_type", sse_key_type)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Input[str]:
        """
        The name of the OTS instance in which table will located.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="maxVersion")
    def max_version(self) -> pulumi.Input[int]:
        """
        The maximum number of versions stored in this table. The valid value is 1-2147483647.
        """
        return pulumi.get(self, "max_version")

    @max_version.setter
    def max_version(self, value: pulumi.Input[int]):
        pulumi.set(self, "max_version", value)

    @property
    @pulumi.getter(name="primaryKeys")
    def primary_keys(self) -> pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]]:
        """
        The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        """
        return pulumi.get(self, "primary_keys")

    @primary_keys.setter
    def primary_keys(self, value: pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]]):
        pulumi.set(self, "primary_keys", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Input[str]:
        """
        The table name of the OTS instance. If changed, a new table would be created.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> pulumi.Input[int]:
        """
        The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        """
        return pulumi.get(self, "time_to_live")

    @time_to_live.setter
    def time_to_live(self, value: pulumi.Input[int]):
        pulumi.set(self, "time_to_live", value)

    @property
    @pulumi.getter(name="deviationCellVersionInSec")
    def deviation_cell_version_in_sec(self) -> Optional[pulumi.Input[str]]:
        """
        The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        """
        return pulumi.get(self, "deviation_cell_version_in_sec")

    @deviation_cell_version_in_sec.setter
    def deviation_cell_version_in_sec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deviation_cell_version_in_sec", value)

    @property
    @pulumi.getter(name="enableSse")
    def enable_sse(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether enable OTS server side encryption. Default value is false.
        """
        return pulumi.get(self, "enable_sse")

    @enable_sse.setter
    def enable_sse(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_sse", value)

    @property
    @pulumi.getter(name="sseKeyType")
    def sse_key_type(self) -> Optional[pulumi.Input[str]]:
        """
        The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        """
        return pulumi.get(self, "sse_key_type")

    @sse_key_type.setter
    def sse_key_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sse_key_type", value)


@pulumi.input_type
class _TableState:
    def __init__(__self__, *,
                 deviation_cell_version_in_sec: Optional[pulumi.Input[str]] = None,
                 enable_sse: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 max_version: Optional[pulumi.Input[int]] = None,
                 primary_keys: Optional[pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]]] = None,
                 sse_key_type: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 time_to_live: Optional[pulumi.Input[int]] = None):
        """
        Input properties used for looking up and filtering Table resources.
        :param pulumi.Input[str] deviation_cell_version_in_sec: The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        :param pulumi.Input[bool] enable_sse: Whether enable OTS server side encryption. Default value is false.
        :param pulumi.Input[str] instance_name: The name of the OTS instance in which table will located.
        :param pulumi.Input[int] max_version: The maximum number of versions stored in this table. The valid value is 1-2147483647.
        :param pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]] primary_keys: The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        :param pulumi.Input[str] sse_key_type: The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        :param pulumi.Input[str] table_name: The table name of the OTS instance. If changed, a new table would be created.
        :param pulumi.Input[int] time_to_live: The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        """
        if deviation_cell_version_in_sec is not None:
            pulumi.set(__self__, "deviation_cell_version_in_sec", deviation_cell_version_in_sec)
        if enable_sse is not None:
            pulumi.set(__self__, "enable_sse", enable_sse)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if max_version is not None:
            pulumi.set(__self__, "max_version", max_version)
        if primary_keys is not None:
            pulumi.set(__self__, "primary_keys", primary_keys)
        if sse_key_type is not None:
            pulumi.set(__self__, "sse_key_type", sse_key_type)
        if table_name is not None:
            pulumi.set(__self__, "table_name", table_name)
        if time_to_live is not None:
            pulumi.set(__self__, "time_to_live", time_to_live)

    @property
    @pulumi.getter(name="deviationCellVersionInSec")
    def deviation_cell_version_in_sec(self) -> Optional[pulumi.Input[str]]:
        """
        The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        """
        return pulumi.get(self, "deviation_cell_version_in_sec")

    @deviation_cell_version_in_sec.setter
    def deviation_cell_version_in_sec(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deviation_cell_version_in_sec", value)

    @property
    @pulumi.getter(name="enableSse")
    def enable_sse(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether enable OTS server side encryption. Default value is false.
        """
        return pulumi.get(self, "enable_sse")

    @enable_sse.setter
    def enable_sse(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "enable_sse", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the OTS instance in which table will located.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="maxVersion")
    def max_version(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of versions stored in this table. The valid value is 1-2147483647.
        """
        return pulumi.get(self, "max_version")

    @max_version.setter
    def max_version(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_version", value)

    @property
    @pulumi.getter(name="primaryKeys")
    def primary_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]]]:
        """
        The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        """
        return pulumi.get(self, "primary_keys")

    @primary_keys.setter
    def primary_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TablePrimaryKeyArgs']]]]):
        pulumi.set(self, "primary_keys", value)

    @property
    @pulumi.getter(name="sseKeyType")
    def sse_key_type(self) -> Optional[pulumi.Input[str]]:
        """
        The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        """
        return pulumi.get(self, "sse_key_type")

    @sse_key_type.setter
    def sse_key_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sse_key_type", value)

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[pulumi.Input[str]]:
        """
        The table name of the OTS instance. If changed, a new table would be created.
        """
        return pulumi.get(self, "table_name")

    @table_name.setter
    def table_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "table_name", value)

    @property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> Optional[pulumi.Input[int]]:
        """
        The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        """
        return pulumi.get(self, "time_to_live")

    @time_to_live.setter
    def time_to_live(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "time_to_live", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deviation_cell_version_in_sec: Optional[pulumi.Input[str]] = None,
                 enable_sse: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 max_version: Optional[pulumi.Input[int]] = None,
                 primary_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePrimaryKeyArgs']]]]] = None,
                 sse_key_type: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 time_to_live: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        Provides an OTS table resource.

        > **NOTE:** From Provider version 1.10.0, the provider field 'ots_instance_name' has been deprecated and
        you should use resource alicloud_ots_table's new field 'instance_name' and 'table_name' to re-import this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraformtest"
        foo = alicloud.ots.Instance("foo",
            description=name,
            accessed_by="Any",
            tags={
                "Created": "TF",
                "For": "acceptance test",
            })
        basic = alicloud.ots.Table("basic",
            instance_name=foo.name,
            table_name=name,
            primary_keys=[
                alicloud.ots.TablePrimaryKeyArgs(
                    name="pk1",
                    type="Integer",
                ),
                alicloud.ots.TablePrimaryKeyArgs(
                    name="pk2",
                    type="String",
                ),
                alicloud.ots.TablePrimaryKeyArgs(
                    name="pk3",
                    type="Binary",
                ),
            ],
            time_to_live=-1,
            max_version=1,
            deviation_cell_version_in_sec="1",
            enable_sse=True,
            sse_key_type="SSE_KMS_SERVICE")
        ```

        ## Import

        OTS table can be imported using id, e.g.

        ```sh
         $ pulumi import alicloud:ots/table:Table table "my-ots:ots_table"
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deviation_cell_version_in_sec: The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        :param pulumi.Input[bool] enable_sse: Whether enable OTS server side encryption. Default value is false.
        :param pulumi.Input[str] instance_name: The name of the OTS instance in which table will located.
        :param pulumi.Input[int] max_version: The maximum number of versions stored in this table. The valid value is 1-2147483647.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePrimaryKeyArgs']]]] primary_keys: The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        :param pulumi.Input[str] sse_key_type: The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        :param pulumi.Input[str] table_name: The table name of the OTS instance. If changed, a new table would be created.
        :param pulumi.Input[int] time_to_live: The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides an OTS table resource.

        > **NOTE:** From Provider version 1.10.0, the provider field 'ots_instance_name' has been deprecated and
        you should use resource alicloud_ots_table's new field 'instance_name' and 'table_name' to re-import this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "terraformtest"
        foo = alicloud.ots.Instance("foo",
            description=name,
            accessed_by="Any",
            tags={
                "Created": "TF",
                "For": "acceptance test",
            })
        basic = alicloud.ots.Table("basic",
            instance_name=foo.name,
            table_name=name,
            primary_keys=[
                alicloud.ots.TablePrimaryKeyArgs(
                    name="pk1",
                    type="Integer",
                ),
                alicloud.ots.TablePrimaryKeyArgs(
                    name="pk2",
                    type="String",
                ),
                alicloud.ots.TablePrimaryKeyArgs(
                    name="pk3",
                    type="Binary",
                ),
            ],
            time_to_live=-1,
            max_version=1,
            deviation_cell_version_in_sec="1",
            enable_sse=True,
            sse_key_type="SSE_KMS_SERVICE")
        ```

        ## Import

        OTS table can be imported using id, e.g.

        ```sh
         $ pulumi import alicloud:ots/table:Table table "my-ots:ots_table"
        ```

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
                 deviation_cell_version_in_sec: Optional[pulumi.Input[str]] = None,
                 enable_sse: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 max_version: Optional[pulumi.Input[int]] = None,
                 primary_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePrimaryKeyArgs']]]]] = None,
                 sse_key_type: Optional[pulumi.Input[str]] = None,
                 table_name: Optional[pulumi.Input[str]] = None,
                 time_to_live: Optional[pulumi.Input[int]] = None,
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
            __props__ = TableArgs.__new__(TableArgs)

            __props__.__dict__["deviation_cell_version_in_sec"] = deviation_cell_version_in_sec
            __props__.__dict__["enable_sse"] = enable_sse
            if instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'instance_name'")
            __props__.__dict__["instance_name"] = instance_name
            if max_version is None and not opts.urn:
                raise TypeError("Missing required property 'max_version'")
            __props__.__dict__["max_version"] = max_version
            if primary_keys is None and not opts.urn:
                raise TypeError("Missing required property 'primary_keys'")
            __props__.__dict__["primary_keys"] = primary_keys
            __props__.__dict__["sse_key_type"] = sse_key_type
            if table_name is None and not opts.urn:
                raise TypeError("Missing required property 'table_name'")
            __props__.__dict__["table_name"] = table_name
            if time_to_live is None and not opts.urn:
                raise TypeError("Missing required property 'time_to_live'")
            __props__.__dict__["time_to_live"] = time_to_live
        super(Table, __self__).__init__(
            'alicloud:ots/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            deviation_cell_version_in_sec: Optional[pulumi.Input[str]] = None,
            enable_sse: Optional[pulumi.Input[bool]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            max_version: Optional[pulumi.Input[int]] = None,
            primary_keys: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePrimaryKeyArgs']]]]] = None,
            sse_key_type: Optional[pulumi.Input[str]] = None,
            table_name: Optional[pulumi.Input[str]] = None,
            time_to_live: Optional[pulumi.Input[int]] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deviation_cell_version_in_sec: The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        :param pulumi.Input[bool] enable_sse: Whether enable OTS server side encryption. Default value is false.
        :param pulumi.Input[str] instance_name: The name of the OTS instance in which table will located.
        :param pulumi.Input[int] max_version: The maximum number of versions stored in this table. The valid value is 1-2147483647.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePrimaryKeyArgs']]]] primary_keys: The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        :param pulumi.Input[str] sse_key_type: The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        :param pulumi.Input[str] table_name: The table name of the OTS instance. If changed, a new table would be created.
        :param pulumi.Input[int] time_to_live: The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TableState.__new__(_TableState)

        __props__.__dict__["deviation_cell_version_in_sec"] = deviation_cell_version_in_sec
        __props__.__dict__["enable_sse"] = enable_sse
        __props__.__dict__["instance_name"] = instance_name
        __props__.__dict__["max_version"] = max_version
        __props__.__dict__["primary_keys"] = primary_keys
        __props__.__dict__["sse_key_type"] = sse_key_type
        __props__.__dict__["table_name"] = table_name
        __props__.__dict__["time_to_live"] = time_to_live
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deviationCellVersionInSec")
    def deviation_cell_version_in_sec(self) -> pulumi.Output[Optional[str]]:
        """
        The max version offset of the table. The valid value is 1-9223372036854775807. Defaults to 86400.
        """
        return pulumi.get(self, "deviation_cell_version_in_sec")

    @property
    @pulumi.getter(name="enableSse")
    def enable_sse(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether enable OTS server side encryption. Default value is false.
        """
        return pulumi.get(self, "enable_sse")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[str]:
        """
        The name of the OTS instance in which table will located.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="maxVersion")
    def max_version(self) -> pulumi.Output[int]:
        """
        The maximum number of versions stored in this table. The valid value is 1-2147483647.
        """
        return pulumi.get(self, "max_version")

    @property
    @pulumi.getter(name="primaryKeys")
    def primary_keys(self) -> pulumi.Output[Sequence['outputs.TablePrimaryKey']]:
        """
        The property of `TableMeta` which indicates the structure information of a table. It describes the attribute value of primary key. The number of `primary_key` should not be less than one and not be more than four.
        """
        return pulumi.get(self, "primary_keys")

    @property
    @pulumi.getter(name="sseKeyType")
    def sse_key_type(self) -> pulumi.Output[Optional[str]]:
        """
        The key type of OTS server side encryption. Only `SSE_KMS_SERVICE` is allowed.
        """
        return pulumi.get(self, "sse_key_type")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> pulumi.Output[str]:
        """
        The table name of the OTS instance. If changed, a new table would be created.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter(name="timeToLive")
    def time_to_live(self) -> pulumi.Output[int]:
        """
        The retention time of data stored in this table (unit: second). The value maximum is 2147483647 and -1 means never expired.
        """
        return pulumi.get(self, "time_to_live")


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

__all__ = ['OtsBackupPlanArgs', 'OtsBackupPlan']

@pulumi.input_type
class OtsBackupPlanArgs:
    def __init__(__self__, *,
                 backup_type: pulumi.Input[str],
                 ots_backup_plan_name: pulumi.Input[str],
                 retention: pulumi.Input[str],
                 disabled: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 ots_details: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 vault_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a OtsBackupPlan resource.
        :param pulumi.Input[str] backup_type: The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] ots_backup_plan_name: The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        :param pulumi.Input[str] retention: Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[bool] disabled: Whether to disable the backup task. Valid values: true, false.
        :param pulumi.Input[str] instance_name: The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]] ots_details: The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]] rules: The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] schedule: Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] vault_id: The ID of backup vault.
        """
        pulumi.set(__self__, "backup_type", backup_type)
        pulumi.set(__self__, "ots_backup_plan_name", ots_backup_plan_name)
        pulumi.set(__self__, "retention", retention)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if ots_details is not None:
            pulumi.set(__self__, "ots_details", ots_details)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if schedule is not None:
            warnings.warn("""Field 'schedule' has been deprecated from version 1.163.0. Use 'rules' instead.""", DeprecationWarning)
            pulumi.log.warn("""schedule is deprecated: Field 'schedule' has been deprecated from version 1.163.0. Use 'rules' instead.""")
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if vault_id is not None:
            pulumi.set(__self__, "vault_id", vault_id)

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> pulumi.Input[str]:
        """
        The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "backup_type")

    @backup_type.setter
    def backup_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "backup_type", value)

    @property
    @pulumi.getter(name="otsBackupPlanName")
    def ots_backup_plan_name(self) -> pulumi.Input[str]:
        """
        The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        """
        return pulumi.get(self, "ots_backup_plan_name")

    @ots_backup_plan_name.setter
    def ots_backup_plan_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "ots_backup_plan_name", value)

    @property
    @pulumi.getter
    def retention(self) -> pulumi.Input[str]:
        """
        Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "retention")

    @retention.setter
    def retention(self, value: pulumi.Input[str]):
        pulumi.set(self, "retention", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to disable the backup task. Valid values: true, false.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="otsDetails")
    def ots_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]]]:
        """
        The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "ots_details")

    @ots_details.setter
    def ots_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]]]):
        pulumi.set(self, "ots_details", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]]]:
        """
        The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[str]]:
        """
        Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of backup vault.
        """
        return pulumi.get(self, "vault_id")

    @vault_id.setter
    def vault_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vault_id", value)


@pulumi.input_type
class _OtsBackupPlanState:
    def __init__(__self__, *,
                 backup_type: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 ots_backup_plan_name: Optional[pulumi.Input[str]] = None,
                 ots_details: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]]] = None,
                 retention: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 vault_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering OtsBackupPlan resources.
        :param pulumi.Input[str] backup_type: The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[bool] disabled: Whether to disable the backup task. Valid values: true, false.
        :param pulumi.Input[str] instance_name: The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] ots_backup_plan_name: The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        :param pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]] ots_details: The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] retention: Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]] rules: The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] schedule: Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] vault_id: The ID of backup vault.
        """
        if backup_type is not None:
            pulumi.set(__self__, "backup_type", backup_type)
        if disabled is not None:
            pulumi.set(__self__, "disabled", disabled)
        if instance_name is not None:
            pulumi.set(__self__, "instance_name", instance_name)
        if ots_backup_plan_name is not None:
            pulumi.set(__self__, "ots_backup_plan_name", ots_backup_plan_name)
        if ots_details is not None:
            pulumi.set(__self__, "ots_details", ots_details)
        if retention is not None:
            pulumi.set(__self__, "retention", retention)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)
        if schedule is not None:
            warnings.warn("""Field 'schedule' has been deprecated from version 1.163.0. Use 'rules' instead.""", DeprecationWarning)
            pulumi.log.warn("""schedule is deprecated: Field 'schedule' has been deprecated from version 1.163.0. Use 'rules' instead.""")
        if schedule is not None:
            pulumi.set(__self__, "schedule", schedule)
        if vault_id is not None:
            pulumi.set(__self__, "vault_id", vault_id)

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "backup_type")

    @backup_type.setter
    def backup_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_type", value)

    @property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to disable the backup task. Valid values: true, false.
        """
        return pulumi.get(self, "disabled")

    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "disabled", value)

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "instance_name")

    @instance_name.setter
    def instance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "instance_name", value)

    @property
    @pulumi.getter(name="otsBackupPlanName")
    def ots_backup_plan_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        """
        return pulumi.get(self, "ots_backup_plan_name")

    @ots_backup_plan_name.setter
    def ots_backup_plan_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ots_backup_plan_name", value)

    @property
    @pulumi.getter(name="otsDetails")
    def ots_details(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]]]:
        """
        The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "ots_details")

    @ots_details.setter
    def ots_details(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanOtsDetailArgs']]]]):
        pulumi.set(self, "ots_details", value)

    @property
    @pulumi.getter
    def retention(self) -> Optional[pulumi.Input[str]]:
        """
        Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "retention")

    @retention.setter
    def retention(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "retention", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]]]:
        """
        The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['OtsBackupPlanRuleArgs']]]]):
        pulumi.set(self, "rules", value)

    @property
    @pulumi.getter
    def schedule(self) -> Optional[pulumi.Input[str]]:
        """
        Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "schedule")

    @schedule.setter
    def schedule(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "schedule", value)

    @property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of backup vault.
        """
        return pulumi.get(self, "vault_id")

    @vault_id.setter
    def vault_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vault_id", value)


class OtsBackupPlan(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_type: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 ots_backup_plan_name: Optional[pulumi.Input[str]] = None,
                 ots_details: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanOtsDetailArgs']]]]] = None,
                 retention: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanRuleArgs']]]]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 vault_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a HBR Ots Backup Plan resource.

        For information about HBR Ots Backup Plan and how to use it, see [What is Ots Backup Plan](https://www.alibabacloud.com/help/en/hybrid-backup-recovery/latest/overview).

        > **NOTE:** Available in v1.163.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "testAcc"
        default = alicloud.hbr.Vault("default",
            vault_name=name,
            vault_type="OTS_BACKUP")
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
            primary_keys=[alicloud.ots.TablePrimaryKeyArgs(
                name="pk1",
                type="Integer",
            )],
            time_to_live=-1,
            max_version=1,
            deviation_cell_version_in_sec="1")
        example = alicloud.hbr.OtsBackupPlan("example",
            ots_backup_plan_name=name,
            vault_id=default.id,
            backup_type="COMPLETE",
            schedule="I|1602673264|PT2H",
            retention="2",
            instance_name=foo.name,
            ots_details=[alicloud.hbr.OtsBackupPlanOtsDetailArgs(
                table_names=[basic.table_name],
            )])
        ```

        ## Import

        HBR Ots Backup Plan can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:hbr/otsBackupPlan:OtsBackupPlan example <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_type: The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[bool] disabled: Whether to disable the backup task. Valid values: true, false.
        :param pulumi.Input[str] instance_name: The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] ots_backup_plan_name: The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanOtsDetailArgs']]]] ots_details: The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] retention: Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanRuleArgs']]]] rules: The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] schedule: Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] vault_id: The ID of backup vault.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: OtsBackupPlanArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a HBR Ots Backup Plan resource.

        For information about HBR Ots Backup Plan and how to use it, see [What is Ots Backup Plan](https://www.alibabacloud.com/help/en/hybrid-backup-recovery/latest/overview).

        > **NOTE:** Available in v1.163.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        config = pulumi.Config()
        name = config.get("name")
        if name is None:
            name = "testAcc"
        default = alicloud.hbr.Vault("default",
            vault_name=name,
            vault_type="OTS_BACKUP")
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
            primary_keys=[alicloud.ots.TablePrimaryKeyArgs(
                name="pk1",
                type="Integer",
            )],
            time_to_live=-1,
            max_version=1,
            deviation_cell_version_in_sec="1")
        example = alicloud.hbr.OtsBackupPlan("example",
            ots_backup_plan_name=name,
            vault_id=default.id,
            backup_type="COMPLETE",
            schedule="I|1602673264|PT2H",
            retention="2",
            instance_name=foo.name,
            ots_details=[alicloud.hbr.OtsBackupPlanOtsDetailArgs(
                table_names=[basic.table_name],
            )])
        ```

        ## Import

        HBR Ots Backup Plan can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:hbr/otsBackupPlan:OtsBackupPlan example <id>
        ```

        :param str resource_name: The name of the resource.
        :param OtsBackupPlanArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(OtsBackupPlanArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backup_type: Optional[pulumi.Input[str]] = None,
                 disabled: Optional[pulumi.Input[bool]] = None,
                 instance_name: Optional[pulumi.Input[str]] = None,
                 ots_backup_plan_name: Optional[pulumi.Input[str]] = None,
                 ots_details: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanOtsDetailArgs']]]]] = None,
                 retention: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanRuleArgs']]]]] = None,
                 schedule: Optional[pulumi.Input[str]] = None,
                 vault_id: Optional[pulumi.Input[str]] = None,
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
            __props__ = OtsBackupPlanArgs.__new__(OtsBackupPlanArgs)

            if backup_type is None and not opts.urn:
                raise TypeError("Missing required property 'backup_type'")
            __props__.__dict__["backup_type"] = backup_type
            __props__.__dict__["disabled"] = disabled
            __props__.__dict__["instance_name"] = instance_name
            if ots_backup_plan_name is None and not opts.urn:
                raise TypeError("Missing required property 'ots_backup_plan_name'")
            __props__.__dict__["ots_backup_plan_name"] = ots_backup_plan_name
            __props__.__dict__["ots_details"] = ots_details
            if retention is None and not opts.urn:
                raise TypeError("Missing required property 'retention'")
            __props__.__dict__["retention"] = retention
            __props__.__dict__["rules"] = rules
            if schedule is not None and not opts.urn:
                warnings.warn("""Field 'schedule' has been deprecated from version 1.163.0. Use 'rules' instead.""", DeprecationWarning)
                pulumi.log.warn("""schedule is deprecated: Field 'schedule' has been deprecated from version 1.163.0. Use 'rules' instead.""")
            __props__.__dict__["schedule"] = schedule
            __props__.__dict__["vault_id"] = vault_id
        super(OtsBackupPlan, __self__).__init__(
            'alicloud:hbr/otsBackupPlan:OtsBackupPlan',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_type: Optional[pulumi.Input[str]] = None,
            disabled: Optional[pulumi.Input[bool]] = None,
            instance_name: Optional[pulumi.Input[str]] = None,
            ots_backup_plan_name: Optional[pulumi.Input[str]] = None,
            ots_details: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanOtsDetailArgs']]]]] = None,
            retention: Optional[pulumi.Input[str]] = None,
            rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanRuleArgs']]]]] = None,
            schedule: Optional[pulumi.Input[str]] = None,
            vault_id: Optional[pulumi.Input[str]] = None) -> 'OtsBackupPlan':
        """
        Get an existing OtsBackupPlan resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_type: The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[bool] disabled: Whether to disable the backup task. Valid values: true, false.
        :param pulumi.Input[str] instance_name: The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] ots_backup_plan_name: The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanOtsDetailArgs']]]] ots_details: The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] retention: Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['OtsBackupPlanRuleArgs']]]] rules: The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] schedule: Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        :param pulumi.Input[str] vault_id: The ID of backup vault.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _OtsBackupPlanState.__new__(_OtsBackupPlanState)

        __props__.__dict__["backup_type"] = backup_type
        __props__.__dict__["disabled"] = disabled
        __props__.__dict__["instance_name"] = instance_name
        __props__.__dict__["ots_backup_plan_name"] = ots_backup_plan_name
        __props__.__dict__["ots_details"] = ots_details
        __props__.__dict__["retention"] = retention
        __props__.__dict__["rules"] = rules
        __props__.__dict__["schedule"] = schedule
        __props__.__dict__["vault_id"] = vault_id
        return OtsBackupPlan(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupType")
    def backup_type(self) -> pulumi.Output[str]:
        """
        The name of the tableStore instance. Valid values: `COMPLETE`, `INCREMENTAL`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "backup_type")

    @property
    @pulumi.getter
    def disabled(self) -> pulumi.Output[bool]:
        """
        Whether to disable the backup task. Valid values: true, false.
        """
        return pulumi.get(self, "disabled")

    @property
    @pulumi.getter(name="instanceName")
    def instance_name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the Table store instance. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "instance_name")

    @property
    @pulumi.getter(name="otsBackupPlanName")
    def ots_backup_plan_name(self) -> pulumi.Output[str]:
        """
        The name of the backup plan. 1~64 characters, the backup plan name of each data source type in a single warehouse required to be unique.
        """
        return pulumi.get(self, "ots_backup_plan_name")

    @property
    @pulumi.getter(name="otsDetails")
    def ots_details(self) -> pulumi.Output[Optional[Sequence['outputs.OtsBackupPlanOtsDetail']]]:
        """
        The details about the Table store instance. See the following `Block ots_detail`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "ots_details")

    @property
    @pulumi.getter
    def retention(self) -> pulumi.Output[str]:
        """
        Backup retention days, the minimum is 1. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "retention")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.OtsBackupPlanRule']]]:
        """
        The backup plan rule. See the following `Block rules`. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def schedule(self) -> pulumi.Output[Optional[str]]:
        """
        Backup strategy. Optional format: `I|{startTime}|{interval}`. It means to execute a backup task every `{interval}` starting from `{startTime}`. The backup task for the elapsed time will not be compensated. If the last backup task has not completed yet, the next backup task will not be triggered. **Note:** Required while source_type equals `OTS_TABLE`.
        """
        return pulumi.get(self, "schedule")

    @property
    @pulumi.getter(name="vaultId")
    def vault_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of backup vault.
        """
        return pulumi.get(self, "vault_id")


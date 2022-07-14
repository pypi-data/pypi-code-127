# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['IngestionArgs', 'Ingestion']

@pulumi.input_type
class IngestionArgs:
    def __init__(__self__, *,
                 display_name: pulumi.Input[str],
                 ingestion_name: pulumi.Input[str],
                 interval: pulumi.Input[str],
                 logstore: pulumi.Input[str],
                 project: pulumi.Input[str],
                 run_immediately: pulumi.Input[bool],
                 source: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Ingestion resource.
        :param pulumi.Input[str] display_name: The name displayed on the web page.
        :param pulumi.Input[str] ingestion_name: Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        :param pulumi.Input[str] interval: Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        :param pulumi.Input[str] logstore: The name of the target logstore.
        :param pulumi.Input[str] project: The name of the log project. It is the only in one Alicloud account.
        :param pulumi.Input[bool] run_immediately: Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        :param pulumi.Input[str] source: Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        :param pulumi.Input[str] description: Ingestion job description.
        :param pulumi.Input[str] time_zone: Which time zone is the log time imported in, e.g. `+0800`.
        """
        pulumi.set(__self__, "display_name", display_name)
        pulumi.set(__self__, "ingestion_name", ingestion_name)
        pulumi.set(__self__, "interval", interval)
        pulumi.set(__self__, "logstore", logstore)
        pulumi.set(__self__, "project", project)
        pulumi.set(__self__, "run_immediately", run_immediately)
        pulumi.set(__self__, "source", source)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[str]:
        """
        The name displayed on the web page.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="ingestionName")
    def ingestion_name(self) -> pulumi.Input[str]:
        """
        Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        """
        return pulumi.get(self, "ingestion_name")

    @ingestion_name.setter
    def ingestion_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "ingestion_name", value)

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Input[str]:
        """
        Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: pulumi.Input[str]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def logstore(self) -> pulumi.Input[str]:
        """
        The name of the target logstore.
        """
        return pulumi.get(self, "logstore")

    @logstore.setter
    def logstore(self, value: pulumi.Input[str]):
        pulumi.set(self, "logstore", value)

    @property
    @pulumi.getter
    def project(self) -> pulumi.Input[str]:
        """
        The name of the log project. It is the only in one Alicloud account.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: pulumi.Input[str]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="runImmediately")
    def run_immediately(self) -> pulumi.Input[bool]:
        """
        Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        """
        return pulumi.get(self, "run_immediately")

    @run_immediately.setter
    def run_immediately(self, value: pulumi.Input[bool]):
        pulumi.set(self, "run_immediately", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Ingestion job description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Which time zone is the log time imported in, e.g. `+0800`.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


@pulumi.input_type
class _IngestionState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ingestion_name: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[str]] = None,
                 logstore: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 run_immediately: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Ingestion resources.
        :param pulumi.Input[str] description: Ingestion job description.
        :param pulumi.Input[str] display_name: The name displayed on the web page.
        :param pulumi.Input[str] ingestion_name: Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        :param pulumi.Input[str] interval: Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        :param pulumi.Input[str] logstore: The name of the target logstore.
        :param pulumi.Input[str] project: The name of the log project. It is the only in one Alicloud account.
        :param pulumi.Input[bool] run_immediately: Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        :param pulumi.Input[str] source: Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        :param pulumi.Input[str] time_zone: Which time zone is the log time imported in, e.g. `+0800`.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if ingestion_name is not None:
            pulumi.set(__self__, "ingestion_name", ingestion_name)
        if interval is not None:
            pulumi.set(__self__, "interval", interval)
        if logstore is not None:
            pulumi.set(__self__, "logstore", logstore)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if run_immediately is not None:
            pulumi.set(__self__, "run_immediately", run_immediately)
        if source is not None:
            pulumi.set(__self__, "source", source)
        if time_zone is not None:
            pulumi.set(__self__, "time_zone", time_zone)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Ingestion job description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name displayed on the web page.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="ingestionName")
    def ingestion_name(self) -> Optional[pulumi.Input[str]]:
        """
        Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        """
        return pulumi.get(self, "ingestion_name")

    @ingestion_name.setter
    def ingestion_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ingestion_name", value)

    @property
    @pulumi.getter
    def interval(self) -> Optional[pulumi.Input[str]]:
        """
        Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        """
        return pulumi.get(self, "interval")

    @interval.setter
    def interval(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interval", value)

    @property
    @pulumi.getter
    def logstore(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the target logstore.
        """
        return pulumi.get(self, "logstore")

    @logstore.setter
    def logstore(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "logstore", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the log project. It is the only in one Alicloud account.
        """
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="runImmediately")
    def run_immediately(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        """
        return pulumi.get(self, "run_immediately")

    @run_immediately.setter
    def run_immediately(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "run_immediately", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Which time zone is the log time imported in, e.g. `+0800`.
        """
        return pulumi.get(self, "time_zone")

    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone", value)


class Ingestion(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ingestion_name: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[str]] = None,
                 logstore: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 run_immediately: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Log service ingestion, this service provides the function of importing logs of various data sources(OSS, MaxCompute) into logstore.
        [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).

        > **NOTE:** Available in 1.161.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_project = alicloud.log.Project("exampleProject",
            description="created by terraform",
            tags={
                "test": "test",
            })
        example_store = alicloud.log.Store("exampleStore",
            project=example_project.name,
            retention_period=3650,
            shard_count=3,
            auto_split=True,
            max_split_shard_count=60,
            append_meta=True)
        example_ingestion = alicloud.log.Ingestion("exampleIngestion",
            project=example_project.name,
            logstore=example_store.name,
            ingestion_name="ingestion_name",
            display_name="display_name",
            description="oss2sls",
            interval="30m",
            run_immediately=True,
            time_zone="+0800",
            source=\"\"\"        {
                  "bucket": "bucket_name",
                  "compressionCodec": "none",
                  "encoding": "UTF-8",
                  "endpoint": "oss-cn-hangzhou-internal.aliyuncs.com",
                  "format": {
                    "escapeChar": "\\",
                    "fieldDelimiter": ",",
                    "fieldNames": [],
                    "firstRowAsHeader": true,
                    "maxLines": 1,
                    "quoteChar": "\"",
                    "skipLeadingRows": 0,
                    "timeField": "",
                    "type": "DelimitedText"
                  },
                  "pattern": "",
                  "prefix": "test-prefix/",
                  "restoreObjectEnabled": false,
                  "roleARN": "acs:ram::1049446484210612:role/aliyunlogimportossrole",
                  "type": "AliyunOSS"
                }
        \"\"\")
        ```

        ## Import

        Log ingestion can be imported using the id or name, e.g.

        ```sh
         $ pulumi import alicloud:log/ingestion:Ingestion example tf-log-project:tf-log-logstore:ingestion_name
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Ingestion job description.
        :param pulumi.Input[str] display_name: The name displayed on the web page.
        :param pulumi.Input[str] ingestion_name: Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        :param pulumi.Input[str] interval: Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        :param pulumi.Input[str] logstore: The name of the target logstore.
        :param pulumi.Input[str] project: The name of the log project. It is the only in one Alicloud account.
        :param pulumi.Input[bool] run_immediately: Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        :param pulumi.Input[str] source: Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        :param pulumi.Input[str] time_zone: Which time zone is the log time imported in, e.g. `+0800`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IngestionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Log service ingestion, this service provides the function of importing logs of various data sources(OSS, MaxCompute) into logstore.
        [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).

        > **NOTE:** Available in 1.161.0+

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        example_project = alicloud.log.Project("exampleProject",
            description="created by terraform",
            tags={
                "test": "test",
            })
        example_store = alicloud.log.Store("exampleStore",
            project=example_project.name,
            retention_period=3650,
            shard_count=3,
            auto_split=True,
            max_split_shard_count=60,
            append_meta=True)
        example_ingestion = alicloud.log.Ingestion("exampleIngestion",
            project=example_project.name,
            logstore=example_store.name,
            ingestion_name="ingestion_name",
            display_name="display_name",
            description="oss2sls",
            interval="30m",
            run_immediately=True,
            time_zone="+0800",
            source=\"\"\"        {
                  "bucket": "bucket_name",
                  "compressionCodec": "none",
                  "encoding": "UTF-8",
                  "endpoint": "oss-cn-hangzhou-internal.aliyuncs.com",
                  "format": {
                    "escapeChar": "\\",
                    "fieldDelimiter": ",",
                    "fieldNames": [],
                    "firstRowAsHeader": true,
                    "maxLines": 1,
                    "quoteChar": "\"",
                    "skipLeadingRows": 0,
                    "timeField": "",
                    "type": "DelimitedText"
                  },
                  "pattern": "",
                  "prefix": "test-prefix/",
                  "restoreObjectEnabled": false,
                  "roleARN": "acs:ram::1049446484210612:role/aliyunlogimportossrole",
                  "type": "AliyunOSS"
                }
        \"\"\")
        ```

        ## Import

        Log ingestion can be imported using the id or name, e.g.

        ```sh
         $ pulumi import alicloud:log/ingestion:Ingestion example tf-log-project:tf-log-logstore:ingestion_name
        ```

        :param str resource_name: The name of the resource.
        :param IngestionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IngestionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 ingestion_name: Optional[pulumi.Input[str]] = None,
                 interval: Optional[pulumi.Input[str]] = None,
                 logstore: Optional[pulumi.Input[str]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 run_immediately: Optional[pulumi.Input[bool]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 time_zone: Optional[pulumi.Input[str]] = None,
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
            __props__ = IngestionArgs.__new__(IngestionArgs)

            __props__.__dict__["description"] = description
            if display_name is None and not opts.urn:
                raise TypeError("Missing required property 'display_name'")
            __props__.__dict__["display_name"] = display_name
            if ingestion_name is None and not opts.urn:
                raise TypeError("Missing required property 'ingestion_name'")
            __props__.__dict__["ingestion_name"] = ingestion_name
            if interval is None and not opts.urn:
                raise TypeError("Missing required property 'interval'")
            __props__.__dict__["interval"] = interval
            if logstore is None and not opts.urn:
                raise TypeError("Missing required property 'logstore'")
            __props__.__dict__["logstore"] = logstore
            if project is None and not opts.urn:
                raise TypeError("Missing required property 'project'")
            __props__.__dict__["project"] = project
            if run_immediately is None and not opts.urn:
                raise TypeError("Missing required property 'run_immediately'")
            __props__.__dict__["run_immediately"] = run_immediately
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["time_zone"] = time_zone
        super(Ingestion, __self__).__init__(
            'alicloud:log/ingestion:Ingestion',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            display_name: Optional[pulumi.Input[str]] = None,
            ingestion_name: Optional[pulumi.Input[str]] = None,
            interval: Optional[pulumi.Input[str]] = None,
            logstore: Optional[pulumi.Input[str]] = None,
            project: Optional[pulumi.Input[str]] = None,
            run_immediately: Optional[pulumi.Input[bool]] = None,
            source: Optional[pulumi.Input[str]] = None,
            time_zone: Optional[pulumi.Input[str]] = None) -> 'Ingestion':
        """
        Get an existing Ingestion resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Ingestion job description.
        :param pulumi.Input[str] display_name: The name displayed on the web page.
        :param pulumi.Input[str] ingestion_name: Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        :param pulumi.Input[str] interval: Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        :param pulumi.Input[str] logstore: The name of the target logstore.
        :param pulumi.Input[str] project: The name of the log project. It is the only in one Alicloud account.
        :param pulumi.Input[bool] run_immediately: Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        :param pulumi.Input[str] source: Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        :param pulumi.Input[str] time_zone: Which time zone is the log time imported in, e.g. `+0800`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _IngestionState.__new__(_IngestionState)

        __props__.__dict__["description"] = description
        __props__.__dict__["display_name"] = display_name
        __props__.__dict__["ingestion_name"] = ingestion_name
        __props__.__dict__["interval"] = interval
        __props__.__dict__["logstore"] = logstore
        __props__.__dict__["project"] = project
        __props__.__dict__["run_immediately"] = run_immediately
        __props__.__dict__["source"] = source
        __props__.__dict__["time_zone"] = time_zone
        return Ingestion(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Ingestion job description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[str]:
        """
        The name displayed on the web page.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="ingestionName")
    def ingestion_name(self) -> pulumi.Output[str]:
        """
        Ingestion job name, it can only contain lowercase letters, numbers, dashes `-` and underscores `_`. It must start and end with lowercase letters or numbers, and the name must be 2 to 128 characters long.
        """
        return pulumi.get(self, "ingestion_name")

    @property
    @pulumi.getter
    def interval(self) -> pulumi.Output[str]:
        """
        Task execution interval, support minute `m`, hour `h`, day `d`, for example 30 minutes `30m`.
        """
        return pulumi.get(self, "interval")

    @property
    @pulumi.getter
    def logstore(self) -> pulumi.Output[str]:
        """
        The name of the target logstore.
        """
        return pulumi.get(self, "logstore")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        """
        The name of the log project. It is the only in one Alicloud account.
        """
        return pulumi.get(self, "project")

    @property
    @pulumi.getter(name="runImmediately")
    def run_immediately(self) -> pulumi.Output[bool]:
        """
        Whether to run the ingestion job immediately, if false, wait for an interval before starting the ingestion.
        """
        return pulumi.get(self, "run_immediately")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        Data source and data format details. [Refer to details](https://www.alibabacloud.com/help/en/doc-detail/147819.html).
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Which time zone is the log time imported in, e.g. `+0800`.
        """
        return pulumi.get(self, "time_zone")


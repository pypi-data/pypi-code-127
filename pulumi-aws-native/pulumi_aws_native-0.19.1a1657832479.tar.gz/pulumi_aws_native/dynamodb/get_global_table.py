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

__all__ = [
    'GetGlobalTableResult',
    'AwaitableGetGlobalTableResult',
    'get_global_table',
    'get_global_table_output',
]

@pulumi.output_type
class GetGlobalTableResult:
    def __init__(__self__, arn=None, attribute_definitions=None, billing_mode=None, global_secondary_indexes=None, replicas=None, s_se_specification=None, stream_arn=None, stream_specification=None, table_id=None, time_to_live_specification=None, write_provisioned_throughput_settings=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if attribute_definitions and not isinstance(attribute_definitions, list):
            raise TypeError("Expected argument 'attribute_definitions' to be a list")
        pulumi.set(__self__, "attribute_definitions", attribute_definitions)
        if billing_mode and not isinstance(billing_mode, str):
            raise TypeError("Expected argument 'billing_mode' to be a str")
        pulumi.set(__self__, "billing_mode", billing_mode)
        if global_secondary_indexes and not isinstance(global_secondary_indexes, list):
            raise TypeError("Expected argument 'global_secondary_indexes' to be a list")
        pulumi.set(__self__, "global_secondary_indexes", global_secondary_indexes)
        if replicas and not isinstance(replicas, list):
            raise TypeError("Expected argument 'replicas' to be a list")
        pulumi.set(__self__, "replicas", replicas)
        if s_se_specification and not isinstance(s_se_specification, dict):
            raise TypeError("Expected argument 's_se_specification' to be a dict")
        pulumi.set(__self__, "s_se_specification", s_se_specification)
        if stream_arn and not isinstance(stream_arn, str):
            raise TypeError("Expected argument 'stream_arn' to be a str")
        pulumi.set(__self__, "stream_arn", stream_arn)
        if stream_specification and not isinstance(stream_specification, dict):
            raise TypeError("Expected argument 'stream_specification' to be a dict")
        pulumi.set(__self__, "stream_specification", stream_specification)
        if table_id and not isinstance(table_id, str):
            raise TypeError("Expected argument 'table_id' to be a str")
        pulumi.set(__self__, "table_id", table_id)
        if time_to_live_specification and not isinstance(time_to_live_specification, dict):
            raise TypeError("Expected argument 'time_to_live_specification' to be a dict")
        pulumi.set(__self__, "time_to_live_specification", time_to_live_specification)
        if write_provisioned_throughput_settings and not isinstance(write_provisioned_throughput_settings, dict):
            raise TypeError("Expected argument 'write_provisioned_throughput_settings' to be a dict")
        pulumi.set(__self__, "write_provisioned_throughput_settings", write_provisioned_throughput_settings)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="attributeDefinitions")
    def attribute_definitions(self) -> Optional[Sequence['outputs.GlobalTableAttributeDefinition']]:
        return pulumi.get(self, "attribute_definitions")

    @property
    @pulumi.getter(name="billingMode")
    def billing_mode(self) -> Optional[str]:
        return pulumi.get(self, "billing_mode")

    @property
    @pulumi.getter(name="globalSecondaryIndexes")
    def global_secondary_indexes(self) -> Optional[Sequence['outputs.GlobalTableGlobalSecondaryIndex']]:
        return pulumi.get(self, "global_secondary_indexes")

    @property
    @pulumi.getter
    def replicas(self) -> Optional[Sequence['outputs.GlobalTableReplicaSpecification']]:
        return pulumi.get(self, "replicas")

    @property
    @pulumi.getter(name="sSESpecification")
    def s_se_specification(self) -> Optional['outputs.GlobalTableSSESpecification']:
        return pulumi.get(self, "s_se_specification")

    @property
    @pulumi.getter(name="streamArn")
    def stream_arn(self) -> Optional[str]:
        return pulumi.get(self, "stream_arn")

    @property
    @pulumi.getter(name="streamSpecification")
    def stream_specification(self) -> Optional['outputs.GlobalTableStreamSpecification']:
        return pulumi.get(self, "stream_specification")

    @property
    @pulumi.getter(name="tableId")
    def table_id(self) -> Optional[str]:
        return pulumi.get(self, "table_id")

    @property
    @pulumi.getter(name="timeToLiveSpecification")
    def time_to_live_specification(self) -> Optional['outputs.GlobalTableTimeToLiveSpecification']:
        return pulumi.get(self, "time_to_live_specification")

    @property
    @pulumi.getter(name="writeProvisionedThroughputSettings")
    def write_provisioned_throughput_settings(self) -> Optional['outputs.GlobalTableWriteProvisionedThroughputSettings']:
        return pulumi.get(self, "write_provisioned_throughput_settings")


class AwaitableGetGlobalTableResult(GetGlobalTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGlobalTableResult(
            arn=self.arn,
            attribute_definitions=self.attribute_definitions,
            billing_mode=self.billing_mode,
            global_secondary_indexes=self.global_secondary_indexes,
            replicas=self.replicas,
            s_se_specification=self.s_se_specification,
            stream_arn=self.stream_arn,
            stream_specification=self.stream_specification,
            table_id=self.table_id,
            time_to_live_specification=self.time_to_live_specification,
            write_provisioned_throughput_settings=self.write_provisioned_throughput_settings)


def get_global_table(table_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGlobalTableResult:
    """
    Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable
    """
    __args__ = dict()
    __args__['tableName'] = table_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:dynamodb:getGlobalTable', __args__, opts=opts, typ=GetGlobalTableResult).value

    return AwaitableGetGlobalTableResult(
        arn=__ret__.arn,
        attribute_definitions=__ret__.attribute_definitions,
        billing_mode=__ret__.billing_mode,
        global_secondary_indexes=__ret__.global_secondary_indexes,
        replicas=__ret__.replicas,
        s_se_specification=__ret__.s_se_specification,
        stream_arn=__ret__.stream_arn,
        stream_specification=__ret__.stream_specification,
        table_id=__ret__.table_id,
        time_to_live_specification=__ret__.time_to_live_specification,
        write_provisioned_throughput_settings=__ret__.write_provisioned_throughput_settings)


@_utilities.lift_output_func(get_global_table)
def get_global_table_output(table_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGlobalTableResult]:
    """
    Version: None. Resource Type definition for AWS::DynamoDB::GlobalTable
    """
    ...

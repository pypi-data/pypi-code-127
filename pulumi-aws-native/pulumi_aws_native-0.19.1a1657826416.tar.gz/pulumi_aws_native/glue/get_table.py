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
    'GetTableResult',
    'AwaitableGetTableResult',
    'get_table',
    'get_table_output',
]

@pulumi.output_type
class GetTableResult:
    def __init__(__self__, id=None, table_input=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if table_input and not isinstance(table_input, dict):
            raise TypeError("Expected argument 'table_input' to be a dict")
        pulumi.set(__self__, "table_input", table_input)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="tableInput")
    def table_input(self) -> Optional['outputs.TableInput']:
        return pulumi.get(self, "table_input")


class AwaitableGetTableResult(GetTableResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTableResult(
            id=self.id,
            table_input=self.table_input)


def get_table(id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTableResult:
    """
    Resource Type definition for AWS::Glue::Table
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:glue:getTable', __args__, opts=opts, typ=GetTableResult).value

    return AwaitableGetTableResult(
        id=__ret__.id,
        table_input=__ret__.table_input)


@_utilities.lift_output_func(get_table)
def get_table_output(id: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTableResult]:
    """
    Resource Type definition for AWS::Glue::Table
    """
    ...

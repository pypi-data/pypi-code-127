# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'ImportValueResult',
    'AwaitableImportValueResult',
    'import_value',
    'import_value_output',
]

@pulumi.output_type
class ImportValueResult:
    def __init__(__self__, value=None):
        if value and not isinstance(value, dict):
            raise TypeError("Expected argument 'value' to be a dict")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Any]:
        return pulumi.get(self, "value")


class AwaitableImportValueResult(ImportValueResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ImportValueResult(
            value=self.value)


def import_value(name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableImportValueResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:index:importValue', __args__, opts=opts, typ=ImportValueResult).value

    return AwaitableImportValueResult(
        value=__ret__.value)


@_utilities.lift_output_func(import_value)
def import_value_output(name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ImportValueResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...

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
    'GetKeyspaceResult',
    'AwaitableGetKeyspaceResult',
    'get_keyspace',
    'get_keyspace_output',
]

@pulumi.output_type
class GetKeyspaceResult:
    def __init__(__self__, tags=None):
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.KeyspaceTag']]:
        return pulumi.get(self, "tags")


class AwaitableGetKeyspaceResult(GetKeyspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeyspaceResult(
            tags=self.tags)


def get_keyspace(keyspace_name: Optional[str] = None,
                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetKeyspaceResult:
    """
    Resource schema for AWS::Cassandra::Keyspace


    :param str keyspace_name: Name for Cassandra keyspace
    """
    __args__ = dict()
    __args__['keyspaceName'] = keyspace_name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:cassandra:getKeyspace', __args__, opts=opts, typ=GetKeyspaceResult).value

    return AwaitableGetKeyspaceResult(
        tags=__ret__.tags)


@_utilities.lift_output_func(get_keyspace)
def get_keyspace_output(keyspace_name: Optional[pulumi.Input[str]] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetKeyspaceResult]:
    """
    Resource schema for AWS::Cassandra::Keyspace


    :param str keyspace_name: Name for Cassandra keyspace
    """
    ...

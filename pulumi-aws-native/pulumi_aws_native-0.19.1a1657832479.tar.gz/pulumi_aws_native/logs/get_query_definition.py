# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetQueryDefinitionResult',
    'AwaitableGetQueryDefinitionResult',
    'get_query_definition',
    'get_query_definition_output',
]

@pulumi.output_type
class GetQueryDefinitionResult:
    def __init__(__self__, log_group_names=None, name=None, query_definition_id=None, query_string=None):
        if log_group_names and not isinstance(log_group_names, list):
            raise TypeError("Expected argument 'log_group_names' to be a list")
        pulumi.set(__self__, "log_group_names", log_group_names)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if query_definition_id and not isinstance(query_definition_id, str):
            raise TypeError("Expected argument 'query_definition_id' to be a str")
        pulumi.set(__self__, "query_definition_id", query_definition_id)
        if query_string and not isinstance(query_string, str):
            raise TypeError("Expected argument 'query_string' to be a str")
        pulumi.set(__self__, "query_string", query_string)

    @property
    @pulumi.getter(name="logGroupNames")
    def log_group_names(self) -> Optional[Sequence[str]]:
        """
        Optionally define specific log groups as part of your query definition
        """
        return pulumi.get(self, "log_group_names")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        A name for the saved query definition
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="queryDefinitionId")
    def query_definition_id(self) -> Optional[str]:
        """
        Unique identifier of a query definition
        """
        return pulumi.get(self, "query_definition_id")

    @property
    @pulumi.getter(name="queryString")
    def query_string(self) -> Optional[str]:
        """
        The query string to use for this definition
        """
        return pulumi.get(self, "query_string")


class AwaitableGetQueryDefinitionResult(GetQueryDefinitionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQueryDefinitionResult(
            log_group_names=self.log_group_names,
            name=self.name,
            query_definition_id=self.query_definition_id,
            query_string=self.query_string)


def get_query_definition(query_definition_id: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQueryDefinitionResult:
    """
    The resource schema for AWSLogs QueryDefinition


    :param str query_definition_id: Unique identifier of a query definition
    """
    __args__ = dict()
    __args__['queryDefinitionId'] = query_definition_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:logs:getQueryDefinition', __args__, opts=opts, typ=GetQueryDefinitionResult).value

    return AwaitableGetQueryDefinitionResult(
        log_group_names=__ret__.log_group_names,
        name=__ret__.name,
        query_definition_id=__ret__.query_definition_id,
        query_string=__ret__.query_string)


@_utilities.lift_output_func(get_query_definition)
def get_query_definition_output(query_definition_id: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQueryDefinitionResult]:
    """
    The resource schema for AWSLogs QueryDefinition


    :param str query_definition_id: Unique identifier of a query definition
    """
    ...

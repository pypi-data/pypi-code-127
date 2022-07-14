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
    'GetPreparedStatementResult',
    'AwaitableGetPreparedStatementResult',
    'get_prepared_statement',
    'get_prepared_statement_output',
]

@pulumi.output_type
class GetPreparedStatementResult:
    def __init__(__self__, description=None, query_statement=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if query_statement and not isinstance(query_statement, str):
            raise TypeError("Expected argument 'query_statement' to be a str")
        pulumi.set(__self__, "query_statement", query_statement)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the prepared statement.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="queryStatement")
    def query_statement(self) -> Optional[str]:
        """
        The query string for the prepared statement.
        """
        return pulumi.get(self, "query_statement")


class AwaitableGetPreparedStatementResult(GetPreparedStatementResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPreparedStatementResult(
            description=self.description,
            query_statement=self.query_statement)


def get_prepared_statement(statement_name: Optional[str] = None,
                           work_group: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPreparedStatementResult:
    """
    Resource schema for AWS::Athena::PreparedStatement


    :param str statement_name: The name of the prepared statement.
    :param str work_group: The name of the workgroup to which the prepared statement belongs.
    """
    __args__ = dict()
    __args__['statementName'] = statement_name
    __args__['workGroup'] = work_group
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:athena:getPreparedStatement', __args__, opts=opts, typ=GetPreparedStatementResult).value

    return AwaitableGetPreparedStatementResult(
        description=__ret__.description,
        query_statement=__ret__.query_statement)


@_utilities.lift_output_func(get_prepared_statement)
def get_prepared_statement_output(statement_name: Optional[pulumi.Input[str]] = None,
                                  work_group: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPreparedStatementResult]:
    """
    Resource schema for AWS::Athena::PreparedStatement


    :param str statement_name: The name of the prepared statement.
    :param str work_group: The name of the workgroup to which the prepared statement belongs.
    """
    ...

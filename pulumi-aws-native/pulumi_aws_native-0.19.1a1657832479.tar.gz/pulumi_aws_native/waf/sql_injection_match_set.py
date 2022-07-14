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
from ._inputs import *

__all__ = ['SqlInjectionMatchSetArgs', 'SqlInjectionMatchSet']

@pulumi.input_type
class SqlInjectionMatchSetArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 sql_injection_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input['SqlInjectionMatchSetSqlInjectionMatchTupleArgs']]]] = None):
        """
        The set of arguments for constructing a SqlInjectionMatchSet resource.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if sql_injection_match_tuples is not None:
            pulumi.set(__self__, "sql_injection_match_tuples", sql_injection_match_tuples)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="sqlInjectionMatchTuples")
    def sql_injection_match_tuples(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SqlInjectionMatchSetSqlInjectionMatchTupleArgs']]]]:
        return pulumi.get(self, "sql_injection_match_tuples")

    @sql_injection_match_tuples.setter
    def sql_injection_match_tuples(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SqlInjectionMatchSetSqlInjectionMatchTupleArgs']]]]):
        pulumi.set(self, "sql_injection_match_tuples", value)


warnings.warn("""SqlInjectionMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)


class SqlInjectionMatchSet(pulumi.CustomResource):
    warnings.warn("""SqlInjectionMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sql_injection_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SqlInjectionMatchSetSqlInjectionMatchTupleArgs']]]]] = None,
                 __props__=None):
        """
        Resource Type definition for AWS::WAF::SqlInjectionMatchSet

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[SqlInjectionMatchSetArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource Type definition for AWS::WAF::SqlInjectionMatchSet

        :param str resource_name: The name of the resource.
        :param SqlInjectionMatchSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlInjectionMatchSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 sql_injection_match_tuples: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SqlInjectionMatchSetSqlInjectionMatchTupleArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""SqlInjectionMatchSet is deprecated: SqlInjectionMatchSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.""")
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
            __props__ = SqlInjectionMatchSetArgs.__new__(SqlInjectionMatchSetArgs)

            __props__.__dict__["name"] = name
            __props__.__dict__["sql_injection_match_tuples"] = sql_injection_match_tuples
        super(SqlInjectionMatchSet, __self__).__init__(
            'aws-native:waf:SqlInjectionMatchSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlInjectionMatchSet':
        """
        Get an existing SqlInjectionMatchSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlInjectionMatchSetArgs.__new__(SqlInjectionMatchSetArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["sql_injection_match_tuples"] = None
        return SqlInjectionMatchSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sqlInjectionMatchTuples")
    def sql_injection_match_tuples(self) -> pulumi.Output[Optional[Sequence['outputs.SqlInjectionMatchSetSqlInjectionMatchTuple']]]:
        return pulumi.get(self, "sql_injection_match_tuples")


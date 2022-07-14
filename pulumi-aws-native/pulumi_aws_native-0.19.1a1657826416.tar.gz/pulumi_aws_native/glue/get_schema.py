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
from ._enums import *

__all__ = [
    'GetSchemaResult',
    'AwaitableGetSchemaResult',
    'get_schema',
    'get_schema_output',
]

@pulumi.output_type
class GetSchemaResult:
    def __init__(__self__, arn=None, checkpoint_version=None, compatibility=None, description=None, initial_schema_version_id=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if checkpoint_version and not isinstance(checkpoint_version, dict):
            raise TypeError("Expected argument 'checkpoint_version' to be a dict")
        pulumi.set(__self__, "checkpoint_version", checkpoint_version)
        if compatibility and not isinstance(compatibility, str):
            raise TypeError("Expected argument 'compatibility' to be a str")
        pulumi.set(__self__, "compatibility", compatibility)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if initial_schema_version_id and not isinstance(initial_schema_version_id, str):
            raise TypeError("Expected argument 'initial_schema_version_id' to be a str")
        pulumi.set(__self__, "initial_schema_version_id", initial_schema_version_id)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        Amazon Resource Name for the Schema.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="checkpointVersion")
    def checkpoint_version(self) -> Optional['outputs.SchemaVersion']:
        return pulumi.get(self, "checkpoint_version")

    @property
    @pulumi.getter
    def compatibility(self) -> Optional['SchemaCompatibility']:
        """
        Compatibility setting for the schema.
        """
        return pulumi.get(self, "compatibility")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description of the schema. If description is not provided, there will not be any default value for this.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="initialSchemaVersionId")
    def initial_schema_version_id(self) -> Optional[str]:
        """
        Represents the version ID associated with the initial schema version.
        """
        return pulumi.get(self, "initial_schema_version_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.SchemaTag']]:
        """
        List of tags to tag the schema
        """
        return pulumi.get(self, "tags")


class AwaitableGetSchemaResult(GetSchemaResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSchemaResult(
            arn=self.arn,
            checkpoint_version=self.checkpoint_version,
            compatibility=self.compatibility,
            description=self.description,
            initial_schema_version_id=self.initial_schema_version_id,
            tags=self.tags)


def get_schema(arn: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSchemaResult:
    """
    This resource represents a schema of Glue Schema Registry.


    :param str arn: Amazon Resource Name for the Schema.
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:glue:getSchema', __args__, opts=opts, typ=GetSchemaResult).value

    return AwaitableGetSchemaResult(
        arn=__ret__.arn,
        checkpoint_version=__ret__.checkpoint_version,
        compatibility=__ret__.compatibility,
        description=__ret__.description,
        initial_schema_version_id=__ret__.initial_schema_version_id,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_schema)
def get_schema_output(arn: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSchemaResult]:
    """
    This resource represents a schema of Glue Schema Registry.


    :param str arn: Amazon Resource Name for the Schema.
    """
    ...

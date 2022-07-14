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
    'GetEntityTypeResult',
    'AwaitableGetEntityTypeResult',
    'get_entity_type',
    'get_entity_type_output',
]

@pulumi.output_type
class GetEntityTypeResult:
    def __init__(__self__, arn=None, created_time=None, description=None, last_updated_time=None, tags=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if last_updated_time and not isinstance(last_updated_time, str):
            raise TypeError("Expected argument 'last_updated_time' to be a str")
        pulumi.set(__self__, "last_updated_time", last_updated_time)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        """
        The entity type ARN.
        """
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        """
        The timestamp when the entity type was created.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The entity type description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="lastUpdatedTime")
    def last_updated_time(self) -> Optional[str]:
        """
        The timestamp when the entity type was last updated.
        """
        return pulumi.get(self, "last_updated_time")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.EntityTypeTag']]:
        """
        Tags associated with this entity type.
        """
        return pulumi.get(self, "tags")


class AwaitableGetEntityTypeResult(GetEntityTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEntityTypeResult(
            arn=self.arn,
            created_time=self.created_time,
            description=self.description,
            last_updated_time=self.last_updated_time,
            tags=self.tags)


def get_entity_type(arn: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEntityTypeResult:
    """
    An entity type for fraud detector.


    :param str arn: The entity type ARN.
    """
    __args__ = dict()
    __args__['arn'] = arn
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:frauddetector:getEntityType', __args__, opts=opts, typ=GetEntityTypeResult).value

    return AwaitableGetEntityTypeResult(
        arn=__ret__.arn,
        created_time=__ret__.created_time,
        description=__ret__.description,
        last_updated_time=__ret__.last_updated_time,
        tags=__ret__.tags)


@_utilities.lift_output_func(get_entity_type)
def get_entity_type_output(arn: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEntityTypeResult]:
    """
    An entity type for fraud detector.


    :param str arn: The entity type ARN.
    """
    ...

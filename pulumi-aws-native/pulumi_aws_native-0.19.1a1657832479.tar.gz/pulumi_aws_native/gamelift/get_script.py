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
    'GetScriptResult',
    'AwaitableGetScriptResult',
    'get_script',
    'get_script_output',
]

@pulumi.output_type
class GetScriptResult:
    def __init__(__self__, arn=None, id=None, name=None, storage_location=None, tags=None, version=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_location and not isinstance(storage_location, dict):
            raise TypeError("Expected argument 'storage_location' to be a dict")
        pulumi.set(__self__, "storage_location", storage_location)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageLocation")
    def storage_location(self) -> Optional['outputs.ScriptS3Location']:
        return pulumi.get(self, "storage_location")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence['outputs.ScriptTag']]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        return pulumi.get(self, "version")


class AwaitableGetScriptResult(GetScriptResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScriptResult(
            arn=self.arn,
            id=self.id,
            name=self.name,
            storage_location=self.storage_location,
            tags=self.tags,
            version=self.version)


def get_script(id: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScriptResult:
    """
    Resource Type definition for AWS::GameLift::Script
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:gamelift:getScript', __args__, opts=opts, typ=GetScriptResult).value

    return AwaitableGetScriptResult(
        arn=__ret__.arn,
        id=__ret__.id,
        name=__ret__.name,
        storage_location=__ret__.storage_location,
        tags=__ret__.tags,
        version=__ret__.version)


@_utilities.lift_output_func(get_script)
def get_script_output(id: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScriptResult]:
    """
    Resource Type definition for AWS::GameLift::Script
    """
    ...

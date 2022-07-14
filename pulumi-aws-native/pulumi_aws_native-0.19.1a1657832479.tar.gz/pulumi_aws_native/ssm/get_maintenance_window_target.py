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
    'GetMaintenanceWindowTargetResult',
    'AwaitableGetMaintenanceWindowTargetResult',
    'get_maintenance_window_target',
    'get_maintenance_window_target_output',
]

@pulumi.output_type
class GetMaintenanceWindowTargetResult:
    def __init__(__self__, description=None, id=None, name=None, owner_information=None, resource_type=None, targets=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if owner_information and not isinstance(owner_information, str):
            raise TypeError("Expected argument 'owner_information' to be a str")
        pulumi.set(__self__, "owner_information", owner_information)
        if resource_type and not isinstance(resource_type, str):
            raise TypeError("Expected argument 'resource_type' to be a str")
        pulumi.set(__self__, "resource_type", resource_type)
        if targets and not isinstance(targets, list):
            raise TypeError("Expected argument 'targets' to be a list")
        pulumi.set(__self__, "targets", targets)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ownerInformation")
    def owner_information(self) -> Optional[str]:
        return pulumi.get(self, "owner_information")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def targets(self) -> Optional[Sequence['outputs.MaintenanceWindowTargetTargets']]:
        return pulumi.get(self, "targets")


class AwaitableGetMaintenanceWindowTargetResult(GetMaintenanceWindowTargetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMaintenanceWindowTargetResult(
            description=self.description,
            id=self.id,
            name=self.name,
            owner_information=self.owner_information,
            resource_type=self.resource_type,
            targets=self.targets)


def get_maintenance_window_target(id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMaintenanceWindowTargetResult:
    """
    Resource Type definition for AWS::SSM::MaintenanceWindowTarget
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ssm:getMaintenanceWindowTarget', __args__, opts=opts, typ=GetMaintenanceWindowTargetResult).value

    return AwaitableGetMaintenanceWindowTargetResult(
        description=__ret__.description,
        id=__ret__.id,
        name=__ret__.name,
        owner_information=__ret__.owner_information,
        resource_type=__ret__.resource_type,
        targets=__ret__.targets)


@_utilities.lift_output_func(get_maintenance_window_target)
def get_maintenance_window_target_output(id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMaintenanceWindowTargetResult]:
    """
    Resource Type definition for AWS::SSM::MaintenanceWindowTarget
    """
    ...

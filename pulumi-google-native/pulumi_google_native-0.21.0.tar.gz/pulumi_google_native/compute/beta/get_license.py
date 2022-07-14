# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetLicenseResult',
    'AwaitableGetLicenseResult',
    'get_license',
    'get_license_output',
]

@pulumi.output_type
class GetLicenseResult:
    def __init__(__self__, charges_use_fee=None, creation_timestamp=None, description=None, kind=None, license_code=None, name=None, resource_requirements=None, self_link=None, transferable=None):
        if charges_use_fee and not isinstance(charges_use_fee, bool):
            raise TypeError("Expected argument 'charges_use_fee' to be a bool")
        if charges_use_fee is not None:
            warnings.warn("""[Output Only] Deprecated. This field no longer reflects whether a license charges a usage fee.""", DeprecationWarning)
            pulumi.log.warn("""charges_use_fee is deprecated: [Output Only] Deprecated. This field no longer reflects whether a license charges a usage fee.""")

        pulumi.set(__self__, "charges_use_fee", charges_use_fee)
        if creation_timestamp and not isinstance(creation_timestamp, str):
            raise TypeError("Expected argument 'creation_timestamp' to be a str")
        pulumi.set(__self__, "creation_timestamp", creation_timestamp)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if license_code and not isinstance(license_code, str):
            raise TypeError("Expected argument 'license_code' to be a str")
        pulumi.set(__self__, "license_code", license_code)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resource_requirements and not isinstance(resource_requirements, dict):
            raise TypeError("Expected argument 'resource_requirements' to be a dict")
        pulumi.set(__self__, "resource_requirements", resource_requirements)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if transferable and not isinstance(transferable, bool):
            raise TypeError("Expected argument 'transferable' to be a bool")
        pulumi.set(__self__, "transferable", transferable)

    @property
    @pulumi.getter(name="chargesUseFee")
    def charges_use_fee(self) -> bool:
        """
        Deprecated. This field no longer reflects whether a license charges a usage fee.
        """
        return pulumi.get(self, "charges_use_fee")

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> str:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        An optional textual description of the resource; provided by the client when the resource is created.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of resource. Always compute#license for licenses.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter(name="licenseCode")
    def license_code(self) -> str:
        """
        The unique code used to attach this license to images, snapshots, and disks.
        """
        return pulumi.get(self, "license_code")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource. The name must be 1-63 characters long and comply with RFC1035.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="resourceRequirements")
    def resource_requirements(self) -> 'outputs.LicenseResourceRequirementsResponse':
        return pulumi.get(self, "resource_requirements")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def transferable(self) -> bool:
        """
        If false, licenses will not be copied from the source resource when creating an image from a disk, disk from snapshot, or snapshot from disk.
        """
        return pulumi.get(self, "transferable")


class AwaitableGetLicenseResult(GetLicenseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLicenseResult(
            charges_use_fee=self.charges_use_fee,
            creation_timestamp=self.creation_timestamp,
            description=self.description,
            kind=self.kind,
            license_code=self.license_code,
            name=self.name,
            resource_requirements=self.resource_requirements,
            self_link=self.self_link,
            transferable=self.transferable)


def get_license(license: Optional[str] = None,
                project: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLicenseResult:
    """
    Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.
    """
    __args__ = dict()
    __args__['license'] = license
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:compute/beta:getLicense', __args__, opts=opts, typ=GetLicenseResult).value

    return AwaitableGetLicenseResult(
        charges_use_fee=__ret__.charges_use_fee,
        creation_timestamp=__ret__.creation_timestamp,
        description=__ret__.description,
        kind=__ret__.kind,
        license_code=__ret__.license_code,
        name=__ret__.name,
        resource_requirements=__ret__.resource_requirements,
        self_link=__ret__.self_link,
        transferable=__ret__.transferable)


@_utilities.lift_output_func(get_license)
def get_license_output(license: Optional[pulumi.Input[str]] = None,
                       project: Optional[pulumi.Input[Optional[str]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLicenseResult]:
    """
    Returns the specified License resource. *Caution* This resource is intended for use only by third-party partners who are creating Cloud Marketplace images.
    """
    ...

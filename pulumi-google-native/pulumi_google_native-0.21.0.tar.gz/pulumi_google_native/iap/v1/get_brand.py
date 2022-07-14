# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetBrandResult',
    'AwaitableGetBrandResult',
    'get_brand',
    'get_brand_output',
]

@pulumi.output_type
class GetBrandResult:
    def __init__(__self__, application_title=None, name=None, org_internal_only=None, support_email=None):
        if application_title and not isinstance(application_title, str):
            raise TypeError("Expected argument 'application_title' to be a str")
        pulumi.set(__self__, "application_title", application_title)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if org_internal_only and not isinstance(org_internal_only, bool):
            raise TypeError("Expected argument 'org_internal_only' to be a bool")
        pulumi.set(__self__, "org_internal_only", org_internal_only)
        if support_email and not isinstance(support_email, str):
            raise TypeError("Expected argument 'support_email' to be a str")
        pulumi.set(__self__, "support_email", support_email)

    @property
    @pulumi.getter(name="applicationTitle")
    def application_title(self) -> str:
        """
        Application name displayed on OAuth consent screen.
        """
        return pulumi.get(self, "application_title")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Identifier of the brand. NOTE: GCP project number achieves the same brand identification purpose as only one brand per project can be created.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orgInternalOnly")
    def org_internal_only(self) -> bool:
        """
        Whether the brand is only intended for usage inside the G Suite organization only.
        """
        return pulumi.get(self, "org_internal_only")

    @property
    @pulumi.getter(name="supportEmail")
    def support_email(self) -> str:
        """
        Support email displayed on the OAuth consent screen.
        """
        return pulumi.get(self, "support_email")


class AwaitableGetBrandResult(GetBrandResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBrandResult(
            application_title=self.application_title,
            name=self.name,
            org_internal_only=self.org_internal_only,
            support_email=self.support_email)


def get_brand(brand_id: Optional[str] = None,
              project: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBrandResult:
    """
    Retrieves the OAuth brand of the project.
    """
    __args__ = dict()
    __args__['brandId'] = brand_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:iap/v1:getBrand', __args__, opts=opts, typ=GetBrandResult).value

    return AwaitableGetBrandResult(
        application_title=__ret__.application_title,
        name=__ret__.name,
        org_internal_only=__ret__.org_internal_only,
        support_email=__ret__.support_email)


@_utilities.lift_output_func(get_brand)
def get_brand_output(brand_id: Optional[pulumi.Input[str]] = None,
                     project: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBrandResult]:
    """
    Retrieves the OAuth brand of the project.
    """
    ...

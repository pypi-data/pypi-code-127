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
    'GetGcpUserAccessBindingResult',
    'AwaitableGetGcpUserAccessBindingResult',
    'get_gcp_user_access_binding',
    'get_gcp_user_access_binding_output',
]

@pulumi.output_type
class GetGcpUserAccessBindingResult:
    def __init__(__self__, access_levels=None, group_key=None, name=None):
        if access_levels and not isinstance(access_levels, list):
            raise TypeError("Expected argument 'access_levels' to be a list")
        pulumi.set(__self__, "access_levels", access_levels)
        if group_key and not isinstance(group_key, str):
            raise TypeError("Expected argument 'group_key' to be a str")
        pulumi.set(__self__, "group_key", group_key)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="accessLevels")
    def access_levels(self) -> Sequence[str]:
        """
        Access level that a user must have to be granted access. Only one access level is supported, not multiple. This repeated field must have exactly one element. Example: "accessPolicies/9522/accessLevels/device_trusted"
        """
        return pulumi.get(self, "access_levels")

    @property
    @pulumi.getter(name="groupKey")
    def group_key(self) -> str:
        """
        Immutable. Google Group id whose members are subject to this binding's restrictions. See "id" in the [G Suite Directory API's Groups resource] (https://developers.google.com/admin-sdk/directory/v1/reference/groups#resource). If a group's email address/alias is changed, this resource will continue to point at the changed group. This field does not accept group email addresses or aliases. Example: "01d520gv4vjcrht"
        """
        return pulumi.get(self, "group_key")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. Assigned by the server during creation. The last segment has an arbitrary length and has only URI unreserved characters (as defined by [RFC 3986 Section 2.3](https://tools.ietf.org/html/rfc3986#section-2.3)). Should not be specified by the client during creation. Example: "organizations/256/gcpUserAccessBindings/b3-BhcX_Ud5N"
        """
        return pulumi.get(self, "name")


class AwaitableGetGcpUserAccessBindingResult(GetGcpUserAccessBindingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGcpUserAccessBindingResult(
            access_levels=self.access_levels,
            group_key=self.group_key,
            name=self.name)


def get_gcp_user_access_binding(gcp_user_access_binding_id: Optional[str] = None,
                                organization_id: Optional[str] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGcpUserAccessBindingResult:
    """
    Gets the GcpUserAccessBinding with the given name.
    """
    __args__ = dict()
    __args__['gcpUserAccessBindingId'] = gcp_user_access_binding_id
    __args__['organizationId'] = organization_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:accesscontextmanager/v1:getGcpUserAccessBinding', __args__, opts=opts, typ=GetGcpUserAccessBindingResult).value

    return AwaitableGetGcpUserAccessBindingResult(
        access_levels=__ret__.access_levels,
        group_key=__ret__.group_key,
        name=__ret__.name)


@_utilities.lift_output_func(get_gcp_user_access_binding)
def get_gcp_user_access_binding_output(gcp_user_access_binding_id: Optional[pulumi.Input[str]] = None,
                                       organization_id: Optional[pulumi.Input[str]] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGcpUserAccessBindingResult]:
    """
    Gets the GcpUserAccessBinding with the given name.
    """
    ...

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetUserTenantsResult',
    'AwaitableGetUserTenantsResult',
    'get_user_tenants',
    'get_user_tenants_output',
]

@pulumi.output_type
class GetUserTenantsResult:
    """
    A collection of values returned by getUserTenants.
    """
    def __init__(__self__, id=None, ids=None, names=None, output_file=None, status=None, tenants=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tenants and not isinstance(tenants, list):
            raise TypeError("Expected argument 'tenants' to be a list")
        pulumi.set(__self__, "tenants", tenants)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Sequence[str]:
        """
        A list of DMS User Tenant IDs (UID).
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of DMS User Tenant names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the user tenant.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tenants(self) -> Sequence['outputs.GetUserTenantsTenantResult']:
        """
        A list of DMS User Tenants. Each element contains the following attributes:
        """
        return pulumi.get(self, "tenants")


class AwaitableGetUserTenantsResult(GetUserTenantsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserTenantsResult(
            id=self.id,
            ids=self.ids,
            names=self.names,
            output_file=self.output_file,
            status=self.status,
            tenants=self.tenants)


def get_user_tenants(ids: Optional[Sequence[str]] = None,
                     output_file: Optional[str] = None,
                     status: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetUserTenantsResult:
    """
    This data source provides a list of DMS User Tenants in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.161.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.dms.get_user_tenants(status="ACTIVE")
    pulumi.export("tid", default.ids[0])
    ```


    :param Sequence[str] ids: A list of DMS User Tenant IDs (TID).
    :param str status: The status of the user tenant.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['outputFile'] = output_file
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:dms/getUserTenants:getUserTenants', __args__, opts=opts, typ=GetUserTenantsResult).value

    return AwaitableGetUserTenantsResult(
        id=__ret__.id,
        ids=__ret__.ids,
        names=__ret__.names,
        output_file=__ret__.output_file,
        status=__ret__.status,
        tenants=__ret__.tenants)


@_utilities.lift_output_func(get_user_tenants)
def get_user_tenants_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            output_file: Optional[pulumi.Input[Optional[str]]] = None,
                            status: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetUserTenantsResult]:
    """
    This data source provides a list of DMS User Tenants in an Alibaba Cloud account according to the specified filters.

    > **NOTE:** Available in 1.161.0+

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.dms.get_user_tenants(status="ACTIVE")
    pulumi.export("tid", default.ids[0])
    ```


    :param Sequence[str] ids: A list of DMS User Tenant IDs (TID).
    :param str status: The status of the user tenant.
    """
    ...

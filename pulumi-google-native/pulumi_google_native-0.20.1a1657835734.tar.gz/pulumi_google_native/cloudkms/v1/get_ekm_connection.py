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
    'GetEkmConnectionResult',
    'AwaitableGetEkmConnectionResult',
    'get_ekm_connection',
    'get_ekm_connection_output',
]

@pulumi.output_type
class GetEkmConnectionResult:
    def __init__(__self__, create_time=None, etag=None, name=None, service_resolvers=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if service_resolvers and not isinstance(service_resolvers, list):
            raise TypeError("Expected argument 'service_resolvers' to be a list")
        pulumi.set(__self__, "service_resolvers", service_resolvers)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time at which the EkmConnection was created.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update requests to ensure the client has an up-to-date value before proceeding.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name for the EkmConnection in the format `projects/*/locations/*/ekmConnections/*`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serviceResolvers")
    def service_resolvers(self) -> Sequence['outputs.ServiceResolverResponse']:
        """
        A list of ServiceResolvers where the EKM can be reached. There should be one ServiceResolver per EKM replica. Currently, only a single ServiceResolver is supported.
        """
        return pulumi.get(self, "service_resolvers")


class AwaitableGetEkmConnectionResult(GetEkmConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEkmConnectionResult(
            create_time=self.create_time,
            etag=self.etag,
            name=self.name,
            service_resolvers=self.service_resolvers)


def get_ekm_connection(ekm_connection_id: Optional[str] = None,
                       location: Optional[str] = None,
                       project: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEkmConnectionResult:
    """
    Returns metadata for a given EkmConnection.
    """
    __args__ = dict()
    __args__['ekmConnectionId'] = ekm_connection_id
    __args__['location'] = location
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:cloudkms/v1:getEkmConnection', __args__, opts=opts, typ=GetEkmConnectionResult).value

    return AwaitableGetEkmConnectionResult(
        create_time=__ret__.create_time,
        etag=__ret__.etag,
        name=__ret__.name,
        service_resolvers=__ret__.service_resolvers)


@_utilities.lift_output_func(get_ekm_connection)
def get_ekm_connection_output(ekm_connection_id: Optional[pulumi.Input[str]] = None,
                              location: Optional[pulumi.Input[str]] = None,
                              project: Optional[pulumi.Input[Optional[str]]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEkmConnectionResult]:
    """
    Returns metadata for a given EkmConnection.
    """
    ...

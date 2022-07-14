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
    'GetResourceRecordSetResult',
    'AwaitableGetResourceRecordSetResult',
    'get_resource_record_set',
    'get_resource_record_set_output',
]

@pulumi.output_type
class GetResourceRecordSetResult:
    def __init__(__self__, kind=None, name=None, routing_policy=None, rrdatas=None, signature_rrdatas=None, ttl=None, type=None):
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if routing_policy and not isinstance(routing_policy, dict):
            raise TypeError("Expected argument 'routing_policy' to be a dict")
        pulumi.set(__self__, "routing_policy", routing_policy)
        if rrdatas and not isinstance(rrdatas, list):
            raise TypeError("Expected argument 'rrdatas' to be a list")
        pulumi.set(__self__, "rrdatas", rrdatas)
        if signature_rrdatas and not isinstance(signature_rrdatas, list):
            raise TypeError("Expected argument 'signature_rrdatas' to be a list")
        pulumi.set(__self__, "signature_rrdatas", signature_rrdatas)
        if ttl and not isinstance(ttl, int):
            raise TypeError("Expected argument 'ttl' to be a int")
        pulumi.set(__self__, "ttl", ttl)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def kind(self) -> str:
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        For example, www.example.com.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routingPolicy")
    def routing_policy(self) -> 'outputs.RRSetRoutingPolicyResponse':
        """
        Configures dynamic query responses based on geo location of querying user or a weighted round robin based routing policy. A ResourceRecordSet should only have either rrdata (static) or routing_policy (dynamic). An error is returned otherwise.
        """
        return pulumi.get(self, "routing_policy")

    @property
    @pulumi.getter
    def rrdatas(self) -> Sequence[str]:
        """
        As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see examples.
        """
        return pulumi.get(self, "rrdatas")

    @property
    @pulumi.getter(name="signatureRrdatas")
    def signature_rrdatas(self) -> Sequence[str]:
        """
        As defined in RFC 4034 (section 3.2).
        """
        return pulumi.get(self, "signature_rrdatas")

    @property
    @pulumi.getter
    def ttl(self) -> int:
        """
        Number of seconds that this ResourceRecordSet can be cached by resolvers.
        """
        return pulumi.get(self, "ttl")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The identifier of a supported record type. See the list of Supported DNS record types.
        """
        return pulumi.get(self, "type")


class AwaitableGetResourceRecordSetResult(GetResourceRecordSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetResourceRecordSetResult(
            kind=self.kind,
            name=self.name,
            routing_policy=self.routing_policy,
            rrdatas=self.rrdatas,
            signature_rrdatas=self.signature_rrdatas,
            ttl=self.ttl,
            type=self.type)


def get_resource_record_set(client_operation_id: Optional[str] = None,
                            location: Optional[str] = None,
                            managed_zone: Optional[str] = None,
                            name: Optional[str] = None,
                            project: Optional[str] = None,
                            type: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetResourceRecordSetResult:
    """
    Fetches the representation of an existing ResourceRecordSet.
    """
    __args__ = dict()
    __args__['clientOperationId'] = client_operation_id
    __args__['location'] = location
    __args__['managedZone'] = managed_zone
    __args__['name'] = name
    __args__['project'] = project
    __args__['type'] = type
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:dns/v2:getResourceRecordSet', __args__, opts=opts, typ=GetResourceRecordSetResult).value

    return AwaitableGetResourceRecordSetResult(
        kind=__ret__.kind,
        name=__ret__.name,
        routing_policy=__ret__.routing_policy,
        rrdatas=__ret__.rrdatas,
        signature_rrdatas=__ret__.signature_rrdatas,
        ttl=__ret__.ttl,
        type=__ret__.type)


@_utilities.lift_output_func(get_resource_record_set)
def get_resource_record_set_output(client_operation_id: Optional[pulumi.Input[Optional[str]]] = None,
                                   location: Optional[pulumi.Input[str]] = None,
                                   managed_zone: Optional[pulumi.Input[str]] = None,
                                   name: Optional[pulumi.Input[str]] = None,
                                   project: Optional[pulumi.Input[Optional[str]]] = None,
                                   type: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetResourceRecordSetResult]:
    """
    Fetches the representation of an existing ResourceRecordSet.
    """
    ...

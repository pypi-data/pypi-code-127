# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetThingPrincipalAttachmentResult',
    'AwaitableGetThingPrincipalAttachmentResult',
    'get_thing_principal_attachment',
    'get_thing_principal_attachment_output',
]

@pulumi.output_type
class GetThingPrincipalAttachmentResult:
    def __init__(__self__, id=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")


class AwaitableGetThingPrincipalAttachmentResult(GetThingPrincipalAttachmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetThingPrincipalAttachmentResult(
            id=self.id)


def get_thing_principal_attachment(id: Optional[str] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetThingPrincipalAttachmentResult:
    """
    Resource Type definition for AWS::IoT::ThingPrincipalAttachment
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iot:getThingPrincipalAttachment', __args__, opts=opts, typ=GetThingPrincipalAttachmentResult).value

    return AwaitableGetThingPrincipalAttachmentResult(
        id=__ret__.id)


@_utilities.lift_output_func(get_thing_principal_attachment)
def get_thing_principal_attachment_output(id: Optional[pulumi.Input[str]] = None,
                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetThingPrincipalAttachmentResult]:
    """
    Resource Type definition for AWS::IoT::ThingPrincipalAttachment
    """
    ...

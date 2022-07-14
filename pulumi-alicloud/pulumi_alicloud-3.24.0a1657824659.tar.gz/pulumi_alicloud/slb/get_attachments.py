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
    'GetAttachmentsResult',
    'AwaitableGetAttachmentsResult',
    'get_attachments',
    'get_attachments_output',
]

@pulumi.output_type
class GetAttachmentsResult:
    """
    A collection of values returned by getAttachments.
    """
    def __init__(__self__, id=None, instance_ids=None, load_balancer_id=None, output_file=None, slb_attachments=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if instance_ids and not isinstance(instance_ids, list):
            raise TypeError("Expected argument 'instance_ids' to be a list")
        pulumi.set(__self__, "instance_ids", instance_ids)
        if load_balancer_id and not isinstance(load_balancer_id, str):
            raise TypeError("Expected argument 'load_balancer_id' to be a str")
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if slb_attachments and not isinstance(slb_attachments, list):
            raise TypeError("Expected argument 'slb_attachments' to be a list")
        pulumi.set(__self__, "slb_attachments", slb_attachments)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="instanceIds")
    def instance_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "instance_ids")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> str:
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="slbAttachments")
    def slb_attachments(self) -> Sequence['outputs.GetAttachmentsSlbAttachmentResult']:
        """
        A list of SLB attachments. Each element contains the following attributes:
        """
        return pulumi.get(self, "slb_attachments")


class AwaitableGetAttachmentsResult(GetAttachmentsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAttachmentsResult(
            id=self.id,
            instance_ids=self.instance_ids,
            load_balancer_id=self.load_balancer_id,
            output_file=self.output_file,
            slb_attachments=self.slb_attachments)


def get_attachments(instance_ids: Optional[Sequence[str]] = None,
                    load_balancer_id: Optional[str] = None,
                    output_file: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAttachmentsResult:
    """
    This data source provides the server load balancer attachments of the current Alibaba Cloud user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    sample_ds = alicloud.slb.get_attachments(load_balancer_id=alicloud_slb_load_balancer["sample_slb"]["id"])
    pulumi.export("firstSlbAttachmentInstanceId", sample_ds.slb_attachments[0].instance_id)
    ```


    :param Sequence[str] instance_ids: List of attached ECS instance IDs.
    :param str load_balancer_id: ID of the SLB with attachments.
    """
    __args__ = dict()
    __args__['instanceIds'] = instance_ids
    __args__['loadBalancerId'] = load_balancer_id
    __args__['outputFile'] = output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:slb/getAttachments:getAttachments', __args__, opts=opts, typ=GetAttachmentsResult).value

    return AwaitableGetAttachmentsResult(
        id=__ret__.id,
        instance_ids=__ret__.instance_ids,
        load_balancer_id=__ret__.load_balancer_id,
        output_file=__ret__.output_file,
        slb_attachments=__ret__.slb_attachments)


@_utilities.lift_output_func(get_attachments)
def get_attachments_output(instance_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                           load_balancer_id: Optional[pulumi.Input[str]] = None,
                           output_file: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAttachmentsResult]:
    """
    This data source provides the server load balancer attachments of the current Alibaba Cloud user.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    sample_ds = alicloud.slb.get_attachments(load_balancer_id=alicloud_slb_load_balancer["sample_slb"]["id"])
    pulumi.export("firstSlbAttachmentInstanceId", sample_ds.slb_attachments[0].instance_id)
    ```


    :param Sequence[str] instance_ids: List of attached ECS instance IDs.
    :param str load_balancer_id: ID of the SLB with attachments.
    """
    ...

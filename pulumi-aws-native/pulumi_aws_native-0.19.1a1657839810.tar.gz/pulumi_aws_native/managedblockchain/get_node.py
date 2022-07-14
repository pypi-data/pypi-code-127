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
    'GetNodeResult',
    'AwaitableGetNodeResult',
    'get_node',
    'get_node_output',
]

@pulumi.output_type
class GetNodeResult:
    def __init__(__self__, arn=None, member_id=None, network_id=None, node_configuration=None, node_id=None):
        if arn and not isinstance(arn, str):
            raise TypeError("Expected argument 'arn' to be a str")
        pulumi.set(__self__, "arn", arn)
        if member_id and not isinstance(member_id, str):
            raise TypeError("Expected argument 'member_id' to be a str")
        pulumi.set(__self__, "member_id", member_id)
        if network_id and not isinstance(network_id, str):
            raise TypeError("Expected argument 'network_id' to be a str")
        pulumi.set(__self__, "network_id", network_id)
        if node_configuration and not isinstance(node_configuration, dict):
            raise TypeError("Expected argument 'node_configuration' to be a dict")
        pulumi.set(__self__, "node_configuration", node_configuration)
        if node_id and not isinstance(node_id, str):
            raise TypeError("Expected argument 'node_id' to be a str")
        pulumi.set(__self__, "node_id", node_id)

    @property
    @pulumi.getter
    def arn(self) -> Optional[str]:
        return pulumi.get(self, "arn")

    @property
    @pulumi.getter(name="memberId")
    def member_id(self) -> Optional[str]:
        return pulumi.get(self, "member_id")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> Optional[str]:
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="nodeConfiguration")
    def node_configuration(self) -> Optional['outputs.NodeConfiguration']:
        return pulumi.get(self, "node_configuration")

    @property
    @pulumi.getter(name="nodeId")
    def node_id(self) -> Optional[str]:
        return pulumi.get(self, "node_id")


class AwaitableGetNodeResult(GetNodeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodeResult(
            arn=self.arn,
            member_id=self.member_id,
            network_id=self.network_id,
            node_configuration=self.node_configuration,
            node_id=self.node_id)


def get_node(node_id: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNodeResult:
    """
    Resource Type definition for AWS::ManagedBlockchain::Node
    """
    __args__ = dict()
    __args__['nodeId'] = node_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:managedblockchain:getNode', __args__, opts=opts, typ=GetNodeResult).value

    return AwaitableGetNodeResult(
        arn=__ret__.arn,
        member_id=__ret__.member_id,
        network_id=__ret__.network_id,
        node_configuration=__ret__.node_configuration,
        node_id=__ret__.node_id)


@_utilities.lift_output_func(get_node)
def get_node_output(node_id: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNodeResult]:
    """
    Resource Type definition for AWS::ManagedBlockchain::Node
    """
    ...

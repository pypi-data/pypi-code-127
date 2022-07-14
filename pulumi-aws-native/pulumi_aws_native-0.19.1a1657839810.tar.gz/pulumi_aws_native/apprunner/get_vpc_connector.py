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
    'GetVpcConnectorResult',
    'AwaitableGetVpcConnectorResult',
    'get_vpc_connector',
    'get_vpc_connector_output',
]

@pulumi.output_type
class GetVpcConnectorResult:
    def __init__(__self__, vpc_connector_arn=None, vpc_connector_revision=None):
        if vpc_connector_arn and not isinstance(vpc_connector_arn, str):
            raise TypeError("Expected argument 'vpc_connector_arn' to be a str")
        pulumi.set(__self__, "vpc_connector_arn", vpc_connector_arn)
        if vpc_connector_revision and not isinstance(vpc_connector_revision, int):
            raise TypeError("Expected argument 'vpc_connector_revision' to be a int")
        pulumi.set(__self__, "vpc_connector_revision", vpc_connector_revision)

    @property
    @pulumi.getter(name="vpcConnectorArn")
    def vpc_connector_arn(self) -> Optional[str]:
        """
        The Amazon Resource Name (ARN) of this VPC connector.
        """
        return pulumi.get(self, "vpc_connector_arn")

    @property
    @pulumi.getter(name="vpcConnectorRevision")
    def vpc_connector_revision(self) -> Optional[int]:
        """
        The revision of this VPC connector. It's unique among all the active connectors ("Status": "ACTIVE") that share the same Name.
        """
        return pulumi.get(self, "vpc_connector_revision")


class AwaitableGetVpcConnectorResult(GetVpcConnectorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpcConnectorResult(
            vpc_connector_arn=self.vpc_connector_arn,
            vpc_connector_revision=self.vpc_connector_revision)


def get_vpc_connector(vpc_connector_arn: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpcConnectorResult:
    """
    The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.


    :param str vpc_connector_arn: The Amazon Resource Name (ARN) of this VPC connector.
    """
    __args__ = dict()
    __args__['vpcConnectorArn'] = vpc_connector_arn
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('aws-native:apprunner:getVpcConnector', __args__, opts=opts, typ=GetVpcConnectorResult).value

    return AwaitableGetVpcConnectorResult(
        vpc_connector_arn=__ret__.vpc_connector_arn,
        vpc_connector_revision=__ret__.vpc_connector_revision)


@_utilities.lift_output_func(get_vpc_connector)
def get_vpc_connector_output(vpc_connector_arn: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpcConnectorResult]:
    """
    The AWS::AppRunner::VpcConnector resource specifies an App Runner VpcConnector.


    :param str vpc_connector_arn: The Amazon Resource Name (ARN) of this VPC connector.
    """
    ...

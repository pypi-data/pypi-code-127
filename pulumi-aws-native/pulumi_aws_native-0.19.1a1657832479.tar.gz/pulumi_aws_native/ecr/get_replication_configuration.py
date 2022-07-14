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
from ._enums import *

__all__ = [
    'GetReplicationConfigurationResult',
    'AwaitableGetReplicationConfigurationResult',
    'get_replication_configuration',
    'get_replication_configuration_output',
]

@pulumi.output_type
class GetReplicationConfigurationResult:
    def __init__(__self__, registry_id=None, replication_configuration=None):
        if registry_id and not isinstance(registry_id, str):
            raise TypeError("Expected argument 'registry_id' to be a str")
        pulumi.set(__self__, "registry_id", registry_id)
        if replication_configuration and not isinstance(replication_configuration, dict):
            raise TypeError("Expected argument 'replication_configuration' to be a dict")
        pulumi.set(__self__, "replication_configuration", replication_configuration)

    @property
    @pulumi.getter(name="registryId")
    def registry_id(self) -> Optional[str]:
        """
        The RegistryId associated with the aws account.
        """
        return pulumi.get(self, "registry_id")

    @property
    @pulumi.getter(name="replicationConfiguration")
    def replication_configuration(self) -> Optional['outputs.ReplicationConfiguration']:
        return pulumi.get(self, "replication_configuration")


class AwaitableGetReplicationConfigurationResult(GetReplicationConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetReplicationConfigurationResult(
            registry_id=self.registry_id,
            replication_configuration=self.replication_configuration)


def get_replication_configuration(registry_id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetReplicationConfigurationResult:
    """
    The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html


    :param str registry_id: The RegistryId associated with the aws account.
    """
    __args__ = dict()
    __args__['registryId'] = registry_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:ecr:getReplicationConfiguration', __args__, opts=opts, typ=GetReplicationConfigurationResult).value

    return AwaitableGetReplicationConfigurationResult(
        registry_id=__ret__.registry_id,
        replication_configuration=__ret__.replication_configuration)


@_utilities.lift_output_func(get_replication_configuration)
def get_replication_configuration_output(registry_id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetReplicationConfigurationResult]:
    """
    The AWS::ECR::ReplicationConfiguration resource configures the replication destinations for an Amazon Elastic Container Registry (Amazon Private ECR). For more information, see https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html


    :param str registry_id: The RegistryId associated with the aws account.
    """
    ...

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
    'GetManagedPolicyResult',
    'AwaitableGetManagedPolicyResult',
    'get_managed_policy',
    'get_managed_policy_output',
]

@pulumi.output_type
class GetManagedPolicyResult:
    def __init__(__self__, groups=None, id=None, policy_document=None, roles=None, users=None):
        if groups and not isinstance(groups, list):
            raise TypeError("Expected argument 'groups' to be a list")
        pulumi.set(__self__, "groups", groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if policy_document and not isinstance(policy_document, dict):
            raise TypeError("Expected argument 'policy_document' to be a dict")
        pulumi.set(__self__, "policy_document", policy_document)
        if roles and not isinstance(roles, list):
            raise TypeError("Expected argument 'roles' to be a list")
        pulumi.set(__self__, "roles", roles)
        if users and not isinstance(users, list):
            raise TypeError("Expected argument 'users' to be a list")
        pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def groups(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "groups")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="policyDocument")
    def policy_document(self) -> Optional[Any]:
        return pulumi.get(self, "policy_document")

    @property
    @pulumi.getter
    def roles(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def users(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "users")


class AwaitableGetManagedPolicyResult(GetManagedPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedPolicyResult(
            groups=self.groups,
            id=self.id,
            policy_document=self.policy_document,
            roles=self.roles,
            users=self.users)


def get_managed_policy(id: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedPolicyResult:
    """
    Resource Type definition for AWS::IAM::ManagedPolicy
    """
    __args__ = dict()
    __args__['id'] = id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('aws-native:iam:getManagedPolicy', __args__, opts=opts, typ=GetManagedPolicyResult).value

    return AwaitableGetManagedPolicyResult(
        groups=__ret__.groups,
        id=__ret__.id,
        policy_document=__ret__.policy_document,
        roles=__ret__.roles,
        users=__ret__.users)


@_utilities.lift_output_func(get_managed_policy)
def get_managed_policy_output(id: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedPolicyResult]:
    """
    Resource Type definition for AWS::IAM::ManagedPolicy
    """
    ...

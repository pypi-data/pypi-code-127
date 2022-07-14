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
    'GetAutoSnapshotPoliciesResult',
    'AwaitableGetAutoSnapshotPoliciesResult',
    'get_auto_snapshot_policies',
    'get_auto_snapshot_policies_output',
]

@pulumi.output_type
class GetAutoSnapshotPoliciesResult:
    """
    A collection of values returned by getAutoSnapshotPolicies.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, policies=None, status=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if policies and not isinstance(policies, list):
            raise TypeError("Expected argument 'policies' to be a list")
        pulumi.set(__self__, "policies", policies)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)

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
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of Auto Snapshot Policy names.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def policies(self) -> Sequence['outputs.GetAutoSnapshotPoliciesPolicyResult']:
        """
        A list of Auto Snapshot Policies. Each element contains the following attributes:
        """
        return pulumi.get(self, "policies")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the automatic snapshot policy.
        """
        return pulumi.get(self, "status")


class AwaitableGetAutoSnapshotPoliciesResult(GetAutoSnapshotPoliciesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutoSnapshotPoliciesResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            policies=self.policies,
            status=self.status)


def get_auto_snapshot_policies(ids: Optional[Sequence[str]] = None,
                               name_regex: Optional[str] = None,
                               output_file: Optional[str] = None,
                               status: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutoSnapshotPoliciesResult:
    """
    This data source provides Auto Snapshot Policies available to the user.

    > **NOTE**: Available in v1.153.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.nas.get_auto_snapshot_policies(ids=["example_value"])
    pulumi.export("nasAutoSnapshotPoliciesId1", ids.policies[0].id)
    ```


    :param Sequence[str] ids: A list of Auto Snapshot Policies IDs.
    :param str name_regex: A regex string to filter results by Auto Snapshot Policy name.
    :param str status: The status of the automatic snapshot policy. Valid values: `Creating`, `Available`.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:nas/getAutoSnapshotPolicies:getAutoSnapshotPolicies', __args__, opts=opts, typ=GetAutoSnapshotPoliciesResult).value

    return AwaitableGetAutoSnapshotPoliciesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        policies=__ret__.policies,
        status=__ret__.status)


@_utilities.lift_output_func(get_auto_snapshot_policies)
def get_auto_snapshot_policies_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                      name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                      status: Optional[pulumi.Input[Optional[str]]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutoSnapshotPoliciesResult]:
    """
    This data source provides Auto Snapshot Policies available to the user.

    > **NOTE**: Available in v1.153.0+.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.nas.get_auto_snapshot_policies(ids=["example_value"])
    pulumi.export("nasAutoSnapshotPoliciesId1", ids.policies[0].id)
    ```


    :param Sequence[str] ids: A list of Auto Snapshot Policies IDs.
    :param str name_regex: A regex string to filter results by Auto Snapshot Policy name.
    :param str status: The status of the automatic snapshot policy. Valid values: `Creating`, `Available`.
    """
    ...

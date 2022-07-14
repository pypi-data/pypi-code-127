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
    'GetSnapshotsResult',
    'AwaitableGetSnapshotsResult',
    'get_snapshots',
    'get_snapshots_output',
]

@pulumi.output_type
class GetSnapshotsResult:
    """
    A collection of values returned by getSnapshots.
    """
    def __init__(__self__, desktop_id=None, id=None, ids=None, name_regex=None, names=None, output_file=None, snapshot_id=None, snapshots=None):
        if desktop_id and not isinstance(desktop_id, str):
            raise TypeError("Expected argument 'desktop_id' to be a str")
        pulumi.set(__self__, "desktop_id", desktop_id)
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
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError("Expected argument 'snapshot_id' to be a str")
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        if snapshots and not isinstance(snapshots, list):
            raise TypeError("Expected argument 'snapshots' to be a list")
        pulumi.set(__self__, "snapshots", snapshots)

    @property
    @pulumi.getter(name="desktopId")
    def desktop_id(self) -> Optional[str]:
        return pulumi.get(self, "desktop_id")

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
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[str]:
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter
    def snapshots(self) -> Sequence['outputs.GetSnapshotsSnapshotResult']:
        return pulumi.get(self, "snapshots")


class AwaitableGetSnapshotsResult(GetSnapshotsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSnapshotsResult(
            desktop_id=self.desktop_id,
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            snapshot_id=self.snapshot_id,
            snapshots=self.snapshots)


def get_snapshots(desktop_id: Optional[str] = None,
                  ids: Optional[Sequence[str]] = None,
                  name_regex: Optional[str] = None,
                  output_file: Optional[str] = None,
                  snapshot_id: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSnapshotsResult:
    """
    This data source provides the Ecd Snapshots of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.169.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.eds.get_snapshots()
    pulumi.export("ecdSnapshotId1", ids.snapshots[0].id)
    ```


    :param str desktop_id: The ID of the cloud desktop to which the snapshot belongs.
    :param Sequence[str] ids: A list of Snapshot IDs.
    :param str name_regex: A regex string to filter results by Snapshot name.
    :param str snapshot_id: The ID of the snapshot.
    """
    __args__ = dict()
    __args__['desktopId'] = desktop_id
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['snapshotId'] = snapshot_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:eds/getSnapshots:getSnapshots', __args__, opts=opts, typ=GetSnapshotsResult).value

    return AwaitableGetSnapshotsResult(
        desktop_id=__ret__.desktop_id,
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        snapshot_id=__ret__.snapshot_id,
        snapshots=__ret__.snapshots)


@_utilities.lift_output_func(get_snapshots)
def get_snapshots_output(desktop_id: Optional[pulumi.Input[Optional[str]]] = None,
                         ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                         name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                         output_file: Optional[pulumi.Input[Optional[str]]] = None,
                         snapshot_id: Optional[pulumi.Input[Optional[str]]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSnapshotsResult]:
    """
    This data source provides the Ecd Snapshots of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.169.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    ids = alicloud.eds.get_snapshots()
    pulumi.export("ecdSnapshotId1", ids.snapshots[0].id)
    ```


    :param str desktop_id: The ID of the cloud desktop to which the snapshot belongs.
    :param Sequence[str] ids: A list of Snapshot IDs.
    :param str name_regex: A regex string to filter results by Snapshot name.
    :param str snapshot_id: The ID of the snapshot.
    """
    ...

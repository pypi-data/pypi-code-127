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
    'GetMetadataImportResult',
    'AwaitableGetMetadataImportResult',
    'get_metadata_import',
    'get_metadata_import_output',
]

@pulumi.output_type
class GetMetadataImportResult:
    def __init__(__self__, create_time=None, database_dump=None, description=None, end_time=None, name=None, state=None, update_time=None):
        if create_time and not isinstance(create_time, str):
            raise TypeError("Expected argument 'create_time' to be a str")
        pulumi.set(__self__, "create_time", create_time)
        if database_dump and not isinstance(database_dump, dict):
            raise TypeError("Expected argument 'database_dump' to be a dict")
        pulumi.set(__self__, "database_dump", database_dump)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if end_time and not isinstance(end_time, str):
            raise TypeError("Expected argument 'end_time' to be a str")
        pulumi.set(__self__, "end_time", end_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if update_time and not isinstance(update_time, str):
            raise TypeError("Expected argument 'update_time' to be a str")
        pulumi.set(__self__, "update_time", update_time)

    @property
    @pulumi.getter(name="createTime")
    def create_time(self) -> str:
        """
        The time when the metadata import was started.
        """
        return pulumi.get(self, "create_time")

    @property
    @pulumi.getter(name="databaseDump")
    def database_dump(self) -> 'outputs.DatabaseDumpResponse':
        """
        Immutable. A database dump from a pre-existing metastore's database.
        """
        return pulumi.get(self, "database_dump")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The description of the metadata import.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="endTime")
    def end_time(self) -> str:
        """
        The time when the metadata import finished.
        """
        return pulumi.get(self, "end_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Immutable. The relative resource name of the metadata import, of the form:projects/{project_number}/locations/{location_id}/services/{service_id}/metadataImports/{metadata_import_id}.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the metadata import.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> str:
        """
        The time when the metadata import was last updated.
        """
        return pulumi.get(self, "update_time")


class AwaitableGetMetadataImportResult(GetMetadataImportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMetadataImportResult(
            create_time=self.create_time,
            database_dump=self.database_dump,
            description=self.description,
            end_time=self.end_time,
            name=self.name,
            state=self.state,
            update_time=self.update_time)


def get_metadata_import(location: Optional[str] = None,
                        metadata_import_id: Optional[str] = None,
                        project: Optional[str] = None,
                        service_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMetadataImportResult:
    """
    Gets details of a single import.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['metadataImportId'] = metadata_import_id
    __args__['project'] = project
    __args__['serviceId'] = service_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:metastore/v1alpha:getMetadataImport', __args__, opts=opts, typ=GetMetadataImportResult).value

    return AwaitableGetMetadataImportResult(
        create_time=__ret__.create_time,
        database_dump=__ret__.database_dump,
        description=__ret__.description,
        end_time=__ret__.end_time,
        name=__ret__.name,
        state=__ret__.state,
        update_time=__ret__.update_time)


@_utilities.lift_output_func(get_metadata_import)
def get_metadata_import_output(location: Optional[pulumi.Input[str]] = None,
                               metadata_import_id: Optional[pulumi.Input[str]] = None,
                               project: Optional[pulumi.Input[Optional[str]]] = None,
                               service_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMetadataImportResult]:
    """
    Gets details of a single import.
    """
    ...

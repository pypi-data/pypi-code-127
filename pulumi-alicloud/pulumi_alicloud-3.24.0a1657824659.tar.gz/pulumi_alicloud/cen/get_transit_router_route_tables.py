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
    'GetTransitRouterRouteTablesResult',
    'AwaitableGetTransitRouterRouteTablesResult',
    'get_transit_router_route_tables',
    'get_transit_router_route_tables_output',
]

@pulumi.output_type
class GetTransitRouterRouteTablesResult:
    """
    A collection of values returned by getTransitRouterRouteTables.
    """
    def __init__(__self__, id=None, ids=None, name_regex=None, names=None, output_file=None, status=None, tables=None, transit_router_id=None, transit_router_route_table_ids=None, transit_router_route_table_names=None, transit_router_route_table_status=None):
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
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tables and not isinstance(tables, list):
            raise TypeError("Expected argument 'tables' to be a list")
        pulumi.set(__self__, "tables", tables)
        if transit_router_id and not isinstance(transit_router_id, str):
            raise TypeError("Expected argument 'transit_router_id' to be a str")
        pulumi.set(__self__, "transit_router_id", transit_router_id)
        if transit_router_route_table_ids and not isinstance(transit_router_route_table_ids, list):
            raise TypeError("Expected argument 'transit_router_route_table_ids' to be a list")
        pulumi.set(__self__, "transit_router_route_table_ids", transit_router_route_table_ids)
        if transit_router_route_table_names and not isinstance(transit_router_route_table_names, list):
            raise TypeError("Expected argument 'transit_router_route_table_names' to be a list")
        pulumi.set(__self__, "transit_router_route_table_names", transit_router_route_table_names)
        if transit_router_route_table_status and not isinstance(transit_router_route_table_status, str):
            raise TypeError("Expected argument 'transit_router_route_table_status' to be a str")
        pulumi.set(__self__, "transit_router_route_table_status", transit_router_route_table_status)

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
        """
        A list of CEN Transit Router Route Table IDs.
        """
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter(name="nameRegex")
    def name_regex(self) -> Optional[str]:
        return pulumi.get(self, "name_regex")

    @property
    @pulumi.getter
    def names(self) -> Sequence[str]:
        """
        A list of name of CEN Transit Router Route Tables.
        """
        return pulumi.get(self, "names")

    @property
    @pulumi.getter(name="outputFile")
    def output_file(self) -> Optional[str]:
        return pulumi.get(self, "output_file")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tables(self) -> Sequence['outputs.GetTransitRouterRouteTablesTableResult']:
        """
        A list of CEN Route Entries. Each element contains the following attributes:
        """
        return pulumi.get(self, "tables")

    @property
    @pulumi.getter(name="transitRouterId")
    def transit_router_id(self) -> str:
        return pulumi.get(self, "transit_router_id")

    @property
    @pulumi.getter(name="transitRouterRouteTableIds")
    def transit_router_route_table_ids(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "transit_router_route_table_ids")

    @property
    @pulumi.getter(name="transitRouterRouteTableNames")
    def transit_router_route_table_names(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "transit_router_route_table_names")

    @property
    @pulumi.getter(name="transitRouterRouteTableStatus")
    def transit_router_route_table_status(self) -> Optional[str]:
        """
        The status of the route table.
        """
        return pulumi.get(self, "transit_router_route_table_status")


class AwaitableGetTransitRouterRouteTablesResult(GetTransitRouterRouteTablesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransitRouterRouteTablesResult(
            id=self.id,
            ids=self.ids,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            status=self.status,
            tables=self.tables,
            transit_router_id=self.transit_router_id,
            transit_router_route_table_ids=self.transit_router_route_table_ids,
            transit_router_route_table_names=self.transit_router_route_table_names,
            transit_router_route_table_status=self.transit_router_route_table_status)


def get_transit_router_route_tables(ids: Optional[Sequence[str]] = None,
                                    name_regex: Optional[str] = None,
                                    output_file: Optional[str] = None,
                                    status: Optional[str] = None,
                                    transit_router_id: Optional[str] = None,
                                    transit_router_route_table_ids: Optional[Sequence[str]] = None,
                                    transit_router_route_table_names: Optional[Sequence[str]] = None,
                                    transit_router_route_table_status: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransitRouterRouteTablesResult:
    """
    This data source provides CEN Transit Router Route Tables available to the user.[What is Cen Transit Router Route Tables](https://help.aliyun.com/document_detail/261237.html)

    > **NOTE:** Available in 1.126.0+


    :param Sequence[str] ids: A list of CEN Transit Router Route Table IDs.
    :param str transit_router_id: ID of the CEN Transit Router Route Table.
    :param Sequence[str] transit_router_route_table_ids: A list of ID of the CEN Transit Router Route Table.
    :param Sequence[str] transit_router_route_table_names: A list of name of the CEN Transit Router Route Table.
    :param str transit_router_route_table_status: The status of the transit router route table to query.
    """
    __args__ = dict()
    __args__['ids'] = ids
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['status'] = status
    __args__['transitRouterId'] = transit_router_id
    __args__['transitRouterRouteTableIds'] = transit_router_route_table_ids
    __args__['transitRouterRouteTableNames'] = transit_router_route_table_names
    __args__['transitRouterRouteTableStatus'] = transit_router_route_table_status
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:cen/getTransitRouterRouteTables:getTransitRouterRouteTables', __args__, opts=opts, typ=GetTransitRouterRouteTablesResult).value

    return AwaitableGetTransitRouterRouteTablesResult(
        id=__ret__.id,
        ids=__ret__.ids,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        status=__ret__.status,
        tables=__ret__.tables,
        transit_router_id=__ret__.transit_router_id,
        transit_router_route_table_ids=__ret__.transit_router_route_table_ids,
        transit_router_route_table_names=__ret__.transit_router_route_table_names,
        transit_router_route_table_status=__ret__.transit_router_route_table_status)


@_utilities.lift_output_func(get_transit_router_route_tables)
def get_transit_router_route_tables_output(ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                           name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                                           output_file: Optional[pulumi.Input[Optional[str]]] = None,
                                           status: Optional[pulumi.Input[Optional[str]]] = None,
                                           transit_router_id: Optional[pulumi.Input[str]] = None,
                                           transit_router_route_table_ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                           transit_router_route_table_names: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                           transit_router_route_table_status: Optional[pulumi.Input[Optional[str]]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransitRouterRouteTablesResult]:
    """
    This data source provides CEN Transit Router Route Tables available to the user.[What is Cen Transit Router Route Tables](https://help.aliyun.com/document_detail/261237.html)

    > **NOTE:** Available in 1.126.0+


    :param Sequence[str] ids: A list of CEN Transit Router Route Table IDs.
    :param str transit_router_id: ID of the CEN Transit Router Route Table.
    :param Sequence[str] transit_router_route_table_ids: A list of ID of the CEN Transit Router Route Table.
    :param Sequence[str] transit_router_route_table_names: A list of name of the CEN Transit Router Route Table.
    :param str transit_router_route_table_status: The status of the transit router route table to query.
    """
    ...

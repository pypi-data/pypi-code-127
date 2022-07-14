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
    'GetProductSetResult',
    'AwaitableGetProductSetResult',
    'get_product_set',
    'get_product_set_output',
]

@pulumi.output_type
class GetProductSetResult:
    def __init__(__self__, display_name=None, index_error=None, index_time=None, name=None):
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if index_error and not isinstance(index_error, dict):
            raise TypeError("Expected argument 'index_error' to be a dict")
        pulumi.set(__self__, "index_error", index_error)
        if index_time and not isinstance(index_time, str):
            raise TypeError("Expected argument 'index_time' to be a str")
        pulumi.set(__self__, "index_time", index_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The user-provided name for this ProductSet. Must not be empty. Must be at most 4096 characters long.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="indexError")
    def index_error(self) -> 'outputs.StatusResponse':
        """
        If there was an error with indexing the product set, the field is populated. This field is ignored when creating a ProductSet.
        """
        return pulumi.get(self, "index_error")

    @property
    @pulumi.getter(name="indexTime")
    def index_time(self) -> str:
        """
        The time at which this ProductSet was last indexed. Query results will reflect all updates before this time. If this ProductSet has never been indexed, this timestamp is the default value "1970-01-01T00:00:00Z". This field is ignored when creating a ProductSet.
        """
        return pulumi.get(self, "index_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name of the ProductSet. Format is: `projects/PROJECT_ID/locations/LOC_ID/productSets/PRODUCT_SET_ID`. This field is ignored when creating a ProductSet.
        """
        return pulumi.get(self, "name")


class AwaitableGetProductSetResult(GetProductSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProductSetResult(
            display_name=self.display_name,
            index_error=self.index_error,
            index_time=self.index_time,
            name=self.name)


def get_product_set(location: Optional[str] = None,
                    product_set_id: Optional[str] = None,
                    project: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProductSetResult:
    """
    Gets information associated with a ProductSet. Possible errors: * Returns NOT_FOUND if the ProductSet does not exist.
    """
    __args__ = dict()
    __args__['location'] = location
    __args__['productSetId'] = product_set_id
    __args__['project'] = project
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('google-native:vision/v1:getProductSet', __args__, opts=opts, typ=GetProductSetResult).value

    return AwaitableGetProductSetResult(
        display_name=__ret__.display_name,
        index_error=__ret__.index_error,
        index_time=__ret__.index_time,
        name=__ret__.name)


@_utilities.lift_output_func(get_product_set)
def get_product_set_output(location: Optional[pulumi.Input[str]] = None,
                           product_set_id: Optional[pulumi.Input[str]] = None,
                           project: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProductSetResult]:
    """
    Gets information associated with a ProductSet. Possible errors: * Returns NOT_FOUND if the ProductSet does not exist.
    """
    ...

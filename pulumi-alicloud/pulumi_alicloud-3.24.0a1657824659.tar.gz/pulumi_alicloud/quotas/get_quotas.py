# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

__all__ = [
    'GetQuotasResult',
    'AwaitableGetQuotasResult',
    'get_quotas',
    'get_quotas_output',
]

@pulumi.output_type
class GetQuotasResult:
    """
    A collection of values returned by getQuotas.
    """
    def __init__(__self__, dimensions=None, group_code=None, id=None, ids=None, key_word=None, name_regex=None, names=None, output_file=None, product_code=None, quota_action_code=None, quota_category=None, quotas=None, sort_field=None, sort_order=None):
        if dimensions and not isinstance(dimensions, list):
            raise TypeError("Expected argument 'dimensions' to be a list")
        pulumi.set(__self__, "dimensions", dimensions)
        if group_code and not isinstance(group_code, str):
            raise TypeError("Expected argument 'group_code' to be a str")
        pulumi.set(__self__, "group_code", group_code)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if key_word and not isinstance(key_word, str):
            raise TypeError("Expected argument 'key_word' to be a str")
        pulumi.set(__self__, "key_word", key_word)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)
        if product_code and not isinstance(product_code, str):
            raise TypeError("Expected argument 'product_code' to be a str")
        pulumi.set(__self__, "product_code", product_code)
        if quota_action_code and not isinstance(quota_action_code, str):
            raise TypeError("Expected argument 'quota_action_code' to be a str")
        pulumi.set(__self__, "quota_action_code", quota_action_code)
        if quota_category and not isinstance(quota_category, str):
            raise TypeError("Expected argument 'quota_category' to be a str")
        pulumi.set(__self__, "quota_category", quota_category)
        if quotas and not isinstance(quotas, list):
            raise TypeError("Expected argument 'quotas' to be a list")
        pulumi.set(__self__, "quotas", quotas)
        if sort_field and not isinstance(sort_field, str):
            raise TypeError("Expected argument 'sort_field' to be a str")
        pulumi.set(__self__, "sort_field", sort_field)
        if sort_order and not isinstance(sort_order, str):
            raise TypeError("Expected argument 'sort_order' to be a str")
        pulumi.set(__self__, "sort_order", sort_order)

    @property
    @pulumi.getter
    def dimensions(self) -> Optional[Sequence['outputs.GetQuotasDimensionResult']]:
        return pulumi.get(self, "dimensions")

    @property
    @pulumi.getter(name="groupCode")
    def group_code(self) -> Optional[str]:
        return pulumi.get(self, "group_code")

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
    @pulumi.getter(name="keyWord")
    def key_word(self) -> Optional[str]:
        return pulumi.get(self, "key_word")

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
    @pulumi.getter(name="productCode")
    def product_code(self) -> str:
        return pulumi.get(self, "product_code")

    @property
    @pulumi.getter(name="quotaActionCode")
    def quota_action_code(self) -> Optional[str]:
        return pulumi.get(self, "quota_action_code")

    @property
    @pulumi.getter(name="quotaCategory")
    def quota_category(self) -> Optional[str]:
        return pulumi.get(self, "quota_category")

    @property
    @pulumi.getter
    def quotas(self) -> Sequence['outputs.GetQuotasQuotaResult']:
        return pulumi.get(self, "quotas")

    @property
    @pulumi.getter(name="sortField")
    def sort_field(self) -> Optional[str]:
        return pulumi.get(self, "sort_field")

    @property
    @pulumi.getter(name="sortOrder")
    def sort_order(self) -> Optional[str]:
        return pulumi.get(self, "sort_order")


class AwaitableGetQuotasResult(GetQuotasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetQuotasResult(
            dimensions=self.dimensions,
            group_code=self.group_code,
            id=self.id,
            ids=self.ids,
            key_word=self.key_word,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file,
            product_code=self.product_code,
            quota_action_code=self.quota_action_code,
            quota_category=self.quota_category,
            quotas=self.quotas,
            sort_field=self.sort_field,
            sort_order=self.sort_order)


def get_quotas(dimensions: Optional[Sequence[pulumi.InputType['GetQuotasDimensionArgs']]] = None,
               group_code: Optional[str] = None,
               key_word: Optional[str] = None,
               name_regex: Optional[str] = None,
               output_file: Optional[str] = None,
               product_code: Optional[str] = None,
               quota_action_code: Optional[str] = None,
               quota_category: Optional[str] = None,
               sort_field: Optional[str] = None,
               sort_order: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetQuotasResult:
    """
    This data source provides the Quotas Quotas of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.115.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.quotas.get_quotas(product_code="ecs",
        name_regex="专有宿主机总数量上限")
    pulumi.export("firstQuotasQuotaId", example.quotas[0].id)
    ```


    :param Sequence[pulumi.InputType['GetQuotasDimensionArgs']] dimensions: The dimensions.
    :param str group_code: The group code.
    :param str key_word: The key word.
    :param str name_regex: A regex string to filter results by Quota name.
    :param str product_code: The product code.
    :param str quota_action_code: The quota action code.
    :param str quota_category: The category of quota. Valid Values: `FlowControl` and `CommonQuota`.
    :param str sort_field: Cloud service ECS specification quota supports setting sorting fields. Valid Values: `TIME`, `TOTAL` and `RESERVED`.
    :param str sort_order: Ranking of cloud service ECS specification quota support. Valid Values: `Ascending` and `Descending`.
    """
    __args__ = dict()
    __args__['dimensions'] = dimensions
    __args__['groupCode'] = group_code
    __args__['keyWord'] = key_word
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    __args__['productCode'] = product_code
    __args__['quotaActionCode'] = quota_action_code
    __args__['quotaCategory'] = quota_category
    __args__['sortField'] = sort_field
    __args__['sortOrder'] = sort_order
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:quotas/getQuotas:getQuotas', __args__, opts=opts, typ=GetQuotasResult).value

    return AwaitableGetQuotasResult(
        dimensions=__ret__.dimensions,
        group_code=__ret__.group_code,
        id=__ret__.id,
        ids=__ret__.ids,
        key_word=__ret__.key_word,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file,
        product_code=__ret__.product_code,
        quota_action_code=__ret__.quota_action_code,
        quota_category=__ret__.quota_category,
        quotas=__ret__.quotas,
        sort_field=__ret__.sort_field,
        sort_order=__ret__.sort_order)


@_utilities.lift_output_func(get_quotas)
def get_quotas_output(dimensions: Optional[pulumi.Input[Optional[Sequence[pulumi.InputType['GetQuotasDimensionArgs']]]]] = None,
                      group_code: Optional[pulumi.Input[Optional[str]]] = None,
                      key_word: Optional[pulumi.Input[Optional[str]]] = None,
                      name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                      output_file: Optional[pulumi.Input[Optional[str]]] = None,
                      product_code: Optional[pulumi.Input[str]] = None,
                      quota_action_code: Optional[pulumi.Input[Optional[str]]] = None,
                      quota_category: Optional[pulumi.Input[Optional[str]]] = None,
                      sort_field: Optional[pulumi.Input[Optional[str]]] = None,
                      sort_order: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetQuotasResult]:
    """
    This data source provides the Quotas Quotas of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.115.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    example = alicloud.quotas.get_quotas(product_code="ecs",
        name_regex="专有宿主机总数量上限")
    pulumi.export("firstQuotasQuotaId", example.quotas[0].id)
    ```


    :param Sequence[pulumi.InputType['GetQuotasDimensionArgs']] dimensions: The dimensions.
    :param str group_code: The group code.
    :param str key_word: The key word.
    :param str name_regex: A regex string to filter results by Quota name.
    :param str product_code: The product code.
    :param str quota_action_code: The quota action code.
    :param str quota_category: The category of quota. Valid Values: `FlowControl` and `CommonQuota`.
    :param str sort_field: Cloud service ECS specification quota supports setting sorting fields. Valid Values: `TIME`, `TOTAL` and `RESERVED`.
    :param str sort_order: Ranking of cloud service ECS specification quota support. Valid Values: `Ascending` and `Descending`.
    """
    ...

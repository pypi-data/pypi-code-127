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
    'GetCertificatesResult',
    'AwaitableGetCertificatesResult',
    'get_certificates',
    'get_certificates_output',
]

@pulumi.output_type
class GetCertificatesResult:
    """
    A collection of values returned by getCertificates.
    """
    def __init__(__self__, certificates=None, domain=None, id=None, ids=None, instance_id=None, name_regex=None, names=None, output_file=None):
        if certificates and not isinstance(certificates, list):
            raise TypeError("Expected argument 'certificates' to be a list")
        pulumi.set(__self__, "certificates", certificates)
        if domain and not isinstance(domain, str):
            raise TypeError("Expected argument 'domain' to be a str")
        pulumi.set(__self__, "domain", domain)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ids and not isinstance(ids, list):
            raise TypeError("Expected argument 'ids' to be a list")
        pulumi.set(__self__, "ids", ids)
        if instance_id and not isinstance(instance_id, str):
            raise TypeError("Expected argument 'instance_id' to be a str")
        pulumi.set(__self__, "instance_id", instance_id)
        if name_regex and not isinstance(name_regex, str):
            raise TypeError("Expected argument 'name_regex' to be a str")
        pulumi.set(__self__, "name_regex", name_regex)
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        pulumi.set(__self__, "names", names)
        if output_file and not isinstance(output_file, str):
            raise TypeError("Expected argument 'output_file' to be a str")
        pulumi.set(__self__, "output_file", output_file)

    @property
    @pulumi.getter
    def certificates(self) -> Sequence['outputs.GetCertificatesCertificateResult']:
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter
    def domain(self) -> Optional[str]:
        return pulumi.get(self, "domain")

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
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

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


class AwaitableGetCertificatesResult(GetCertificatesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificatesResult(
            certificates=self.certificates,
            domain=self.domain,
            id=self.id,
            ids=self.ids,
            instance_id=self.instance_id,
            name_regex=self.name_regex,
            names=self.names,
            output_file=self.output_file)


def get_certificates(domain: Optional[str] = None,
                     ids: Optional[Sequence[str]] = None,
                     instance_id: Optional[str] = None,
                     name_regex: Optional[str] = None,
                     output_file: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificatesResult:
    """
    This data source provides the Waf Certificates of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.135.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.waf.get_certificates(ids=["your_certificate_id"],
        instance_id="your_instance_id",
        domain="your_domain_name")
    pulumi.export("wafCertificate", default.certificates[0])
    ```


    :param str domain: The domain that you want to add to WAF.
    :param Sequence[str] ids: A list of Certificate IDs.
    :param str instance_id: WAF instance ID.
    :param str name_regex: A regex string to filter results by Certificate name.
    """
    __args__ = dict()
    __args__['domain'] = domain
    __args__['ids'] = ids
    __args__['instanceId'] = instance_id
    __args__['nameRegex'] = name_regex
    __args__['outputFile'] = output_file
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('alicloud:waf/getCertificates:getCertificates', __args__, opts=opts, typ=GetCertificatesResult).value

    return AwaitableGetCertificatesResult(
        certificates=__ret__.certificates,
        domain=__ret__.domain,
        id=__ret__.id,
        ids=__ret__.ids,
        instance_id=__ret__.instance_id,
        name_regex=__ret__.name_regex,
        names=__ret__.names,
        output_file=__ret__.output_file)


@_utilities.lift_output_func(get_certificates)
def get_certificates_output(domain: Optional[pulumi.Input[Optional[str]]] = None,
                            ids: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                            instance_id: Optional[pulumi.Input[str]] = None,
                            name_regex: Optional[pulumi.Input[Optional[str]]] = None,
                            output_file: Optional[pulumi.Input[Optional[str]]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCertificatesResult]:
    """
    This data source provides the Waf Certificates of the current Alibaba Cloud user.

    > **NOTE:** Available in v1.135.0+.

    ## Example Usage

    Basic Usage

    ```python
    import pulumi
    import pulumi_alicloud as alicloud

    default = alicloud.waf.get_certificates(ids=["your_certificate_id"],
        instance_id="your_instance_id",
        domain="your_domain_name")
    pulumi.export("wafCertificate", default.certificates[0])
    ```


    :param str domain: The domain that you want to add to WAF.
    :param Sequence[str] ids: A list of Certificate IDs.
    :param str instance_id: WAF instance ID.
    :param str name_regex: A regex string to filter results by Certificate name.
    """
    ...

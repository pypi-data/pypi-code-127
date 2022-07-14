# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'DomainAuthConfigArgs',
    'DomainCacheConfigArgs',
    'DomainCertificateConfigArgs',
    'DomainConfigFunctionArgArgs',
    'DomainHttpHeaderConfigArgs',
    'DomainNewCertificateConfigArgs',
    'DomainNewSourceArgs',
    'DomainPage404ConfigArgs',
    'DomainParameterFilterConfigArgs',
    'DomainReferConfigArgs',
]

@pulumi.input_type
class DomainAuthConfigArgs:
    def __init__(__self__, *,
                 auth_type: Optional[pulumi.Input[str]] = None,
                 master_key: Optional[pulumi.Input[str]] = None,
                 slave_key: Optional[pulumi.Input[str]] = None,
                 timeout: Optional[pulumi.Input[int]] = None):
        if auth_type is not None:
            pulumi.set(__self__, "auth_type", auth_type)
        if master_key is not None:
            pulumi.set(__self__, "master_key", master_key)
        if slave_key is not None:
            pulumi.set(__self__, "slave_key", slave_key)
        if timeout is not None:
            pulumi.set(__self__, "timeout", timeout)

    @property
    @pulumi.getter(name="authType")
    def auth_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "auth_type")

    @auth_type.setter
    def auth_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_type", value)

    @property
    @pulumi.getter(name="masterKey")
    def master_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "master_key")

    @master_key.setter
    def master_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "master_key", value)

    @property
    @pulumi.getter(name="slaveKey")
    def slave_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "slave_key")

    @slave_key.setter
    def slave_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "slave_key", value)

    @property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "timeout")

    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "timeout", value)


@pulumi.input_type
class DomainCacheConfigArgs:
    def __init__(__self__, *,
                 cache_content: pulumi.Input[str],
                 cache_type: pulumi.Input[str],
                 ttl: pulumi.Input[int],
                 cache_id: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "cache_content", cache_content)
        pulumi.set(__self__, "cache_type", cache_type)
        pulumi.set(__self__, "ttl", ttl)
        if cache_id is not None:
            pulumi.set(__self__, "cache_id", cache_id)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="cacheContent")
    def cache_content(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cache_content")

    @cache_content.setter
    def cache_content(self, value: pulumi.Input[str]):
        pulumi.set(self, "cache_content", value)

    @property
    @pulumi.getter(name="cacheType")
    def cache_type(self) -> pulumi.Input[str]:
        return pulumi.get(self, "cache_type")

    @cache_type.setter
    def cache_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "cache_type", value)

    @property
    @pulumi.getter
    def ttl(self) -> pulumi.Input[int]:
        return pulumi.get(self, "ttl")

    @ttl.setter
    def ttl(self, value: pulumi.Input[int]):
        pulumi.set(self, "ttl", value)

    @property
    @pulumi.getter(name="cacheId")
    def cache_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "cache_id")

    @cache_id.setter
    def cache_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cache_id", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class DomainCertificateConfigArgs:
    def __init__(__self__, *,
                 private_key: Optional[pulumi.Input[str]] = None,
                 server_certificate: Optional[pulumi.Input[str]] = None,
                 server_certificate_status: Optional[pulumi.Input[str]] = None):
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if server_certificate is not None:
            pulumi.set(__self__, "server_certificate", server_certificate)
        if server_certificate_status is not None:
            pulumi.set(__self__, "server_certificate_status", server_certificate_status)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="serverCertificate")
    def server_certificate(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server_certificate")

    @server_certificate.setter
    def server_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_certificate", value)

    @property
    @pulumi.getter(name="serverCertificateStatus")
    def server_certificate_status(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "server_certificate_status")

    @server_certificate_status.setter
    def server_certificate_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_certificate_status", value)


@pulumi.input_type
class DomainConfigFunctionArgArgs:
    def __init__(__self__, *,
                 arg_name: pulumi.Input[str],
                 arg_value: pulumi.Input[str]):
        """
        :param pulumi.Input[str] arg_name: The name of arg.
        :param pulumi.Input[str] arg_value: The value of arg.
        """
        pulumi.set(__self__, "arg_name", arg_name)
        pulumi.set(__self__, "arg_value", arg_value)

    @property
    @pulumi.getter(name="argName")
    def arg_name(self) -> pulumi.Input[str]:
        """
        The name of arg.
        """
        return pulumi.get(self, "arg_name")

    @arg_name.setter
    def arg_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "arg_name", value)

    @property
    @pulumi.getter(name="argValue")
    def arg_value(self) -> pulumi.Input[str]:
        """
        The value of arg.
        """
        return pulumi.get(self, "arg_value")

    @arg_value.setter
    def arg_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "arg_value", value)


@pulumi.input_type
class DomainHttpHeaderConfigArgs:
    def __init__(__self__, *,
                 header_key: pulumi.Input[str],
                 header_value: pulumi.Input[str],
                 header_id: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "header_key", header_key)
        pulumi.set(__self__, "header_value", header_value)
        if header_id is not None:
            pulumi.set(__self__, "header_id", header_id)

    @property
    @pulumi.getter(name="headerKey")
    def header_key(self) -> pulumi.Input[str]:
        return pulumi.get(self, "header_key")

    @header_key.setter
    def header_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "header_key", value)

    @property
    @pulumi.getter(name="headerValue")
    def header_value(self) -> pulumi.Input[str]:
        return pulumi.get(self, "header_value")

    @header_value.setter
    def header_value(self, value: pulumi.Input[str]):
        pulumi.set(self, "header_value", value)

    @property
    @pulumi.getter(name="headerId")
    def header_id(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "header_id")

    @header_id.setter
    def header_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "header_id", value)


@pulumi.input_type
class DomainNewCertificateConfigArgs:
    def __init__(__self__, *,
                 cert_name: Optional[pulumi.Input[str]] = None,
                 cert_type: Optional[pulumi.Input[str]] = None,
                 force_set: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 server_certificate: Optional[pulumi.Input[str]] = None,
                 server_certificate_status: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] cert_name: The SSL certificate name.
        :param pulumi.Input[str] cert_type: The SSL certificate type, can be "upload", "cas" and "free".
        :param pulumi.Input[str] force_set: Set `1` to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set `0` to work the verification.
        :param pulumi.Input[str] private_key: The SSL private key. This is required if `server_certificate_status` is `on`
        :param pulumi.Input[str] server_certificate: The SSL server certificate string. This is required if `server_certificate_status` is `on`
        :param pulumi.Input[str] server_certificate_status: This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
        """
        if cert_name is not None:
            pulumi.set(__self__, "cert_name", cert_name)
        if cert_type is not None:
            pulumi.set(__self__, "cert_type", cert_type)
        if force_set is not None:
            pulumi.set(__self__, "force_set", force_set)
        if private_key is not None:
            pulumi.set(__self__, "private_key", private_key)
        if server_certificate is not None:
            pulumi.set(__self__, "server_certificate", server_certificate)
        if server_certificate_status is not None:
            pulumi.set(__self__, "server_certificate_status", server_certificate_status)

    @property
    @pulumi.getter(name="certName")
    def cert_name(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL certificate name.
        """
        return pulumi.get(self, "cert_name")

    @cert_name.setter
    def cert_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_name", value)

    @property
    @pulumi.getter(name="certType")
    def cert_type(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL certificate type, can be "upload", "cas" and "free".
        """
        return pulumi.get(self, "cert_type")

    @cert_type.setter
    def cert_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_type", value)

    @property
    @pulumi.getter(name="forceSet")
    def force_set(self) -> Optional[pulumi.Input[str]]:
        """
        Set `1` to ignore the repeated verification for certificate name, and cover the information of the origin certificate (with the same name). Set `0` to work the verification.
        """
        return pulumi.get(self, "force_set")

    @force_set.setter
    def force_set(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_set", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL private key. This is required if `server_certificate_status` is `on`
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter(name="serverCertificate")
    def server_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL server certificate string. This is required if `server_certificate_status` is `on`
        """
        return pulumi.get(self, "server_certificate")

    @server_certificate.setter
    def server_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_certificate", value)

    @property
    @pulumi.getter(name="serverCertificateStatus")
    def server_certificate_status(self) -> Optional[pulumi.Input[str]]:
        """
        This parameter indicates whether or not enable https. Valid values are `on` and `off`. Default value is `on`.
        """
        return pulumi.get(self, "server_certificate_status")

    @server_certificate_status.setter
    def server_certificate_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_certificate_status", value)


@pulumi.input_type
class DomainNewSourceArgs:
    def __init__(__self__, *,
                 content: pulumi.Input[str],
                 type: pulumi.Input[str],
                 port: Optional[pulumi.Input[int]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        :param pulumi.Input[str] content: The address of source. Valid values can be ip or doaminName. Each item's `content` can not be repeated.
        :param pulumi.Input[str] type: The type of the source. Valid values are `ipaddr`, `domain` and `oss`.
        :param pulumi.Input[int] port: The port of source. Valid values are `443` and `80`. Default value is `80`.
        :param pulumi.Input[int] priority: Priority of the source. Valid values are `0` and `100`. Default value is `20`.
        :param pulumi.Input[int] weight: Weight of the source. Valid values are from `0` to `100`. Default value is `10`, but if type is `ipaddr`, the value can only be `10`.
        """
        pulumi.set(__self__, "content", content)
        pulumi.set(__self__, "type", type)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter
    def content(self) -> pulumi.Input[str]:
        """
        The address of source. Valid values can be ip or doaminName. Each item's `content` can not be repeated.
        """
        return pulumi.get(self, "content")

    @content.setter
    def content(self, value: pulumi.Input[str]):
        pulumi.set(self, "content", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        The type of the source. Valid values are `ipaddr`, `domain` and `oss`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port of source. Valid values are `443` and `80`. Default value is `80`.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of the source. Valid values are `0` and `100`. Default value is `20`.
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Weight of the source. Valid values are from `0` to `100`. Default value is `10`, but if type is `ipaddr`, the value can only be `10`.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


@pulumi.input_type
class DomainPage404ConfigArgs:
    def __init__(__self__, *,
                 custom_page_url: Optional[pulumi.Input[str]] = None,
                 error_code: Optional[pulumi.Input[str]] = None,
                 page_type: Optional[pulumi.Input[str]] = None):
        if custom_page_url is not None:
            pulumi.set(__self__, "custom_page_url", custom_page_url)
        if error_code is not None:
            pulumi.set(__self__, "error_code", error_code)
        if page_type is not None:
            pulumi.set(__self__, "page_type", page_type)

    @property
    @pulumi.getter(name="customPageUrl")
    def custom_page_url(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "custom_page_url")

    @custom_page_url.setter
    def custom_page_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_page_url", value)

    @property
    @pulumi.getter(name="errorCode")
    def error_code(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "error_code")

    @error_code.setter
    def error_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "error_code", value)

    @property
    @pulumi.getter(name="pageType")
    def page_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "page_type")

    @page_type.setter
    def page_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "page_type", value)


@pulumi.input_type
class DomainParameterFilterConfigArgs:
    def __init__(__self__, *,
                 enable: Optional[pulumi.Input[str]] = None,
                 hash_key_args: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        if enable is not None:
            pulumi.set(__self__, "enable", enable)
        if hash_key_args is not None:
            pulumi.set(__self__, "hash_key_args", hash_key_args)

    @property
    @pulumi.getter
    def enable(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "enable")

    @enable.setter
    def enable(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "enable", value)

    @property
    @pulumi.getter(name="hashKeyArgs")
    def hash_key_args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "hash_key_args")

    @hash_key_args.setter
    def hash_key_args(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "hash_key_args", value)


@pulumi.input_type
class DomainReferConfigArgs:
    def __init__(__self__, *,
                 refer_lists: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allow_empty: Optional[pulumi.Input[str]] = None,
                 refer_type: Optional[pulumi.Input[str]] = None):
        pulumi.set(__self__, "refer_lists", refer_lists)
        if allow_empty is not None:
            pulumi.set(__self__, "allow_empty", allow_empty)
        if refer_type is not None:
            pulumi.set(__self__, "refer_type", refer_type)

    @property
    @pulumi.getter(name="referLists")
    def refer_lists(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        return pulumi.get(self, "refer_lists")

    @refer_lists.setter
    def refer_lists(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "refer_lists", value)

    @property
    @pulumi.getter(name="allowEmpty")
    def allow_empty(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "allow_empty")

    @allow_empty.setter
    def allow_empty(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "allow_empty", value)

    @property
    @pulumi.getter(name="referType")
    def refer_type(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "refer_type")

    @refer_type.setter
    def refer_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "refer_type", value)



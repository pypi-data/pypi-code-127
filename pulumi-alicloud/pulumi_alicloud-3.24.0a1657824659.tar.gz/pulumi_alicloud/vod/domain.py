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

__all__ = ['DomainArgs', 'Domain']

@pulumi.input_type
class DomainArgs:
    def __init__(__self__, *,
                 domain_name: pulumi.Input[str],
                 sources: pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]],
                 check_url: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Domain resource.
        :param pulumi.Input[str] domain_name: The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        :param pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]] sources: The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        :param pulumi.Input[str] check_url: The URL that is used for health checks.
        :param pulumi.Input[str] scope: This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               * `Key`: It can be up to 64 characters in length. It cannot be a null string.
               * `Value`: It can be up to 128 characters in length. It can be a null string.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        """
        pulumi.set(__self__, "domain_name", domain_name)
        pulumi.set(__self__, "sources", sources)
        if check_url is not None:
            pulumi.set(__self__, "check_url", check_url)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if top_level_domain is not None:
            pulumi.set(__self__, "top_level_domain", top_level_domain)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Input[str]:
        """
        The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]:
        """
        The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter(name="checkUrl")
    def check_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL that is used for health checks.
        """
        return pulumi.get(self, "check_url")

    @check_url.setter
    def check_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "check_url", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        * `Key`: It can be up to 64 characters in length. It cannot be a null string.
        * `Value`: It can be up to 128 characters in length. It can be a null string.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="topLevelDomain")
    def top_level_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The top-level domain name.
        """
        return pulumi.get(self, "top_level_domain")

    @top_level_domain.setter
    def top_level_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "top_level_domain", value)


@pulumi.input_type
class _DomainState:
    def __init__(__self__, *,
                 cert_name: Optional[pulumi.Input[str]] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 gmt_created: Optional[pulumi.Input[str]] = None,
                 gmt_modified: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]] = None,
                 ssl_protocol: Optional[pulumi.Input[str]] = None,
                 ssl_pub: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None,
                 weight: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Domain resources.
        :param pulumi.Input[str] cert_name: The name of the certificate. The value of this parameter is returned if HTTPS is enabled.
        :param pulumi.Input[str] check_url: The URL that is used for health checks.
        :param pulumi.Input[str] cname: The CNAME that is assigned to the domain name for CDN. You must add a CNAME record in the system of your Domain Name System (DNS) service provider to map the domain name for CDN to the CNAME.
        :param pulumi.Input[str] description: The description of the domain name for CDN.
        :param pulumi.Input[str] domain_name: The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        :param pulumi.Input[str] gmt_created: The time when the domain name for CDN was added. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        :param pulumi.Input[str] gmt_modified: The last time when the domain name for CDN was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        :param pulumi.Input[str] scope: This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        :param pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]] sources: The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        :param pulumi.Input[str] ssl_protocol: Indicates whether the Secure Sockets Layer (SSL) certificate is enabled. Valid values: `on`,`off`.
        :param pulumi.Input[str] ssl_pub: The public key of the certificate. The value of this parameter is returned if HTTPS is enabled.
        :param pulumi.Input[str] status: The status of the domain name for CDN. Value values:
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               * `Key`: It can be up to 64 characters in length. It cannot be a null string.
               * `Value`: It can be up to 128 characters in length. It can be a null string.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        :param pulumi.Input[str] weight: The weight of the origin server.
        """
        if cert_name is not None:
            pulumi.set(__self__, "cert_name", cert_name)
        if check_url is not None:
            pulumi.set(__self__, "check_url", check_url)
        if cname is not None:
            pulumi.set(__self__, "cname", cname)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if domain_name is not None:
            pulumi.set(__self__, "domain_name", domain_name)
        if gmt_created is not None:
            pulumi.set(__self__, "gmt_created", gmt_created)
        if gmt_modified is not None:
            pulumi.set(__self__, "gmt_modified", gmt_modified)
        if scope is not None:
            pulumi.set(__self__, "scope", scope)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if ssl_protocol is not None:
            pulumi.set(__self__, "ssl_protocol", ssl_protocol)
        if ssl_pub is not None:
            pulumi.set(__self__, "ssl_pub", ssl_pub)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if top_level_domain is not None:
            pulumi.set(__self__, "top_level_domain", top_level_domain)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="certName")
    def cert_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the certificate. The value of this parameter is returned if HTTPS is enabled.
        """
        return pulumi.get(self, "cert_name")

    @cert_name.setter
    def cert_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert_name", value)

    @property
    @pulumi.getter(name="checkUrl")
    def check_url(self) -> Optional[pulumi.Input[str]]:
        """
        The URL that is used for health checks.
        """
        return pulumi.get(self, "check_url")

    @check_url.setter
    def check_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "check_url", value)

    @property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[str]]:
        """
        The CNAME that is assigned to the domain name for CDN. You must add a CNAME record in the system of your Domain Name System (DNS) service provider to map the domain name for CDN to the CNAME.
        """
        return pulumi.get(self, "cname")

    @cname.setter
    def cname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the domain name for CDN.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> Optional[pulumi.Input[str]]:
        """
        The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        """
        return pulumi.get(self, "domain_name")

    @domain_name.setter
    def domain_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "domain_name", value)

    @property
    @pulumi.getter(name="gmtCreated")
    def gmt_created(self) -> Optional[pulumi.Input[str]]:
        """
        The time when the domain name for CDN was added. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        return pulumi.get(self, "gmt_created")

    @gmt_created.setter
    def gmt_created(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gmt_created", value)

    @property
    @pulumi.getter(name="gmtModified")
    def gmt_modified(self) -> Optional[pulumi.Input[str]]:
        """
        The last time when the domain name for CDN was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        return pulumi.get(self, "gmt_modified")

    @gmt_modified.setter
    def gmt_modified(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gmt_modified", value)

    @property
    @pulumi.getter
    def scope(self) -> Optional[pulumi.Input[str]]:
        """
        This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]]:
        """
        The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['DomainSourceArgs']]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter(name="sslProtocol")
    def ssl_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        Indicates whether the Secure Sockets Layer (SSL) certificate is enabled. Valid values: `on`,`off`.
        """
        return pulumi.get(self, "ssl_protocol")

    @ssl_protocol.setter
    def ssl_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_protocol", value)

    @property
    @pulumi.getter(name="sslPub")
    def ssl_pub(self) -> Optional[pulumi.Input[str]]:
        """
        The public key of the certificate. The value of this parameter is returned if HTTPS is enabled.
        """
        return pulumi.get(self, "ssl_pub")

    @ssl_pub.setter
    def ssl_pub(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ssl_pub", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        The status of the domain name for CDN. Value values:
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        * `Key`: It can be up to 64 characters in length. It cannot be a null string.
        * `Value`: It can be up to 128 characters in length. It can be a null string.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="topLevelDomain")
    def top_level_domain(self) -> Optional[pulumi.Input[str]]:
        """
        The top-level domain name.
        """
        return pulumi.get(self, "top_level_domain")

    @top_level_domain.setter
    def top_level_domain(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "top_level_domain", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[str]]:
        """
        The weight of the origin server.
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "weight", value)


class Domain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a VOD Domain resource.

        For information about VOD Domain and how to use it, see [What is Domain](https://www.alibabacloud.com/help/product/29932.html).

        > **NOTE:** Available in v1.136.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.vod.Domain("default",
            domain_name="your_domain_name",
            scope="domestic",
            sources=[alicloud.vod.DomainSourceArgs(
                source_content="your_source_content",
                source_port="80",
                source_type="domain",
            )],
            tags={
                "key1": "value1",
                "key2": "value2",
            })
        ```

        ## Import

        VOD Domain can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vod/domain:Domain example <domain_name>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] check_url: The URL that is used for health checks.
        :param pulumi.Input[str] domain_name: The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        :param pulumi.Input[str] scope: This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]] sources: The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               * `Key`: It can be up to 64 characters in length. It cannot be a null string.
               * `Value`: It can be up to 128 characters in length. It can be a null string.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DomainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a VOD Domain resource.

        For information about VOD Domain and how to use it, see [What is Domain](https://www.alibabacloud.com/help/product/29932.html).

        > **NOTE:** Available in v1.136.0+.

        ## Example Usage

        Basic Usage

        ```python
        import pulumi
        import pulumi_alicloud as alicloud

        default = alicloud.vod.Domain("default",
            domain_name="your_domain_name",
            scope="domestic",
            sources=[alicloud.vod.DomainSourceArgs(
                source_content="your_source_content",
                source_port="80",
                source_type="domain",
            )],
            tags={
                "key1": "value1",
                "key2": "value2",
            })
        ```

        ## Import

        VOD Domain can be imported using the id, e.g.

        ```sh
         $ pulumi import alicloud:vod/domain:Domain example <domain_name>
        ```

        :param str resource_name: The name of the resource.
        :param DomainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DomainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 check_url: Optional[pulumi.Input[str]] = None,
                 domain_name: Optional[pulumi.Input[str]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 top_level_domain: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DomainArgs.__new__(DomainArgs)

            __props__.__dict__["check_url"] = check_url
            if domain_name is None and not opts.urn:
                raise TypeError("Missing required property 'domain_name'")
            __props__.__dict__["domain_name"] = domain_name
            __props__.__dict__["scope"] = scope
            if sources is None and not opts.urn:
                raise TypeError("Missing required property 'sources'")
            __props__.__dict__["sources"] = sources
            __props__.__dict__["tags"] = tags
            __props__.__dict__["top_level_domain"] = top_level_domain
            __props__.__dict__["cert_name"] = None
            __props__.__dict__["cname"] = None
            __props__.__dict__["description"] = None
            __props__.__dict__["gmt_created"] = None
            __props__.__dict__["gmt_modified"] = None
            __props__.__dict__["ssl_protocol"] = None
            __props__.__dict__["ssl_pub"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["weight"] = None
        super(Domain, __self__).__init__(
            'alicloud:vod/domain:Domain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cert_name: Optional[pulumi.Input[str]] = None,
            check_url: Optional[pulumi.Input[str]] = None,
            cname: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain_name: Optional[pulumi.Input[str]] = None,
            gmt_created: Optional[pulumi.Input[str]] = None,
            gmt_modified: Optional[pulumi.Input[str]] = None,
            scope: Optional[pulumi.Input[str]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]]] = None,
            ssl_protocol: Optional[pulumi.Input[str]] = None,
            ssl_pub: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            top_level_domain: Optional[pulumi.Input[str]] = None,
            weight: Optional[pulumi.Input[str]] = None) -> 'Domain':
        """
        Get an existing Domain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cert_name: The name of the certificate. The value of this parameter is returned if HTTPS is enabled.
        :param pulumi.Input[str] check_url: The URL that is used for health checks.
        :param pulumi.Input[str] cname: The CNAME that is assigned to the domain name for CDN. You must add a CNAME record in the system of your Domain Name System (DNS) service provider to map the domain name for CDN to the CNAME.
        :param pulumi.Input[str] description: The description of the domain name for CDN.
        :param pulumi.Input[str] domain_name: The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        :param pulumi.Input[str] gmt_created: The time when the domain name for CDN was added. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        :param pulumi.Input[str] gmt_modified: The last time when the domain name for CDN was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        :param pulumi.Input[str] scope: This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['DomainSourceArgs']]]] sources: The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        :param pulumi.Input[str] ssl_protocol: Indicates whether the Secure Sockets Layer (SSL) certificate is enabled. Valid values: `on`,`off`.
        :param pulumi.Input[str] ssl_pub: The public key of the certificate. The value of this parameter is returned if HTTPS is enabled.
        :param pulumi.Input[str] status: The status of the domain name for CDN. Value values:
        :param pulumi.Input[Mapping[str, Any]] tags: A mapping of tags to assign to the resource.
               * `Key`: It can be up to 64 characters in length. It cannot be a null string.
               * `Value`: It can be up to 128 characters in length. It can be a null string.
        :param pulumi.Input[str] top_level_domain: The top-level domain name.
        :param pulumi.Input[str] weight: The weight of the origin server.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _DomainState.__new__(_DomainState)

        __props__.__dict__["cert_name"] = cert_name
        __props__.__dict__["check_url"] = check_url
        __props__.__dict__["cname"] = cname
        __props__.__dict__["description"] = description
        __props__.__dict__["domain_name"] = domain_name
        __props__.__dict__["gmt_created"] = gmt_created
        __props__.__dict__["gmt_modified"] = gmt_modified
        __props__.__dict__["scope"] = scope
        __props__.__dict__["sources"] = sources
        __props__.__dict__["ssl_protocol"] = ssl_protocol
        __props__.__dict__["ssl_pub"] = ssl_pub
        __props__.__dict__["status"] = status
        __props__.__dict__["tags"] = tags
        __props__.__dict__["top_level_domain"] = top_level_domain
        __props__.__dict__["weight"] = weight
        return Domain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="certName")
    def cert_name(self) -> pulumi.Output[str]:
        """
        The name of the certificate. The value of this parameter is returned if HTTPS is enabled.
        """
        return pulumi.get(self, "cert_name")

    @property
    @pulumi.getter(name="checkUrl")
    def check_url(self) -> pulumi.Output[Optional[str]]:
        """
        The URL that is used for health checks.
        """
        return pulumi.get(self, "check_url")

    @property
    @pulumi.getter
    def cname(self) -> pulumi.Output[str]:
        """
        The CNAME that is assigned to the domain name for CDN. You must add a CNAME record in the system of your Domain Name System (DNS) service provider to map the domain name for CDN to the CNAME.
        """
        return pulumi.get(self, "cname")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        The description of the domain name for CDN.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainName")
    def domain_name(self) -> pulumi.Output[str]:
        """
        The domain name for CDN that you want to add to ApsaraVideo VOD. Wildcard domain names are supported. Start the domain name with a period (.). Example: `.example.com.`.
        """
        return pulumi.get(self, "domain_name")

    @property
    @pulumi.getter(name="gmtCreated")
    def gmt_created(self) -> pulumi.Output[str]:
        """
        The time when the domain name for CDN was added. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        return pulumi.get(self, "gmt_created")

    @property
    @pulumi.getter(name="gmtModified")
    def gmt_modified(self) -> pulumi.Output[str]:
        """
        The last time when the domain name for CDN was modified. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        """
        return pulumi.get(self, "gmt_modified")

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Output[Optional[str]]:
        """
        This parameter is applicable to users of level 3 or higher in mainland China and users outside mainland China. Valid values:
        """
        return pulumi.get(self, "scope")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence['outputs.DomainSource']]:
        """
        The information about the address of the origin server. For more information about the Sources parameter, See the following `Block sources`.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="sslProtocol")
    def ssl_protocol(self) -> pulumi.Output[str]:
        """
        Indicates whether the Secure Sockets Layer (SSL) certificate is enabled. Valid values: `on`,`off`.
        """
        return pulumi.get(self, "ssl_protocol")

    @property
    @pulumi.getter(name="sslPub")
    def ssl_pub(self) -> pulumi.Output[str]:
        """
        The public key of the certificate. The value of this parameter is returned if HTTPS is enabled.
        """
        return pulumi.get(self, "ssl_pub")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        The status of the domain name for CDN. Value values:
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        A mapping of tags to assign to the resource.
        * `Key`: It can be up to 64 characters in length. It cannot be a null string.
        * `Value`: It can be up to 128 characters in length. It can be a null string.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="topLevelDomain")
    def top_level_domain(self) -> pulumi.Output[Optional[str]]:
        """
        The top-level domain name.
        """
        return pulumi.get(self, "top_level_domain")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[str]:
        """
        The weight of the origin server.
        """
        return pulumi.get(self, "weight")


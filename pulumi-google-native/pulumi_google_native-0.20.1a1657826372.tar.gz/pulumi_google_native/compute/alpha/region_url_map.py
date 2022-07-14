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
from ._enums import *
from ._inputs import *

__all__ = ['RegionUrlMapArgs', 'RegionUrlMap']

@pulumi.input_type
class RegionUrlMapArgs:
    def __init__(__self__, *,
                 region: pulumi.Input[str],
                 default_route_action: Optional[pulumi.Input['HttpRouteActionArgs']] = None,
                 default_service: Optional[pulumi.Input[str]] = None,
                 default_url_redirect: Optional[pulumi.Input['HttpRedirectActionArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 header_action: Optional[pulumi.Input['HttpHeaderActionArgs']] = None,
                 host_rules: Optional[pulumi.Input[Sequence[pulumi.Input['HostRuleArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input['PathMatcherArgs']]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tests: Optional[pulumi.Input[Sequence[pulumi.Input['UrlMapTestArgs']]]] = None):
        """
        The set of arguments for constructing a RegionUrlMap resource.
        :param pulumi.Input['HttpRouteActionArgs'] default_route_action: defaultRouteAction takes effect when none of the hostRules match. The load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend. If defaultRouteAction specifies any weightedBackendServices, defaultService must not be set. Conversely if defaultService is set, defaultRouteAction cannot contain any weightedBackendServices. Only one of defaultRouteAction or defaultUrlRedirect must be set. UrlMaps for external HTTP(S) load balancers support only the urlRewrite action within defaultRouteAction. defaultRouteAction has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        :param pulumi.Input[str] default_service: The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect , or defaultRouteAction.weightedBackendService must be set. defaultService has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        :param pulumi.Input['HttpRedirectActionArgs'] default_url_redirect: When none of the specified hostRules match, the request is redirected to a URL specified by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or defaultRouteAction must not be set. Not supported when the URL map is bound to a target gRPC proxy.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input['HttpHeaderActionArgs'] header_action: Specifies changes to request and response headers that need to take effect for the selected backendService. The headerAction specified here take effect after headerAction specified under pathMatcher. headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        :param pulumi.Input[Sequence[pulumi.Input['HostRuleArgs']]] host_rules: The list of host rules to use against the URL.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[Sequence[pulumi.Input['PathMatcherArgs']]] path_matchers: The list of named PathMatchers to use against the URL.
        :param pulumi.Input[str] request_id: begin_interface: MixerMutationRequestBuilder Request ID to support idempotency.
        :param pulumi.Input[Sequence[pulumi.Input['UrlMapTestArgs']]] tests: The list of expected URL mapping tests. Request to update the UrlMap succeeds only if all test cases pass. You can specify a maximum of 100 tests per UrlMap. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        """
        pulumi.set(__self__, "region", region)
        if default_route_action is not None:
            pulumi.set(__self__, "default_route_action", default_route_action)
        if default_service is not None:
            pulumi.set(__self__, "default_service", default_service)
        if default_url_redirect is not None:
            pulumi.set(__self__, "default_url_redirect", default_url_redirect)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if header_action is not None:
            pulumi.set(__self__, "header_action", header_action)
        if host_rules is not None:
            pulumi.set(__self__, "host_rules", host_rules)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if path_matchers is not None:
            pulumi.set(__self__, "path_matchers", path_matchers)
        if project is not None:
            pulumi.set(__self__, "project", project)
        if request_id is not None:
            pulumi.set(__self__, "request_id", request_id)
        if tests is not None:
            pulumi.set(__self__, "tests", tests)

    @property
    @pulumi.getter
    def region(self) -> pulumi.Input[str]:
        return pulumi.get(self, "region")

    @region.setter
    def region(self, value: pulumi.Input[str]):
        pulumi.set(self, "region", value)

    @property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> Optional[pulumi.Input['HttpRouteActionArgs']]:
        """
        defaultRouteAction takes effect when none of the hostRules match. The load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend. If defaultRouteAction specifies any weightedBackendServices, defaultService must not be set. Conversely if defaultService is set, defaultRouteAction cannot contain any weightedBackendServices. Only one of defaultRouteAction or defaultUrlRedirect must be set. UrlMaps for external HTTP(S) load balancers support only the urlRewrite action within defaultRouteAction. defaultRouteAction has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        """
        return pulumi.get(self, "default_route_action")

    @default_route_action.setter
    def default_route_action(self, value: Optional[pulumi.Input['HttpRouteActionArgs']]):
        pulumi.set(self, "default_route_action", value)

    @property
    @pulumi.getter(name="defaultService")
    def default_service(self) -> Optional[pulumi.Input[str]]:
        """
        The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect , or defaultRouteAction.weightedBackendService must be set. defaultService has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        """
        return pulumi.get(self, "default_service")

    @default_service.setter
    def default_service(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_service", value)

    @property
    @pulumi.getter(name="defaultUrlRedirect")
    def default_url_redirect(self) -> Optional[pulumi.Input['HttpRedirectActionArgs']]:
        """
        When none of the specified hostRules match, the request is redirected to a URL specified by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or defaultRouteAction must not be set. Not supported when the URL map is bound to a target gRPC proxy.
        """
        return pulumi.get(self, "default_url_redirect")

    @default_url_redirect.setter
    def default_url_redirect(self, value: Optional[pulumi.Input['HttpRedirectActionArgs']]):
        pulumi.set(self, "default_url_redirect", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> Optional[pulumi.Input['HttpHeaderActionArgs']]:
        """
        Specifies changes to request and response headers that need to take effect for the selected backendService. The headerAction specified here take effect after headerAction specified under pathMatcher. headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        """
        return pulumi.get(self, "header_action")

    @header_action.setter
    def header_action(self, value: Optional[pulumi.Input['HttpHeaderActionArgs']]):
        pulumi.set(self, "header_action", value)

    @property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['HostRuleArgs']]]]:
        """
        The list of host rules to use against the URL.
        """
        return pulumi.get(self, "host_rules")

    @host_rules.setter
    def host_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['HostRuleArgs']]]]):
        pulumi.set(self, "host_rules", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PathMatcherArgs']]]]:
        """
        The list of named PathMatchers to use against the URL.
        """
        return pulumi.get(self, "path_matchers")

    @path_matchers.setter
    def path_matchers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PathMatcherArgs']]]]):
        pulumi.set(self, "path_matchers", value)

    @property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "project")

    @project.setter
    def project(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project", value)

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> Optional[pulumi.Input[str]]:
        """
        begin_interface: MixerMutationRequestBuilder Request ID to support idempotency.
        """
        return pulumi.get(self, "request_id")

    @request_id.setter
    def request_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "request_id", value)

    @property
    @pulumi.getter
    def tests(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['UrlMapTestArgs']]]]:
        """
        The list of expected URL mapping tests. Request to update the UrlMap succeeds only if all test cases pass. You can specify a maximum of 100 tests per UrlMap. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        """
        return pulumi.get(self, "tests")

    @tests.setter
    def tests(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['UrlMapTestArgs']]]]):
        pulumi.set(self, "tests", value)


class RegionUrlMap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_route_action: Optional[pulumi.Input[pulumi.InputType['HttpRouteActionArgs']]] = None,
                 default_service: Optional[pulumi.Input[str]] = None,
                 default_url_redirect: Optional[pulumi.Input[pulumi.InputType['HttpRedirectActionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 header_action: Optional[pulumi.Input[pulumi.InputType['HttpHeaderActionArgs']]] = None,
                 host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PathMatcherArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UrlMapTestArgs']]]]] = None,
                 __props__=None):
        """
        Creates a UrlMap resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['HttpRouteActionArgs']] default_route_action: defaultRouteAction takes effect when none of the hostRules match. The load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend. If defaultRouteAction specifies any weightedBackendServices, defaultService must not be set. Conversely if defaultService is set, defaultRouteAction cannot contain any weightedBackendServices. Only one of defaultRouteAction or defaultUrlRedirect must be set. UrlMaps for external HTTP(S) load balancers support only the urlRewrite action within defaultRouteAction. defaultRouteAction has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        :param pulumi.Input[str] default_service: The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect , or defaultRouteAction.weightedBackendService must be set. defaultService has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        :param pulumi.Input[pulumi.InputType['HttpRedirectActionArgs']] default_url_redirect: When none of the specified hostRules match, the request is redirected to a URL specified by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or defaultRouteAction must not be set. Not supported when the URL map is bound to a target gRPC proxy.
        :param pulumi.Input[str] description: An optional description of this resource. Provide this property when you create the resource.
        :param pulumi.Input[pulumi.InputType['HttpHeaderActionArgs']] header_action: Specifies changes to request and response headers that need to take effect for the selected backendService. The headerAction specified here take effect after headerAction specified under pathMatcher. headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostRuleArgs']]]] host_rules: The list of host rules to use against the URL.
        :param pulumi.Input[str] name: Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PathMatcherArgs']]]] path_matchers: The list of named PathMatchers to use against the URL.
        :param pulumi.Input[str] request_id: begin_interface: MixerMutationRequestBuilder Request ID to support idempotency.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UrlMapTestArgs']]]] tests: The list of expected URL mapping tests. Request to update the UrlMap succeeds only if all test cases pass. You can specify a maximum of 100 tests per UrlMap. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RegionUrlMapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Creates a UrlMap resource in the specified project using the data included in the request.

        :param str resource_name: The name of the resource.
        :param RegionUrlMapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RegionUrlMapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_route_action: Optional[pulumi.Input[pulumi.InputType['HttpRouteActionArgs']]] = None,
                 default_service: Optional[pulumi.Input[str]] = None,
                 default_url_redirect: Optional[pulumi.Input[pulumi.InputType['HttpRedirectActionArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 header_action: Optional[pulumi.Input[pulumi.InputType['HttpHeaderActionArgs']]] = None,
                 host_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['HostRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 path_matchers: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PathMatcherArgs']]]]] = None,
                 project: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 request_id: Optional[pulumi.Input[str]] = None,
                 tests: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['UrlMapTestArgs']]]]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        else:
            opts = copy.copy(opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RegionUrlMapArgs.__new__(RegionUrlMapArgs)

            __props__.__dict__["default_route_action"] = default_route_action
            __props__.__dict__["default_service"] = default_service
            __props__.__dict__["default_url_redirect"] = default_url_redirect
            __props__.__dict__["description"] = description
            __props__.__dict__["header_action"] = header_action
            __props__.__dict__["host_rules"] = host_rules
            __props__.__dict__["name"] = name
            __props__.__dict__["path_matchers"] = path_matchers
            __props__.__dict__["project"] = project
            if region is None and not opts.urn:
                raise TypeError("Missing required property 'region'")
            __props__.__dict__["region"] = region
            __props__.__dict__["request_id"] = request_id
            __props__.__dict__["tests"] = tests
            __props__.__dict__["creation_timestamp"] = None
            __props__.__dict__["fingerprint"] = None
            __props__.__dict__["kind"] = None
            __props__.__dict__["self_link"] = None
        replace_on_changes = pulumi.ResourceOptions(replace_on_changes=["project", "region"])
        opts = pulumi.ResourceOptions.merge(opts, replace_on_changes)
        super(RegionUrlMap, __self__).__init__(
            'google-native:compute/alpha:RegionUrlMap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RegionUrlMap':
        """
        Get an existing RegionUrlMap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RegionUrlMapArgs.__new__(RegionUrlMapArgs)

        __props__.__dict__["creation_timestamp"] = None
        __props__.__dict__["default_route_action"] = None
        __props__.__dict__["default_service"] = None
        __props__.__dict__["default_url_redirect"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["fingerprint"] = None
        __props__.__dict__["header_action"] = None
        __props__.__dict__["host_rules"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["path_matchers"] = None
        __props__.__dict__["project"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["request_id"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["tests"] = None
        return RegionUrlMap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTimestamp")
    def creation_timestamp(self) -> pulumi.Output[str]:
        """
        Creation timestamp in RFC3339 text format.
        """
        return pulumi.get(self, "creation_timestamp")

    @property
    @pulumi.getter(name="defaultRouteAction")
    def default_route_action(self) -> pulumi.Output['outputs.HttpRouteActionResponse']:
        """
        defaultRouteAction takes effect when none of the hostRules match. The load balancer performs advanced routing actions, such as URL rewrites and header transformations, before forwarding the request to the selected backend. If defaultRouteAction specifies any weightedBackendServices, defaultService must not be set. Conversely if defaultService is set, defaultRouteAction cannot contain any weightedBackendServices. Only one of defaultRouteAction or defaultUrlRedirect must be set. UrlMaps for external HTTP(S) load balancers support only the urlRewrite action within defaultRouteAction. defaultRouteAction has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        """
        return pulumi.get(self, "default_route_action")

    @property
    @pulumi.getter(name="defaultService")
    def default_service(self) -> pulumi.Output[str]:
        """
        The full or partial URL of the defaultService resource to which traffic is directed if none of the hostRules match. If defaultRouteAction is also specified, advanced routing actions, such as URL rewrites, take effect before sending the request to the backend. However, if defaultService is specified, defaultRouteAction cannot contain any weightedBackendServices. Conversely, if routeAction specifies any weightedBackendServices, service must not be specified. Only one of defaultService, defaultUrlRedirect , or defaultRouteAction.weightedBackendService must be set. defaultService has no effect when the URL map is bound to a target gRPC proxy that has the validateForProxyless field set to true.
        """
        return pulumi.get(self, "default_service")

    @property
    @pulumi.getter(name="defaultUrlRedirect")
    def default_url_redirect(self) -> pulumi.Output['outputs.HttpRedirectActionResponse']:
        """
        When none of the specified hostRules match, the request is redirected to a URL specified by defaultUrlRedirect. If defaultUrlRedirect is specified, defaultService or defaultRouteAction must not be set. Not supported when the URL map is bound to a target gRPC proxy.
        """
        return pulumi.get(self, "default_url_redirect")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        An optional description of this resource. Provide this property when you create the resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field is ignored when inserting a UrlMap. An up-to-date fingerprint must be provided in order to update the UrlMap, otherwise the request will fail with error 412 conditionNotMet. To see the latest fingerprint, make a get() request to retrieve a UrlMap.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter(name="headerAction")
    def header_action(self) -> pulumi.Output['outputs.HttpHeaderActionResponse']:
        """
        Specifies changes to request and response headers that need to take effect for the selected backendService. The headerAction specified here take effect after headerAction specified under pathMatcher. headerAction is not supported for load balancers that have their loadBalancingScheme set to EXTERNAL. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        """
        return pulumi.get(self, "header_action")

    @property
    @pulumi.getter(name="hostRules")
    def host_rules(self) -> pulumi.Output[Sequence['outputs.HostRuleResponse']]:
        """
        The list of host rules to use against the URL.
        """
        return pulumi.get(self, "host_rules")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Type of the resource. Always compute#urlMaps for url maps.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pathMatchers")
    def path_matchers(self) -> pulumi.Output[Sequence['outputs.PathMatcherResponse']]:
        """
        The list of named PathMatchers to use against the URL.
        """
        return pulumi.get(self, "path_matchers")

    @property
    @pulumi.getter
    def project(self) -> pulumi.Output[str]:
        return pulumi.get(self, "project")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="requestId")
    def request_id(self) -> pulumi.Output[Optional[str]]:
        """
        begin_interface: MixerMutationRequestBuilder Request ID to support idempotency.
        """
        return pulumi.get(self, "request_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        Server-defined URL for the resource.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def tests(self) -> pulumi.Output[Sequence['outputs.UrlMapTestResponse']]:
        """
        The list of expected URL mapping tests. Request to update the UrlMap succeeds only if all test cases pass. You can specify a maximum of 100 tests per UrlMap. Not supported when the URL map is bound to a target gRPC proxy that has validateForProxyless field set to true.
        """
        return pulumi.get(self, "tests")


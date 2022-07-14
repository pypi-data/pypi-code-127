# coding: utf-8

"""
    Signadot API

    API for Signadot Sandboxes  # noqa: E501

    OpenAPI spec version: 2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from signadot_sdk_snapshot.api_client import ApiClient


class SandboxesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_sandbox(self, org_name, sandbox_name, **kwargs):  # noqa: E501
        """Delete a Sandbox  # noqa: E501

        Delete a given sandbox  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sandbox(org_name, sandbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :param str sandbox_name: Sandbox Name (required)
        :param bool force: force
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_sandbox_with_http_info(org_name, sandbox_name, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_sandbox_with_http_info(org_name, sandbox_name, **kwargs)  # noqa: E501
            return data

    def delete_sandbox_with_http_info(self, org_name, sandbox_name, **kwargs):  # noqa: E501
        """Delete a Sandbox  # noqa: E501

        Delete a given sandbox  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_sandbox_with_http_info(org_name, sandbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :param str sandbox_name: Sandbox Name (required)
        :param bool force: force
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name', 'sandbox_name', 'force']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_sandbox" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if self.api_client.client_side_validation and ('org_name' not in params or
                                                       params['org_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `org_name` when calling `delete_sandbox`")  # noqa: E501
        # verify the required parameter 'sandbox_name' is set
        if self.api_client.client_side_validation and ('sandbox_name' not in params or
                                                       params['sandbox_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sandbox_name` when calling `delete_sandbox`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']  # noqa: E501
        if 'sandbox_name' in params:
            path_params['sandboxName'] = params['sandbox_name']  # noqa: E501

        query_params = []
        if 'force' in params:
            query_params.append(('force', params['force']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgName}/sandboxes/{sandboxName}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EmptyResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_sandbox(self, org_name, sandbox_name, **kwargs):  # noqa: E501
        """Get a Sandbox  # noqa: E501

        Fetch the details about a given sandbox  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sandbox(org_name, sandbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :param str sandbox_name: Sandbox Name (required)
        :return: Sandbox
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_sandbox_with_http_info(org_name, sandbox_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_sandbox_with_http_info(org_name, sandbox_name, **kwargs)  # noqa: E501
            return data

    def get_sandbox_with_http_info(self, org_name, sandbox_name, **kwargs):  # noqa: E501
        """Get a Sandbox  # noqa: E501

        Fetch the details about a given sandbox  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_sandbox_with_http_info(org_name, sandbox_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :param str sandbox_name: Sandbox Name (required)
        :return: Sandbox
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name', 'sandbox_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_sandbox" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if self.api_client.client_side_validation and ('org_name' not in params or
                                                       params['org_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `org_name` when calling `get_sandbox`")  # noqa: E501
        # verify the required parameter 'sandbox_name' is set
        if self.api_client.client_side_validation and ('sandbox_name' not in params or
                                                       params['sandbox_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sandbox_name` when calling `get_sandbox`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']  # noqa: E501
        if 'sandbox_name' in params:
            path_params['sandboxName'] = params['sandbox_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgName}/sandboxes/{sandboxName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sandbox',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_sandboxes(self, org_name, **kwargs):  # noqa: E501
        """List Sandboxes  # noqa: E501

        List all sandboxes under the specified Signadot org.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_sandboxes(org_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :return: list[Sandbox]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_sandboxes_with_http_info(org_name, **kwargs)  # noqa: E501
        else:
            (data) = self.list_sandboxes_with_http_info(org_name, **kwargs)  # noqa: E501
            return data

    def list_sandboxes_with_http_info(self, org_name, **kwargs):  # noqa: E501
        """List Sandboxes  # noqa: E501

        List all sandboxes under the specified Signadot org.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_sandboxes_with_http_info(org_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :return: list[Sandbox]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_sandboxes" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if self.api_client.client_side_validation and ('org_name' not in params or
                                                       params['org_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `org_name` when calling `list_sandboxes`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgName}/sandboxes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Sandbox]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def upsert_sandbox(self, org_name, sandbox_name, data, **kwargs):  # noqa: E501
        """Create a new sandbox  # noqa: E501

        Creates a new sandbox with the provided parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_sandbox(org_name, sandbox_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :param str sandbox_name: Sandbox Name (required)
        :param Sandbox data: Request to create sandbox (required)
        :return: Sandbox
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.upsert_sandbox_with_http_info(org_name, sandbox_name, data, **kwargs)  # noqa: E501
        else:
            (data) = self.upsert_sandbox_with_http_info(org_name, sandbox_name, data, **kwargs)  # noqa: E501
            return data

    def upsert_sandbox_with_http_info(self, org_name, sandbox_name, data, **kwargs):  # noqa: E501
        """Create a new sandbox  # noqa: E501

        Creates a new sandbox with the provided parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_sandbox_with_http_info(org_name, sandbox_name, data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str org_name: Signadot Org Name (required)
        :param str sandbox_name: Sandbox Name (required)
        :param Sandbox data: Request to create sandbox (required)
        :return: Sandbox
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_name', 'sandbox_name', 'data']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_sandbox" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'org_name' is set
        if self.api_client.client_side_validation and ('org_name' not in params or
                                                       params['org_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `org_name` when calling `upsert_sandbox`")  # noqa: E501
        # verify the required parameter 'sandbox_name' is set
        if self.api_client.client_side_validation and ('sandbox_name' not in params or
                                                       params['sandbox_name'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `sandbox_name` when calling `upsert_sandbox`")  # noqa: E501
        # verify the required parameter 'data' is set
        if self.api_client.client_side_validation and ('data' not in params or
                                                       params['data'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `data` when calling `upsert_sandbox`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'org_name' in params:
            path_params['orgName'] = params['org_name']  # noqa: E501
        if 'sandbox_name' in params:
            path_params['sandboxName'] = params['sandbox_name']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'data' in params:
            body_params = params['data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/orgs/{orgName}/sandboxes/{sandboxName}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Sandbox',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

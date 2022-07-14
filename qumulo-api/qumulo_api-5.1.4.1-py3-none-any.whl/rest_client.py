# Copyright (c) 2014 Qumulo, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

# qumulo_python_versions = { 3.6, latest }

"""
rest_client provides exactly one public type called RestClient, which wraps all
REST requests in qumulo.rest.*

For each function qumulo.rest.xxx.yyy(conninfo, credentials, a, b, c),
there will be a method RestClient.xxx.yyy(a, b, c). The conninfo and
credentials parameters are set up in the RestClient constructor, should they be
provided.

Moreover, the return type from these requests is not a (dict, etag) tuple,
but a python object with the fields set to the key, value items from the dict,
along with an etag field. (Nobody is returning an etag field.)
"""

import functools
import types

from typing import (
    Any,
    AnyStr,
    Callable,
    FrozenSet,
    IO,
    Iterator,
    Mapping,
    Optional,
    Sequence,
    Type,
    Union,
)

import qumulo.lib.request as request
import qumulo.rest  # Pull in all the REST client modules and methods

from qumulo.lib.auth import Credentials
from qumulo.rest import dns, web_ui


class ETagStripperIterator:
    def __init__(
        self, iterator: Iterator[object], etag_strip_function: Callable[[object], object]
    ) -> None:
        self.iterator = iterator
        self.etag_strip_function = etag_strip_function

    def __iter__(self) -> Iterator[object]:
        return self

    def __next__(self) -> object:
        return self.etag_strip_function(next(self.iterator))


# XXX patrick: Fix the return type
def _wrap_rest_request(request_method: Callable[..., request.RestResponse]) -> Callable[..., Any]:
    """
    Wrap a function that begins with the two parameters conninfo and credentials
    returning a function suitable for use as a method on a rest module class.
    """

    @functools.wraps(request_method)
    def wrapper(self: Any, *args: object, **kwargs: object) -> Any:
        with_etag = kwargs.pop('with_etag', False)

        # If the user asked for us to include the etag, they will get it;
        # otherwise, it's more useful to just return the decoded JSON response.
        def etag_stripper(response: Any) -> Any:
            if not (hasattr(response, 'data') and hasattr(response, 'etag')):
                return ETagStripperIterator(response, etag_stripper)

            if with_etag:
                return response
            else:
                return response.data

        try:
            response = request_method(self.client.conninfo, None, *args, **kwargs)
        except request.RequestError as e:
            self.client.handle_request_error(e)
            response = request_method(self.client.conninfo, None, *args, **kwargs)

        return etag_stripper(response)

    return wrapper


class RestClient:
    """
    Provide access to the entire Qumulo Core REST API surface.

    N.B. The class is partially defined here, then filled out with reflection
         over the qumulo.rest namespace to add properties for each module.
    """

    Error = request.RequestError

    # rest module attributes
    ad: Any
    analytics: Any
    audit: Any
    auth: Any
    checksumming: Any
    cluster: Any
    dns: dns.Dns
    encryption: Any
    fs: Any
    ftp: Any
    groups: Any
    kerberos: Any
    ldap: Any
    network: Any
    nfs: Any
    node_state: Any
    object_replication: Any
    quota: Any
    replication: Any
    roles: Any
    shutdown: Any
    smb: Any
    snapshot: Any
    support: Any
    time_config: Any
    tree_delete: Any
    unconfigured_node_operations: Any
    upgrade: Any
    upgrade_v2: Any
    users: Any
    version: Any
    web_ui: web_ui.WebUi

    def __init__(
        self,
        address: str,
        port: int,
        credentials: Optional[Credentials] = None,
        timeout: Optional[int] = None,
        user_agent: Optional[str] = None,
    ) -> None:
        """
        :param address: The IP address or hostname of a Qumulo Core file system.
        :param port: Port on which the Qumulo Core REST API server is listening (typically 8000).
        :param credentials: An instance of Credentials. If None, login() must be called before
            using any REST API endpoints that require authentication.
        :param timeout: Connection timeout duration in seconds. See
            https://docs.python.org/3/library/socket.html#socket.socket.settimeout for more
            information about Python socket timeouts.
        :param user_agent: The value to use in the User-Agent header for this client. If None, no
            User-Agent header will be included.
        """
        self.conninfo = request.Connection(
            address, port, credentials, timeout=timeout, user_agent=user_agent
        )

        self.web_ui = web_ui.WebUi(self.conninfo)

    def clone(self) -> 'RestClient':
        return RestClient(
            self.conninfo.host,
            self.conninfo.port,
            self.conninfo.credentials,
            self.conninfo.timeout,
            self.conninfo.user_agent,
        )

    @property
    def port(self) -> int:
        return self.conninfo.port

    @property
    def chunked(self) -> bool:
        return self.conninfo.chunked

    @chunked.setter
    def chunked(self, new_value: bool) -> None:
        self.conninfo.chunked = new_value

    @property
    def chunk_size(self) -> int:
        return self.conninfo.chunk_size

    @chunk_size.setter
    def chunk_size(self, new_value: int) -> None:
        self.conninfo.chunk_size = new_value

    @property
    def credentials(self) -> Optional[Credentials]:
        return self.conninfo.credentials

    @credentials.setter
    def credentials(self, credentials: Credentials) -> None:
        self.conninfo.credentials = credentials

    def handle_request_error(self, _request_error: request.RequestError) -> None:
        # pylint: disable=misplaced-bare-raise
        raise

    def login(self, username: str, password: str) -> Credentials:
        response_data = self.auth.login(username, password)
        self.conninfo.credentials = Credentials.from_login_response(response_data)
        return self.conninfo.credentials

    # A lot of HTTPExceptions cause the connection to always fail after receiving the error over it.
    # Force reconnect on next use. API modules like web_ui have references to connifo, so we need to
    # keep the same instance.
    def refresh_connection(self) -> None:
        self.conninfo.close()

    def close(self) -> None:
        """
        Close the underlying network connection.

        An explicit close() should not strictly be necessary, as refcount GC will also
        ensure the connection gets closed.  This provides a stronger guarantee or
        tighter control if desired (e.g. it might be useful when a long lived instance
        has long idle periods).

        This client may be re-used after being closed (with the effect of implicitly
        re-opening the connection).
        """
        self.conninfo.close()

    def request(
        self,
        method: str,
        uri: str,
        body: Optional[Union[Sequence[object], Mapping[str, object]]] = None,
        body_file: Optional[IO[AnyStr]] = None,
        if_match: Optional[str] = None,
        request_content_type: Optional[str] = None,
        response_file: Optional[IO[bytes]] = None,
        headers: Optional[Mapping[str, str]] = None,
        with_etag: bool = False,
    ) -> Any:
        """
        Make a raw request against the Qumulo REST API, returning a RestResponse with JSON-decoded
        data payload and an optional etag.
        """
        response = self.conninfo.send_request(
            method=method,
            uri=uri,
            body=body,
            body_file=body_file,
            if_match=if_match,
            request_content_type=request_content_type,
            response_file=response_file,
            headers=headers,
        )
        if with_etag:
            return response
        else:
            return response.data


def _wrap_rest_module(module: types.ModuleType, existing_property: Optional[property]) -> property:
    """
    Given a module, return a property that mimics it.

    This is tricky because we want to wrap each function in the module, and bind
    its first two arguments with fields in the RestClient object. However, we
    don't have the RestClient object instantiated at this point. So, what we
    return is the ability to create the mimicking class, instead of the class
    itself.
    """

    class RestModule:
        __doc__ = module.__doc__

        def __init__(self, client: RestClient):
            self.client = client

    if existing_property is None:
        wrapped_class: Callable[..., Any] = RestModule
    else:
        wrapped_class = existing_property.fget  # get the existing class

    for name, method in vars(module).items():
        if callable(method) and getattr(method, 'request', False):
            setattr(wrapped_class, name, _wrap_rest_request(method))

    return property(wrapped_class)


def _wrap_all_rest_modules(
    root: types.ModuleType, cls: Type[RestClient], exclude_modules: FrozenSet[str] = frozenset()
) -> None:
    """
    Wrap all rest modules loaded in the provided root module, adding a property
    to the RestClient type for each. If a property already exists, it will not
    be overwritten.

    This allows the private modules to dominate the public ones.
    """
    for name, module in vars(root).items():
        if name in exclude_modules:
            continue

        if isinstance(module, types.ModuleType):
            existing_property = getattr(cls, name, None)
            setattr(cls, name, _wrap_rest_module(module, existing_property))


# These modules have been moved to the new pattern of directly adding attributes to the RestClient.
DIRECT_MODULES = frozenset(['web_ui'])
_wrap_all_rest_modules(qumulo.rest, RestClient, exclude_modules=DIRECT_MODULES)

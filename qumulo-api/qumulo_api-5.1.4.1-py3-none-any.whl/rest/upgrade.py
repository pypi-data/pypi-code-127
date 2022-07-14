# Copyright (c) 2013 Qumulo, Inc.
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

from typing import Optional

import qumulo.lib.request as request

from qumulo.lib.auth import Credentials
from qumulo.lib.uri import UriBuilder


@request.request
def verify(
    conninfo: request.Connection,
    _credentials: Optional[Credentials],
    image_path: object,
    override_version: Optional[bool] = False,
) -> request.RestResponse:
    """
    Verify that the given image path can be used to upgrade the cluster and
    retrieve details about the upgrade.

    Warning: override_version allows an unsafe upgrade, which can result in
    corruption if used improperly. It should never be used on a production
    system.  It is useful when upgrading from a non-release build.
    """
    req = {'image_path': str(image_path)}
    method = 'POST'
    uri = UriBuilder(path='/v1/upgrade/verify-image')
    if override_version:
        uri.add_query_param('override_compatibility_check', 'true')

    return conninfo.send_request(method, str(uri), body=req)


@request.request
def config_get(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/upgrade/settings'

    return conninfo.send_request(method, uri)


@request.request
def config_put(
    conninfo: request.Connection,
    _credentials: Optional[Credentials],
    install_path: object,
    target: object,
    override_version: Optional[bool] = False,
) -> request.RestResponse:
    """
    Set upgrade config.

    Warning: override_version allows an unsafe upgrade, which can result in
    corruption if used improperly. It should never be used on a production
    system.  It is useful when upgrading from a non-release build.
    """
    req = {'install_path': str(install_path), 'target': str(target)}
    method = 'PUT'
    uri = UriBuilder(path='/v1/upgrade/settings')
    if override_version:
        uri.add_query_param('override_compatibility_check', 'true')

    return conninfo.send_request(method, str(uri), body=req)


@request.request
def status_get(
    conninfo: request.Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/upgrade/status'

    return conninfo.send_request(method, uri)

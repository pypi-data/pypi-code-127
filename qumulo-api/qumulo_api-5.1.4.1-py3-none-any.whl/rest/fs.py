# Copyright (c) 2012 Qumulo, Inc.
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

from typing import Any, cast, Dict, IO, Iterable, Iterator, List, Mapping, Optional, Union

from typing_extensions import Protocol

import qumulo.lib.request as request

from qumulo.lib.auth import Credentials
from qumulo.lib.identity_util import ApiIdentity, Identity
from qumulo.lib.opts import str_decode
from qumulo.lib.request import Connection
from qumulo.lib.uri import UriBuilder


@request.request
def read_fs_stats(
    conninfo: Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    method = 'GET'
    uri = '/v1/file-system'
    return conninfo.send_request(method, str(uri))


def ref(path: Optional[str], id_: Optional[str]) -> str:
    """
    A "ref" is either a path or file ID. Here, given an argument for both,
    where only one is really present, return the ref.
    """
    assert (path is not None) ^ (id_ is not None), 'One of path or id is required'
    if path is not None and not path.startswith('/'):
        raise ValueError('Path must be absolute.')
    return path if path is not None else str(id_)


@request.request
def set_acl(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    control: Optional[Iterable[str]] = None,
    aces: Optional[Iterable[Mapping[str, object]]] = None,
    if_match: Optional[str] = None,
    posix_special_permissions: Optional[Iterable[str]] = None,
) -> request.RestResponse:

    if not control or not aces:
        raise ValueError('Must specify both control flags and ACEs')

    # Don't require POSIX special permissions in the input ACL
    if not posix_special_permissions:
        posix_special_permissions = []

    uri = build_files_uri([ref(path, id_), 'info', 'acl'])

    if_match = None if not if_match else str(if_match)

    config = {
        'aces': list(aces),
        'control': list(control),
        'posix_special_permissions': list(posix_special_permissions),
    }
    method = 'PUT'

    return conninfo.send_request(method, str(uri), body=config, if_match=if_match)


@request.request
def set_acl_v2(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    acl: Mapping[str, object],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    if_match: Optional[str] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(path, id_), 'info', 'acl'], api_version=2)
    if_match = None if not if_match else str(if_match)
    method = 'PUT'
    return conninfo.send_request(method, str(uri), body=acl, if_match=if_match)


@request.request
def get_file_attr(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    id_: Optional[str] = None,
    path: Optional[str] = None,
    snapshot: Optional[int] = None,
    stream_id: Optional[str] = None,
) -> request.RestResponse:
    method = 'GET'

    uri = None
    if stream_id:
        uri = build_files_uri([ref(path, id_), 'streams', stream_id, 'attributes'])
    else:
        uri = build_files_uri([ref(path, id_), 'info', 'attributes'])

    if snapshot:
        uri.add_query_param('snapshot', snapshot)
    return conninfo.send_request(method, str(uri))


class FSIdentity:
    def __init__(self, id_type: str, value: object) -> None:
        self.id_type = id_type
        self.value = value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, FSIdentity):
            return NotImplemented

        return self.id_type == other.id_type and self.value == other.value

    def body(self) -> Dict[str, str]:
        return {'id_type': self.id_type, 'id_value': str(self.value)}


class NFSUID(FSIdentity):
    def __init__(self, uid: object) -> None:
        super().__init__('NFS_UID', uid)


class NFSGID(FSIdentity):
    def __init__(self, gid: object) -> None:
        super().__init__('NFS_GID', gid)


class SMBSID(FSIdentity):
    def __init__(self, sid: object) -> None:
        super().__init__('SMB_SID', sid)


class LocalUser(FSIdentity):
    def __init__(self, name: object) -> None:
        super().__init__('LOCAL_USER', str_decode(name))


class LocalGroup(FSIdentity):
    def __init__(self, name: object) -> None:
        super().__init__('LOCAL_GROUP', str_decode(name))


class InternalIdentity(FSIdentity):
    def __init__(self, name: object) -> None:
        super().__init__('INTERNAL', name)


@request.request
def set_file_attr(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    mode: Optional[str] = None,
    owner: Optional[str] = None,
    group: Optional[str] = None,
    size: Optional[object] = None,
    creation_time: Optional[str] = None,
    access_time: Optional[str] = None,
    modification_time: Optional[str] = None,
    change_time: Optional[str] = None,
    id_: Optional[str] = None,
    extended_attributes: Optional[Mapping[str, bool]] = None,
    if_match: Optional[str] = None,
    path: Optional[str] = None,
    stream_id: Optional[str] = None,
) -> request.RestResponse:
    """
    Updates select file attributes on the specified file system object.
    Attributes that are not to be updated should have None specified as
    their values.
    """
    method = 'PATCH'

    uri = None
    if stream_id:
        uri = build_files_uri([ref(path, id_), 'streams', stream_id, 'attributes'])
    else:
        uri = build_files_uri([ref(path, id_), 'info', 'attributes'])

    if_match = None if not if_match else str(if_match)
    config: Dict[str, object] = {}
    if mode is not None:
        config['mode'] = str(mode)

    if owner is not None:
        if isinstance(owner, FSIdentity):
            config['owner_details'] = owner.body()
        else:
            config['owner'] = str(owner)

    if group is not None:
        if isinstance(group, FSIdentity):
            config['group_details'] = group.body()
        else:
            config['group'] = str(group)

    if size is not None:
        config['size'] = str(size)

    if creation_time is not None:
        config['creation_time'] = str(creation_time)

    if access_time is not None:
        config['access_time'] = str(access_time)

    if modification_time is not None:
        config['modification_time'] = str(modification_time)

    if change_time is not None:
        config['change_time'] = str(change_time)

    if extended_attributes is not None:
        config['extended_attributes'] = extended_attributes

    return conninfo.send_request(method, str(uri), body=config, if_match=if_match)


@request.request
def write_file(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    data_file: IO[str],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    if_match: Optional[str] = None,
    offset: Optional[int] = None,
    stream_id: Optional[str] = None,
) -> request.RestResponse:
    """
    @param data_file The data to be written to the file
    @param path      Path to the file. If None, id must not be None
    @param id        File id of the file. If None, path must not be None
    @param if_match  If not None, it will be the etag to use
    @param offset    The position to write in the file.
                     If None, the contents will be completely replaced
    """
    if stream_id:
        uri = build_files_uri([ref(path, id_), 'streams', stream_id, 'data'])
    else:
        uri = build_files_uri([ref(path, id_), 'data'])

    if_match = None if not if_match else str(if_match)
    if offset is None:
        method = 'PUT'
    else:
        method = 'PATCH'
        uri = uri.add_query_param('offset', offset)

    return conninfo.send_request(
        method,
        str(uri),
        body_file=data_file,
        if_match=if_match,
        request_content_type=request.CONTENT_TYPE_BINARY,
    )


class CopyProgressTracker(Protocol):
    def update_to_completion(self) -> None:
        ...

    def update(self, copied_bytes: int) -> None:
        ...


@request.request
def copy(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    source_path: Optional[str] = None,
    source_id: Optional[str] = None,
    source_snapshot: Optional[int] = None,
    target_path: Optional[str] = None,
    target_id: Optional[str] = None,
    source_stream_id: Optional[str] = None,
    target_stream_id: Optional[str] = None,
    source_etag: Optional[str] = None,
    target_etag: Optional[str] = None,
    progress_tracker: Optional[CopyProgressTracker] = None,
) -> str:
    method = 'POST'

    source_ref = ref(source_path, source_id)
    source_ref_key = 'source_id' if source_id else 'source_path'

    target_ref = ref(target_path, target_id)
    if target_stream_id:
        uri = build_files_uri([target_ref, 'streams', target_stream_id])
    else:
        uri = build_files_uri([target_ref])
    uri.add_path_component('copy-chunk')

    body: Dict[str, object] = {source_ref_key: source_ref}

    if source_stream_id is not None:
        body['source_stream_id'] = source_stream_id

    if source_etag is not None:
        body['source_etag'] = source_etag

    if source_snapshot:
        body.update({'source_snapshot': source_snapshot})

    do_request = lambda body, etag: conninfo.send_request(
        method, str(uri), body=body, if_match=etag
    )

    result = body
    last_copied_offset = 0
    while True:
        result, target_etag = do_request(result, target_etag)
        if not result:
            if progress_tracker is not None:
                progress_tracker.update_to_completion()
            break

        new_offset = int(cast(str, result['target_offset']))
        copied_bytes = new_offset - last_copied_offset
        last_copied_offset = new_offset

        if progress_tracker is not None:
            progress_tracker.update(copied_bytes)

    assert target_etag is not None
    return target_etag


@request.request
def get_acl(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(path, id_), 'info', 'acl'])

    method = 'GET'

    if snapshot:
        uri.add_query_param('snapshot', snapshot)

    return conninfo.send_request(method, str(uri))


@request.request
def get_acl_v2(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(path, id_), 'info', 'acl'], api_version=2)
    if snapshot:
        uri.add_query_param('snapshot', snapshot)
    return conninfo.send_request('GET', str(uri))


@request.request
def read_directory(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    page_size: Optional[int] = None,
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
    smb_pattern: Optional[str] = None,
) -> request.RestResponse:
    """
    @param page_size   How many entries to return
    @param path        Directory to read, by path
    @param id_         Directory to read, by ID
    @param snapshot    Snapshot ID of directory to read
    @param smb_pattern SMB style match pattern.
    """
    uri = build_files_uri([ref(path, id_), 'entries']).append_slash()

    method = 'GET'

    if page_size is not None:
        uri.add_query_param('limit', page_size)

    if snapshot:
        uri.add_query_param('snapshot', snapshot)

    if smb_pattern:
        uri.add_query_param('smb-pattern', smb_pattern)

    return conninfo.send_request(method, str(uri))


@request.request
def read_file(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    file_: IO[bytes],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
    offset: Optional[int] = None,
    length: Optional[int] = None,
    stream_id: Optional[str] = None,
) -> request.RestResponse:
    uri = None
    if stream_id:
        uri = build_files_uri([ref(path, id_), 'streams', stream_id, 'data'])
    else:
        uri = build_files_uri([ref(path, id_), 'data'])

    if snapshot is not None:
        uri.add_query_param('snapshot', snapshot)
    if offset is not None:
        uri.add_query_param('offset', offset)
    if length is not None:
        uri.add_query_param('length', length)

    method = 'GET'
    return conninfo.send_request(method, str(uri), response_file=file_)


@request.request
def create_file(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    name: str,
    dir_path: Optional[str] = None,
    dir_id: Optional[str] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(dir_path, dir_id), 'entries']).append_slash()

    config = {'name': str(name).rstrip('/'), 'action': 'CREATE_FILE'}

    method = 'POST'
    return conninfo.send_request(method, str(uri), body=config)


DEVICE_TYPES = ('FS_FILE_TYPE_UNIX_BLOCK_DEVICE', 'FS_FILE_TYPE_UNIX_CHARACTER_DEVICE')


def validate_major_minor_numbers(file_type: str, major_minor_numbers: Optional[object]) -> None:
    if file_type in DEVICE_TYPES:
        if major_minor_numbers is None:
            raise ValueError('major_minor_numbers required for ' + file_type)
    elif major_minor_numbers is not None:
        raise ValueError('cannot use major_minor_numbers with ' + file_type)


@request.request
def create_unix_file(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    name: str,
    file_type: str,
    major_minor_numbers: Optional[Mapping[str, int]] = None,
    dir_path: Optional[str] = None,
    dir_id: Optional[str] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(dir_path, dir_id), 'entries']).append_slash()

    config: Dict[str, object] = {
        'name': str(name).rstrip('/'),
        'action': 'CREATE_UNIX_FILE',
        'unix_file_type': file_type,
    }

    validate_major_minor_numbers(file_type, major_minor_numbers)

    if major_minor_numbers is not None:
        config['major_minor_numbers'] = major_minor_numbers

    method = 'POST'
    return conninfo.send_request(method, str(uri), body=config)


@request.request
def create_directory(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    name: str,
    dir_path: Optional[str] = None,
    dir_id: Optional[str] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(dir_path, dir_id), 'entries']).append_slash()

    config = {'name': str(name), 'action': 'CREATE_DIRECTORY'}

    method = 'POST'
    return conninfo.send_request(method, str(uri), body=config)


@request.request
def create_symlink(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    name: str,
    target: Union[str, bytes],
    dir_path: Optional[str] = None,
    dir_id: Optional[str] = None,
    target_type: Optional[str] = None,
) -> request.RestResponse:
    # symlink targets are expected to be a utf-8 string in QFSD, so restrict
    # the target parameter to being byte arrays that can be decoded to a utf-8
    # string, or a string. This aligns with the behavior of read_file which
    # returns a utf-8 string as a byte array
    if isinstance(target, bytes):
        target = target.decode('utf-8')
    else:
        assert isinstance(target, str)

    uri = build_files_uri([ref(dir_path, dir_id), 'entries']).append_slash()

    config = {'name': str(name).rstrip('/'), 'old_path': target, 'action': 'CREATE_SYMLINK'}
    if target_type is not None:
        config['symlink_target_type'] = target_type

    method = 'POST'
    return conninfo.send_request(method, str(uri), body=config)


@request.request
def create_link(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    name: str,
    target: Union[str, bytes],
    dir_path: Optional[str] = None,
    dir_id: Optional[str] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(dir_path, dir_id), 'entries']).append_slash()

    config = {'name': str(name).rstrip('/'), 'old_path': str(target), 'action': 'CREATE_LINK'}

    method = 'POST'
    return conninfo.send_request(method, str(uri), body=config)


@request.request
def rename(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    name: str,
    source: str,
    dir_path: Optional[str] = None,
    dir_id: Optional[str] = None,
    clobber: bool = False,
) -> request.RestResponse:
    """
    Rename a file or directory from the full path "source" to the destination
    directory (parent of the new location) specified by either dir_path or
    dir_id and new name "name".
    """
    uri = build_files_uri([ref(dir_path, dir_id), 'entries']).append_slash()

    config = {
        'name': str(name).rstrip('/'),
        'old_path': str(source),
        'action': 'RENAME',
        'clobber': clobber,
    }

    method = 'POST'
    return conninfo.send_request(method, str(uri), body=config)


@request.request
def delete(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
) -> request.RestResponse:
    uri = build_files_uri([ref(path, id_)])
    method = 'DELETE'
    return conninfo.send_request(method, str(uri))


@request.request
def read_dir_aggregates(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    recursive: bool = False,
    max_entries: Optional[int] = None,
    max_depth: Optional[int] = None,
    order_by: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
) -> request.RestResponse:
    method = 'GET'

    aggregate = 'recursive-aggregates' if recursive else 'aggregates'
    uri = build_files_uri([ref(path, id_), aggregate]).append_slash()

    if max_entries is not None:
        uri.add_query_param('max-entries', max_entries)
    if max_depth is not None:
        uri.add_query_param('max-depth', max_depth)
    if order_by is not None:
        uri.add_query_param('order-by', order_by)
    if snapshot is not None:
        uri.add_query_param('snapshot', snapshot)
    return conninfo.send_request(method, str(uri))


@request.request
def get_file_samples(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: str,
    count: int,
    by_value: str,
    id_: Optional[str] = None,
) -> request.RestResponse:
    method = 'GET'

    uri = build_files_uri([ref(path, id_), 'sample']).append_slash()
    uri.add_query_param('by-value', by_value)
    uri.add_query_param('limit', count)

    return conninfo.send_request(method, str(uri))


@request.request
def resolve_paths(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    ids: Dict[str, object],
    snapshot: Optional[int] = None,
) -> request.RestResponse:
    method = 'POST'
    uri = build_files_uri(['resolve'])

    if snapshot:
        uri.add_query_param('snapshot', snapshot)

    return conninfo.send_request(method, str(uri), body=ids)


@request.request
def punch_hole(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    offset: int,
    size: int,
    path: Optional[str] = None,
    id_: Optional[str] = None,
    if_match: Optional[str] = None,
    stream_id: Optional[str] = None,
) -> request.RestResponse:

    if stream_id:
        uri = build_files_uri([ref(path, id_), 'streams', stream_id, 'punch-hole'])
    else:
        uri = build_files_uri([ref(path, id_), 'punch-hole'])

    if_match = None if not if_match else str(if_match)
    body = {'offset': str(offset), 'size': str(size)}
    return conninfo.send_request('POST', str(uri), body=body, if_match=if_match)


# __        __    _ _
# \ \      / /_ _(_) |_ ___ _ __ ___
#  \ \ /\ / / _` | | __/ _ \ '__/ __|
#   \ V  V / (_| | | ||  __/ |  \__ \
#    \_/\_/ \__,_|_|\__\___|_|  |___/
#  FIGLET: Waiters
#
VALID_WAITER_PROTO_TYPE_COMBINATIONS = [('nlm', 'byte-range')]


@request.request
def list_waiters_by_file(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    file_path: Optional[str] = None,
    file_id: Optional[str] = None,
    snapshot_id: Optional[str] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> request.RestResponse:
    assert (protocol, lock_type) in VALID_WAITER_PROTO_TYPE_COMBINATIONS
    uri = build_files_uri(
        [ref(file_path, file_id), 'locks', protocol, lock_type, 'waiters'], append_slash=True
    )
    if limit:
        uri.add_query_param('limit', limit)
    if after:
        uri.add_query_param('after', after)
    if snapshot_id:
        uri.add_query_param('snapshot', snapshot_id)
    return conninfo.send_request('GET', str(uri))


@request.request
def list_waiters_by_client(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    owner_name: Optional[str] = None,
    owner_address: Optional[str] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> request.RestResponse:
    assert (protocol, lock_type) in VALID_WAITER_PROTO_TYPE_COMBINATIONS
    uri = build_files_uri(['locks', protocol, lock_type, 'waiters'], append_slash=True)
    if limit:
        uri.add_query_param('limit', limit)
    if after:
        uri.add_query_param('after', after)
    if owner_name:
        uri.add_query_param('owner_name', owner_name)
    if owner_address:
        uri.add_query_param('owner_address', owner_address)
    return conninfo.send_request('GET', str(uri))


@request.request
def list_all_waiters_by_file(
    conninfo: Connection,
    credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    file_path: Optional[str] = None,
    file_id: Optional[str] = None,
    snapshot_id: Optional[str] = None,
    limit: int = 1000,
) -> List[Dict[str, object]]:
    """
    Re-assembles the paginated list of lock waiters for the given file.
    """
    result = list_waiters_by_file(
        conninfo, credentials, protocol, lock_type, file_path, file_id, snapshot_id, limit
    )
    return _get_remaining_pages_for_list_lock_requests(
        conninfo, credentials, result, limit, req_type='waiters'
    )


@request.request
def list_all_waiters_by_client(
    conninfo: Connection,
    credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    owner_name: Optional[str] = None,
    owner_address: Optional[str] = None,
    limit: int = 1000,
) -> List[Dict[str, object]]:
    """
    Re-assembles the paginated list of lock waiters for the given client.
    """
    result = list_waiters_by_client(
        conninfo, credentials, protocol, lock_type, owner_name, owner_address, limit
    )
    return _get_remaining_pages_for_list_lock_requests(
        conninfo, credentials, result, limit, req_type='waiters'
    )


#  _               _
# | |    ___   ___| | _____
# | |   / _ \ / __| |/ / __|
# | |__| (_) | (__|   <\__ \
# |_____\___/ \___|_|\_\___/
# FIGLET: Locks

VALID_LOCK_PROTO_TYPE_COMBINATIONS = [
    ('smb', 'byte-range'),
    ('smb', 'share-mode'),
    ('nlm', 'byte-range'),
    ('nfs4', 'byte-range'),
]


@request.request
def list_locks_by_file(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    file_path: Optional[str] = None,
    file_id: Optional[str] = None,
    snapshot_id: Optional[str] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> request.RestResponse:
    assert (protocol, lock_type) in VALID_LOCK_PROTO_TYPE_COMBINATIONS
    uri = build_files_uri(
        [ref(file_path, file_id), 'locks', protocol, lock_type], append_slash=True
    )
    if limit:
        uri.add_query_param('limit', limit)
    if after:
        uri.add_query_param('after', after)
    if snapshot_id:
        uri.add_query_param('snapshot', snapshot_id)
    return conninfo.send_request('GET', str(uri))


@request.request
def list_locks_by_client(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    owner_name: Optional[str] = None,
    owner_address: Optional[str] = None,
    limit: Optional[int] = None,
    after: Optional[str] = None,
) -> request.RestResponse:
    assert (protocol, lock_type) in VALID_LOCK_PROTO_TYPE_COMBINATIONS
    uri = build_files_uri(['locks', protocol, lock_type], append_slash=True)
    if limit:
        uri.add_query_param('limit', limit)
    if after:
        uri.add_query_param('after', after)
    if owner_name:
        uri.add_query_param('owner_name', owner_name)
    if owner_address:
        uri.add_query_param('owner_address', owner_address)
    return conninfo.send_request('GET', str(uri))


def _get_remaining_pages_for_list_lock_requests(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    result: request.RestResponse,
    limit: int,
    req_type: str = 'grants',
) -> List[Dict[str, object]]:
    """
    Given the first page of a lock grant listing, retrieves all subsequent
    pages, and returns the complete grant list.
    @p req_type can either be 'grants' or 'waiters'
    """
    full_list = result.data[req_type]
    while len(result.data[req_type]) == limit:
        # If we got a full page, there are probably more pages.  Waiting for
        # an empty page would also be reasonable, but carries the risk of
        # never terminating if clients are frequently taking new locks.
        result = conninfo.send_request('GET', result.data['paging']['next'])
        full_list += result.data[req_type]
    return full_list


@request.request
def list_all_locks_by_file(
    conninfo: Connection,
    credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    file_path: Optional[str] = None,
    file_id: Optional[str] = None,
    snapshot_id: Optional[str] = None,
    limit: int = 1000,
) -> List[Dict[str, object]]:
    """
    Re-assembles the paginated list of lock grants for the given file.
    """
    result = list_locks_by_file(
        conninfo, credentials, protocol, lock_type, file_path, file_id, snapshot_id, limit
    )
    return _get_remaining_pages_for_list_lock_requests(conninfo, credentials, result, limit)


@request.request
def list_all_locks_by_client(
    conninfo: Connection,
    credentials: Optional[Credentials],
    protocol: str,
    lock_type: str,
    owner_name: Optional[str] = None,
    owner_address: Optional[str] = None,
    limit: int = 1000,
) -> List[Dict[str, object]]:
    """
    Re-assembles the paginated list of lock grants for the given client.
    """
    result = list_locks_by_client(
        conninfo, credentials, protocol, lock_type, owner_name, owner_address, limit
    )
    return _get_remaining_pages_for_list_lock_requests(conninfo, credentials, result, limit)


@request.request
def release_nlm_locks_by_client(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    owner_name: Optional[str] = None,
    owner_address: Optional[str] = None,
) -> request.RestResponse:
    assert owner_name or owner_address
    protocol, lock_type = 'nlm', 'byte-range'
    uri = build_files_uri(['locks', protocol, lock_type], append_slash=True)
    if owner_name:
        uri.add_query_param('owner_name', owner_name)
    if owner_address:
        uri.add_query_param('owner_address', owner_address)
    return conninfo.send_request('DELETE', str(uri))


@request.request
def release_nlm_lock(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    offset: int,
    size: int,
    owner_id: str,
    file_path: Optional[str] = None,
    file_id: Optional[str] = None,
    snapshot: Optional[int] = None,
) -> request.RestResponse:
    protocol, lock_type = 'nlm', 'byte-range'
    uri = build_files_uri(
        [ref(file_path, file_id), 'locks', protocol, lock_type], append_slash=True
    )
    uri.add_query_param('offset', offset)
    uri.add_query_param('size', size)
    uri.add_query_param('owner_id', owner_id)
    if snapshot is not None:
        uri.add_query_param('snapshot', snapshot)
    return conninfo.send_request('DELETE', str(uri))


#  _   _      _
# | | | | ___| |_ __   ___ _ __ ___
# | |_| |/ _ \ | '_ \ / _ \ '__/ __|
# |  _  |  __/ | |_) |  __/ |  \__ \
# |_| |_|\___|_| .__/ \___|_|  |___/
#              |_|
#
def build_files_uri(
    components: Iterable[str], append_slash: bool = False, api_version: int = 1
) -> UriBuilder:
    uri = UriBuilder(path=f'/v{api_version}/files')

    if components:
        for component in components:
            uri.add_path_component(component)

    if append_slash:
        uri.append_slash()

    return uri


# Return an iterator that reads an entire directory. Each iteration returns a
# page of files, which will be the specified page size or less.
@request.request
def read_entire_directory(
    conninfo: Connection,
    credentials: Optional[Credentials],
    page_size: Optional[int] = None,
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
    smb_pattern: Optional[str] = None,
) -> Iterator[request.RestResponse]:
    # Perform initial read_directory normally.
    result = read_directory(
        conninfo,
        credentials,
        page_size=page_size,
        path=path,
        id_=id_,
        snapshot=snapshot,
        smb_pattern=smb_pattern,
    )
    next_uri = result.data['paging']['next']
    yield result

    while next_uri != '':
        # Perform raw read_directory with paging URI.
        result = conninfo.send_request('GET', next_uri)
        next_uri = result.data['paging']['next']
        yield result


@request.request
def enumerate_entire_directory(
    conninfo: Connection, credentials: Optional[Credentials], **kwargs: Any
) -> Iterator[request.RestResponse]:
    """
    Same as @ref read_entire_directory but hides the paging mechanism and yields
    individual directory entries.
    """
    for result in read_entire_directory(conninfo, credentials, **kwargs):
        for entry in result.data['files']:
            yield request.RestResponse(entry, result.etag)


# Return an iterator that reads an entire directory. Each iteration returns a
# page of files. Any fs_no_such_entry_error returned is logged and ignored,
# ending the iteration.
def read_entire_directory_and_ignore_not_found(
    conninfo: Connection,
    credentials: Optional[Credentials],
    page_size: Optional[int] = None,
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
) -> Iterator[request.RestResponse]:
    try:
        yield from read_entire_directory(conninfo, credentials, page_size, path, id_, snapshot)
    except request.RequestError as e:
        if e.status_code != 404 or e.error_class != 'fs_no_such_entry_error':
            raise


# Return an iterator that walks a file system tree depth-first and pre-order
@request.request
def tree_walk_preorder(
    conninfo: Connection,
    credentials: Optional[Credentials],
    path: str,
    snapshot: Optional[int] = None,
    max_depth: int = -1,
) -> Iterator[request.RestResponse]:
    def call_read_dir(
        conninfo: Connection, credentials: Optional[Credentials], id_: str, max_depth: int
    ) -> Iterator[request.RestResponse]:
        if max_depth == 0:
            return

        max_depth -= 1

        for result in read_entire_directory_and_ignore_not_found(
            conninfo, credentials, id_=id_, snapshot=snapshot
        ):
            if 'files' in result.data:
                for f in result.data['files']:
                    yield request.RestResponse(f, result.etag)

                    if f['type'] == 'FS_FILE_TYPE_DIRECTORY':
                        yield from call_read_dir(conninfo, credentials, f['id'], max_depth)

    result = get_file_attr(conninfo, credentials, path=path, snapshot=snapshot)
    yield result

    yield from call_read_dir(conninfo, credentials, result.data['id'], max_depth)


# Return an iterator that walks a file system tree depth-first and post-order
@request.request
def tree_walk_postorder(
    conninfo: Connection,
    credentials: Optional[Credentials],
    path: str,
    snapshot: Optional[int] = None,
) -> Iterator[request.RestResponse]:
    def call_read_dir(
        conninfo: Connection, credentials: Optional[Credentials], id_: str
    ) -> Iterator[request.RestResponse]:
        for result in read_entire_directory_and_ignore_not_found(
            conninfo, credentials, id_=id_, snapshot=snapshot
        ):
            if 'files' in result.data:
                for f in result.data['files']:
                    if f['type'] == 'FS_FILE_TYPE_DIRECTORY':
                        yield from call_read_dir(conninfo, credentials, f['id'])
                    yield request.RestResponse(f, result.etag)

    result = get_file_attr(conninfo, credentials, path=path, snapshot=snapshot)

    yield from call_read_dir(conninfo, credentials, result.data['id'])

    yield result


@request.request
def acl_explain_posix_mode(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
) -> request.RestResponse:
    method = 'POST'

    uri = build_files_uri([ref(path, id_), 'info', 'acl', 'explain-posix-mode'])

    return conninfo.send_request(method, str(uri))


@request.request
def acl_explain_chmod(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    mode: Optional[str] = None,
) -> request.RestResponse:
    method = 'POST'

    uri = build_files_uri([ref(path, id_), 'info', 'acl', 'explain-set-mode'])

    return conninfo.send_request(method, str(uri), body={'mode': mode})


IdentityTypes = Union[ApiIdentity, Identity, str]


@request.request
def acl_explain_rights(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    user: IdentityTypes,
    group: IdentityTypes,
    ids: Optional[Iterable[IdentityTypes]] = None,
    path: Optional[str] = None,
    id_: Optional[str] = None,
) -> request.RestResponse:
    method = 'POST'
    """
    @param user      User for whom to explain rights.
    @param path      Path to the file. If None, id must not be None
    @param id        File id of the file. If None, path must not be None
    @param group     User's primary group.
    @param ids       User's additional groups and related identities.
    """

    uri = build_files_uri([ref(path, id_), 'info', 'acl', 'explain-rights'])

    payload = {'user': Identity(user).dictionary()}
    if group:
        payload['primary_group'] = Identity(group).dictionary()
    if ids:
        payload['auxiliary_identities'] = [Identity(i).dictionary() for i in ids]

    return conninfo.send_request(method, str(uri), body=payload)


#     _    ____  ____
#    / \  |  _ \/ ___|
#   / _ \ | | | \___ \
#  / ___ \| |_| |___) |
# /_/   \_\____/|____/
#  FIGLET: ADS
#


@request.request
def list_named_streams(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    path: Optional[str] = None,
    id_: Optional[str] = None,
    snapshot: Optional[int] = None,
) -> request.RestResponse:
    method = 'GET'
    uri = build_files_uri([ref(path, id_), 'streams']).append_slash()

    if snapshot is not None:
        uri.add_query_param('snapshot', snapshot)
    return conninfo.send_request(method, str(uri))


@request.request
def create_stream(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    stream_name: str,
    path: Optional[str] = None,
    id_: Optional[str] = None,
    if_match: Optional[str] = None,
) -> request.RestResponse:
    method = 'POST'
    uri = build_files_uri([ref(path, id_), 'streams']).append_slash()
    if_match = None if not if_match else str(if_match)

    config = {'stream_name': stream_name}
    return conninfo.send_request(method, str(uri), body=config, if_match=if_match)


@request.request
def remove_stream(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    stream_id: str,
    path: Optional[str] = None,
    id_: Optional[str] = None,
) -> request.RestResponse:
    method = 'DELETE'
    uri = build_files_uri([ref(path, id_), 'streams', stream_id])

    return conninfo.send_request(method, str(uri))


@request.request
def rename_stream(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    old_id: str,
    new_name: str,
    path: Optional[str] = None,
    id_: Optional[str] = None,
    if_match: Optional[str] = None,
) -> request.RestResponse:
    method = 'POST'

    uri = build_files_uri([ref(path, id_), 'streams', old_id, 'rename'])
    if_match = None if not if_match else str(if_match)
    config = {'stream_name': new_name}
    return conninfo.send_request(method, str(uri), body=config, if_match=if_match)


#  ____            _                               _     _
# / ___| _   _ ___| |_ ___ _ __ ___      __      _(_) __| | ___
# \___ \| | | / __| __/ _ \ '_ ` _ \ ____\ \ /\ / / |/ _` |/ _ \
#  ___) | |_| \__ \ ||  __/ | | | | |_____\ V  V /| | (_| |  __/
# |____/ \__, |___/\__\___|_| |_| |_|      \_/\_/ |_|\__,_|\___|
#        |___/
#           _   _   _
#  ___  ___| |_| |_(_)_ __   __ _ ___
# / __|/ _ \ __| __| | '_ \ / _` / __|
# \__ \  __/ |_| |_| | | | | (_| \__ \
# |___/\___|\__|\__|_|_| |_|\__, |___/
#                           |___/
#  FIGLET: System-wide settings
#


@request.request
def get_permissions_settings(
    conninfo: Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    return conninfo.send_request('GET', '/v1/file-system/settings/permissions')


@request.request
def set_permissions_settings(
    conninfo: Connection, _credentials: Optional[Credentials], mode: str
) -> request.RestResponse:
    """
    @param mode  NATIVE, _DEPRECATED_MERGED_V1, or CROSS_PROTOCOL
    """
    return conninfo.send_request('PUT', '/v1/file-system/settings/permissions', body={'mode': mode})


@request.request
def get_atime_settings(
    conninfo: Connection, _credentials: Optional[Credentials]
) -> request.RestResponse:
    return conninfo.send_request('GET', '/v1/file-system/settings/atime')


@request.request
def set_atime_settings(
    conninfo: Connection,
    _credentials: Optional[Credentials],
    enabled: Optional[bool] = None,
    granularity: Optional[str] = None,
) -> request.RestResponse:
    payload: Dict[str, Union[bool, str]] = {}
    if enabled is not None:
        payload['enabled'] = enabled
    if granularity is not None:
        payload['granularity'] = granularity

    return conninfo.send_request('PATCH', '/v1/file-system/settings/atime', body=payload)

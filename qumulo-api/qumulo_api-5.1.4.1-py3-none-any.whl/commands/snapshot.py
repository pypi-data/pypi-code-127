# Copyright (c) 2016 Qumulo, Inc.
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

import re

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace, SUPPRESS
from datetime import datetime
from typing import Any, Dict, Mapping, Optional, Sequence, Tuple

import qumulo.lib.opts
import qumulo.lib.request as request
import qumulo.rest.fs as fs
import qumulo.rest.snapshot as snapshot

from qumulo.lib.auth import Credentials
from qumulo.lib.opts import str_decode
from qumulo.rest_client import RestClient

EXPIRATION_HELP_MSG = (
    'Time of snapshot expiration. An empty string indicates that the snapshot never expires. '
    'The time format follows RFC 3339, a normalized subset of ISO 8601.'
)

POLICY_TTL_HELP = (
    'Duration after which to expire snapshots created by this '
    'policy, in format <quantity><units>, where <quantity> is a positive '
    'integer less than 100 and <units> is one of [months, weeks, days, hours, '
    'minutes], For example, 5days or 1hours. Empty string or never indicates snapshots '
    'should never expire.'
)

PERIOD_HELP = (
    'How often to take a snapshot, in the format <quantity><units>, '
    'where <quantity> is a positive integer less than 100 and <units> is one '
    'of [hours, minutes], For example, 5minutes or 6hours.'
)

NAME_TEMPLATE_HELP = (
    'Template for custom naming of policy snapshots. '
    'Available variables: {ID}, {Year}, {Month}, {Day}, {Hour}, {Minute}, {Policy}, {Directory}. '
    'For example, {ID}_snapshot_taken_at_{Hour}_{Minute}.'
    '(default: {ID}_{Policy} for snapshots on root directory. '
    '{ID}_{Policy}_{Directory} for all other directory snapshots.) '
)


class ListAllSnapshotsCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_list_snapshots'

    SYNOPSIS = 'List all snapshots'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument(
            '--exclude-in-delete',
            action='store_const',
            const=snapshot.InDeleteFilter.EXCLUDE_IN_DELETE,
            dest='in_delete_filter',
            help='Exclude all snapshots in process of being deleted.',
        )
        group.add_argument(
            '--only-in-delete',
            action='store_const',
            const=snapshot.InDeleteFilter.ONLY_IN_DELETE,
            dest='in_delete_filter',
            help='Display only snapshots in process of being deleted.',
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        in_delete_filter = (
            args.in_delete_filter if args.in_delete_filter else snapshot.InDeleteFilter.ALL
        )
        print(
            snapshot.list_snapshots(rest_client.conninfo, rest_client.credentials, in_delete_filter)
        )


class GetSnapshotCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_get_snapshot'

    SYNOPSIS = 'Get a single snapshot'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i', '--id', type=int, required=True, help='Identifier of the snapshot to list.'
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        print(snapshot.get_snapshot(rest_client.conninfo, rest_client.credentials, args.id))


class CreateSnapshotCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_create_snapshot'

    SYNOPSIS = 'Create a new snapshot'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument(
            '--source-file-id', type=str_decode, default=None, help='ID of directory to snapshot'
        )
        group.add_argument(
            '--path', type=str_decode, default=None, help='Path of directory to snapshot'
        )

        parser.add_argument(
            '-e', '--expiration', type=str_decode, default=None, help=EXPIRATION_HELP_MSG
        )
        parser.add_argument('-n', '--name', type=str_decode, default=None, help='Snapshot name')

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        print(
            snapshot.create_snapshot(
                rest_client.conninfo,
                rest_client.credentials,
                args.name,
                args.expiration,
                args.source_file_id,
                args.path,
            )
        )


class ModifySnapshotCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_modify_snapshot'

    SYNOPSIS = 'Modify an existing snapshot'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument('-i', '--id', type=int, required=True, help='Snapshot ID')
        parser.add_argument(
            '-e', '--expiration', type=str_decode, default=None, help=EXPIRATION_HELP_MSG
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        print(
            snapshot.modify_snapshot(
                rest_client.conninfo, rest_client.credentials, args.id, args.expiration
            )
        )


class DeleteSnapshotCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_delete_snapshot'

    SYNOPSIS = 'Delete a single snapshot'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument('-i', '--id', type=int, required=True, help='Snapshot ID')

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        snapshot.delete_snapshot(rest_client.conninfo, rest_client.credentials, args.id)


class ListAllSnapshotStatusesCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_list_statuses'

    SYNOPSIS = 'List all snapshot statuses'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        group = parser.add_mutually_exclusive_group(required=False)
        group.add_argument(
            '--exclude-in-delete',
            action='store_const',
            const=snapshot.InDeleteFilter.EXCLUDE_IN_DELETE,
            dest='in_delete_filter',
            help='Exclude all snapshots in process of being deleted.',
        )
        group.add_argument(
            '--only-in-delete',
            action='store_const',
            const=snapshot.InDeleteFilter.ONLY_IN_DELETE,
            dest='in_delete_filter',
            help='Display only snapshots in process of being deleted.',
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        in_delete_filter = (
            args.in_delete_filter if args.in_delete_filter else snapshot.InDeleteFilter.ALL
        )
        print(
            snapshot.list_snapshot_statuses(
                rest_client.conninfo, rest_client.credentials, in_delete_filter
            )
        )


class GetSnapshotStatusCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_get_status'

    SYNOPSIS = 'Get a single snapshot status'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i', '--id', type=int, required=True, help='Identifier of the snapshot.'
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        print(snapshot.get_snapshot_status(rest_client.conninfo, rest_client.credentials, args.id))


ALLOWED_DAYS = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'ALL']


def get_on_days(days_of_week: str) -> Sequence[str]:
    days = [day.strip().upper() for day in days_of_week.split(',')]

    if 'ALL' in days:
        if len(days) > 1:
            raise ValueError('ALL cannot be used in conjunction with other days')

        # API parlance for "ALL"
        return ['EVERY_DAY']

    if not set(days).issubset(set(ALLOWED_DAYS)):
        raise ValueError(f'Invalid days: {days}; allowed days are: {ALLOWED_DAYS}')

    return days


def get_schedule_info(
    creation_schedule: Optional[Mapping[str, object]], time_to_live_str: Optional[str]
) -> Mapping[str, object]:
    schedule: Dict[str, Any] = {}
    if creation_schedule is not None:
        schedule.update({'creation_schedule': creation_schedule})
    if time_to_live_str is not None:
        schedule.update({'expiration_time_to_live': time_to_live_str})
    return schedule


def parse_period(period_str: str) -> Tuple[int, str]:
    m = re.search(r'(\d+)(\w+)', period_str)
    if m is None:
        raise ValueError(PERIOD_HELP)
    value = int(m.group(1))
    units_str = m.group(2).lower()
    if units_str in ('minute', 'minutes'):
        units = 'FIRE_IN_MINUTES'
    elif units_str in ('hour', 'hours'):
        units = 'FIRE_IN_HOURS'
    else:
        raise ValueError(PERIOD_HELP)
    return value, units


def get_schedule_hourly_or_less(args: Namespace) -> Mapping[str, object]:
    try:
        start_time = datetime.strptime(
            args.start_time if args.start_time is not None else '0:0', '%H:%M'
        )
    except ValueError:
        raise ValueError('Bad format for start time')
    try:
        end_time = datetime.strptime(
            args.end_time if args.end_time is not None else '23:59', '%H:%M'
        )
    except ValueError:
        raise ValueError('Bad format for end time')
    if start_time > end_time:
        raise ValueError('Start time must be less than end time')

    interval_value, interval_units = parse_period(args.period if hasattr(args, 'period') else None)

    return {
        'frequency': 'SCHEDULE_HOURLY_OR_LESS',
        'timezone': args.timezone,
        'on_days': get_on_days(args.days_of_week),
        'window_start_hour': start_time.hour,
        'window_start_minute': start_time.minute,
        'window_end_hour': end_time.hour,
        'window_end_minute': end_time.minute,
        'fire_every_interval': interval_units,
        'fire_every': interval_value,
    }


def create_hourly_or_less(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.create_policy(
            conninfo,
            credentials,
            args.name,
            get_schedule_info(
                get_schedule_hourly_or_less(args), args.time_to_live if args.time_to_live else ''
            ),
            args.snapshot_name_template,
            args.file_id,
            args.enabled,
        )
    )


def get_schedule_daily(args: Namespace) -> Mapping[str, object]:
    try:
        at_time_of_day = datetime.strptime(args.at, '%H:%M')
    except ValueError:
        raise ValueError('Bad format for time of day')

    return {
        'frequency': 'SCHEDULE_DAILY_OR_WEEKLY',
        'timezone': args.timezone,
        'on_days': get_on_days(args.days_of_week),
        'hour': at_time_of_day.hour,
        'minute': at_time_of_day.minute,
    }


def create_daily(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.create_policy(
            conninfo,
            credentials,
            args.name,
            get_schedule_info(
                get_schedule_daily(args), args.time_to_live if args.time_to_live else ''
            ),
            args.snapshot_name_template,
            args.file_id,
            args.enabled,
        )
    )


def get_schedule_monthly(args: Namespace) -> Mapping[str, object]:
    try:
        at_time_of_day = datetime.strptime(args.at, '%H:%M')
    except ValueError:
        raise ValueError('Bad format for time of day')

    return {
        'frequency': 'SCHEDULE_MONTHLY',
        'timezone': args.timezone,
        'day_of_month': 128 if hasattr(args, 'last_day_of_month') else args.day_of_month,
        'hour': at_time_of_day.hour,
        'minute': at_time_of_day.minute,
    }


def create_monthly(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.create_policy(
            conninfo,
            credentials,
            args.name,
            get_schedule_info(
                get_schedule_monthly(args), args.time_to_live if args.time_to_live else ''
            ),
            args.snapshot_name_template,
            args.file_id,
            args.enabled,
        )
    )


def add_hourly_specific_args(hourly_parser: ArgumentParser) -> None:
    hourly_parser.add_argument(
        '-s',
        '--start-time',
        type=str_decode,
        default='0:00',
        help='Do not take snapshots before this 24 hour time of day.',
    )
    hourly_parser.add_argument(
        '-e',
        '--end-time',
        type=str_decode,
        default='23:59',
        help='Do not take snapshots after this 24 hour time of day.',
    )
    hourly_parser.add_argument(
        '-p', '--period', type=str_decode, required=True, default=SUPPRESS, help=PERIOD_HELP
    )


def add_monthly_specific_args(monthly_parser: ArgumentParser) -> None:
    day_group = monthly_parser.add_mutually_exclusive_group(required=True)
    day_group.add_argument(
        '-d',
        '--day-of-month',
        type=int,
        default=SUPPRESS,
        help='The day of the month on which to take a snapshot.',
    )
    day_group.add_argument(
        '-l',
        '--last-day-of-month',
        action='store_true',
        default=SUPPRESS,
        help='Take a snapshot on the last day of the month.',
    )


def add_general_schedule_args(schedule_parser: ArgumentParser) -> None:
    schedule_parser.add_argument(
        '-z',
        '--timezone',
        type=str_decode,
        default='UTC',
        help=(
            'The time zone according to which the schedule is interpreted. '
            '(For example: America/Los_Angeles or UTC). For a complete list of supported time '
            'zones, see the qq time_list_timezones command.'
        ),
    )


# Shared by hourly and daily subcommands
hourly_daily_common_parser = ArgumentParser(add_help=False)
hourly_daily_common_parser.add_argument(
    '-d',
    '--days-of-week',
    type=str_decode,
    default='ALL',
    help=(
        'Days of the week to allow snapshots. Comma separated list '
        '(For example: MON,TUE,WED,THU,FRI,SAT,SUN,ALL).'
    ),
)

# Shared by daily and monthly subcommands
daily_monthly_common_parser = ArgumentParser(add_help=False)
daily_monthly_common_parser.add_argument(
    '-a',
    '--at',
    type=str_decode,
    required=True,
    default=SUPPRESS,
    help='Take a snapshot at this time of day, in 24-hour format. (For example: 20:00)',
)


class CreatePolicyCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_create_policy'

    SYNOPSIS = 'Create a new snapshot scheduling policy.'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        subparsers = parser.add_subparsers(dest='command')
        subparsers.required = True

        # Shared by all subcommands
        common_parser = ArgumentParser(add_help=False)
        common_parser.add_argument(
            '-n',
            '--name',
            type=str_decode,
            required=True,
            default=SUPPRESS,
            help='Name of the policy',
        )
        parser.set_defaults(name=None)
        common_parser.add_argument(
            '--snapshot-name-template', type=str_decode, default=SUPPRESS, help=NAME_TEMPLATE_HELP
        )
        parser.set_defaults(snapshot_name_template=None)

        # Directory
        group = common_parser.add_mutually_exclusive_group(required=False)
        group.add_argument(
            '--path',
            type=str_decode,
            default=SUPPRESS,
            help='Path of directory upon which to take snapshots.',
        )
        parser.set_defaults(path=None)
        group.add_argument(
            '--file-id',
            type=str_decode,
            default=SUPPRESS,
            help=(
                'ID of directory upon which to take snapshots. (Defaults to root directory if no '
                'path and no file id is given.)'
            ),
        )
        parser.set_defaults(file_id=None)
        common_parser.add_argument(
            '-t', '--time-to-live', type=str_decode, default=SUPPRESS, help=POLICY_TTL_HELP
        )
        parser.set_defaults(time_to_live=None)
        add_general_schedule_args(common_parser)

        # Enabled?
        group = common_parser.add_mutually_exclusive_group(required=False)
        group.add_argument(
            '--enabled',
            dest='enabled',
            action='store_true',
            default=SUPPRESS,
            help='Create policy enabled (This is the default).',
        )
        group.add_argument(
            '--disabled',
            dest='enabled',
            action='store_false',
            default=SUPPRESS,
            help='Create policy disabled.',
        )
        parser.set_defaults(enabled=None)

        # Hourly or less subparser
        hourly_parser = subparsers.add_parser(
            'hourly_or_less',
            parents=[common_parser, hourly_daily_common_parser],
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        add_hourly_specific_args(hourly_parser)
        hourly_parser.set_defaults(command=create_hourly_or_less)

        # Daily subparser
        daily_parser = subparsers.add_parser(
            'daily',
            parents=[common_parser, hourly_daily_common_parser, daily_monthly_common_parser],
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        daily_parser.set_defaults(command=create_daily)

        # Monthly subparser
        monthly_parser = subparsers.add_parser(
            'monthly',
            parents=[common_parser, daily_monthly_common_parser],
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        add_monthly_specific_args(monthly_parser)
        monthly_parser.set_defaults(command=create_monthly)

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        if args.path:
            attr = fs.get_file_attr(rest_client.conninfo, rest_client.credentials, path=args.path)
            args.file_id = attr.lookup('file_number')

        args.command(rest_client.conninfo, rest_client.credentials, args)


def modify_non_schedule_fields(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.modify_policy(
            conninfo,
            credentials,
            args.id,
            name=args.name,
            snapshot_name_template=args.snapshot_name_template,
            schedule_info=get_schedule_info(None, args.time_to_live),
            enabled=args.enabled,
        )
    )


def modify_hourly(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.modify_policy(
            conninfo,
            credentials,
            args.id,
            name=args.name,
            snapshot_name_template=args.snapshot_name_template,
            schedule_info=get_schedule_info(get_schedule_hourly_or_less(args), args.time_to_live),
            enabled=args.enabled,
        )
    )


def modify_daily(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.modify_policy(
            conninfo,
            credentials,
            args.id,
            name=args.name,
            snapshot_name_template=args.snapshot_name_template,
            schedule_info=get_schedule_info(get_schedule_daily(args), args.time_to_live),
            enabled=args.enabled,
        )
    )


def modify_monthly(
    conninfo: request.Connection, credentials: Optional[Credentials], args: Namespace
) -> None:
    print(
        snapshot.modify_policy(
            conninfo,
            credentials,
            args.id,
            name=args.name,
            snapshot_name_template=args.snapshot_name_template,
            schedule_info=get_schedule_info(get_schedule_monthly(args), args.time_to_live),
            enabled=args.enabled,
        )
    )


class ModifyPolicyCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_modify_policy'

    SYNOPSIS = 'Modify an existing snapshot scheduling policy.'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        common_parser = ArgumentParser(add_help=False)

        common_parser.add_argument(
            '-i',
            '--id',
            type=int,
            required=True,
            default=SUPPRESS,
            help='Identifier of the snapshot policy to modify.',
        )
        parser.set_defaults(id=None)
        common_parser.add_argument(
            '-n', '--name', type=str_decode, default=SUPPRESS, help='Name of the policy'
        )
        parser.set_defaults(name=None)
        common_parser.add_argument(
            '-t', '--time-to-live', type=str_decode, default=SUPPRESS, help=POLICY_TTL_HELP
        )
        parser.set_defaults(time_to_live=None)
        common_parser.add_argument(
            '--snapshot-name-template', type=str_decode, default=SUPPRESS, help=NAME_TEMPLATE_HELP
        )
        parser.set_defaults(snapshot_name_template=None)

        group = common_parser.add_mutually_exclusive_group(required=False)
        group.add_argument(
            '--enabled',
            dest='enabled',
            action='store_true',
            default=SUPPRESS,
            help='Enable the policy.',
        )
        group.add_argument(
            '--disabled',
            dest='enabled',
            action='store_false',
            default=SUPPRESS,
            help='Disable the policy.',
        )
        parser.set_defaults(enabled=None)

        subparsers = parser.add_subparsers(dest='command')
        subparsers.required = True

        # Non schedule fields subparser
        modify_non_schedule_fields_parser = subparsers.add_parser(
            'modify_non_schedule_fields', parents=[common_parser]
        )
        modify_non_schedule_fields_parser.set_defaults(command=modify_non_schedule_fields)

        # Hourly or less subparser
        hourly_parser = subparsers.add_parser(
            'change_to_hourly_or_less',
            parents=[common_parser, hourly_daily_common_parser],
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        add_hourly_specific_args(hourly_parser)
        add_general_schedule_args(hourly_parser)
        hourly_parser.set_defaults(command=modify_hourly)

        # Daily subparser
        daily_parser = subparsers.add_parser(
            'change_to_daily',
            parents=[common_parser, hourly_daily_common_parser, daily_monthly_common_parser],
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        add_general_schedule_args(daily_parser)
        daily_parser.set_defaults(command=modify_daily)

        # Monthly subparser
        monthly_parser = subparsers.add_parser(
            'change_to_monthly',
            parents=[common_parser, daily_monthly_common_parser],
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        add_monthly_specific_args(monthly_parser)
        add_general_schedule_args(monthly_parser)
        monthly_parser.set_defaults(command=modify_monthly)

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        args.command(rest_client.conninfo, rest_client.credentials, args)


class ListAllPoliciesCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_list_policies'

    SYNOPSIS = 'List all policies'

    @staticmethod
    def main(rest_client: RestClient, _args: Namespace) -> None:
        print(snapshot.list_policies(rest_client.conninfo, rest_client.credentials))


class GetPolicyCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_get_policy'

    SYNOPSIS = 'Get a single policy'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i', '--id', type=int, required=True, help='Identifier of the snapshot policy to list.'
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        print(snapshot.get_policy(rest_client.conninfo, rest_client.credentials, args.id))


class DeletePolicyCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_delete_policy'

    SYNOPSIS = 'Delete a single scheduling policy'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i',
            '--id',
            type=int,
            required=True,
            help='Identifier of the snapshot policy to delete.',
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        snapshot.delete_policy(rest_client.conninfo, rest_client.credentials, args.id)


class ListPolicyStatusesCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_list_policy_statuses'

    SYNOPSIS = 'List all snapshot policy statuses'

    @staticmethod
    def main(rest_client: RestClient, _args: Namespace) -> None:
        print(snapshot.list_policy_statuses(rest_client.conninfo, rest_client.credentials))


class GetPolicyStatusCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_get_policy_status'

    SYNOPSIS = 'Get a single snapshot policy status'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i', '--id', type=int, required=True, help='Identifier of the snapshot policy.'
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        print(snapshot.get_policy_status(rest_client.conninfo, rest_client.credentials, args.id))


class GetSnapshotTotalUsedCapacity(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_get_total_used_capacity'

    SYNOPSIS = 'Get the total space consumed by all snapshots.'

    @staticmethod
    def main(rest_client: RestClient, _args: Namespace) -> None:
        print(snapshot.get_total_used_capacity(rest_client.conninfo, rest_client.credentials))


class CalculateUsedCapacity(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_calculate_used_capacity'

    SYNOPSIS = 'Get the space used by the snapshots specified.'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i',
            '--ids',
            type=str_decode,
            help=(
                'Identifiers of the snapshots for which to calculate '
                'capacity usage (as a comma separated list).'
            ),
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        try:
            ids = [int(i) for i in args.ids.split(',')]
        except Exception:
            raise ValueError(
                'Snapshot identifiers must be specified as '
                'a comma separated list of positive integers.'
            )
        print(snapshot.calculate_used_capacity(rest_client.conninfo, rest_client.credentials, ids))


class GetUsedCapacityPerSnapshotCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_get_capacity_used_per_snapshot'

    SYNOPSIS = (
        'Get the approximate amount of space for each snapshot that '
        'would be reclaimed if that snapshot were deleted.'
    )

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '-i',
            '--id',
            type=int,
            required=False,
            help=(
                'If set, will return capacity usage of the snapshot with the '
                'specified id. If omitted, will return capacity usage of all '
                'snapshots.'
            ),
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        if args.id is None:
            print(
                snapshot.capacity_used_per_snapshot(rest_client.conninfo, rest_client.credentials)
            )
        else:
            print(
                snapshot.capacity_used_by_snapshot(
                    rest_client.conninfo, rest_client.credentials, args.id
                )
            )


class SnapshotTreeDiffCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_diff'

    SYNOPSIS = 'List the changed files and directories between two snapshots.'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--newer-snapshot', help='Snapshot ID of the newer snapshot', required=True, type=int
        )
        parser.add_argument(
            '--older-snapshot', help='Snapshot ID of the older snapshot', required=True, type=int
        )
        parser.add_argument(
            '--page-size', help='Max snapshot diff entries to return per request', type=int
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        for res in snapshot.get_all_snapshot_tree_diff(
            rest_client.conninfo,
            rest_client.credentials,
            args.newer_snapshot,
            args.older_snapshot,
            limit=args.page_size,
        ):
            print(res)


class SnapshotFileDiffCommand(qumulo.lib.opts.Subcommand):
    NAME = 'snapshot_file_diff'

    SYNOPSIS = 'List changed byte ranges of a file between two snapshots.'

    @staticmethod
    def options(parser: ArgumentParser) -> None:
        parser.add_argument(
            '--newer-snapshot', help='Snapshot ID of the newer snapshot', required=True, type=int
        )
        parser.add_argument(
            '--older-snapshot', help='Snapshot ID of the older snapshot', required=True, type=int
        )
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--path', help='Path to file', type=str_decode)
        group.add_argument('--file-id', help='File ID', type=str_decode)
        parser.add_argument(
            '--page-size', help='Maximum number of entries to return per request', type=int
        )

    @staticmethod
    def main(rest_client: RestClient, args: Namespace) -> None:
        for res in snapshot.get_all_snapshot_file_diff(
            rest_client.conninfo,
            rest_client.credentials,
            newer_snap=args.newer_snapshot,
            older_snap=args.older_snapshot,
            path=args.path,
            file_id=args.file_id,
            limit=args.page_size,
        ):
            print(res)

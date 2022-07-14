#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_safety
----------------------------------

Tests for `safety` module.
"""


import json
import os
import unittest
from datetime import datetime
from http import HTTPStatus
from io import StringIO
from json import JSONDecodeError
from unittest.mock import Mock, patch

import click as click
from packaging.version import parse
from requests.exceptions import RequestException

from safety import util, safety
from safety.errors import MalformedDatabase
from safety.formatter import SafetyFormatter
from safety.models import CVE
from safety.safety import ignore_vuln_if_needed, get_closest_ver, precompute_remediations, compute_sec_ver, \
    calculate_remediations, read_vulnerabilities
from safety.util import SafetyContext
from tests.resources import VALID_REPORT, VULNS, SCANNED_PACKAGES, REMEDIATIONS
from tests.test_cli import get_vulnerability


class TestSafety(unittest.TestCase):

    def setUp(self) -> None:
        self.maxDiff = None
        self.dirname = os.path.dirname(__file__)
        self.report = VALID_REPORT
        self.report_vulns = VULNS
        self.report_packages = SCANNED_PACKAGES
        self.report_remediations = REMEDIATIONS

    def test_check_from_file(self):
        reqs = StringIO("Django==1.8.1")
        packages = util.read_requirements(reqs)

        vulns, _ = safety.check(
            packages=packages,
            key=None,
            db_mirror=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "test_db"
            ),
            cached=0,
            ignore_vulns={},
            ignore_severity_rules=None,
            proxy={},
            telemetry=False
        )
        self.assertEqual(len(vulns), 2)

    def test_check_from_file_with_hash_pins(self):
        reqs = StringIO(("Django==1.8.1 "
                         "--hash=sha256:c6c7e7a961e2847d050d214ca96dc3167bb5f2b25cd5c6cb2eea96e1717f4ade"))
        packages = util.read_requirements(reqs)

        vulns, _ = safety.check(
            packages=packages,
            key=None,
            db_mirror=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "test_db"
            ),
            cached=0,
            ignore_vulns={},
            ignore_severity_rules=None,
            proxy={},
            telemetry=False
        )
        self.assertEqual(len(vulns), 2)

    def test_multiple_versions(self):
        # Probably used for external tools using safety.check directly
        reqs = StringIO("Django==1.8.1\n\rDjango==1.7.0")
        packages = util.read_requirements(reqs)

        vulns, _ = safety.check(
            packages=packages,
            key=None,
            db_mirror=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "test_db"
            ),
            cached=0,
            ignore_vulns={},
            ignore_severity_rules=None,
            proxy={},
            telemetry=False
        )
        self.assertEqual(len(vulns), 4)

    def test_check_live(self):
        reqs = StringIO("insecure-package==0.1")
        packages = util.read_requirements(reqs)

        vulns, _ = safety.check(
            packages=packages,
            key=None,
            db_mirror=False,
            cached=0,
            ignore_vulns={},
            ignore_severity_rules=None,
            proxy={},
            telemetry=False
        )

        self.assertEqual(len(vulns), 1)

    def test_check_live_cached(self):
        from safety.constants import CACHE_FILE

        # lets clear the cache first
        try:
            with open(CACHE_FILE, 'w') as f:
                f.write(json.dumps({}))
        except Exception:
            pass

        reqs = StringIO("insecure-package==0.1")
        packages = util.read_requirements(reqs)

        vulns, _ = safety.check(
            packages=packages,
            key=None,
            db_mirror=False,
            cached=60 * 60,
            ignore_vulns={},
            ignore_severity_rules=None,
            proxy={},
            telemetry=False
        )
        self.assertEqual(len(vulns), 1)

        reqs = StringIO("insecure-package==0.1")
        packages = util.read_requirements(reqs)
        # make a second call to use the cache
        vulns, _ = safety.check(
            packages=packages,
            key=None,
            db_mirror=False,
            cached=60 * 60,
            ignore_vulns={},
            ignore_severity_rules=None,
            proxy={},
            telemetry=False
        )
        self.assertEqual(len(vulns), 1)

    def test_get_packages_licenses(self):
        reqs = StringIO("Django==1.8.1\n\rinvalid==1.0.0")
        packages = util.read_requirements(reqs)
        licenses_db = safety.get_licenses(
            db_mirror=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "test_db"
            ),
            cached=0,
            key="foobarqux",
            proxy={},
            telemetry=False
        )
        self.assertIn("licenses", licenses_db)
        self.assertIn("packages", licenses_db)
        self.assertIn("BSD-3-Clause", licenses_db['licenses'])
        self.assertIn("django", licenses_db['packages'])

        pkg_licenses = util.get_packages_licenses(packages, licenses_db)

        self.assertIsInstance(pkg_licenses, list)
        for pkg_license in pkg_licenses:
            license = pkg_license['license']
            version = pkg_license['version']
            if pkg_license['package'] == 'django':
                self.assertEqual(license, 'BSD-3-Clause')
                self.assertEqual(version, '1.8.1')
            elif pkg_license['package'] == 'invalid':
                self.assertEqual(license, 'unknown')
                self.assertEqual(version, '1.0.0')
            else:
                raise AssertionError(
                    "unexpected package '" + pkg_license['package'] + "' was found"
                )

    def test_get_packages_licenses_without_api_key(self):
        from safety.errors import InvalidKeyError

        # without providing an API-KEY
        with self.assertRaises(InvalidKeyError) as error:
            safety.get_licenses(
                db_mirror=False,
                cached=0,
                proxy={},
                key=None,
                telemetry=False
            )
        db_generic_exception = error.exception
        self.assertEqual(str(db_generic_exception), 'The API-KEY was not provided.')

    @patch("safety.safety.session")
    def test_get_packages_licenses_with_invalid_api_key(self, requests_session):
        from safety.errors import InvalidKeyError

        mock = Mock()
        mock.status_code = 403
        requests_session.get.return_value = mock

        # proving an invalid API-KEY
        with self.assertRaises(InvalidKeyError):
            safety.get_licenses(
                db_mirror=False,
                cached=0,
                proxy={},
                key="INVALID",
                telemetry=False
            )

    @patch("safety.safety.session")
    def test_get_packages_licenses_db_fetch_error(self, requests_session):
        from safety.errors import DatabaseFetchError

        mock = Mock()
        mock.status_code = 500
        requests_session.get.return_value = mock

        with self.assertRaises(DatabaseFetchError):
            safety.get_licenses(
                db_mirror=False,
                cached=0,
                proxy={},
                key="MY-VALID-KEY",
                telemetry=False
            )

    def test_get_packages_licenses_with_invalid_db_file(self):
        from safety.errors import DatabaseFileNotFoundError

        with self.assertRaises(DatabaseFileNotFoundError):
            safety.get_licenses(
                db_mirror='/my/invalid/path',
                cached=0,
                proxy={},
                key=None,
                telemetry=False
            )

    @patch("safety.safety.session")
    def test_get_packages_licenses_very_often(self, requests_session):
        from safety.errors import TooManyRequestsError

        # if the request is made too often, an 429 error is raise by PyUp.io
        mock = Mock()
        mock.status_code = 429
        requests_session.get.return_value = mock

        with self.assertRaises(TooManyRequestsError):
            safety.get_licenses(
                db_mirror=False,
                cached=0,
                proxy={},
                key="MY-VALID-KEY",
                telemetry=False
            )

    @patch("safety.safety.session")
    def test_get_cached_packages_licenses(self, requests_session):
        import copy
        from safety.constants import CACHE_FILE

        licenses_db = {
            "licenses": {
                "BSD-3-Clause": 2
            },
            "packages": {
                "django": [
                    {
                        "start_version": "0.0",
                        "license_id": 2
                    }
                ]
            }
        }
        original_db = copy.deepcopy(licenses_db)

        mock = Mock()
        mock.json.return_value = licenses_db
        mock.status_code = 200
        requests_session.get.return_value = mock

        # lets clear the cache first
        try:
            with open(CACHE_FILE, 'w') as f:
                f.write(json.dumps({}))
        except Exception:
            pass

        # In order to cache the db (and get), we must set cached as True
        response = safety.get_licenses(
            db_mirror=False,
            cached=60 * 60,  # Cached for one hour
            proxy={},
            key="MY-VALID-KEY",
            telemetry=False
        )
        self.assertEqual(response, licenses_db)

        # now we should have the db in cache
        # changing the "live" db to test if we are getting the cached db
        licenses_db['licenses']['BSD-3-Clause'] = 123

        resp = safety.get_licenses(
            db_mirror=False,
            cached=60 * 60,  # Cached for one hour
            proxy={},
            key="MY-VALID-KEY",
            telemetry=False
        )

        self.assertNotEqual(resp, licenses_db)
        self.assertEqual(resp, original_db)

    def test_report_licenses_bare(self):
        reqs = StringIO("Django==1.8.1\n\rinexistent==1.0.0")
        packages = util.read_requirements(reqs)

        # Using DB: test.test_db.licenses.json
        licenses_db = safety.get_licenses(
            db_mirror=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "test_db"
            ),
            cached=0,
            key=None,
            proxy={},
            telemetry=False
        )

        pkgs_licenses = util.get_packages_licenses(packages, licenses_db)
        output_report = SafetyFormatter(output='bare').render_licenses([], pkgs_licenses)

        self.assertEqual(output_report, "BSD-3-Clause unknown")

    @patch('safety.formatters.json.get_report_brief_info')
    def test_report_licenses_json(self, get_report_brief_info):
        get_report_brief_info.return_value = {'scan_target': 'environment',
                                              'scanned': ['/usr/local/lib/python3.9/site-packages'],
                                              'api_key': True,
                                              'packages_found': 2,
                                              'timestamp': '2022-03-03 16:31:30',
                                              'safety_version': '2.0.0.dev6'}

        reqs = StringIO("Django==1.8.1\n\rinexistent==1.0.0")
        packages = util.read_requirements(reqs)

        # Using DB: test.test_db.licenses.json
        licenses_db = safety.get_licenses(
            db_mirror=os.path.join(
                os.path.dirname(os.path.realpath(__file__)),
                "test_db"
            ),
            cached=0,
            key=None,
            proxy={},
            telemetry=False
        )

        pkgs_licenses = util.get_packages_licenses(packages, licenses_db)
        output_report = SafetyFormatter(output='json').render_licenses([], pkgs_licenses)

        expected_result = json.dumps(
            {
                "report_meta": {
                    "scan_target": "environment",
                    "scanned": ["/usr/local/lib/python3.9/site-packages"],
                    "api_key": True,
                    "packages_found": 2,
                    "timestamp": "2022-03-03 16:31:30",
                    "safety_version": "2.0.0.dev6"},
                "announcements": [],
                "licenses": [
                    {
                        "package": "django",
                        "version": "1.8.1",
                        "license": "BSD-3-Clause"
                    },
                    {
                        "package": "inexistent",
                        "version": "1.0.0",
                        "license": "unknown",
                    }
                ]
            },
            indent=4
        )
        # Packages without license are reported as "N/A"
        self.assertEqual(output_report.rstrip(), expected_result)

    @patch("safety.util.get_used_options")
    @patch("safety.safety.session")
    @patch.object(click, 'get_current_context', Mock(command=Mock(name=Mock(return_value='check'))))
    def test_get_announcements_catch_request_exceptions(self, requests_session, get_used_options):
        get_used_options.return_value = {'key': {'--key': 1}, 'output': {'--output': 1}}
        requests_session.get.side_effect = RequestException()
        self.assertEqual(safety.get_announcements('somekey', {}), [])

    @patch("safety.util.get_used_options")
    @patch("safety.safety.session")
    @patch.object(click, 'get_current_context', Mock(command=Mock(name=Mock(return_value='check'))))
    def test_get_announcements_catch_unhandled_http_codes(self, requests_session, get_used_options):
        get_used_options.return_value = {'key': {'--key': 1}, 'output': {'--output': 1}}

        unhandled_status = [status for status in HTTPStatus if status != HTTPStatus.OK]

        for http_status in unhandled_status:
            mock = Mock()
            mock.status_code = http_status.value
            requests_session.get.return_value = mock

            self.assertEqual(safety.get_announcements('somekey', {}), [])

    @patch("safety.util.get_used_options")
    @patch("safety.safety.session")
    @patch.object(click, 'get_current_context', Mock(command=Mock(name=Mock(return_value='check'))))
    def test_get_announcements_http_ok(self, requests_session, get_used_options):

        announcements = {
            "announcements": [{
                "type": "notice",
                "message": "You are using an outdated version of Safety. Please upgrade to Safety version 1.2.3"
                },
                {
                "type": "error",
                "message": "You are using an vulnerable version of Safety. Please upgrade now"
                }]
        }

        expected = announcements.get('announcements')

        mock = Mock()
        mock.status_code = HTTPStatus.OK.value
        mock.json.return_value = announcements
        requests_session.post.return_value = mock

        self.assertEqual(safety.get_announcements('somekey', {}), expected)

    @patch("safety.util.get_used_options")
    @patch("safety.safety.session")
    @patch.object(click, 'get_current_context', Mock(command=Mock(name=Mock(return_value='check'))))
    def test_get_announcements_wrong_json_response_handling(self, requests_session, get_used_options):
        # wrong JSON structure
        announcements = {
                "type": "notice",
                "message": "You are using an outdated version of Safety. Please upgrade to Safety version 1.2.3"
        }

        mock = Mock()
        mock.status_code = HTTPStatus.OK.value
        mock.json.return_value = announcements
        requests_session.get.return_value = mock

        self.assertEqual(safety.get_announcements('somekey', {}), [])

        # JSONDecodeError

        mock = Mock()
        mock.status_code = HTTPStatus.OK.value
        mock.json.side_effect = JSONDecodeError(msg='Expecting value', doc='', pos=0)
        requests_session.get.return_value = mock

        self.assertEqual(safety.get_announcements('somekey', {}), [])

    def test_ignore_vulns_by_unknown_severity(self):
        cve_no_cvss = CVE(name='PYUP-123', cvssv2=None, cvssv3=None)
        ignore_vulns = {}
        ignore_rules = {'ignore-cvss-unknown-severity': True}
        ignore_vuln_if_needed(vuln_id='1234', cve=cve_no_cvss, ignore_vulns=ignore_vulns,
                              ignore_severity_rules=ignore_rules)
        EXPECTED = {
            '1234': {'reason': 'Unknown CVSS severity, ignored by severity rule in policy file.', 'expires': None}}

        self.assertEqual(ignore_vulns, EXPECTED)

    def test_dont_ignore_vulns_by_unknown_severity(self):
        cve_no_cvss = CVE(name='PYUP-123', cvssv2=None, cvssv3=None)
        ignore_vulns = {}
        ignore_rules = {'ignore-cvss-unknown-severity': False}
        ignore_vuln_if_needed(vuln_id='1234', cve=cve_no_cvss, ignore_vulns=ignore_vulns,
                              ignore_severity_rules=ignore_rules)

        self.assertEqual(ignore_vulns, {})

    def test_ignore_vulns_by_base_score(self):
        cve_cvss_medium = CVE(name='CVE-123', cvssv2={'base_score': '4,3', 'impact_score': '2,9'},
                              cvssv3={'base_score': '6.1', 'impact_score': '2.7', 'base_severity': 'MEDIUM'})
        ignore_vulns = {}
        ignore_rules = {'ignore-cvss-severity-below': 7}
        ignore_vuln_if_needed(vuln_id='1234', cve=cve_cvss_medium, ignore_vulns=ignore_vulns,
                              ignore_severity_rules=ignore_rules)
        m_b_score = cve_cvss_medium.cvssv3.get('base_score')

        EXPECTED = {
            '1234': {
                'reason': f"Ignored by severity rule in policy file, {float(m_b_score)} < 7.0", 'expires': None}
        }
        self.assertEqual(ignore_vulns, EXPECTED)

        cve_cvss_critical = CVE(name='PVE-124', cvssv2=None,
                                cvssv3={'base_score': '9.8', 'impact_score': '5.9', 'base_severity': 'CRITICAL'})
        ignore_vulns = {}
        ignore_rules = {'ignore-cvss-severity-below': 7}
        ignore_vuln_if_needed(vuln_id='1235', cve=cve_cvss_critical, ignore_vulns=ignore_vulns,
                              ignore_severity_rules=ignore_rules)
        self.assertEqual(ignore_vulns, {})

        cve_cvss_high = CVE(name='PVE-125', cvssv2=None,
                            cvssv3={'base_score': '7.0', 'impact_score': '5.9', 'base_severity': 'HIGH'})
        ignore_vulns = {}
        ignore_rules = {'ignore-cvss-severity-below': 7}
        ignore_vuln_if_needed(vuln_id='1236', cve=cve_cvss_high, ignore_vulns=ignore_vulns,
                              ignore_severity_rules=ignore_rules)
        self.assertEqual(ignore_vulns, {})

    def test_get_closest_ver(self):
        versions = get_closest_ver(versions=['1.2', '1.3', '1.3.1', '1.3.2.dev5'], version='1.3.1')
        EXPECTED = {'minor': parse('1.3'), 'major': parse('1.3.2.dev5')}
        self.assertEqual(versions, EXPECTED)

        versions = get_closest_ver(versions=['1.2', '1.3', '1.3.1'], version='1.3.1')
        EXPECTED = {'minor': parse('1.3'), 'major': None}
        self.assertEqual(versions, EXPECTED)

        versions = get_closest_ver(versions=['1.2', '1.3', '1.3.1'], version='1.2')
        EXPECTED = {'minor': None, 'major': parse('1.3')}
        self.assertEqual(versions, EXPECTED)

        versions = get_closest_ver(versions=[], version='1.2')
        EXPECTED = {'minor': None, 'major': None}
        self.assertEqual(versions, EXPECTED)

        versions = get_closest_ver(versions=['1.2', '1.3'], version=None)
        EXPECTED = {'minor': None, 'major': None}
        self.assertEqual(versions, EXPECTED)

    def test_precompute_remediations(self):
        numpy_pkg = {'name': 'numpy', 'version': '1.22.0', 'secure_versions': ['1.22.3'],
                     'insecure_versions': ['1.22.2', '1.22.1', '1.22.0', '1.22.0rc3', '1.21.5']}
        vulns = [
            get_vulnerability(pkg_kwargs=numpy_pkg, vuln_kwargs={'affected_versions': ['1.22.0', '1.21.5']}),
            get_vulnerability(pkg_kwargs=numpy_pkg,
                              vuln_kwargs={'affected_versions': ['1.22.0', '1.22.0rc3']}),
            get_vulnerability(vuln_kwargs={'ignored': True}, pkg_kwargs={'name': 'django'})
        ]
        remediations = {}
        package_meta = {}
        precompute_remediations(remediations=remediations, package_metadata=package_meta, vulns=vulns,
                                ignored_vulns=set())

        EXPECTED = {'numpy': {'insecure_versions': ['1.22.2', '1.22.1', '1.22.0', '1.22.0rc3', '1.21.5'],
                              'secure_versions': ['1.22.3'], 'version': '1.22.0'}}
        self.assertEqual(package_meta, EXPECTED)

        EXPECTED = {'numpy': {'vulns_found': 2, 'version': '1.22.0', 'more_info_url': 'https://pyup.io/package/foo'}}

        self.assertEqual(remediations, EXPECTED)

    def test_compute_sec_ver(self):
        test_filename = os.path.join(self.dirname, "test_db/insecure_full_affected_versions.json")
        db_full = None
        with open(test_filename) as f:
            db_full = json.loads(f.read())
        self.assertIsNotNone(db_full)

        pre_pkg_meta = {'numpy': {'insecure_versions': ['1.22.2', '1.22.1', '1.22.0', '1.22.0rc3', '1.21.5'],
                                  'secure_versions': ['1.22.3'], 'version': '1.22.0'}}
        # The vuln affecting '1.21.5' was ignored by the user
        ignored_vulns = set()
        ignored_vulns.add('29')
        rem = {'numpy': {'vulns_found': 1, 'version': '1.22.0', 'more_info_url': 'https://pyup.io/package/foo'}}
        compute_sec_ver(remediations=rem, package_metadata=pre_pkg_meta, ignored_vulns=ignored_vulns, db_full=db_full)
        EXPECTED = {'numpy': {'vulns_found': 1, 'version': '1.22.0', 'secure_versions': ['1.22.3', '1.21.5'],
                              'closest_secure_version': {'major': parse('1.22.3'), 'minor': parse('1.21.5')},
                              'more_info_url': 'https://pyup.io/package/foo'}}
        self.assertEqual(rem, EXPECTED)

        pre_pkg_meta = {'numpy': {'insecure_versions': ['1.22.2', '1.22.1', '1.22.0', '1.22.0rc3', '1.21.5'],
                                  'secure_versions': ['1.22.3'], 'version': '1.22.0'}}
        ignored_vulns = set()
        rem = {'numpy': {'vulns_found': 2, 'version': '1.22.0', 'more_info_url': 'https://pyup.io/package/foo'}}
        compute_sec_ver(remediations=rem, package_metadata=pre_pkg_meta, ignored_vulns=ignored_vulns, db_full=db_full)
        EXPECTED = {'numpy': {'vulns_found': 2,
                              'version': '1.22.0', 'secure_versions': ['1.22.3'],
                              'closest_secure_version': {'major': parse('1.22.3'), 'minor': None},
                              'more_info_url': 'https://pyup.io/package/foo'}}

        self.assertEqual(rem, EXPECTED)

    @patch("safety.safety.compute_sec_ver")
    @patch("safety.safety.precompute_remediations")
    def test_calculate_remediations(self, precompute_remediations, compute_sec_ver):
        test_filename = os.path.join(self.dirname, "test_db/insecure_full_affected_versions.json")
        db_full = None
        with open(test_filename) as f:
            db_full = json.loads(f.read())
        self.assertIsNotNone(db_full)

        numpy_pkg = {'name': 'numpy', 'version': '1.22.0', 'secure_versions': ['1.22.3'],
                     'insecure_versions': ['1.22.2', '1.22.1', '1.22.0', '1.22.0rc3', '1.21.5']}

        vulns = [
            get_vulnerability(pkg_kwargs=numpy_pkg, vuln_kwargs={'affected_versions': ['1.22.0', '1.21.5']}),
            get_vulnerability(pkg_kwargs=numpy_pkg,
                              vuln_kwargs={'affected_versions': ['1.22.0', '1.22.0rc3']}),
            get_vulnerability(vuln_kwargs={'ignored': True}, pkg_kwargs={'name': 'django'})
        ]

        remediations = calculate_remediations(vulns, db_full)

        precompute_remediations.assert_called()
        compute_sec_ver.assert_called()

    def test_read_vulnerabilities_decode_error(self):
        with open(os.path.join(self.dirname, "test_db", "report_invalid_decode_error.json")) as f:
            self.assertRaises(MalformedDatabase, lambda: read_vulnerabilities(f))

    @patch("safety.safety.json.load")
    def test_read_vulnerabilities_type_error(self, json_load):
        json_load.side_effect = TypeError('foobar')
        with open(os.path.join(self.dirname, "test_db", "report.json")) as f:
            self.assertRaises(MalformedDatabase, lambda: read_vulnerabilities(f))

    def test_read_vulnerabilities(self):
        with open(os.path.join(self.dirname, "test_db", "report.json")) as f:
            self.assertDictEqual(self.report, read_vulnerabilities(f))

    def test_review_without_recommended_fix(self):
        vulns, remediations, packages = safety.review(self.report)
        self.assertListEqual(packages, list(self.report_packages.values()))
        self.assertDictEqual(remediations, self.report_remediations)
        self.assertListEqual(vulns, self.report_vulns)

    def test_report_with_recommended_fix(self):
        REMEDIATIONS_WITH_FIX = {'django': {'version': '4.0.1', 'vulns_found': 4, 'secure_versions': ['2.2.28', '3.2.13', '4.0.4'],
                                            'closest_secure_version': {'major': parse('4.0.4'),
                                                                       'minor': None},
                                            'more_info_url': 'https://pyup.io/packages/pypi/django/'}}

        with open(os.path.join(self.dirname, "test_db", "report_with_recommended_fix.json")) as f:
            vulns, remediations, packages = safety.review(read_vulnerabilities(f))
            self.assertDictEqual(remediations, REMEDIATIONS_WITH_FIX)

import os

from avocado.core import exit_codes
from avocado.utils import process, script
from selftests.utils import AVOCADO, BASEDIR, TestCaseTmpDir

CONFIG = """[job.output.testlogs]
statuses = ["FAIL", "CANCEL"]"""


class TestLogsUI(TestCaseTmpDir):
    def setUp(self):
        super().setUp()
        with open(
            os.path.join(self.tmpdir.name, "config"), "w", encoding="utf-8"
        ) as config:
            config.write(CONFIG)

    def test(self):
        cmd_line = (
            "%s --config=%s run -- examples/tests/passtest.py "
            "examples/tests/failtest.py "
            "examples/tests/canceltest.py "
        )
        cmd_line %= (AVOCADO, os.path.join(self.tmpdir.name, "config"))
        result = process.run(cmd_line, ignore_status=True)
        self.assertEqual(
            result.exit_status,
            exit_codes.AVOCADO_TESTS_FAIL,
            (f"Avocado did not return rc {exit_codes.AVOCADO_ALL_OK}:" f"\n {result}"),
        )
        stdout_lines = result.stdout_text.splitlines()
        self.assertNotIn(
            'Log file "debug.log" content for test "1-examples/tests/passtest.py'
            ':PassTest.test" (PASS)',
            stdout_lines,
        )
        self.assertIn(
            'Log file "debug.log" content for test "2-examples/tests/failtest.py:FailTest.test" (FAIL):',
            stdout_lines,
        )
        self.assertIn(
            'Log file "debug.log" content for test "3-examples/tests/canceltest.py'
            ':CancelTest.test" (CANCEL):',
            stdout_lines,
        )


class TestLogsFilesUI(TestCaseTmpDir):
    def setUp(self):
        super().setUp()
        self.config_file = script.TemporaryScript(
            "avocado.conf",
            "[job.output.testlogs]\n"
            "statuses = ['FAIL']\n"
            "logfiles = ['stdout', 'stderr', 'DOES_NOT_EXIST']\n",
        )
        self.config_file.save()

    def test_simpletest_logfiles(self):
        fail_test = os.path.join(BASEDIR, "examples", "tests", "failtest.sh")
        cmd_line = (
            f"{AVOCADO} --config {self.config_file.path} run "
            f"--job-results-dir {self.tmpdir.name} "
            f"--disable-sysinfo -- {fail_test}"
        )
        result = process.run(cmd_line, ignore_status=True)
        expected_rc = exit_codes.AVOCADO_TESTS_FAIL
        self.assertEqual(
            result.exit_status,
            expected_rc,
            (f"Avocado did not return rc {expected_rc}:" f"\n {result}"),
        )
        self.assertNotIn('Log file "debug.log" content', result.stdout_text)
        self.assertIn('Log file "stdout" content', result.stdout_text)
        self.assertIn('Log file "stderr" content', result.stdout_text)
        self.assertRegex(
            result.stderr_text, r'Failure to access log file.*DOES_NOT_EXIST"'
        )

    def tearDown(self):
        super().tearDown()
        self.config_file.remove()


class TestLogging(TestCaseTmpDir):
    def test_job_log(self):
        pass_test = os.path.join(BASEDIR, "examples", "tests", "passtest.py")
        cmd_line = f"{AVOCADO} run --job-results-dir " f"{self.tmpdir.name} {pass_test}"
        process.run(cmd_line)
        log_file = os.path.join(self.tmpdir.name, "latest", "job.log")
        with open(log_file, "r", encoding="utf-8") as fp:
            log = fp.read()
        self.assertIn("passtest.py:PassTest.test: STARTED", log)
        self.assertIn("passtest.py:PassTest.test: PASS", log)

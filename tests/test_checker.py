import os
import subprocess
import sys
import unittest

from docker_check import checker

DOCKERIZED = bool(int(os.getenv('DOCKERIZED', 0) or 0))
WINDOWS = sys.platform == 'win32'

if DOCKERIZED:
    # noinspection PyMethodMayBeStatic
    class InsideDockerTest:
        def test__has_dockerenv(self):
            if WINDOWS:
                raise unittest.SkipTest
            assert checker.has_dockerenv() is True

        def test__has_docker_in_proc_1_cgroup(self):
            if WINDOWS:
                raise unittest.SkipTest
            assert checker.has_docker_in_proc_1_cgroup() is True

        def test__has_cexecsvc(self):
            if not WINDOWS:
                raise unittest.SkipTest
            assert checker.has_cexecsvc() is True

        def test__is_inside_container(self):
            assert checker.is_inside_container() is True


if not DOCKERIZED:
    # noinspection PyMethodMayBeStatic
    class OutsideDockerTest:
        def test__has_dockerenv(self):
            if WINDOWS:
                raise unittest.SkipTest
            assert checker.has_dockerenv() is False

        def test__has_docker_in_proc_1_cgroup(self):
            if WINDOWS:
                raise unittest.SkipTest
            assert checker.has_docker_in_proc_1_cgroup() is False

        def test__has_cexecsvc(self):
            if not WINDOWS:
                raise unittest.SkipTest
            assert checker.has_cexecsvc() is False

        def test__is_inside_container(self):
            assert checker.is_inside_container() is None

        def test_docker(self):
            process = subprocess.Popen(['docker', 'run', '--rm', 'docker_check'], stdout=subprocess.PIPE)
            out, err = process.communicate()
            if WINDOWS:
                assert b'2 passed' in out
            else:
                assert b'3 passed' in out

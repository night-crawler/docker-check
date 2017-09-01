import typing as t
import os


def has_dockerenv() -> bool:
    return os.path.exists('/.dockerenv')


def has_docker_in_proc_1_cgroup() -> t.Union[bool, None]:
    with open('/proc/1/cgroup', 'r') as f:
        if 'docker' in f.read():
            return True
    return False


def is_inside_container() -> t.Union[bool, None]:
    if has_dockerenv():
        return True

    if has_docker_in_proc_1_cgroup():
        return True

    return None

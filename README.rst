docker-check
------------

A small Python utility that tries to check if we are inside a Docker container.


Installation
------------
.. code:: bash

    pip install -e git+https://github.com/night-crawler/docker-check.git@HEAD#egg=async-fetcher


Sample
------

.. code:: python

    from docker_check import checker
    checker.has_dockerenv()
    checker.has_docker_in_proc_1_cgroup()
    checker.is_inside_container()


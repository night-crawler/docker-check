### docker-check

A small Python utility that tries to check if we are inside a Docker container.

Supports Linux and Windows containers.

### Installation
```bash
pip install -e git+https://github.com/night-crawler/docker-check.git@HEAD#egg=docker-check
# OR
pip install docker-check
```

### Usage

```python
from docker_check import checker
if checker.is_inside_container():
    print('Inside container')
else:
    print('Not inside container')
```

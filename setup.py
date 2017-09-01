from setuptools import setup, find_packages
from docker_check import __version__


with open('README.rst', 'r') as f:
    long_description = f.read()


setup(
    name='docker_check',
    version=__version__,
    packages=find_packages(),
    url='https://github.com/night-crawler/docker-check',
    license='MIT',
    author='night-crawler',
    author_email='lilo.panic@gmail.com',
    description='A small Python utility that tries to check if we are inside a Docker container.',
    long_description=long_description,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
    ],
    requires=[]
)

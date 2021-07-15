import os
from pip._internal.req import parse_requirements
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


# parse_requirements() returns generator of pip.req.InstallRequirement objects

setup(
    name="pyorchestration",
    version="0.0.1",
    author="Andrea Capuano",
    author_email="andrealfie@gmail.com",
    description=("pyorchestration!"),
    license="BSD",
    keywords="example documentation tutorial",
    url="http://packages.python.org/an_example_pypi_project",
    packages=['pyorchestration', 'test', 'pyorchestration.core'],
    install_requires=[
        'amqp==5.0.6',
        'attrs==21.2.0',
        'billiard==3.6.4.0',
        'celery==5.1.2',
        'click==7.1.2',
        'click-didyoumean==0.0.3',
        'click-plugins==1.1.1',
        'click-repl==0.2.0',
        'iniconfig==1.1.1',
        'kombu==5.1.0',
        'packaging==21.0',
        'pluggy==0.13.1',
        'prompt-toolkit==3.0.19',
        'py==1.10.0',
        'pyparsing==2.4.7',
        'pytest==6.2.4',
        'pytz==2021.1',
        'PyYAML==5.4.1',
        'redis==3.5.3',
        'six==1.16.0',
        'toml==0.10.2',
        'vine==5.0.0',
        'wcwidth==0.2.5'
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

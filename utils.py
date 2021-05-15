"""Utility functions for the workshop."""

from __future__ import print_function
from distutils.version import LooseVersion as Version
import importlib
import sys

OK = '\x1b[42m[ OK ]\x1b[0m'
FAIL = '\x1b[41m[FAIL]\x1b[0m'


def run_env_check():
    """Check that the packages we need are installed and the Python version is high enough."""
    # check the python version
    print('Using Python in %s:' % sys.prefix)
    python_version = Version(sys.version)
    if python_version >= '3.7.1' and python_version < '3.9.0':
        print(OK, 'Python is version %s\n' % sys.version)
    else:
        print(FAIL, 'Python version >= 3.7.1 and < 3.9.0 is required, but %s is installed.\n' % sys.version)

    # read in the requirements
    with open('requirements.txt', 'r') as file:
        requirements = {}
        for line in file.read().splitlines():
            if line.startswith('./'):
                line = line.replace('./', '')
            try:
                pkg, version = line.split('==')
            except ValueError:
                pkg, version = line, None

            requirements[pkg.replace('-', '_')] = version

    # check the requirements
    for pkg, req_version in requirements.items():
        try:
            mod = importlib.import_module(pkg)
            if req_version:
                version = mod.__version__
                if Version(version) != req_version:
                    print(FAIL, '%s version %s is required, but %s installed.' % (pkg, req_version, version))
                    continue
            print(OK, '%s' % pkg)
        except ImportError:
            print(FAIL, '%s not installed.' % pkg)

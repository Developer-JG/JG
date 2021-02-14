import sys
import io

from setuptools import setup, find_packages, __version__ as setuptools_version
from pkg_resources import parse_version

import pkg_resources

try:
    import _markerlib.markers
except ImportError:
    _markerlib = None


# _markerlib.default_environment() obtains its data from _VARS
# and wraps it in another dict, but _markerlib_evaluate writes
# to the dict while it is iterating the keys, causing an error
# on Python 3 only.
# Replace _markerlib.default_environment to return a custom dict
# that has all the necessary markers, and ignores any writes.

class Python3MarkerDict(dict):

    def __setitem__(self, key, value):
        pass

    def pop(self, i=-1):
        return self[i]


if _markerlib and sys.version_info[0] >= 3:
    env = _markerlib.markers._VARS
    for key in list(env):
        new_key = key.replace('.', '_')
        if new_key != key:
            env[new_key] = env[key]

    _markerlib.markers._VARS = Python3MarkerDict(env)

    def default_environment():
        return _markerlib.markers._VARS

    _markerlib.default_environment = default_environment

# Avoid the very buggy pkg_resources.parser, which doesn't consistently
# recognise the markers needed by this setup.py
# Change this to setuptools 20.10.0 to support all markers.
if pkg_resources:
    if parse_version(setuptools_version) < parse_version('20.10.0'):
        MarkerEvaluation = pkg_resources.MarkerEvaluation

        del pkg_resources.parser
        pkg_resources.evaluate_marker = MarkerEvaluation._markerlib_evaluate
        MarkerEvaluation.evaluate_marker = MarkerEvaluation._markerlib_evaluate

setup(
    name='JG',
    version='0',
    description=('Convert between Travis-CI `.travis.yml` files and Tox `tox.ini` files'),
    long_description=long_description,
    keywords='tox, travis, continuous integration, CI',
    author='jeonggyu_hwang',
    author_email='h5638880@naver.com',
    url='https://github.com/Developer-JG/JG',
    packages=find_packages(),
    zip_safe=False,
    install_requires=install_requires,
    test_suite='JG.tests',
    entry_points = """\
      [console_scripts]
      panci = panci.cli:main
      panci-tox-quickstart = panci.toxquickstart:main
    """,
    license='CC-BY-NC-SA',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: tox',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Testing',
    ],
)

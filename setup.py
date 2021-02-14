import os
import sys
from setuptools import setup, find_packages

install_requires = ['PyYAML']

version = sys.version_info[:2]

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.md')).read()

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

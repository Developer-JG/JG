import os
import sys
from setuptools import setup, find_packages

install_requires = ['PyYAML']

<<<<<<< HEAD
packages = [
    about['JG'],
]
=======
version = sys.version_info[:2]
>>>>>>> 69b3c2c0c309943507ab9b86f3ff0fbcf6af425e

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.md')).read()

setup(
<<<<<<< HEAD
    name=about['JG'],
    version=about['1.0'],
    license=about['CC-BY-NC-SA],
    description=about['All codes in Developer_JG'],
    long_description=open('README.rst').read(),
    author=about['jeonggyu_hwang'],
    author_email=about['h5638880@naver.com'],
    url=about['https://github.com/Developer-JG/JG'],
    packages=packages,
    include_package_data=True,
=======
    name='JG',
    version='0',
    description=('Convert between Travis-CI `.travis.yml` files and Tox `tox.ini` files'),
    long_description=long_description,
    keywords='tox, travis, continuous integration, CI',
    author='jeonggyu_hwang',
    author_email='h5638880@naver.com',
    url='https://github.com/Developer-JG/JG',
    packages=find_packages(),
>>>>>>> 69b3c2c0c309943507ab9b86f3ff0fbcf6af425e
    zip_safe=False,
    install_requires=install_requires,
<<<<<<< HEAD
    classifiers=[
=======
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
>>>>>>> 69b3c2c0c309943507ab9b86f3ff0fbcf6af425e
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

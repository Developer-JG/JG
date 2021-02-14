import os
import sys
from setuptools import setup, find_packages

install_requires = ['PyYAML']

version = sys.version_info[:2]

if version < (2,7) or (3,0) <= version <= (3,1):
    install_requires += ['argparse']

this_dir = os.path.dirname(__file__)
long_description = "\n" + open(os.path.join(this_dir, 'README.rst')).read()

setup(
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
    zip_safe=False,
    platforms='any',
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Build Tools',
    ],
)

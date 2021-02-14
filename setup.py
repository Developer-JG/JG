from setuptools import setup

about = {}
with open('pur/JG.py') as f:
    exec(f.read(), about)

packages = [
    about['JG'],
]

install_requires = [x.strip() for x in open('requirements.txt').readlines()]

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

from setuptools import setup, find_packages

setup(
    name             = 'JG',
    version          = '1.0',
    description      = 'All codes in Developer_JG',
    author           = 'jeonggyu hwang',
    author_email     = 'h5638880@naver.com',
    url              = 'https://github.com/Developer-JG/JG',
    download_url     = 'https://github.com/Developer-JG/JG.git',
    install_requires = [ ],
    packages         = find_packages(exclude = []),
    python_requires  = '>=3',
    classifiers      = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)

pip install setuptools

# -*- encoding: utf-8 -*-
'''
@Time    :   2022-12-26 17:19:19
@Author  :   宋昊阳
@Contact :   1627635056@qq.com
'''

import os
from setuptools import setup, find_packages

VERSION = "0.0.1.2"
DESCRIPTION = "Easy ops"

setup(
    name="lkops",
    version=VERSION,
    author='tico',
    author_email="1627635056@qq.com",
    description=DESCRIPTION,
    # long_description_content='text/markdown',
    # long_description=open("README.md", encoding='utf-8').read(),
    packages=find_packages(),
    # install_requires=[
        # "flask",
        # "pandas",
        # "DBUtils",
        # "py2neo",
        # "gevent",
        # "sqlalchemy",
        # "flask_compress",
        # "flask_apscheduler"
    # ],
    keywords=['python', 'laikang'],
    classifiers= [
        "Programming Language :: Python :: 3"
    ]
)
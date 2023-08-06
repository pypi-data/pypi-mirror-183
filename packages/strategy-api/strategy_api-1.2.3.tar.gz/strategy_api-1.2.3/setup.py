#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author   : Kevin
# @Time     : 2022/12/12

import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='strategy_api',
    version='1.2.3',
    author='Kevin',
    author_email='1782552261@qq.com',
    description='框架更新，添加网关字典，可链接多个网关，选择网关控制',
    long_description=long_description,
    url='https://gitee.com/Jason520deng/strategy_api',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)


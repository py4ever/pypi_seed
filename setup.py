#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/4 11:36 上午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: OpenSource
# @File : setup.py
# @Project : pypi_seed


from distutils.core import setup
from setuptools import find_packages

from pypi_seed.setting import *

README_RST = os.path.join(os.getcwd(), "README.rst")
with open(README_RST, 'r') as rfile:
    LONG_DESCRIPTION = rfile.read()

setup(name=NAME,  # 包名
      version=VERSION,  # 版本号
      keywords=("pypi_seed", "seed", "generator", "levin", "leixuewei"),
      description='A small tool to demo on upload package to pypi and utility scripts to generate a pypi seed',
      long_description=LONG_DESCRIPTION if LONG_DESCRIPTION else """A small tool to generate a pypi seed 
and it's also a good pypi project example!
Powered by py4ever team!""",
      author='levin',
      author_email='991219092@qq.com',
      url='https://github.com/py4ever/pypi_seed',
      install_requires=[],
      license='Apache License 2.0',
      packages=find_packages(),
      platforms=["all"],
      entry_points={
          'console_scripts': [
              'pypiseed = pypi_seed.main:main',
              'pypi-seed = pypi_seed.main:main',
              'pypi_seed = pypi_seed.main:main',
              'ppseed = pypi_seed.main:main',
              'ppc = pypi_seed.main:main'
          ]
      },
      classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
      )

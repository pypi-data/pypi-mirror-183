#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time: 2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
  name = "typy-module-commands",
  version = "0.1.0",
  keywords = ("命令行","commands"),
  description = "快速构建命令行功能",
  long_description = "快速构建命令行功能",
  license = "MIT Licence",

  url = "https://gitee.com/tpyp/tpyp-module-commands",
  author = "唐茄茄",
  author_email = "584231366@qq.com",

  packages = find_packages(),
  include_package_data = True,
  platforms = "any",
  install_requires = []
)
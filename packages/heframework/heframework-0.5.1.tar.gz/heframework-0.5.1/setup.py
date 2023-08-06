#!/usr/bin/env python

from distutils.core import setup

setup(name='heframework',
      version='0.5.1',
      description='本次更新: 修复choose在json模式下返回None的错误',
      author='heStudio',
      author_email='hestudio@hestudio.org',
      url='https://gitee.com/hestudio-framework/main-windows/',
      packages=["heframework","heframework.src"],
     )


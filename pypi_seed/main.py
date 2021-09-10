#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/5 12:07 上午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : main.py
# @Project : pypi_seed

import sys
import pypi_seed.argsparser as argsparser
from pypi_seed.generator import do_generate

def main():
    if len(sys.argv) <= 1:
        argsparser.show_help()
        sys.exit(0)
    do_generate()


if __name__ == '__main__':
    main()

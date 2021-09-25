#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/25 10:14 上午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : template_loader.py
# @Project : pypi_seed
import os

import pypi_seed

"""
a template loader to load the template in a easy way
"""

MPATH = os.path.dirname(pypi_seed.__file__)
TPATH = os.path.join(MPATH, "template")


def resolve(path):
    return os.path.join(TPATH, path + ".template")


def load_template(template_path):
    """
    load template file which is needed
    for seed to generate file per template
    """
    tpath = resolve(template_path)
    if not os.path.exists(tpath):
        raise IOError("Cannot resolve template on path " + tpath)
    with open(tpath, 'r') as f:
        return f.read()
    return None

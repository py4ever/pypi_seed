#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/25 9:32 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : guide.py
# @Project : pypi_seed

"""
generate guideline per locale
"""

import locale
import os
import pypi_seed.template_loader as tl


def generate_doc(guide_path):
    with open(guide_path, "w") as file:
        file.write(tl.load_template("quickstart.en"))


def generate_zn_doc(guide_path):
    with open(guide_path, "w") as file:
        file.write(tl.load_template("quickstart.zh"))


def generate_quickstart(dir):
    loc = locale.getlocale()
    zone = loc[0]
    guide_path = os.path.join(dir, "quickstart.md")
    if zone:
        if zone.startswith("Chinese") or zone.startswith("zh_CN"):
            generate_zn_doc(guide_path)
    generate_doc(guide_path)

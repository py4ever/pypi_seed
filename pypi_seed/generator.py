#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/9 11:09 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : generator.py
# @Project : pypi_seed
import os
import pathlib

from pypi_seed import argsparser
from pypi_seed.template import TEMPLATE, README


def do_generate():
    conf = argsparser.args2dict()
    print("project setting: %s" % str(conf))
    generate(**conf)


def generate(dir=".", project="pypi_sample", author="pypi_seed"):
    seed_dir = os.path.join(dir, project)
    print("will generate project at %s " % seed_dir)
    if os.path.exists(seed_dir):
        print("project is already generated")
        return
    os.makedirs(seed_dir)
    setup_py = os.path.join(seed_dir, "setup.py")
    data = TEMPLATE % (project, author)
    with open(setup_py, "w") as file:
        file.write(data)
    print("[stage1] %s created" % setup_py)
    readme = os.path.join(seed_dir, "README.md")
    data = README % (project, author)
    with open(readme, "w") as file:
        file.write(data)
    print("[stage2] %s created" % readme)
    module_dir = os.path.join(seed_dir, project)
    try:
        if not os.path.exists(module_dir):
            os.mkdir(module_dir)
        init_file = os.path.join(module_dir, "__init__.py")
        if not os.path.exists(init_file):
            pathlib.Path(init_file).touch()
        print("[stage3] module dir created at %s" % module_dir)
    except Exception as e:
        print("[warning] %s" % str(e))
    print("cool, now your turn to work on your pypi lib as all completed.")
    print("powered by py4ever team")
    print("further discussion please contact qq group [Python全栈技术学习交流] or https://jq.qq.com/?_wv=1027&k=ISjeG32x")


if __name__ == '__main__':
    do_generate()

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
from pypi_seed.template_loader import load_template


def do_generate():
    conf = argsparser.args2dict()
    if conf:
        if 'verbose' in conf and conf['verbose']:
            print("project setting: %s" % str(conf))
        generate(**conf)


def generate(dir=".", project="pypi_sample", author="pypi_seed"):
    seed_dir = os.path.join(dir, project)
    print("will generate project at %s " % seed_dir)
    if os.path.exists(seed_dir):
        print("project is already generated")
        return
    os.makedirs(seed_dir)
    stage_id = 0
    stage_id = generate_setup(author, project, seed_dir, stage_id)
    stage_id = generate_gitignore(seed_dir, stage_id)
    stage_id = generate_readme(author, project, seed_dir, stage_id)
    stage_id = generate_module(project, seed_dir, stage_id)
    stage_id = generate_test(project, seed_dir, stage_id)
    print("Cool, pypi-seed has completed the project generation")
    print("Now your turn, to develop your own library and share it on pypi ")
    print("Powered by py4ever team")
    print(
        "Further discussion please contact qq group [Python全栈技术学习交流] or join by this link https://jq.qq.com/?_wv=1027&k=ISjeG32x")
    return stage_id


def generate_module(project, seed_dir, stage_id):
    stage_id += 1
    module_dir = os.path.join(seed_dir, project)
    try:
        if not os.path.exists(module_dir):
            os.mkdir(module_dir)
        init_file = os.path.join(module_dir, "__init__.py")
        if not os.path.exists(init_file):
            pathlib.Path(init_file).touch()
        print("[stage-%s] module dir created at %s" % (stage_id, module_dir))
        main_py = os.path.join(module_dir, "main.py")
        data = load_template("main.py") % (project, project)
        with open(main_py, "w") as file:
            file.write(data)
        print("[stage-%s] module main.py created at %s" % (stage_id, main_py))
    except Exception as e:
        print("[warning] %s" % str(e))
    finally:
        return stage_id


def generate_test(project, seed_dir, stage_id):
    stage_id += 1
    test_dir = os.path.join(seed_dir, 'tests')
    try:
        if not os.path.exists(test_dir):
            os.mkdir(test_dir)
        init_file = os.path.join(test_dir, "__init__.py")
        if not os.path.exists(init_file):
            pathlib.Path(init_file).touch()
        print("[stage-%s] testcase dir created at %s" % (stage_id, test_dir))
        test_main = os.path.join(test_dir, "test_main.py")
        data = load_template("test_main.py") % (project, project, project)
        with open(test_main, "w") as file:
            file.write(data)
        print("[stage-%s] testcase test_main.py created at %s" % (stage_id, test_main))
    except Exception as e:
        print("[warning] %s" % str(e))
    finally:
        return stage_id


def generate_gitignore(seed_dir, stage_id):
    stage_id += 1
    gitignore = os.path.join(seed_dir, '.gitignore')
    data = load_template("gitignore.py")
    with open(gitignore, "w") as file:
        file.write(data)
    print("[stage-%s] %s created" % (stage_id, gitignore))
    return stage_id


def generate_readme(author, project, seed_dir, stage_id):
    stage_id += 1
    readme = os.path.join(seed_dir, "README.md")
    data = load_template("readme.md") % (project, author)
    with open(readme, "w") as file:
        file.write(data)
    print("[stage-%s] %s created" % (stage_id, readme))
    stage_id += 1
    readme = os.path.join(seed_dir, "README.rst")
    data = load_template("readme.rst") % (project, project, author)
    with open(readme, "w") as file:
        file.write(data)
    print("[stage-%s] %s created" % (stage_id, readme))
    return stage_id


def generate_setup(author, project, seed_dir, stage_id):
    stage_id += 1
    setup_py = os.path.join(seed_dir, "setup.py")
    data = load_template("setup.py") % (project, author)
    with open(setup_py, "w") as file:
        file.write(data)
    print("[stage-%s] %s created" % (stage_id, setup_py))
    return stage_id


if __name__ == '__main__':
    do_generate()

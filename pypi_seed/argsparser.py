#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/9 11:02 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : argsparser.py
# @Project : pypi_seed
import getopt
import os
import sys

from pypi_seed.setting import VERSION


def print_error(msg):
    print("\033[0;31;40m%s\033[0m" % msg)


def show_all_samples():
    print("option1: ")
    print("pypiseed --project demo_project --author testuser --dir=/tmp ")
    print("option2: ")
    print("ppc --project demo_project --author testuser --dir=/tmp ")
    print("option3: ")
    print("ppc -p demo_project -a testuser -d /tmp ")
    print("option4: ")
    print("ppc -p demo_project -a testuser -d /tmp --cli ")


def show_sample_run():
    print("option1: ")
    print("pypiseed --project demo_project --author testuser --dir=/tmp ")
    print("option2: ")
    print("ppc -p demo_project -a testuser -d /tmp ")


def show_version():
    print('pypi-seed version %s' % VERSION)
    print('ClIs:')
    print('\tpypiseed')
    print('\tppc')


def show_help():
    show_version()
    print('usage:')
    print('\t-h, --help: print help message.')
    print('\t-v, --version: print help message.')
    print('\t-p, --project: your desired project name')
    print('\t-d, --dir: where to save the sample project after code-generation')
    print('\t-a, --author: the author information')
    print('\t--cli: generate sample cli-project')
    print("===========================================")
    show_all_samples()
    show_about()


def show_about():
    print("===========================================")
    print("pypi_seed #种子项目")
    print("欢迎关注公众号【雷学委】【孤寒者】【布小禅】，加入Python开发者阵营！")
    print("Welcome to subscribe wechat-media【雷学委】【孤寒者】【布小禅】and join python group！")
    print("Further queries please contact qq：【Python全栈技术学习交流】Click this link=> https://jq.qq.com/?_wv=1027&k=ISjeG32x ")
    print("===========================================")


def args2dict():
    argv = sys.argv[1:]
    verbose = False
    try:
        opts, args = getopt.getopt(argv, "hvp:d:a:",
                                   ["help",
                                    "version",
                                    "cli",
                                    "verbose",
                                    "project=",
                                    "dir=",
                                    "author=", ])
    except Exception as e:
        print("parameters: %s " % argv)
        raise ValueError("Looks like missing value, please check usage by '-h'. Current error : %s " % str(e))
    project = None
    path = None
    author = None
    cli = False
    print("opts is %s" % opts)
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            show_help()
            return None
        if opt in ['-v', '--version']:
            show_version()
            return None
        if opt in ['--verbose']:
            verbose = True
        if opt in ['--cli']:
            cli = True
        if opt in ['-p', '--project']:
            print("project: %s" % arg)
            project = arg
        elif opt in ['-a', '--author']:
            print("author: %s" % arg)
            author = arg
        elif opt in ['-d', '--dir']:
            print("directory: %s" % arg)
            path = arg
    if project is None:
        print_error("Missing project, please input project with '-p' or '--project', e.g. -p my_project")
        show_sample_run()
        return None
    if author is None:
        print_error("Missing author, please input author with '-a' or '--author', e.g. -a testuser")
        show_sample_run()
        return None
    if path is None:
        path = os.getcwd()
        print("path is not given, so will use default as current directory : %s" % path)
    return dict(name=project, author=author, dir=path, verbose=verbose, with_cli=cli)


if __name__ == "__main__":
    print(args2dict())

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


def show_sample_run():
    print("option1: ")
    print("pypiseed --project demo_project --author testuser --dir=/tmp ")
    print("option2: ")
    print("pyseed --project demo_project --author testuser --dir=/tmp ")


def show_help():
    print('pypiseed/pyseed version %s' % VERSION)
    print('usage:')
    print('-h, --help: print help message.')
    print('-p, --project: your desired project name')
    print('-d, --dir: where to save the sample project after code-generation')
    print('-a, --author: the author information')
    print("===========================================")
    show_sample_run()
    show_about()


def show_about():
    print("===========================================")
    print("pypi_seed #种子项目")
    print("欢迎关注公众号【雷学委】【孤寒】【布小禅】，加入Python开发者阵营！")
    print("Welcome to subscribe wechat-media【雷学委】【孤寒】【布小禅】and join python group！")
    print("Further queries please contact qq：【Python全栈技术学习交流】Click this link=> https://jq.qq.com/?_wv=1027&k=ISjeG32x ")
    print("===========================================")


def args2dict():
    argv = sys.argv[1:]
    if '-h' in argv or '--help' in argv:
        show_help()
        exit(0)
    try:
        opts, args = getopt.getopt(argv, "p:d:a",
                                   ["project=",
                                    "dir=",
                                    "author=", ])
    except Exception as e:
        raise ValueError("Looks like missing value, please check usage by '-h'. Current error : %s " % str(e))
    project = None
    path = None
    author = None
    print("opts is %s" % opts)
    for opt, arg in opts:
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
        print("please input project with '-p' or '--project', e.g. -p my_project ")
        raise ValueError("Missing project")
    if author is None:
        print("please input author with '-a' or '--author', e.g. -a whoami ")
        raise ValueError("Missing author")
    if path is None:
        path = os.getcwd()
        print("path is not given, so will use default as current directory : %s" % path)
    return dict(project=project, author=author, dir=path)


if __name__ == "__main__":
    print(args2dict())

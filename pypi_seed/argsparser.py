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


def show_sample_run():
    print("option1: ")
    print("pypiseed -p demo_project -a testuser -P '/tmp' ")
    print("option2: ")
    print("pyseed -p demo_project -a testuser -P '/tmp' ")


def show_help():
    print('usage:')
    print('-h, --help: print help message.')
    print('-p, --project: your desired project name')
    print('-P, --path: where to save the sample project after code-generation')
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
        opts, args = getopt.getopt(argv, "p:P:a",
                                   ["path=",
                                    "author=",
                                    "project="])
    except Exception as e:
        raise ValueError("Looks like missing value, please check usage by '-h'. Current error : %s " % str(e))
    project = author = path = None
    for opt, arg in opts:
        if opt in ['-p', '--project']:
            project = arg
        elif opt in ['-a', '--author']:
            author = arg
        elif opt in ['-P', '--path']:
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
    return dict(project=project, author=author, path=path)


if __name__ == "__main__":
    print(args2dict())

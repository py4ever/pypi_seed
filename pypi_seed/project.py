#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/25 7:48 下午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : project.py
# @Project : pypi_seed


class ProjectMeta(object):
    def __init__(self, name, author, dir, with_cli=False, verbose=False):
        self.name = name
        self.author = author
        self.dir = dir
        self.with_cli = with_cli
        self.verbose = verbose

    def __str__(self):
        return 'ProjectMeta(name:%s, author:%s, dir:%s, with_cli:%s, verbose:%s)' \
               % (self.name, self.author, self.dir, self.with_cli, self.verbose)


def dict2project(**kwargs):
    return ProjectMeta(**kwargs)


if __name__ == '__main__':
    print("proj:%s" % str(ProjectMeta("demo", "leixuewei", "/tmp")))
    dict = {"name": "demo", "author": "leixuewei", "dir": "/tmp"}
    print(str(dict2project(**dict)))

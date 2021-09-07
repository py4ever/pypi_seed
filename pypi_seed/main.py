#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/9/5 12:07 上午
# @Author : LeiXueWei
# @CSDN/Juejin/Wechat: 雷学委
# @XueWeiTag: CodingDemo
# @File : main.py
# @Project : pypi_seed
import os


def main():
    print("pypi_seed 种子项目")
    print("欢迎关注公众号【雷学委】【孤寒】【布小禅】，加入Python开发者阵营！")
    print("===========================================")
    print("如何创建项目：")
    print("1）打开python终端REPL：")
    print("2）输入下面代码：")
    print("import pypi_seed.main as pm")
    print("pm.generate() #当前目录生成pypi_sample")
    print("#或者加一个路径参数")
    print("pm.generate('/tmp') #当前目录生成/tmp/pypi_sample")
    print("===========================================")
    print("其他问题可以找qq：【Python全栈技术学习交流】：https://jq.qq.com/?_wv=1027&k=ISjeG32x ")
    print("===========================================")


def generate(path="."):
    seed_dir = os.path.join(path, "pypi_sample")
    print("will generate project at %s " % seed_dir)
    if os.path.exists(seed_dir):
        print("project is already generated")
        return
    os.mkdir(seed_dir)
    setuppy = os.path.join(seed_dir,"setup.py")



if __name__ == '__main__':
    main()

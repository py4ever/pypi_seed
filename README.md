# pypi_seed aka ppc

Hey, this is a seed generator to generate
- a seed project that available to be uploaded to pypi.org
- it provides 'cli' to customize the seed before generation
- support the standard python project generation or CLI python lib generation( run with '--cli' option)

'ppc' here is a shortcut, short for PyPiSeed(P-P-C).

一个pypi的项目模板（种子项目） \
用途：
1) 提供了cli（命令行工具帮你生成符合pypi上传要求的库）
2) 本示例库有社区维护，还有大量专业的Python大佬一起合作。
3) 支持生成普通标准Python模块或者cli库模版项目（加上--cli选项）

这里的 'ppc' 就是一个快捷调用pypiseed的指令，它是谐音了PyPiSeed（P-P-C），方便使用者记忆，比输入pypiseed更快速。



# Installation / 安装

Get pypi_seed by pip (通过PIP工具来安装pypi_seed)
```bash
pip install pypi_seed
```


# Use pypi_seed as CLI / 命令行使用

We can call the cli 'ppc' or 'pypiseed' or 'ppseed'： \
调用下面两个命令行即可。

```bash
ppc --project=demo_project --author=testuser --dir=/tmp
```

```bash
pypiseed --project=demo_project --author=testuser --dir=/tmp
```

```bash
ppseed --project=demo_project --author=testuser --dir=/tmp
```


# APIs / 程序接口调用

Open the python on terminal and type in below codes: \
打开python终端REPL， 输入下面代码：

- opt1 generate a seed project with the default options 

默认生成方法，需要自己修改作者，项目名字（仅做试手）
```
import pypi_seed.generator as pm
pm.generate() #当前目录生成pypi_sample
```

- opt2 generate a seed project with the user customized options

定制生成自己的pypi库

```
import pypi_seed.generator as pm
#take a path parameter # 或者加一个路径参数
pm.generate('/tmp') #当前目录生成/tmp/pypi_sample
```

也可以定制作者项目信息，再生成自己的pypi库

```
import pypi_seed.generator as pm
#take all params # 当前目录生成/tmp/pypi_sample，作者Lei小花"
pm.generate(path="/tmp", project="pypi_sample", author="Lei小花") 
```

# More background why I develop this module / 更多背后的故事

Actually I come up with this idea after I developed some other python library and I do build some samples project as references for daily work.

And after I wrote some blogs on programming on python as well as some study on Jupyter/Django projects, I realized I have to build this. 

Other things like tackling with 'rst' file error or repeating the project sketch stuff which is kinda some 'boil-plain' work

So I develop this module and after installation, you will get 'pypiseed' or 'ppseed' or a shortcut 'ppc'. 

当我开发了很多python模块/项目之后，突然想起了干这个事情了，写个项目生成器，因此写了这个 pypi-seed。

我写了很多python相关的博客，也看过很多开源的python项目，像Jupyter，Django等项目，吸取了一些项目组织的优点。

当然，创建新项目需要准备rst说明文件，还有项目的基础配置等等，每次从0搭建都比较费时。

这里做了一个简单的命令行工具'pypi-seed'或者'ppseed'或者'ppc', 一行命令帮助开发者创建自己的项目！

# Further discussion / 更多使用问题

Please raise PR or find the tencent group chat : https://jq.qq.com/?_wv=1027&k=ISjeG32x 

其他问题可以找qq：【Python全栈技术学习交流】：https://jq.qq.com/?_wv=1027&k=ISjeG32x 

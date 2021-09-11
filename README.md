# pypi_seed

Hey, this is a seed generator to generate
- a seed project that available to be uploaded to pypi.org
- it provides 'cli' to customize the seed before generation


一个pypi的项目模板（种子项目） \
用途：
1) 提供了cli（命令行工具帮你生成符合pypi上传要求的库）
2) 本示例库有社区维护，还有大量专业的Python大佬一起合作。

# Installation / 安装

Get pypi_seed by pip (通过PIP工具来安装pypi_seed)
```bash
pip install pypi_seed
```


# Use pypi_seed as CLI / 命令行使用

We can call the cli 'pypiseed' or 'pyseed'： \
调用下面两个命令行即可。
```bash
pypiseed --project=demo_project --author=testuser --dir=/tmp
```

```bash
pyseed --project=demo_project --author=testuser --dir=/tmp
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


# Further discussion / 更多使用问题

Please raise PR or find the tencent group chat : https://jq.qq.com/?_wv=1027&k=ISjeG32x 

其他问题可以找qq：【Python全栈技术学习交流】：https://jq.qq.com/?_wv=1027&k=ISjeG32x 

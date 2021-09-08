# pypi_seed

一个pypi的项目模板（种子项目） \
用途：
1) 提供了cli（命令行工具帮你生成符合pypi上传要求的库）
2) 本示例库有社区维护，还有大量专业的Python大佬一起合作。

# 安装

```bash
pip install pypi_seed
```


# 使用


打开python终端REPL， 输入下面代码：

定制生成自己的pypi库

```
import pypi_seed.main as pm
pm.generate() #当前目录生成pypi_sample
#或者加一个路径参数
pm.generate('/tmp') #当前目录生成/tmp/pypi_sample
```



默认生成方法，需要自己修改作者，项目名字
```
import pypi_seed.main as pm
pm.generate() #当前目录生成pypi_sample
```

# 更多使用问题

其他问题可以找qq：【Python全栈技术学习交流】：https://jq.qq.com/?_wv=1027&k=ISjeG32x 

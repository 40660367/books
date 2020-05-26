# Jupyter 魔法函数(Magic)

## Magic是什么？

- 为实现一些快捷操作，提升效率。Notebook中提供了Magic开关，能极大得优化我们使用Notebook的体验。实现一些单纯python要很麻烦才能实现的功能。
- Magic 开关分为两大类：`%line magic` 和 `%%cell magic`

| 符号       | 功能                                               |
| ---------- | -------------------------------------------------- |
| %：        | 行魔法函数，只对本行代码生效。                     |
| %%：       | Cell魔法函数，在整个Cell中生效，必须放于Cell首行。 |
| %lsmagic： | 列出所有的魔法函数                                 |
| %magic     | 查看各个魔法函数的说明                             |
| ?          | 后面加上魔法函数名称，可以查看该函数的说明         |

**常用魔法函数的示例：**

| 魔法函数            | 作用                                                         |
| ------------------- | ------------------------------------------------------------ |
| %%writefile         | 写入外部python脚本                                           |
| %run                | 调用外部python脚本                                           |
| %timeit             | 测试单行语句的执行时间                                       |
| %%timeit            | 测试整个单元中代码的执行时间                                 |
| % matplotlib inline | 显示 matplotlib 包生成的图形                                 |
| %%writefile         | 写入文件                                                     |
| %pdb                | 调试程序                                                     |
| %pwd                | 查看当前工作目录                                             |
| %ls                 | 查看目录文件列表                                             |
| %reset              | 清除全部变量                                                 |
| %who                | 查看所有全局变量的名称，若给定类型参数，只返回该类型的变量列表 |
| %whos               | 显示所有的全局变量名称、类型、值/信息                        |
| %xmode Plain        | 设置为当异常发生时只展示简单的异常信息                       |
| %xmode Verbose      | 设置为当异常发生时展示详细的异常信息                         |
| %debug bug          | 调试，输入quit退出调试                                       |
| %env                | 列出全部环境变量                                             |

注意这些命令是在Python kernel中适用的，其他 kernel 不一定适用

## 实验环境配置
[环境安装](/setup.html)

```python
%lsmagic #Magic函数总览
```
```python
%quickref #Magic函数的简要说明
```

## Line Magic

```python
a='string in python'
b=5
def myfun1():
    pass
a
b
```

```python
%config ZMQInteractiveShell.ast_node_interactivity='all'
```

```python
a='string in python'
b=5
def myfun1():
    pass
a
b
```

```python
%whos
#查看全局成员变员
```

```python
%reset
#清空全局成员变员
```

```python
%whos
#再次查看全局成员变员
```

## Cell Magic
### 对单元格中代码进行计时
```python
%%timeit 50
for item in range(100):
    a=item
    del a
#
```

```python
%%time 
for item in range(100000):
    a=item
    del a
```
### 单元格显示SVG
```python
%%SVG
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 400" width="500" height="200">
  <rect x="80" y="60" width="250" height="250" rx="20" style="fill:red; stroke:black; fill-opacity:0.7" />
  <rect x="280" y="110" width="250" height="250" rx="40" style="fill:blue; stroke:black; fill-opacity:0.5;" />
</svg>
```
### 单元格显示HTML
```python
%%html
<table>
<tr>
<th>Header 1</th>
<th>Header 2</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
<marquee style='width: 30%; color: blue;'><b>Hey There!!!</b></marquee>
```
### 在单元格中调用系统命令
```python
%%system
ls
```

```python
!ls
#或者直接在单元格中使用!ls
```

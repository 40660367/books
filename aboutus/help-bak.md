# Linux命令在线运行

本课程的一大特点是每节的代码都是可以在线实时运行的，您可以随时改变一些命令，通过运行结果进一步理解改动所带来的影响。  
本教程将使用 Linux 的发行版本 Ubuntu 为例来为大家介绍 Linux 系统的应用。  
我们认为，这种交互式的学习体验对于学习Linux非常重要。因为Linux课程的学习在只有文字解释在这时候可能比较苍白无力，而且不足以覆盖所有细节。读者需要不断改动命令、观察运行结果并总结经验，从而逐步领悟和掌握Linux系统。

#### 练习:熟悉在线使用Linux命令

使用网页底部的Terminal,输入`date`并按回车,将得到系统时间。

### Git命令在线运行

本课程的一大特点是每节的代码都是可以在线实时运行的，您可以随时改变一些命令，通过运行结果进一步理解改动所带来的影响。  
本教程将使用 Linux 的发行版本 Ubuntu 为例来为大家介绍Git课程。  
我们认为，这种交互式的学习体验对于学习Linux非常重要。因为Linux课程的学习在只有文字解释在这时候可能比较苍白无力，而且不足以覆盖所有细节。读者需要不断改动命令、观察运行结果并总结经验，从而逐步领悟和掌握Linx系统。

## 如何使用本课程

### 关于用户环境

该课程为每位浏览用户提供独立的在线学习环境，用户可安全，高效地进行学习。

本课程的后端是基于Jupyter Notebook构建的。

**说明：环境不保留用户任何个人数据，为安全考虑也请勿放置任何含有个人信息的敏感数据。**

### 关于代码框

本课程中的代码均可在线运行，帮助您提升学习效率。

**Python在线运行的简单示例**

```Python
#从Python中导入并显示Python之禅
import this
```

**注意**：代码框的执行请一定要按顺序执行。

### 关于代码框输出结果不全的问题：

通常当您需要在同一个代码框中输出多个结果时，代码框默认只返回最后一个结果。

如在执行下列代码框，通常会只有最后一行`2 /4 `的结果`0.5`输出。

```Python
5 + 4  # 加法
4.3 - 2 # 减法
3 * 7  # 乘法
2 / 4  # 除法，得到一个浮点数
```

**解决办法：**

- 使用`print()`函数将输出结果进行打印

- 使用魔法函数`%config ZMQInteractiveShell.ast_node_interactivity='all'`后，强制代码框返回所有的结果。

```Python
%config ZMQInteractiveShell.ast_node_interactivity='all'
```

```Python
5 + 4  # 加法
4.3 - 2 # 减法
3 * 7  # 乘法
2 / 4  # 除法，得到一个浮点数
```

### 关于魔法函数%

`%`开头的为魔法函数的标志，常用于执行普通Python代码不太方便执行的操作，如`%%writefile hello.py`为把代码框中的内容写入至文件`hello.py`这个文件中。``%%time``为计时该代码框运行时间。

```Python
%%writefile hello.py
print('Hello,Python')
```

`!`为调用操作系统命令的标志，如`!ls`为列出当前目录下所有的文件,`!pwd`为列出当前路径，`!python`为调用Python

使用`!ls`调用`ls`命令查看上一个代码框写入的文件

```Python
!ls
```

使用`!cat调用`cat`命令查看上一个代码框写入的文件的内容

```Python
!cat hello.py
```

使用`!python`调用`python`来执行这个文件

```Python
!python hello.py
```

关于更多的魔法函数可自行百度。

### 学习中其它常见问题

如果您在使用过程中遇到问题，请点击页面最底部的使用帮助，常见问题在那里均可得到解决。

如果还是没有解决，请加在线客服群，我们将尽快为您解决。	









## 其他工具介绍

### IDLE - 自带的集成开发工具

IDLE是安装Python环境时自带的集成开发工具，如下图所示。但是由于IDLE的用户体验并不是那么好所以很少在实际开发中被采用。

### Jupyter Notebook - 更好的交互式编程工具

当然，我们可以通过安装Jupyter工具并运行名为notebook的程序在浏览器窗口中进行交互式代码编写操作。

`pip install jupyter`，然后执行`jupyter notebook`。实际上本课程的后端也是基于Jupyter Notebook构建的。

## 交互式运行Python程序

在您本地环境的命令行后，输入python或python3进入Python交互式环境。

在《动手学Python》课程网页上已经默认进入交互式环境。

#### 练习确认Python的版本

```Python
import sys

print(sys.version_info)
print(sys.version)
```

### 解释式运行Python程序 

#### 练习：在命令行确认Python的版本

```Shell
!python --version
```

#### 练习：使用Python帮助

```Python
!python -h
```

#### 练习：编写并运行Python源码

可以用文本编辑工具（如使用VS Code）编写Python源代码并用py作为后缀名保存文件。

也可以在《动手学Python》课程网页上直接将源码写入文件。

```Python
%%writefile hello.py
print('hello, Python!')
```

使用`!cat`查看刚刚写入的文件的内容

```Python
!cat hello.py
```

执行Python源码。看看是否输出了"hello, Python!"。

```Python
!python hello.py
```

## 如何使用本课程

### 关于用户环境

该课程为每位浏览用户提供独立的在线学习环境，用户可安全，高效地进行学习。

本课程的后端是基于Jupyter Notebook构建的。

**说明：环境不保留用户任何个人数据，为安全考虑也请勿放置任何含有个人信息的敏感数据。**

### 关于代码框

本课程中的代码均可在线运行，帮助您提升学习效率。

**Python在线运行的简单示例**

```Python
#从Python中导入并显示Python之禅
import this
```

**注意**：代码框的执行请一定要按顺序执行。

### 关于代码框输出结果不全的问题：

通常当您需要在同一个代码框中输出多个结果时，代码框默认只返回最后一个结果。

如在执行下列代码框，通常会只有最后一行`2 /4 `的结果`0.5`输出。

```Python
5 + 4  # 加法
4.3 - 2 # 减法
3 * 7  # 乘法
2 / 4  # 除法，得到一个浮点数
```

**解决办法：**

- 使用`print()`函数将输出结果进行打印

- 使用魔法函数`%config ZMQInteractiveShell.ast_node_interactivity='all'`后，强制代码框返回所有的结果。

```Python
%config ZMQInteractiveShell.ast_node_interactivity='all'
```

```Python
5 + 4  # 加法
4.3 - 2 # 减法
3 * 7  # 乘法
2 / 4  # 除法，得到一个浮点数
```

### 关于魔法函数%

`%`开头的为魔法函数的标志，常用于执行普通Python代码不太方便执行的操作，如`%%writefile hello.py`为把代码框中的内容写入至文件`hello.py`这个文件中。``%%time``为计时该代码框运行时间。

```Python
%%writefile hello.py
print('Hello,Python')
```

`!`为调用操作系统命令的标志，如`!ls`为列出当前目录下所有的文件,`!pwd`为列出当前路径，`!python`为调用Python

使用`!ls`调用`ls`命令查看上一个代码框写入的文件

```Python
!ls
```

使用`!cat调用`cat`命令查看上一个代码框写入的文件的内容

```Python
!cat hello.py
```

使用`!python`调用`python`来执行这个文件

```Python
!python hello.py
```

关于更多的魔法函数可自行百度。\





## 使用帮助

### 如何使用本教程

本《动手学R语言》课程中的代码均可在线运行，帮助您提升学习效率。

如果您在使用过程中遇到问题，请在询问帮助信息中查看已列出的常见问题。如果还是没有解决，请加在线客服群，我们将尽快为您解决。

*** 一个R在线运行的简单示例 ***

```R
#直方图显示1000个来自均值为5的正态分布的随机数
hist(rnorm(1000,mean=5),col = rainbow(10))
```

### 学习中的常见问题

请点击页面最底部的使用帮助，常见问题在那里均可得到解决   

如果您还有困惑，请加入下方互动学习微信群
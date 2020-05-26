# Shell 简介		

shell为您提供了对UNIX系统的接口。向你收集的输入，并根据输入执行程序。当一个程序执行完毕后，它会显示该程序的输出。

shell是一个环境，我们可以运行我们的命令，程序和shell脚本。shell有不同的风格，就像有不同风格的操作系统。每个的shell的风格，有它自己的一套识别的命令和功能。

## Shell 提示符

提示符下这就是所谓的命令提示符下$，发出shell。虽然会显示提示，您可以键入一个命令。

shell读取输入后按Enter键。它决定了想要的命令和执行输入的第一个字符。一个字是一个完整的字符集。空格和制表符分隔单词。

以下是一个简单的例子date命令显示当前日期和时间：

```bash
date
```

你可以定制你的命令提示符下使用环境变量PS1环境教程解释。

## Shell 类型

在UNIX系统下有两种主要类型的shell：

1. 		Bourne shell. 如果您使用的是Bourne类型的shell，默认提示符为$字符。
2. 		C shell.如果您使用的是C型的shell，默认的提示字符％。

再还有各种Bourne shell的子类别列示如下：

- Bourne shell ( sh)
- Korn shell ( ksh)
- Bourne Again shell ( bash)
- POSIX shell ( sh)

不同的C型shell如下：

- C shell ( csh)
- ENEX/TOPS C shell ( tcsh)

原来的UNIX shell写于20世纪70年代中期，由斯蒂芬·伯恩，在新泽西AT＆T贝尔实验室。

Bourne shell 是第一个shell 出现在UNIX系统上，因此，它被称为 "the shell".

Bourne shell的安装通常为 /bin/sh 在大多数UNIX版本。出于这个原因，它是编写脚本使用在几个不同的版本的UNIX shell。

在本教程中，我们将要覆盖大多数基于传播Borne Shell概念。

## 	Shell 脚本

shell脚本的基本概念是一个命令列表中列出的顺序执行。 ＃是shell脚本注释前面一英镑符号。

条件测试，如值A大于B值，循环我们去通过大量的数据，读取和存储数据的文件和变量的读取和存储数据，该脚本可能包含的功能。

shell脚本和函数都解释。这意味着他们不会被编译。

我们将在接下来的几个教程写了许多脚本。这将是一个简单的文本文件，在其中，我们会把我们所有的命令和其他一些必要的结构，告诉shell环境做什么，什么时候做。

## 	示例脚本：

假设我们创建了一个test.sh脚本。注意：所有的脚本 .sh扩展。添加任何东西到脚本，需要提醒系统正在启动一个shell脚本。例如：

```shell
#!/bin/sh
```

这是告诉系统使用Bourne shell的执行下面的命令。

要创建一个包含这些命令的脚本，然后添加命令：

```shell
#!/bin/sh
pwd
ls
```

## 	Shell 注释

你可以把注释，在你的脚本如下：

文件名:test.sh

```shell
#!/bin/sh

# Script follows here
pwd
ls
```

现在，你的shell脚本，可随时执行如下：

```bash
bash /share/lesson/shell/test.sh
```

如果需要使得此脚本可自己执行，就需要给这个脚本加上执行权限：

```bash
chmod +x test.sh
```

## 	扩展Shell脚本：

Shell脚本有几个必要的结构告诉shell环境做什么，什么时候做。当然，大多数脚本是比上述更加复杂。

shell毕竟，真正的编程语言，完成变量，控制结构，等等。无论脚本变得多么复杂，但是，它仍然是顺序执行的命令的列表。

下面的脚本使用读命令从键盘输入，并将其分配给变量PERSON的值，并最终打印在stdout。

文件名:read.sh								

```shell
#!/bin/sh
# Script follows here

echo "What is your name?"
read PERSON
echo "Hello, $PERSON"
```

下面是运行的脚本示例：

```bash
bash /share/lesson/shell/read.sh
```
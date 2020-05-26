# Shell 特殊变量

以前的教程中说过有关在变量名中使用某些非字母数字字符。这是因为这些字符中使用特殊的Unix变量的名称。这些变量被保留用于特定功能。

例如，$字符表示进程ID号，或PID，在当前shell：

```bash
echo $$
bash
echo $$
exit
echo $$
```

康康

以下下表显示了一些特殊的变量，你可以在你的shell脚本中使用：

| 变量    | 描述                                                         |
| ------- | ------------------------------------------------------------ |
| **$0**  | The filename of the current script.                          |
| **$n**  | These variables correspond to the arguments with which a script was invoked. Here n is a positive decimal number corresponding to the position of an argument (the first argument is $1, the second argument is $2, and so on). |
| **$#**  | The number of arguments supplied to a script.                |
| **$\*** | All the arguments are double quoted. If a script receives two arguments, $* is equivalent to $1 $2. |
| **$@**  | All the arguments are individually double quoted. If a script receives two arguments, $@ is equivalent to $1 $2. |
| **$?**  | The exit status of the last command executed.                |
| **$$**  | The process number of the current shell. For shell scripts, this is the process ID under which they are executing. |
| **$!**  | The process number of the last background command.           |

## 	命令行参数：

该命令行参数 $1, $2, $3,...$9 是位置参数，与0美元指向实际的命令程序

shell脚本，函数和 $1, $2, $3,...$9 作为参数的命令。

下面的脚本使用命令行相关的各种特殊变量：

文件名:variable-special.sh

```shell
#!/bin/sh

echo "File Name: $0"
echo "First Parameter : $1"
echo "First Parameter : $2"
echo "Quoted Values: $@"
echo "Quoted Values: $*"
echo "Total Number of Parameters : $#"
```

```bash
bash /share/lesson/shell/variable-special.sh a b c d
```

康康

## 	特殊参数$ *和$ @：

有特殊的参数，允许在一次访问所有的命令行参数。 $ *和$ @都将相同的行动，除非它们被括在双引号“”。

这两个参数指定的命令行参数，但“$ *”特殊参数需要整个列表作为一个参数之间用空格和“$ @”特殊参数需要整个列表，将其分为不同的参数。

我们可以写下面所示的命令行参数处理数目不详的$ *$ @特殊参数的shell脚本：

文件名:variable-sp.sh

```shell
#!/bin/sh

for TOKEN in $*
do
   echo $TOKEN
done
```

```bash
bash /share/lesson/shell/variable-sp.sh Lucy Liu is 23 Years Old
```

康康

注：在这里 do...done是一种循环，在以后的教程中将介绍。

## 	退出状态：

 $? 变量表示前一个命令的退出状态。

退出状态是一个数值，完成后返回的每一个命令。作为一项规则，大多数命令返回，如果他们不成功退出状态为0，如果他们是成功的。

一些命令返回其他特殊退出状态。例如，一些命令区分类型的错误，并且将返回各种退出值取决于特定类型失效。

成功的命令如下面的例子：

```bash
bash /share/lesson/shell/variable-sp.sh test is test
echo $?
```

```bash
bash /share/lesson/shell/variable-sp-noexist.sh test is test
echo $?
```
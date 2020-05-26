# Shell 替换

## 替换是什么？

Shell当它遇到一个表达式，其中包含一个或多个特殊字符进行替换。

## 例子：

下面的例子，同时使打印取代的其值的变量的值。同时“ ”是一个新行取代：

文件名:substitution1.sh

```shell
#!/bin/sh

a=10
echo -e "Value of a is $a 
"
```

这里-e选项可以解释反斜杠转义。

```bash
bash /share/lesson/shell/substitution1.sh
```

康康

文件名:substitution2.sh

尝试把-e去掉，看看结果

```shell
#!/bin/sh

a=10
echo "Value of a is $a 
"
```

```bash
bash /share/lesson/shell/substitution2.sh
```

康康

您可以使用-n选项来禁用插入新行。

## 	命令替换：

命令替换shell执行的机制，一组给定的命令，然后替换它们的输出在命令。

## 	语法

执行命令替换的命令时，被给定为：

```shell
`command`
```

当执行命令替换，确保您使用的是反引号，不是单引号字符。

## 	例子：

命令替换一般是用一个命令的输出分配给一个变量。下面的例子演示命令替换：

文件名:substitution3.sh

```shell
#!/bin/sh

DATE=`date`
echo "Date is $DATE"

USERS=`who | wc -l`
echo "Logged in user are $USERS"

UP=`date ; uptime`
echo "Uptime is $UP"
```

```bash
bash /share/lesson/shell/substitution3.sh
```

康康

## 	变量替换：

变量替换可使Shell程序员操纵变量的值，根据其状态。

这里是所有可能的替换如下表：

| 格式                | 描述                                                         |
| ------------------- | ------------------------------------------------------------ |
| **${var}**          | Substitue the value of *var*.                                |
| **${var:-word}**    | If *var* is null or unset, *word* is substituted for **var**. The value of *var* does not change. |
| **${var:=word}**    | If *var* is null or unset, *var* is set to the value of **word**. |
| **${var:?message}** | If *var* is null or unset, *message* is printed to standard error. This checks that variables are set correctly. |
| **${var:+word}**    | If *var* is set, *word* is substituted for var. The value of *var* does not change. |

康康

## 	例子：

下面的例子显示各种状态，上述替换：

文件名:substitution4.sh

```shell
#!/bin/sh
echo ${var:-"Variable is not set"}
echo "1 - Value of var is ${var}"

echo ${var:="Variable is not set"}
echo "2 - Value of var is ${var}"

unset var
echo ${var:+"This is default value"}
echo "3 - Value of var is $var"

var="Prefix"
echo ${var:+"This is default value"}
echo "4 - Value of var is $var"

echo ${var:?"Print this message"}
echo "5 - Value of var is ${var}"
```

```bash
bash /share/lesson/shell/substitution4.sh
```

康康
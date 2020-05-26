# Shell 条件语句

在编写shell脚本，有可能是一种情况，当你需要采取一个路径两条路径。所以，需要利用条件语句，让程序作出正确的决策和执行正确的动作。

UNIX Shell支持条件语句，从而根据不同的条件下执行不同的操作。在这里，我们将解释以下两个逻辑条件语句：

- if...else 语句
- case...esac 条件语句

## 	if...else 语句:

if else语句是有用的决策语句，可以用来从一个给定的选项中选择一个选项。

UNIX Shell支持以下形式的if.. else语句：

大部分的 if 语句检查前面的章节中讨论的关系运算符的关系。

###  if...fi语句

if...fi 语句的基本控制语句，它允许Shell有条件作出决定并执行语句。

#### 语法

```shell
if [ expression ]
then
   Statement(s) to be executed if expression is true
fi
```

Shell expression求值。如果结果值是true，给定statement被执行。如果 expression 为false ，则没有语句将不会被执行。大部分的时候，会使用比较操作符决策。

关注对括号和表达之间的空间。这个空间是强制性的，否则语法错误。

如果expression 是一个shell命令，那么它会被假定如此，如果它执行后返回0。如果它是一个布尔表达式，那么返回true。

#### 	示例 

文件名:iffi.sh

```shell
#!/bin/sh

a=10
b=20

if [ $a == $b ]
then
   echo "a is equal to b"
fi

if [ $a != $b ]
then
   echo "a is not equal to b"
fi
```

```shell
bash /share/lesson/shell/iffi.sh
```

康康

###  if...else...fi 语句

if...else...fi 语句是控制语句，它允许下一个表格执行语句 Shell 更可控的方式在两个选择之间作出决定。

####	语法

```shell
if [ expression ]
then
   Statement(s) to be executed if expression is true
else
   Statement(s) to be executed if expression is not true
fi
```

 Shell expression 求值。如果结果值是真实的，给定 statement(s) 被执行。如果表达式为 false，则语句将不会被执行。 

#### 例子：

文件名:ifelsefi.sh

```shell
#!/bin/sh

a=10
b=20

if [ $a == $b ]
then
   echo "a is equal to b"
else
   echo "a is not equal to b"
fi
```

```shell
bash /share/lesson/shell/ifelsefi.sh
```

康康

### if...elif...fi语句

#### 语法

```shell
if [ expression 1 ]
then
   Statement(s) to be executed if expression 1 is true
elif [ expression 2 ]
then
   Statement(s) to be executed if expression 2 is true
elif [ expression 3 ]
then
   Statement(s) to be executed if expression 3 is true
else
   Statement(s) to be executed if no expression is true
fi
```

#### 示例:

文件名:ifeliffi.sh

```shell
#!/bin/sh

a=10
b=20

if [ $a == $b ]
then
   echo "a is equal to b"
elif [ $a -gt $b ]
then
   echo "a is greater than b"
elif [ $a -lt $b ]
then
   echo "a is less than b"
else
   echo "None of the condition met"
fi
```

```shell
bash /share/lesson/shell/ifeliffi.sh
```

康康

## 	case...esac 语句:

if...elif 可以使用多个 elif  语句执行多分支。然而，这并不总是最佳的解决方案，尤其是当所有的分支依赖于一个单一的变量的值。

UNIX Shell支持  case...esac 语句处理正是由于这个情况，它这样做更有效地比 if... elif 语句。

目前只有一种形式的情况下，这里详细case...esac 语句：

UNIX shell 的 case...esac 语句，比较像其他编程语言里的 switch...case ，如C或C + +和Perl等非常相似。



可以使用多个if...elif 语句执行多分支。然而，这并不总是最佳的解决方案，尤其是当所有的分支依赖于一个单一的变量的值。

Shell支持 case...esac 语句处理正是这种情况下，它这样做比 if...elif 语句更有效。

#### 	语法

case...esac 语句基本语法 是为了给一个表达式计算和几种不同的语句来执行基于表达式的值。

解释器检查每一种情况下对表达式的值，直到找到一个匹配。如果没有匹配，默认情况下会被使用。

```shell
case word in
  pattern1)
     Statement(s) to be executed if pattern1 matches
     ;;
  pattern2)
     Statement(s) to be executed if pattern2 matches
     ;;
  pattern3)
     Statement(s) to be executed if pattern3 matches
     ;;
esac
```

这里的字符串字每个模式进行比较，直到找到一个匹配。执行语句匹配模式。如果没有找到匹配，声明退出的情况下不执行任何动作。

没有最大数量的模式，但最小是一个。

当语句部分执行，命令;; 表明程序流程跳转到结束整个 case 语句。和C编程语言的 break 类似。

#### 例1：

文件名:caseesac.sh

```shell
#!/bin/sh

FRUIT="kiwi"

case "$FRUIT" in
   "apple") echo "Apple pie is quite tasty." 
   ;;
   "banana") echo "I like banana nut bread." 
   ;;
   "kiwi") echo "New Zealand is famous for kiwi." 
   ;;
esac
```

```shell
bash /share/lesson/shell/ifeliffi.sh
```

康康

#### 例2：

case语句是一个很好用的命令行参数如下计算：

文件名:easc-parm.sh					

```shell
#!/bin/sh

option="${1}" 
case ${option} in 
   -f) FILE="${2}" 
      echo "File name is $FILE"
      ;; 
   -d) DIR="${2}" 
      echo "Dir name is $DIR"
      ;; 
   *)  
      echo "`basename ${0}`:usage: [-f file] | [-d directory]" 
      exit 1 # Command to come out of the program with status 1
      ;; 
esac 
```

```shell
bash /share/lesson/shell/easc-parm.sh -f /etc/passwd
```

```shell
bash /share/lesson/shell/easc-parm.sh -d /var
```

康康


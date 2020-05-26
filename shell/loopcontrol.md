# Shell 循环控制

到目前为止，我们已经看到了，创建循环和使用循环来完成不同的任务。有时候，你需要停止循环或跳过循环迭代。

在本教程中，您将了解以下两个语句用于控制 Shell 循环：

1. break 语句
2. continue 语句

## 无限循环：

循环有限的生命，他们跳出来，一旦条件是 false 还是 false 取决于循环。

由于所需的条件是不符合一个循环可能永远持续下去。永远不会终止执行一个循环执行无限次数。出于这个原因，这样的循环被称为无限循环。

## 	例子：

下面是一个简单的例子，使用while循环显示数字0到9：

```shell
#!/bin/sh

a=10

while [ $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```

这个循环将永远持续下去，因为常是大于10，它永远不会成为小于10。所以这是无限循环真实的例子。

## 	break语句：

break语句用于终止整个循环的执行，完成后所有行代码break语句的执行。然后，它逐级的代码跟在循环结束。

## 	语法

将用于以下break语句退出循环：

```shell
break
```

将用于以下break语句退出循环：

```shell
break n
```

这里n指定的第n个封闭的循环退出。

## 	例子：

下面是一个简单的例子展示了循环将终止只要一变为5：

文件名:loop-break.sh

```shell
#!/bin/sh

a=0

while [ $a -lt 10 ]
do
   echo $a
   if [ $a -eq 5 ]
   then
      break
   fi
   a=`expr $a + 1`
done
```

```bash
bash /share/lesson/shell/loop-break.sh
```

康康

下面是一个简单的嵌套循环的例子。这个脚本打破两个循环，如果的 var1 等于2 和 var2 等于0：

文件名:loop-break1.sh

```
#!/bin/sh

for var1 in 1 2 3
do
   for var2 in 0 5
   do
      if [ $var1 -eq 2 -a $var2 -eq 0 ]
      then
         break 2
      else
         echo "$var1 $var2"
      fi
   done
done
```

内循环有一个 break 命令与参数2。这表明，如果条件得到满足应该跳出外循环，并最终从内循环跳出。

```bash
bash /share/lesson/shell/loop-break1.sh
```

康康

## 	continue 语句:

continue语句break命令类似，但它会导致当前迭代的循环退出，而不是整个循环。

这种参数是有用的，当一个错误已经发生，但你想尝试执行下一个循环迭代。

## 	语法

```shell
continue
```

和break语句一样，一个整数参数可以给continue命令跳过嵌套循环的命令。

```shell
continue n
```

这里n指定第n个封闭循环 continue 。

## 	例子：

下面的循环利用continue语句返回，并开始处理下一个语句：

文件名:loop-continue.sh

```shell
#!/bin/sh

NUMS="1 2 3 4 5 6 7"

for NUM in $NUMS
do
   Q=`expr $NUM % 2`
   if [ $Q -eq 0 ]
   then
      echo "Number is an even number!!"
      continue
   fi
   echo "Found odd number"
done
```

```bash
bash /share/lesson/shell/loop-continue.sh
```

康康
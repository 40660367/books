# Shell until 循环 			

完美的情况下，你需要执行的一组命令某个条件为真时，while循环执行。

有时候，你需要执行一组命令，直到某个条件为真。

## 语法

```
until command
do
   Statement(s) to be executed until command is true
done
```

这里Shell命令进行评估计算。如果结果值是false，给定语句（s）被执行。如果命令没有语句为true，那么将不执行，程序会跳转到下一行done语句后。

## 例子：

下面是一个简单的例子，它使用直到循环显示数字0到9：

文件名:loop-until.sh

```shell
#!/bin/sh

a=0

until [ ! $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```

```bash
bash /share/lesson/shell/loop-until.sh
```


# Shell while循环 			

while循环，使您能够重复执行一组命令，直到某些条件发生。它通常用于当你需要反复操纵的变量值。

### 语法

```shell
while command
do
   Statement(s) to be executed if command is true
done
```

​	这里Shell命令进行计算。如果结果值是 true，给定语句被执行。如果命令为 false，那么没有语句将不执行，程序将跳转到done语句后的下一行。

### 例子：

使用while循环显示数字0到9,每一次执行这个循环，变量a进行检查，看该值是否小于10。如果a的值小于10，此测试条件的退出状态为0。在这种情况下，当前值的将显示，然后按1递增。
文件名：loop-while.sh

```shell
#!/bin/sh

a=0

while [ $a -lt 10 ]
do
   echo $a
   a=`expr $a + 1`
done
```

```bash
bash /share/lesson/shell/loop-while.sh
```



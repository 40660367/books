# Shell 嵌套循环

所有支持嵌套循环的概念，这意味着可以把一个循环内其他类似或不同的循环。这种嵌套可以去高达无限数量的时间根据需要。

嵌套的while循环和类似的方式，可以嵌套其他循环的基础上的编程要求下面是一个例子：

## 	嵌套while循环：

作为另一个while循环的身体的一部分，这是可以使用一个while循环。

### 	语法：

```shell
while command1 ; # this is loop1, the outer loop
do
   Statement(s) to be executed if command1 is true

   while command2 ; # this is loop2, the inner loop
   do
      Statement(s) to be executed if command2 is true
   done

   Statement(s) to be executed if command1 is true
done
```

### 例子：

这里是循环嵌套一个简单的例子，让我们添加另一个倒计时循环内的循环，数到九：

文件名：loop-nested.sh

```shell
#!/bin/sh

a=0
while [ "$a" -lt 10 ]    # this is loop1
do
   b="$a"
   while [ "$b" -ge 0 ]  # this is loop2
   do
      echo -n "$b "
      b=`expr $b - 1`
   done
   echo
   a=`expr $a + 1`
done
```

```bash
bash /share/lesson/shell/loop-nested.sh
```

康康

注意 echo -n 是如何工作。在这里，-n选项echo ，以避免打印一个新行字符。


# Shell for循环

循环操作项目清单。重复一组命令列表中的每个项目。

## 	语法

```shell
for var in word1 word2 ... wordN
do
   Statement(s) to be executed for every word.
done
```

var是一个变量，word1 到 wordN 是由空格分隔的字符（字）序列的名称。每次for 循环的执行，变量var的值被设置为下一个单词的列表中的字，word1 到 wordN 。

## 	例子：

下面是一个简单的例子，它使用for循环跨越通过给定的数字列表：

文件名:loop-for1.sh

```shell
#!/bin/sh

for var in 0 1 2 3 4 5 6 7 8 9
do
   echo $var
done
```

```bash
bash /share/lesson/shell/loop-for1.sh
```

康康



下面的例子显示所有文件开始 .bash在home目录。执行这个脚本： 						

文件名:loop-for2.sh		

```shell
#!/bin/sh

for FILE in $HOME/.bash*
do
   echo $FILE
done
```

```bash
bash /share/lesson/shell/loop-for2.sh
```

康康
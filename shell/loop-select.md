# Shell select循环			

select 循环提供了一个简单的方法来创建一个编号的菜单，用户可从中选择。它是有用的，当你需要从列表中选择，要求用户选择一个或多个项目。

## 语法

```shell
select var in word1 word2 ... wordN
do
   Statement(s) to be executed for every word.
done
```

var是一个变量，word1 到 wordN是由空格分隔的字符（字）序列的名称。每次for循环的执行，变量var的值被设置为下一个单词的列表中的字，由 word1 到wordN。

对于每一个选择的一组命令将被执行，在循环中。这个循环在ksh，并已被改编成的bash。这不是在sh。

## 例子：

下面是一个简单的例子，让用户选择的首选饮品：

文件名:loop-select.sh

```shell
#!/bin/sh

select DRINK in tea cofee water juice appe all none

do
	case $DRINK in
      tea|cofee|water|all) 
         echo "Go to canteen"
         ;;
      juice|appe)
         echo "Available at home"
      ;;
      none) 
         break 
      ;;
      *) echo "ERROR: Invalid selection" 
      ;;
   esac
done
```

```bash
#您可以更改显示的提示选择循环通过改变变量PS3如下：
PS3="Please make a selection => " ; export PS3

#运行这个文件
bash /share/lesson/shell/loop-select.sh
```

康康
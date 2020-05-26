# Shell 基本运算符

有各种不同的运算符shell都支持。本教程是基于默认shell（Bourne），所以我们要涵盖所有重要的Bourne Shell运算符。

有以下的运算符，我们将要讨论的：

- 算术运算符。
- 关系运算符。
- 布尔运算符。
- 字符串运算符。
- 文件测试操作。

## expr命令

Bourne shell的最初并没有任何机制来执行简单的算术，但它使用外部程序，无论是awk或必须简单的程序expr。

下面是简单的例子，把两个数相加：

文件名: expr.sh

```shell
#!/bin/sh

val="1 + 1"
echo "Total value : $val"

var2=`expr 1+1`
echo "Total value : $var2"

var3=`expr 1 + 1`
echo "Total value : $var3"
```

```bash
bash /share/lesson/shell/expr.sh
```

康康

- 运算符和表达式之间必须有空格，例如1+1是不正确的，因为它应该写成1 + 1。
- ``，称为倒逗号之间应包含完整的表达。

## 	算术运算符：

算术运算符有以下Bourne Shell支持。

假设变量a=10,变量b=20：

| 运算符 | 描述                                                         | 例子                                |
| ------ | ------------------------------------------------------------ | ----------------------------------- |
| +      | Addition - Adds values on either side of the operator        | `expr $a + $b` will give 30         |
| -      | Subtraction - Subtracts right hand operand from left hand operand | `expr $a - $b` will give -10        |
| *      | Multiplication - Multiplies values on either side of the operator | `expr $a * $b` will give 200        |
| /      | Division - Divides left hand operand by right hand operand   | `expr $b / $a` will give 2          |
| %      | Modulus - Divides left hand operand by right hand operand and returns remainder | `expr $b % $a` will give 0          |
| =      | Assignment - Assign right operand in left operand            | a=$b would assign value of b into a |
| ==     | Equality - Compares two numbers, if both are same then returns true. | [ $a == $b ] would return false.    |
| !=     | Not Equality - Compares two numbers, if both are different then returns true. | [ $a != $b ] would return true.     |

这是非常重要的，这里要注意，所有的条件式将放在方括号内，他们身边有一个空格，例如 [ $a == $b ]是正确的，为[$a==$b] 是不正确的。

所有的算术计算，使用长整数。

**示例：**

文件名:operator-arithmetic.sh

```shell
#!/bin/sh

a=10
b=20
val=`expr $a + $b`
echo "a + b : $val"

val=`expr $a - $b`
echo "a - b : $val"

val=`expr $a * $b`
echo "a * b : $val"

val=`expr $b / $a`
echo "b / a : $val"

val=`expr $b % $a`
echo "b % a : $val"

if [ $a == $b ]
then
   echo "a is equal to b"
fi

if [ $a != $b ]
then
   echo "a is not equal to b"
fi
```

```bash
bash /share/lesson/shell/operator-arithmetic.sh
```

康康

## 	关系运算符：

Bourne Shell的支持，关系运算符的具体数值。这些运算符不能使用字符串值，除非它们的值是数字。

例如，运算符将努力检查10和20之间的关系，以及在“10”和“20”，但不是“10”和“21”之间。

假设变量a=10,变量b=20：

| 运算符 | 描述                                                         | 示例                       |
| ------ | ------------------------------------------------------------ | -------------------------- |
| -eq    | Checks if the value of two operands are equal or not, if yes then condition becomes true. | [ $a -eq $b ] is not true. |
| -ne    | Checks if the value of two operands are equal or not, if values are not equal then condition becomes true. | [ $a -ne $b ] is true.     |
| -gt    | Checks if the value of left operand is greater than the value of right operand, if yes then condition becomes true. | [ $a -gt $b ] is not true. |
| -lt    | Checks if the value of left operand is less than the value of right operand, if yes then condition becomes true. | [ $a -lt $b ] is true.     |
| -ge    | Checks if the value of left operand is greater than or equal to the value of right operand, if yes then condition becomes true. | [ $a -ge $b ] is not true. |
| -le    | Checks if the value of left operand is less than or equal to the value of right operand, if yes then condition becomes true. | [ $a -le $b ] is true.     |

这里要注意，所有的条件式将放在方括号内，他们周围有一个空格，这是非常重要的，例如 [ $a <= $b ]是正确的， [$a <= $b]是不正确的。

示例：

文件名：operator-relational.sh

```shell
#!/bin/sh

a=10
b=20

if [ $a -eq $b ]
then
   echo "$a -eq $b : a is equal to b"
else
   echo "$a -eq $b: a is not equal to b"
fi

if [ $a -ne $b ]
then
   echo "$a -ne $b: a is not equal to b"
else
   echo "$a -ne $b : a is equal to b"
fi

if [ $a -gt $b ]
then
   echo "$a -gt $b: a is greater than b"
else
   echo "$a -gt $b: a is not greater than b"
fi

if [ $a -lt $b ]
then
   echo "$a -lt $b: a is less than b"
else
   echo "$a -lt $b: a is not less than b"
fi

if [ $a -ge $b ]
then
   echo "$a -ge $b: a is greater or  equal to b"
else
   echo "$a -ge $b: a is not greater or equal to b"
fi

if [ $a -le $b ]
then
   echo "$a -le $b: a is less or  equal to b"
else
   echo "$a -le $b: a is not less or equal to b"
fi
```

```bash
bash /share/lesson/shell/operator-relational.sh
```

康康

## 	布尔运算：

布尔运算符有以下Bourne Shell的支持。

假设变量一个变量b=10，然后变量b=20：

| 运算符 | 描述                                                         | 示例                                  |
| ------ | ------------------------------------------------------------ | ------------------------------------- |
| !      | This is logical negation. This inverts a true condition into false and vice versa. | [ ! false ] is true.                  |
| -o     | This is logical OR. If one of the operands is true then condition would be true. | [ $a -lt 20 -o $b -gt 100 ] is true.  |
| -a     | This is logical AND. If both the operands are true then condition would be true otherwise it would be false. | [ $a -lt 20 -a $b -gt 100 ] is false. |

示例：

文件名：operator-boolean.sh

```shell
#!/bin/sh

a=10
b=20

if [ $a != $b ]
then
   echo "$a != $b : a is not equal to b"
else
   echo "$a != $b: a is equal to b"
fi

if [ $a -lt 100 -a $b -gt 15 ]
then
   echo "$a -lt 100 -a $b -gt 15 : returns true"
else
   echo "$a -lt 100 -a $b -gt 15 : returns false"
fi

if [ $a -lt 100 -o $b -gt 100 ]
then
   echo "$a -lt 100 -o $b -gt 100 : returns true"
else
   echo "$a -lt 100 -o $b -gt 100 : returns false"
fi

if [ $a -lt 5 -o $b -gt 100 ]
then
   echo "$a -lt 100 -o $b -gt 100 : returns true"
else
   echo "$a -lt 100 -o $b -gt 100 : returns false"
fi
```

```bash
bash /share/lesson/shell/operator-boolean.sh
```

康康

## 	字符串运算符：

有下列字符串运算由Bourne Shell支持。

假设变量a=“abc”和变量b=“efg”：

| 运算符 | 描述                                                         | 例子                     |
| ------ | ------------------------------------------------------------ | ------------------------ |
| =      | Checks if the value of two operands are equal or not, if yes then condition becomes true. | [ $a = $b ] is not true. |
| !=     | Checks if the value of two operands are equal or not, if values are not equal then condition becomes true. | [ $a != $b ] is true.    |
| -z     | Checks if the given string operand size is zero. If it is zero length then it returns true. | [ -z $a ] is not true.   |
| -n     | Checks if the given string operand size is non-zero. If it is non-zero length then it returns true. | [ -z $a ] is not false.  |
| str    | Check if str is not the empty string. If it is empty then it returns false. | [ $a ] is not false.     |

示例：

文件名：operator-string.sh

```shell
#!/bin/sh

a="abc"
b="efg"

if [ $a = $b ]
then
   echo "$a = $b : a is equal to b"
else
   echo "$a = $b: a is not equal to b"
fi

if [ $a != $b ]
then
   echo "$a != $b : a is not equal to b"
else
   echo "$a != $b: a is equal to b"
fi

if [ -z $a ]
then
   echo "-z $a : string length is zero"
else
   echo "-z $a : string length is not zero"
fi

if [ -n $a ]
then
   echo "-n $a : string length is not zero"
else
   echo "-n $a : string length is zero"
fi

if [ $a ]
then
   echo "$a : string is not empty"
else
   echo "$a : string is empty"
fi
```

```bash
bash /share/lesson/shell/operator-string.sh
```

康康

注意：运算符和表达式之间必须有空格，例如2+2是不正确的，因为它应该写成2 + 2.

## 	文件测试操作：

有以下是操作测试Unix文件相关联的各种属性。

假设一个的变量文件保存现有文件名“test”，其大小为100字节，有读，写和执行权限：

| 操作符  | 描述                                                         | 示例                      |
| ------- | ------------------------------------------------------------ | ------------------------- |
| -b file | Checks if file is a block special file if yes then condition becomes true. | [ -b $file ] is false.    |
| -c file | Checks if file is a character special file if yes then condition becomes true. | [ -b $file ] is false.    |
| -d file | Check if file is a directory if yes then condition becomes true. | [ -d $file ] is not true. |
| -f file | Check if file is an ordinary file as opposed to a directory or special file if yes then condition becomes true. | [ -f $file ] is true.     |
| -g file | Checks if file has its set group ID (SGID) bit set if yes then condition becomes true. | [ -g $file ] is false.    |
| -k file | Checks if file has its sticky bit set if yes then condition becomes true. | [ -k $file ] is false.    |
| -p file | Checks if file is a named pipe if yes then condition becomes true. | [ -p $file ] is false.    |
| -t file | Checks if file descriptor is open and associated with a terminal if yes then condition becomes true. | [ -t $file ] is false.    |
| -u file | Checks if file has its set user id (SUID) bit set if yes then condition becomes true. | [ -u $file ] is false.    |
| -r file | Checks if file is readable if yes then condition becomes true. | [ -r $file ] is true.     |
| -w file | Check if file is writable if yes then condition becomes true. | [ -w $file ] is true.     |
| -x file | Check if file is execute if yes then condition becomes true. | [ -x $file ] is true.     |
| -s file | Check if file has size greater than 0 if yes then condition becomes true. | [ -s $file ] is true.     |
| -e file | Check if file exists. Is true even if file is a directory but exists. | [ -e $file ] is true.     |

示例:

文件名：operator-file.sh

```shell
#!/bin/sh

file="/share/lesson/shell/operator-file.sh"

if [ -r $file ]
then
   echo "File has read access"
else
   echo "File does not have read access"
fi

if [ -w $file ]
then
   echo "File has write permission"
else
   echo "File does not have write permission"
fi

if [ -x $file ]
then
   echo "File has execute permission"
else
   echo "File does not have execute permission"
fi

if [ -f $file ]
then
   echo "File is an ordinary file"
else
   echo "This is sepcial file"
fi

if [ -d $file ]
then
   echo "File is a directory"
else
   echo "This is not a directory"
fi

if [ -s $file ]
then
   echo "File size is zero"
else
   echo "File size is not zero"
fi

if [ -e $file ]
then
   echo "File exists"
else
   echo "File does not exist"
fi
```

```bash
bash /share/lesson/shell/operator-file.sh
```

与使用stat命令查看该文件信息，两者进行对比

```bash
stat /share/lesson/shell/operator-file.sh
```

康康


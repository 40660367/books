# Shell 输入/输出重定向

大多数[Unix系统命令从终端的输入和发送所产生的输出返回到您的终端。一个命令通常从一个地方叫标准输入，默认情况下，这恰好是你的终端读取输入。

同样，一个命令通常写入其输出到标准输出，这也是默认情况下，从你的终端。

## 	输出重定向

通常用于标准输出命令的输出可以很容易地转移到一个文件中代替。这种能力被称为输出重定向：

如果记号> file附加任何命令，通常写入其输出到标准输出，该命令的输出将被写入文件，而不是你的终端：

检查使用 who 命令，将完整的输出重定向命令在用户文件。

```bash
who > users
```

请注意，没有输出出现在终端中。这是因为输出已被重定向到指定的文件从默认的标准输出设备（终端）。如果想检查用户的文件，然后将完整的内容：

```bash
cat users
```

如果命令输出重定向到一个文件，该文件已经包含了一些数据，这些数据将会丢失。考虑这个例子：

```bash
echo line 1 > users
cat users
```

您可以使用>>运算符将输出附加在现有的文件如下：

```bash
echo line 2 >> users
cat users
```

## 	输入重定向

正如一个命令的输出可以被重定向到一个文件中，所以可以输入一个命令从文件重定向。作为不是字符>用于输出重定向，小于字符<用于重定向一个命令的输入。

通常需要的命令，他们从标准输入的输入可以有自己的这种方式从文件输入重定向。例如，上面生成的文件中的用户的数量来计算的行，可以执行如下命令：

```bash
wc -l users
```

在这里，它产生的输出2行。可以指望的文件中的行数 wc 命令的标准输入重定向用户从文件：

```bash
wc -l < /etc/passwd
```

请注意，在由两种形式的wc命令产生的输出是有区别的。在第一种情况下，该文件的用户的名称列出的行数，在第二种情况下，它不是。

在第一种情况下，wc 知道，它是用户从文件读取输入。

在第二种情况下，只知道它是从标准输入读取输入，所以它不显示文件名。

## 	Here 文档:

 here document 是用来输入重定向到一个交互式shell脚本或程序。

在一个shell脚本中，我们可以运行一个交互式程序，无需用户操作，通过提供互动程序或交互式shell脚本所需的输入。

这里的文件的一般形式是：

```
command << delimiter
document
delimiter
```

这里的 shell 解释<<操作指令读取输入，直到它找到含有指定分隔符线。所有输入行的行分隔符，然后送入标准输入的命令。

分界符告诉shell 这里文件已完成。没有它，shell 不断的读取输入。分隔符必须是一个字不包含空格或制表符。

以下是输入命令wc -1 进行计数的行的总数：

```bash
wc -l << EOF
	This is a simple lookup program 
	for good (and bad) restaurants
	in Cape Town.
EOF
```

## 	丢弃输出

有时会需要执行命令，但不想显示在屏幕上的输出。在这种情况下，可以丢弃的输出重定向到文件 /dev/null:

```
command > /dev/null
```

这里 command 是要执行的命令的名字。文件/dev/null 是一个特殊的文件自动放弃其所有的输入。

同时要放弃一个命令的输出和错误输出，使用标准的重定向到STDOUT 到 STDERR重定向：		

```
command > /dev/null 2>&1
```

在这里，2代表stderr和1代表STDOUT。可以上显示一条消息到STDERR 到 STDERR重定向标准输入到如下：

```bash
echo message 1>&2
```

## 	重定向命令

以下是命令，可以使用重定向的完整列表：

| 命令        | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| pgm > file  | Output of pgm is redirected to file                          |
| pgm < file  | Program pgm reads its input from file.                       |
| pgm >> file | Output of pgm is appended to file.                           |
| n > file    | Output from stream with descriptor n redirected to file.     |
| n >> file   | Output from stream with descriptor n appended to file.       |
| n >& m      | Merge output from stream n with stream m.                    |
| n <& m      | Merge input from stream n with stream m.                     |
| << tag      | Standard input comes from here through next tag at start of line. |
| \|          | Takes output from one program, or process, and sends it to another. |

需要注意的是文件描述符0是正常标准输入（STDIN），1是标准输出（STDOUT），标准错误输出（STDERR）。
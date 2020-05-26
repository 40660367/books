# Shell 引用			

## 元字符：

UNIX Shell提供各种元字符有特殊的意义，同时利用他们在任何Shell脚本，并导致终止一个字，除非引用。

举个例子： ?匹配一个单一的系统字符，而列出文件中的目录和*匹配多个字符。下面是一个清单shell特殊字符（也称为元字符）：

```shell
* ? [ ] ' "  $ ; & ( ) | ^ < > new-line space tab
```

它与前可能被引用的字符（例如，放置自身） .

###  例子：

下面的例子，显示了如何打印  a * 或 a ?:

文件名:quoting1.sh

```shell
#!/bin/sh

echo Hello; Word
```

```bash
bash /share/lesson/shell/quoting1.sh
```

康康



现在，让我们尝试使用带引号的字符：

文件名:quoting2.sh

$符号同样也是一个元字符，所以它必须被引用，以避免特殊处理：

```
#!/bin/sh
echo "Hello; Word"
echo "I have $1,000"
```

```bash
bash /share/lesson/shell/quoting2.sh
```

康康



以下四种形式引用：

| 引用             | 描述                                                         |
| ---------------- | ------------------------------------------------------------ |
| **Single quote** | All special characters between these quotes lose their special meaning. |
| **Double quote** | Most special characters between these quotes lose their special meaning with these exceptions:  			 				 					$ 				 					` 				 					$ 				 					' 				 					" |
| **Backslash**    | Any character immediately following the backslash loses its special meaning. |
| **Back Quote**   | Anything in between back quotes would be treated as a command and would be executed. |

## 	单引号：

考虑以下echo命令，其中包含许多特殊的shell字符：

```bash
echo <-$1,000.**?>; [y|n](update)
```

将在每个特殊字符前的反斜杠是繁琐的，使该行难以阅读：

有一个简单的方法来引用一大组字符。将一个单引号（'）的开头和结尾的字符串：

```bash
echo '<-$1,000.**?>; [y|n](update)'
```

单引号内的任何字符均以一个反斜杠，就好像是在前面的每个字符。所以，现在这个echo命令将显示正确。

如果要输出一个字符串内出现一个单引号，你不应该把单引号内的整个字符串，而不是对子进行使用反斜杠（）如下：

```bash
echo 'It\'s Shell Programming'
```

## 双引号：

```bash
VAR=Lucy
echo '$VAR owes <-$1,000.**>; [ as of (`date +%m/%d`) ]'
```

所以这不是你想显示什么。很明显，**单引号防止变量替换。**

如果想替换的变量值和倒置逗号如预期那样运作，那么就需要在双引号命令如下：

```bash
VAR=Lucy
echo "$VAR owes <-$1,000.**>; [ as of (`date +%m/%d`) ]"
```

双引号带走下列以外的所有字符的特殊含义：

- $ 参数替代。
- 用于命令替换的反引号。
- $ 使字面美元标志。
- ` 使文字反引号。
- " 启用嵌入式双引号。
-  启用嵌入式反斜杠。
- 所有其他字符是文字（而不是指定）。

单引号内的任何字符均以一个反斜杠，就好像是在前面的每个字符。所以，现在这个echo命令将显示正确。

如果要输出一个字符串内出现一个单引号，不应该把单引号内的整个字符串，而不是对子进行使用反斜杠（）如下：

## 	反引号：

把反引号之间的任何shell命令将执行命令

### 语法

下面是一个简单的语法，把反引号之间的任何Shell命令：

### 语法

```bash
var=`command`
```

### 例子：

执行date命令，产生的结果将被存储在 DATA 变量。			 								

```bash
DATE=`date`
echo "Current Date: $DATE"
```
与上一个例子类似
```bash
BINS=`ls /usr/bin`
echo $BINS
```


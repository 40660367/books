# Go语言 常量(const)

常量是指程序在执行过程中可能不会改变的固定值。 这些固定值也称为文字。

常量可以是任何基本数据类型，如整数常量，浮点常量，字符常量或字符串常量。 还有枚举常量。

**常量**一般会被编译器视为常规变量，只是它们的值不能在定义之后被修改。


## 整数文字

整数文字可以是十进制，八进制或十六进制常数。 前缀指定基数：前缀是`0x`或`0X`为十六进制，前缀是`0`的为八进制，十进制的前缀则无任何内容。

整数文字还可以有一个后缀，它是`U`和`L`的组合，分别用于`unsigned`和`long`。后缀可以是大写或小写，可以是任意顺序。

这里是一些有效的整数文字的例子：

```go
212         /* 合法 */
215u        /* 合法 */
0xFeeL      /* 合法 */
078         /* 非法: 8 is not an octal digit */
032UU       /* 非法: cannot repeat a suffix */
```

以下是其他各种类型的整数文字的示例：

```go
85         /* decimal */
0213       /* octal */
0x4b       /* hexadecimal */
30         /* int */
30u        /* unsigned int */
30l        /* long */
30ul       /* unsigned long */
```

## 浮点文字

浮点文字有整数部分，小数点，小数部分和指数部分。您可以以十进制形式或指数形式来表示浮点文字。
在使用十进制形式表示时，必须包括小数点，指数或两者，并且在使用指数形式表示时，必须包括整数部分，小数部分或两者。带符号的指数由`e`或`E`引入。

下面是一些浮点文字的示例：

```go
3.14159       /* 合法 */
314159E-5L    /* 合法 */
510E          /* 非法: incomplete exponent */
210f          /* 非法: no decimal or exponent */
.e55          /* 非法: missing integer or fraction */
Go
```

### 转义序列

Go中有一些字符，当它们前面有一个反斜杠，它们将具有特殊的意义，它们用于表示类似换行符(`\n`)或制表符(`\t`)。 这里，有一些这样的转义序列代码的列表：

| 转义序列  | 含义                   |
| --------- | ---------------------- |
| `\\`      | `\`字符                |
| `\'`      | `'`字符                |
| `\"`      | `"`字符                |
| `\?`      | `?`字符                |
| `\a`      | 警报或响铃             |
| `\b`      | 退格                   |
| `\f`      | 换页                   |
| `\n`      | 新行                   |
| `\r`      | 回车                   |
| `\t`      | 水平制表格             |
| `\v`      | 水直制表格             |
| `\ooo`    | 八位数字一到三位数     |
| `\xhh...` | 一位或多位的十六进制数 |

**以下是显示几个转义序列字符的示例：**

文件名:escape.go

```go
package main

import "fmt"

func main() {
   fmt.Printf("Hello\tWorld!")
}
```

```bash
go run /share/lesson/go/escape.go
```

康康

## 字符串文字

字符串文字或常量用双引号`""`括起来。字符串包含与字符文字类似的字符：纯字符，转义序列和通用字符。可以使用字符串文字将长行拆分为多个行，并使用空格分隔它们。

这里是一些字符串文字的例子。下面这三种形式都是相同的字符串。

```go
"hello, dear"

"hello, \

dear"

"hello, " "d" "ear"
```

### const关键字

可以使用`const`前缀来声明具有特定类型的常量，如下所示：

```go
const variable type = value;
```

下面的例子详细解释：

文件名:const.go

```go
package main

import "fmt"

func main() {
   const LENGTH int = 10
   const WIDTH int = 5   
   var area int

   area = LENGTH * WIDTH
   fmt.Printf("value of area : %d", area) 
   fmt.Printf("\n")  
}
```

```bash
go run /share/lesson/go/const.go
```

康康

> 注：以大写字母来定义常量是一个很好的编程习惯。
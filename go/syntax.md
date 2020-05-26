# Go语言 基础语法

您已经看到Go程序的基本结构，因此很容易理解Go编程语言的其他基本构建块。

## Go语言中的标记

Go程序是由各种标记组成的，标记可以是关键字，标识符，常量，字符串文字或符号。例如，以下Go语句由六个标记组成：

```go
fmt.Println("Hello, World!")
```

每个标记单独表示为：

```go
fmt
.
Println
(
"Hello, World!"
)
```

## 行分隔符

在Go程序中，行分隔符键是语句终止符。 也就是说，每个单独的语句不需要特殊的分隔符如：`;` ，也不需要像在C编译器放置`;` 作为语句终止符以指示一个逻辑实体的结束。

例如，以下是两个不同的语句：

```go
fmt.Println("Hello, World!")
fmt.Println("I am in Go Programming World!")
```

## 注释

注释就类似在Go程序中帮助文本，并且它们被编译器忽略。 它们以`/*`开始，并以字符`*/`结尾，如下所示：

```go
/* This is Go Hello World program! */
```

不能在注释中包含注释，并且不能在字符串或字符文字中出现。

## 标识符

Go标识符是用于标识变量，函数或任何其他用户定义项目的名称。标识符以字母`A`到`Z`或`a`到`z`或下划线`_`开头，后跟零个或多个字母，下划线和数字(`0`到`9`)组成。

标识符 = 字母 {字母 | unicode数字}。

Go不允许在标识符中使用标点符号，例如`@`, `$` 和 `%`。 Go是一种区分大小写的编程语言。 因此，`Manpower`和`manpower`在Go中是两个不同的标识符。以下是一些可接受(合法)的标识符示例：

```go
mahesh   kumar   abc   move_name   a_123
myname50   _temp   j   a23b9   retVal
```

## 关键词

以下列表显示Go中的保留字。这些保留字不能用作常量或变量或任何其他标识符名称。

| break    | default     | func   | interface | select |
| -------- | ----------- | ------ | --------- | ------ |
| case     | defer       | go     | map       | struct |
| chan     | else        | goto   | package   | switch |
| const    | fallthrough | if     | range     | type   |
| continue | for         | import | return    | var    |

## Go语言的空白行

只包含空格的行，或者可能带有注释，被称为空行，Go编译器完全忽略它。

空白行是用于描述空格，制表符，换行符和注释的术语。 空格将语句的一部分与另一个语句隔开，并使编译器能够识别语句中的一个元素(例如`int`)结束和下一个元素开始的位置。因此，在下面的语句中：

```go
var age int;
```

在`int`和`age`之间必须至少有一个空格字符(通常是一个空格)，以便编译器能够区分它们。 另一方面，如以下语句中：

```go
fruit = apples + oranges;   // get the total fruit
```

在 `fruit` 和`=`之间，或在`=`和`apples`之间可不需要空格字符，但是如果想要增加可读性，那么可以随意添加。
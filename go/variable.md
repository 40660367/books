# Go语言 变量(variable)

变量只是给程序可以操作的存储区域的名字。Go中的每个变量都有一个特定的类型，它决定了变量的内存大小和布局; 可以存储在存储器内的值的范围; 以及可以应用于该变量的一组操作。

变量的名称可以由字母，数字和下划线字符组成。它必须以字母或下划线开头。大写和小写字母是不同的名称，因为Go是区分大小写的。基于前一章中解释的基本类型，有以下基本变量类型：

| 类型    | 描述                                             |
| ------- | ------------------------------------------------ |
| byte    | 通常为单个八位字节(一个字节)，这是一个字节类型。 |
| int     | 机器最自然的整数大小。                           |
| float32 | 单精度浮点值。                                   |

Go编程语言还允许定义各种其他类型的变量，我们将在后续章节中介绍如枚举，指针，数组，结构，联合等。在本章中，只学习研究基本变量类型。

## Go变量定义


变量定义意味着告诉编译器为变量创建存储的位置和大小。变量定义需要指定数据类型，并包含该类型的一个或多个变量的列表，如下所示：

```go
var variable_list optional_data_type;
```

这里，`optional_data_type`是有效的Go数据类型，包括：`byte`，`int`，`float32`，`complex64`，`boolean`等或任何用户定义的对象等，并且`variable_list`可以包括一个或多个用逗号分隔的标识符变量名称。一些有效的声明如下所示：

```go
var  i, j int;
var  c, byte;
var  f, salary float32;
d = 42;
```

`var i，j，k;`这一行，声明和定义变量`i`，`j`和`k`; 它指示编译器创建名称为`i`，`j`和`k`的类型为`int`的变量。

变量可以在它们的声明时初始化(赋值一个初始值)。变量的类型由编译器基于传递给它的值自动判断。初始化器由一个等号和一个常量表达式组成，如下所示：

```go
variable_name = value;
```

一些例子是：

```go
d = 3, f = 5;    // declaration of d and f. Here d and f are int
```

对于没有初始化器的定义：具有静态存储的变量使用`nil`隐式初始化(所有字节都为`0`); 所有其他变量的初始值为其数据类型的零值。

## 静态类型声明

静态类型变量声明为编译器提供了保证，即一个给定类型和名称的变量，以便编译器继续进行进一步编译，而不需要有关变量的完整详细信息。变量声明仅在编译时有其意义，编译器需要在链接程序时按实际的变量声明执行。

### 示例

尝试下面的示例，其中变量已声明为一个类型，并已在`main`函数中定义和初始化：

文件名:printtype.go

```go
package main

import "fmt"

func main() {
   var x = "go language"
   var y = 100
   fmt.Println(x)
   fmt.Printf("x is of type %T\n", x)
   fmt.Printf("y is of type %T\n", y)
}
```

```bash
go run /share/lesson/go/printtype.go
```

康康

## 动态类型声明/类型推断

动态类型变量声明要求编译器根据传递给它的值来解释变量的类型。但编译器并不需要指定一个变量为静态类型。

### 示例

看看下面的示例，这里的变量声明没有任何类型，并已在`main`函数中定义和初始化。注意，在类型推断的情况下，已经将变量`y`初始化为 `:=` 运算符，其中`x`使用`=`运算符初始化。

文件名:printtype1.go

```go
package main

import "fmt"

func main() {
   var x float64 = 20.0

   y := 42 
   fmt.Println(x)
   fmt.Println(y)
   fmt.Printf("x is of type %T\n", x)
   fmt.Printf("y is of type %T\n", y)    
}
```

```shell
go run /share/lesson/go/printtype1.go
```

康康

## 混合变量声明

不同类型的变量可以在一次声明中使用类型推断。

### 示例

文件名:printtype2.go

```go
package main

import "fmt"

func main() {
   var a, b, c = 3, 4, "foo"  

   fmt.Println(a)
   fmt.Println(b)
   fmt.Println(c)
   fmt.Printf("a is of type %T\n", a)
   fmt.Printf("b is of type %T\n", b)
   fmt.Printf("c is of type %T\n", c)
}
```

```
go run /share/lesson/go/printtype2.go
```

康康

### Go中的左值和右值：

Go中有两种表达式：

1. 左值(`lvalue`)：引用存储器位置的表达式称为“`lvalue`”表达式。左值可能出现在作业的左侧或右侧。
2. 右值(`rvalue`)：术语**右值**(`rvalue`)是指存储在内存中某个地址的数据值。右值是不能赋值给它的值的表达式，右值只可能出现在赋值的右侧而不是左侧。

变量是左值，因此可能出现在赋值的左侧。数字文字是右值，因此不可能分配，也不能出现在左侧。以下是有效的语句：

```go
x = 20.0
```

但以下不是有效的语句，并会生成编译时错误：

```go
10 = 20
```
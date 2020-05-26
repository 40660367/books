# Go语言 指针(pointer)

Go中的指针是很容易学习，也是比较有趣的。

一些Go编程任务使用指针更容易执行，并且不使用指针不能执行其他任务，例如通过引用调用。 因此，有必要学习指针，成为一个完美的Go程序员。现在我们开始通过简单和容易的步骤来学习Go编程中的指针。


如众所知，每个变量都是一个内存位置，每个内存位置都有其定义的地址，可以使用”和”号(&)运算符来访问它，这个运算符表示内存中的地址。参考下面的例子，它将打印定义的变量的地址：

文件名:pointer.go

```go
package main

import "fmt"

func main() {
   var a int = 10   

   fmt.Printf("Address of a variable: %x\n", &a  )
}
```

```shell
go run /share/lesson/go/pointer.go
```

康康

所以要明白什么是内存地址，以及如何访问它，基础的概念讲到这里就结束了。现在让我们看看什么是指针。

## 什么是指针？

指针是一个变量，其值是另一个变量的地址，即存储器位置的直接地址。类似变量或常量一样，必须要先声明一个指针，然后才能使用它来存储任何变量地址。指针变量声明的一般形式是：

```go
var var-name *var-type
```

这里，`var-type`是指针的基类型; 它必须是有效的Go数据类型，`var-name`是指针变量的名称。用于声明指针的星号(`*`)与用于乘法的星号相同。但是，在此语句中，星号(`*`)用于将变量指定为指针。以下是有效的指针声明：

```go
var ip *int        /* pointer to an integer */
var fp *float32    /* pointer to a float */
```

所有指针的值的实际数据类型(无论是整数，浮点数还是其他数据类型)都是相同的，它表示内存地址的长十六进制数。不同数据类型的指针的唯一区别是指针所指向的是变量或常量的数据类型。

## 如何使用指针？

有几个重要的操作，将非常频繁地使用指针来实现。

- 定义一个指针变量
- 将一个变量的地址赋值给一个指针 
- 最后访问指针变量中可用地址的值

这是通过使用一元运算符`*`来返回位于操作数指定的地址的变量的值。下面的例子使用这些操作：

文件名:pointer-address.go

```go
package main

import "fmt"

func main() {
   var a int= 20   /* actual variable declaration */
   var ip *int        /* pointer variable declaration */

   ip = &a  /* store address of a in pointer variable*/

   fmt.Printf("Address of a variable: %x\n", &a  )

   /* address stored in pointer variable */
   fmt.Printf("Address stored in ip variable: %x\n", ip )

   /* access the value using the pointer */
   fmt.Printf("Value of *ip variable: %d\n", *ip )
}
```

```bash
go run /share/lesson/go/pointer-address.go
```

康康

## 在Go语言中的nil指针

Go编译器为指针变量分配一个`Nil`值，以防指针没有确切的地址分配。这是在变量声明的时候完成的。指定为`nil`值的指针称为`nil`指针。

`nil`指针是在几个标准库中定义的值为零的常量。参考下面的程序：

文件名:pointer-nil.go

```go
package main

import "fmt"

func main() {
   var  ptr *int
   fmt.Printf("The value of ptr is : %x\n", ptr  )
}
```

当上面的代码编译和执行时，它产生结果如下：

```bash
go run /share/lesson/go/pointer-nil.go
```

在大多数操作系统上，程序不允许访问地址`0`处的内存，因为该内存是由操作系统保留的。 然而，存储器地址`0`具有特殊意义; 它表示指针不打算指向可访问的存储器位置。但是按照惯例，如果指针包含`nil`(零)值，则假设它不指向任何东西。

要检查是否为`nil`指针，可以使用`if`语句，如下所示：

```go
if(ptr != nil)     /* succeeds if p is not nil */
if(ptr == nil)    /* succeeds if p is null */
```

## 有关指针的详细信息

指针有很多但很简单的概念，它们对Go编程非常重要。下面几个重要的指针概念，对于Go程序员应该要清楚：

| 概念           | 描述                                                         |
| -------------- | ------------------------------------------------------------ |
| Go指针数组     | 可以定义数组来保存一些指针                                   |
| Go指针的指针   | Go允许有指针指向指针等等                                     |
| 传递指针到函数 | 通过引用或地址传递参数都允许被调用函数在调用函数中更改传递的参数。 |
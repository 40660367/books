# Go语言 函数(function)


函数是一组执行任务的语句。 每个Go程序至少有一个函数，也就是`main()`函数，所有最小的程序可以定义附加的函数。

可以将代码分成单独的函数。如何在不同的函数之间划分代码取决于程序员，但在逻辑上，通常每个函数执行一个特定的任务。

函数声明告诉编译器有关函数的名称，返回类型和参数。 函数定义提供了函数的实际主体。

Go标准库提供了许多内置的函数，在编写程序时可以调用。 例如，函数`len()`接受各种类型的参数，并返回类型的长度。 例如，如果一个字符串传递给它，它将返回字符串的字节长度，如果一个数组传递给它，它将返回数组长度，也就是数组中的元素数量。

函数有各种不同的叫法(名称)，如**方法**或**子例程**或**过程**等。

### 定义函数

Go编程语言中函数定义的一般形式如下：

```go
func function_name( [parameter list] ) [return_types]
{
   body of the function
}
```

Go编程语言中的函数定义包括函数头和函数体。这里是一个函数的所有部分：

1. **func**开始一个函数的声明。
2. **函数名称**(function_name)：这是函数的名称。函数名和参数列表一起构成函数签名。
3. **参数**：参数类似于占位符。 调用函数时，将一个值传递给参数。 此值称为实际参数或参数。 参数列表指的是函数的参数的类型，顺序和数量。 参数是可选的; 即，函数可以不用包含参数。
4. 返回类型：函数可以有返回值列表。`return_types`是函数返回的值的数据类型的列表。某些函数执行所需的操作，而不用(无)返回值。在这种情况下，`return_type`就不是必需的。
5. 函数体：函数体包含定义函数的功能的语句集合。

### 示例

以下是一个名为`max()`的函数的源代码。此函数使用两个参数`num1`和`num2`，并返回这两个参数的最大值：

```go
/* function returning the max between two numbers */
func max(num1, num2 int) int
{
   /* local variable declaration */
   result int

   if (num1 > num2) {
      result = num1
   } else {
      result = num2
   }
   return result 
}
```

### 调用函数

在创建Go函数时，需要给出函数的定义。要使用函数，必须调用该函数来执行定义的任务。
当程序调用一个函数时，程序控制转移到被调用的函数。 被调用函数执行定义的任务，并且在返回语句执行时或者到达函数结束闭包括时，它返回程序控制回到主程序。

要调用函数，只需要传递所需的参数以及函数名称，如果函数返回一个值，那么可以存储返回的值。 例如：

文件名:function.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var a int = 100
   var b int = 200
   var ret int

   /* calling a function to get max value */
   ret = max(a, b) // 存储返回的值到 ret 变量中

   fmt.Printf( "Max value is : %d\n", ret )
}

/* function returning the max between two numbers */
func max(num1, num2 int) int {
   /* local variable declaration */
   var result int

   if (num1 > num2) {
      result = num1
   } else {
      result = num2
   }
   return result 
}
```

在这里保持`max()`函数与`main()`函数一起编译源代码。

```bash
go run /share/lesson/go/function.go
```

康康

### 从函数返回多个值

Go函数可以返回多个值。 例如：

文件名:function-return.go

```go
package main

import "fmt"

func swap(x, y string) (string, string) {
   return y, x
}

func main() {
   a, b := swap("Hippo", "Curry")
   fmt.Println(a, b)
}
```

```bash
go run /share/lesson/go/function-return.go
```

康康

### 函数参数

如果函数要使用参数，它必须声明接受参数值的变量。这些变量称为函数的形式参数。
形式参数与函数内部的其他局部变量一样，在进入函数时创建，在退出时被销毁。
在调用函数时，有两种方法可以将参数传递给函数：

| 调用类型   | 描述                                                         |
| ---------- | ------------------------------------------------------------ |
| [按值调用](./function-ref-by-value.html) | 此方法将参数的实际值复制到函数的形式参数中。 在这种情况下，对函数中的参数所做的更改不会影响参数的值，退出函数后参数的值还是原值。 |
| [按引用调用](./function-ref-by-reference.html) | 此方法将参数的地址复制到形式参数中。在函数内部，地址用于访问在调用中使用的实际参数。这意味着对参数所做的更改会影响参数的值，退出函数后参数的值是函数内部被修改后的值。 |

默认情况下，Go使用按值调用来传递参数。一般来说，函数中的代码不能改变用于调用函数的参数，所以调用`max()`函数使用的也是相同的方法。

### 函数用法

| 函数用法       | 描述                                       |
| -------------- | ------------------------------------------ |
| [函数作为值使用](./function-as-value.html) | 函数可以即时创建，并且可以用作值。         |
| [函数闭包](./function-closure.html)       | 函数闭包是匿名函数，可以在动态规划中使用。 |
| [方法](./function-method.html)           | 方法是使用接收器的特殊函数。               |
# Go语言 变量作用域(scope)	

任何编程中的作用域是程序的一个区域，它定义了变量可以存在，并且在超出该变量范围不能被访问。 在Go编程语言中有三个可以声明变量的地方：

1. 在函数或块中声明的为局部变量。
2. 在所有函数之外声明的变量称为全局变量。
3. 在定义函数参数变量时，称为形参。


下面来看看什么是局部变量和全局变量，以及什么是形式参数。

## 局部变量

在函数或块中声明的变量称为局部变量。 它们只能由在函数或代码块中的语句使用。局部变量对于它们自己以外的函数是未知的。以下是使用局部变量的示例。这里所有的变量`a`，`b`和`c`都是`main()`函数的局部变量。

文件名:scope-local.go

```go
package main

import "fmt"

func main() {
   /* local variable declaration */
   var a, b, c int 

   /* actual initialization */
   a = 10
   b = 20
   c = a + b

   fmt.Printf ("value of a = %d, b = %d and c = %d\n", a, b, c)
}
```

```shell
go run /share/lesson/go/scope-local.go
```

康康

## 全局变量

全局变量在函数之外定义，通常在程序之上。 全局变量将在程序的整个生命周期中都有保持它的值，并且可以在程序定义的任何函数内访问到它们。

全局变量可以通过任何函数访问。 也就是说，一个全局变量可以声明后在整个程序中使用。 以下是使用全局变量和局部变量的示例：

文件名:scope-global.go

```go
package main

import "fmt"

/* global variable declaration */
var g int

func main() {

   /* local variable declaration */
   var a, b int

   /* actual initialization */
   a = 10
   b = 20
   g = a + b

   fmt.Printf("value of a = %d, b = %d and g = %d\n", a, b, g)
}
```

```shell
go run /share/lesson/go/scope-local.go
```

康康

在程序中，局部变量和全局变量的名称可以相同，但函数内部的局部变量的值将优先(也就是说局部变量会覆盖全局变量)。 以下是一个示例：

文件名:scope-name.go

```go
package main

import "fmt"

/* global variable declaration */
var g int = 20

func main() {
   /* local variable declaration */
   var g int = 10

   fmt.Printf ("value of g = %d\n",  g)
}
```

```shell
go run /share/lesson/go/scope-name.go
```

康康

## 形式参数

函数参数 - 形式参数在函数中会作为局部变量，它们将优先于全局变量。以下是一个示例：

文件名:scope-parm.go

```go
package main

import "fmt"

/* global variable declaration */
var a int = 20;

func main() {
   /* local variable declaration in main function */
   var a int = 10
   var b int = 20
   var c int = 0

   fmt.Printf("value of a in main() = %d\n",  a);
   c = sum( a, b);
   fmt.Printf("value of c in main() = %d\n",  c);
}

/* function to add two integers */
func sum(a, b int) int {
   fmt.Printf("value of a in sum() = %d\n",  a);
   fmt.Printf("value of b in sum() = %d\n",  b);

   return a + b;
}
```

```shell
go run /share/lesson/go/scope-parm.go
```

康康

## 初始化局部变量和全局变量

当一个局部变量作为全局变量被初始化为它们对应的零值时。指针初始化为`nil`。

| 数据类型 | 初始默认值 |
| -------- | ---------- |
| int      | 0          |
| float32  | 0          |
| 指针     | nil        |
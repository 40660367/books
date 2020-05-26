# Go语言 按值调用函数

通过传递参数到函数的方法的调用是指将参数的实际值复制到函数的形式参数中。 在这种情况下，在函数中对参数所做的更改不会影响参数值。

默认情况下，Go编程语言使用按值调用方法传递参数。 一般来说，函数中的代码不能改变传入函数的参数。参考函数`swap()`定义如下。

```go
/* function definition to swap the values */
func swap(int x, int y) int {
   var temp int

   temp = x /* save the value of x */
   x = y    /* put y into x */
   y = temp /* put temp into y */

   return temp;
}
```

现在，通过传递实际值来调用函数`swap()`，完整的代码如下例所示：

文件名:function-refbyvalue.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var a int = 100
   var b int= 200

   fmt.Printf("Before swap, value of a : %d\n", a )
   fmt.Printf("Before swap, value of b : %d\n", b )

   /* calling a function to swap the values.
   * &a indicates pointer to a ie. address of variable a and 
   * &b indicates pointer to b ie. address of variable b.
   */
   swap(&a, &b)

   fmt.Printf("After swap, value of a : %d\n", a )
   fmt.Printf("After swap, value of b : %d\n", b )
}

func swap(x *int, y *int) {
   var temp int
   temp = *x    /* save the value at address x */
   *x = *y    /* put y into x */
   *y = temp    /* put temp into y */
}
```

```bash
go run /share/lesson/go/function-refbyvalue.go
```

康康
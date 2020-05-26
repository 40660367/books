# Go语言 通过引用调用函数

通过将引数传递给函数的引用方法的调用，是指将参数的地址复制到形式参数中。 在函数内部，地址用于访问在调用中使用的实际参数。 这意味着对参数所做的更改会影响传递的参数的值。

要通过引用传递值，须将参数指针传递给函数，就像传递其他值一样。 因此，需要将函数参数声明为指针类型，如以下函数`swap()`，它交换的参数是指向的两个整数变量的值。

```go
/* function definition to swap the values */
func swap(x *int, y *int) {
   var temp int
   temp = *x    /* save the value at address x */
   *x = *y      /* put y into x */
   *y = temp    /* put temp into y */
}
```

要了解学习Go指针的更多信息，可以查看[Go语言 指针](./pointer.html)。

现在，通过引用传递值来调用函数`swap()`，如下例所示：

文件名:function-refbyreference.go

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
go run /share/lesson/go/function-refbyreference.go
```

康康
# Go语言 函数作为值使用

Go编程语言提供了灵活性，可以即时创建函数并将其用作值使用。在下面的示例中，我们已经使用函数定义初始化了一个变量。 这个函数变量的用途仅仅是使用内置的`math.sqrt()`函数。 

文件名:function-value.go

```go
package main

import (
   "fmt"
   "math"
)
func main(){
   /* declare a function variable */
   getSquareRoot := func(x float64) float64 {
      return math.Sqrt(x)
   }

   /* use the function */
   fmt.Println(getSquareRoot(9))

}
```

```shell
go run /share/lesson/go/function-value.go
```

康康
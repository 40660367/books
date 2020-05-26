# Go语言 错误处理(error)

Go编程提供了一个非常简单的错误处理框架，以及内置的错误接口类型，如下声明：

```go
type error interface {
   Error() string
}
```

函数通常返回错误作为最后一个返回值。 可使用`errors.New`来构造一个基本的错误消息，如下所示：

```go
func Sqrt(value float64)(float64, error) {
   if(value < 0){
      return 0, errors.New("Math: negative number passed to Sqrt")
   }
   return math.Sqrt(value)
}
```

使用返回值和错误消息，如下所示 - 

```go
result, err:= Sqrt(-1)

if err != nil {
   fmt.Println(err)
}
```

### 示例

文件名:error.go

```go
package main

import "errors"
import "fmt"
import "math"

func Sqrt(value float64)(float64, error) {
   if(value < 0){
      return 0, errors.New("Math: negative number passed to Sqrt")
   }
   return math.Sqrt(value), nil
}

func main() {
   result, err:= Sqrt(-1)

   if err != nil {
      fmt.Println(err)
   }else {
      fmt.Println(result)
   }

   result, err = Sqrt(9)

   if err != nil {
      fmt.Println(err)
   }else {
      fmt.Println(result)
   }
}
```

```bash
go run /share/lesson/go/error.go
```

康康
# Go语言 方法(method)	

Go编程语言支持一种叫作方法的特殊类型的函数。 在方法声明语法中，存在“接收器”以表示函数的容器。 此接收器可用于使用“`.`”运算符调用函数。 

### 语法

```go
func (variable_name variable_data_type) function_name() [return_type]{
   /* function body*/
}
```

参考示例：

文件名: function-method.go

```go
package main

import (
   "fmt"
   "math"
)

/* define a circle */
type Circle struct {
   x,y,radius float64
}

/* define a method for circle */
func(circle Circle) area() float64 {
   return math.Pi * circle.radius * circle.radius
}

func main(){
   circle := Circle{x:0, y:0, radius:5}
   fmt.Printf("Circle area: %f", circle.area())
}
```

```bash
go run /share/lesson/go/function-method.go
```

康康
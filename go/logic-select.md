# Go语言 select语句

Go编程语言中`select`语句的语法如下：

```go
select {
    case communication clause  :
       statement(s);      
    case communication clause  :
       statement(s); 
    /* you can have any number of case statements */
    default : /* Optional */
       statement(s);
}
```

以下规则适用于`select`语句：

- 在`select`语句中可以有任意数量的`case`语句。每个`case`语句后面都跟要比较的值和冒号。
- `case`语句中的类型必须是通信通道操作的。
- 当发生通道操作时，将执行该`case`语句之后的语句。 在`case`语句中可不需要`break`语句。
- `select`语句可以有一个可选的`default`语句，它必须出现在`select`语句的结尾。`default`语句可用于在没有任何`case`语句为真时执行任务。在`default`语句不需要`break`语句。

### 示例

文件名:logic-select.go

```go
package main

import "fmt"

func main() {
   var c1, c2, c3 chan int
   var i1, i2 int
   select {
      case i1 = <-c1:
         fmt.Printf("received ", i1, " from c1\n")
      case c2 <- i2:
         fmt.Printf("sent ", i2, " to c2\n")
      case i3, ok := (<-c3):  // same as: i3, ok := <-c3
         if ok {
            fmt.Printf("received ", i3, " from c3\n")
         } else {
            fmt.Printf("c3 is closed\n")
         }
      default:
         fmt.Printf("no communication\n")
   }    
}
```
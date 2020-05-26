# Go语言 嵌套for循环

Go编程语言允许在另一个循环内使用一个循环。 以下部分显示了几个例子来说明这个概念。

## 语法

Go编程语言中的嵌套for循环的语法是：

```go
for [condition |  ( init; condition; increment ) | Range]
{
   for [condition |  ( init; condition; increment ) | Range]
   {
      statement(s);
   }
   statement(s);
}
```

### 示例

以下程序使用嵌套`for`循环来从`2`到`100`中查找素数：

文件名:loop-fornested.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var i, j int

   for i=2; i < 100; i++ {
      for j=2; j <= (i/j); j++ {
         if(i%j==0) {
            break; // if factor found, not prime
         }
      }
      if(j > (i/j)) {
         fmt.Printf("%d is prime\n", i);
      }
   }  
}
```

```bash
go run /share/lesson/go/loop-fornested.go
```

康康
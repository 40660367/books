# Go语言 goto语句

Go编程语言中的`goto`语句提供了从`goto`到相同函数中的带标签语句的无条件跳转。

> 注意：在许多编程语言中都不建议使用`goto`语句，因为它很难跟踪程序的控制流程，使得程序难以理解和难以修改。任何使用`goto`的程序都可以重写，因此不需要`goto`。

Go中的`goto`语句的语法如下：

```go
goto label;
..
.
label: statement;
```

这里的标签(`label`)可以是任何纯文本，除了Go关键字，它可以设置在Go程序中的任何地方：上面或下面使用`goto`语句。

### 流程图

![img](./images/loopcontrol-goto.jpg)

### 示例

文件名:loopcontrol-goto.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var a int = 10

   /* do loop execution */
   LOOP: for a < 20 {
      if a == 15 {
         /* skip the iteration */
         a = a + 1
         goto LOOP
      }
      fmt.Printf("value of a: %d\n", a)
      a++     
   }  
}
```

```bash
go run /share/lesson/go/loopcontrol-continue.go
```

康康
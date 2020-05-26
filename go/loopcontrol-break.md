# Go语言 break语句

Go编程语言中的`break`语句有以下两种用法：

1. 当在循环中遇到break语句时，循环立即终止，并且程序控制在循环之后的下一语句处恢复执行。
2. 它可以用于在`switch`语句中终止一个`case`语句。

如果使用嵌套循环(即在另一个循环中有一个循环)，`break`语句可用于停止最内层循环的执行，并开始执行块后的下一行代码。

Go中的`break`语句的语法如下：

```go
break;
```

### 流程图

![img](./images/loopcontrol-break.png)

### 示例

文件名:loopcontrol-break.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var a int = 10

   /* for loop execution */
   for a < 20 {
      fmt.Printf("value of a: %d\n", a);
      a++;
      if a > 15 {
         /* terminate the loop using break statement */
         break;
      }
   }
}
```

```bash
go run /share/lesson/go/loopcontrol-break.go
```

康康


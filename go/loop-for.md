# Go语言 for循环

`for`循环是一种重复控制结构，它允许您有效地编写需要执行特定次数的循环。


## 语法

Go编程语言中的`for`循环的语法是：

```go
for [condition |  ( init; condition; increment ) | Range]
{
   statement(s);
}
```

下面是`for`循环中的控制流程：

1. 如果条件可用，则只要条件为真，`for`循环就执行。
2. 如果`for`子句是( init; condition; increment )，则存在
   - **init**步骤首先执行，并且只执行一次。此步骤允许您声明和初始化循环控制变量。不需要在这里放置语句，只要有一个分号出现。
   - 接下来，评估(求值)条件。 如果为真，则执行循环体。 如果为`false`，循环的主体不执行，控制流跳到`for`循环之后的下一个语句。
   - 在`for`循环的主体执行后，控制流跳回到**increment**语句。此语句允许更新任何循环控制变量。 此语句可以留空，只要有一个分号出现。
   - 现在再次评估(求值)条件。 如果为真，则循环执行并且过程重复(循环体，然后增加(**increment**)步骤，然后再次进入条件**increment**)。条件变为假后，`for`循环终止。
3. 如果范围(**range**)可用，则对该范围中的每个项目执行`for`循环。

### 示例

文件名:loop-for.go

```go
package main

import "fmt"

func main() {

   var b int = 15
   var a int

   numbers := [6]int{1, 2, 3, 5} 

   /* for loop execution */
   for a := 0; a < 10; a++ {
      fmt.Printf("value of a: %d\n", a)
   }

   for a < b {
      a++
      fmt.Printf("value of a: %d\n", a)
      }

   for i,x:= range numbers {
      fmt.Printf("value of x = %d at %d\n", x,i)
   }   
}
```

```bash
go run /share/lesson/go/loop-for.go
```

康康
# Go语言 逻辑判断

决策结构要求程序员指定要由程序评估(求值)或测试的一个或多个条件，以及如果条件被确定为真则要执行一个或多个语句，以及还可以可选地在条件被确定为假时，评估(求值)或测试的一个或多个条件。

Go编程语言提供以下类型的决策语句。单击以下相关链接以学习或了解其详细信息。


| 语句                                 | 描述                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| if语句                               | **if语句**由布尔表达式后跟一个或多个语句组成。               |
| if…else语句                          | **if语句**后面可以是一个可选的`else`语句，当布尔表达式为`false`时执行`else`语句。 |
| [嵌套if语句](./logic-if-nested.html) | 可在另一个`if`或`else if`语句中使用一个`if`或`else if`语句。 |
| switch语句                           | **switch语句**允许根据值列表测试变量的相等性。               |
| [select语句](./logic-select.html)    | select语句与`switch`语句类似，因为`case`语句指的是通道通信。 |

## if语句

文件名:if.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var a int = 10

   /* check the boolean condition using if statement */
   if( a < 20 ) {
       /* if condition is true then print the following */
       fmt.Printf("a is less than 20\n" )
   }
   fmt.Printf("value of a is : %d\n", a)
}
```

```bash
go run /share/lesson/go/if.go
```

康康

## if…else语句

文件名:ifelse.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var a int = 100;

   /* check the boolean condition */
   if( a < 20 ) {
       /* if condition is true then print the following */
       fmt.Printf("a is less than 20\n" );
   } else {
       /* if condition is false then print the following */
       fmt.Printf("a is not less than 20\n" );
   }
   fmt.Printf("value of a is : %d\n", a);
}
```

```bash
go run /share/lesson/go/ifelse.go
```

康康

## switch

**switch语句**允许根据值列表测试变量的相等性。 每个值被称为一个情况(`case`)，并且对于每个开关情况(switch case)检查接通的变量。

在Go编程中，**switch**有两种类型。

- **表达式开关(switch)** - 在表达式开关(switch)中，`case`包含与开关(switch)表达式的值进行比较的表达式。
- **类型开关(switch)** - 在类型开关(switch)中，`case`包含与特殊注释的开关(switch)表达式的类型进行比较的类型。

### 表达式开关(switch)

Go编程语言中的表达式**switch语句**的语法如下：

```go
switch(boolean-expression or integral type){
    case boolean-expression or integral type  :
       statement(s);      
    case boolean-expression or integral type  :
       statement(s); 
    /* you can have any number of case statements */
    default : /* Optional */
       statement(s);
}
```

以下规则适用于`switch`语句：

- 在`switch`语句中使用的表达式必须具有整数或布尔表达式， 或者是一个具有单个转换函数为整数或布尔值的类类型。如果未传递表达式，则默认值为`true`。
- 在`switch`语句中可以有任意数量的`case`语句。 每个`case`后面都跟要比较的值和冒号。
- `case`的常量表达式必须是与`switch`语句的变量是相同的数据类型，并且它必须是常量或文字。
- 当被打开的变量等于一个`case`中的值，那么将执行`case`之后的语句。在`case`语句中可不需要`break`语句。
- `switch`语句可有一个可选的 `default`，它必须出现在`switch`语句的末尾。 `default`可用于在没有任何 `case` 为真时执行任务。`default`之后可不需要 `break` 语句。

### 流程图

![img](./images/switch.jpg)

### 示例

文件名:logic-switch.go

```go
package main

import "fmt"

func main() {
   /* local variable definition */
   var grade string = "B"
   var marks int = 90

   switch marks {
      case 90: grade = "A"
      case 80: grade = "B"
      case 50,60,70 : grade = "C"
      default: grade = "D"  
   }

   switch {
      case grade == "A" :
         fmt.Printf("Excellent!\n" )     
      case grade == "B", grade == "C" :
         fmt.Printf("Well done\n" )      
      case grade == "D" :
         fmt.Printf("You passed\n" )      
      case grade == "F":
         fmt.Printf("Better try again\n" )
      default:
         fmt.Printf("Invalid grade\n" );
   }
   fmt.Printf("Your grade is  %s\n", grade );      
}
```

```bash
go run /share/lesson/go/logic-switch.go
```

康康
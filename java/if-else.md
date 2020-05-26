# Java if...else语句

`if`语句后面可以跟一个可选的`else`语句，`else`语句在布尔表达式为`false`时执行。

**语法**

以下是`if...else`语句的语法 - 

```java
if(boolean_expression) {
   // 布尔表达式为true时执行
}else {
   // 布尔表达式为false时执行
}
```

如果布尔表达式的计算结果为`true`，那么将执行`if`代码块，否则将执行`else`代码块。

![if...else流程图](./images/if-else.jpg)

<iframe src="//player.bilibili.com/player.html?aid=62042179&bvid=BV1ot411u7Hw&cid=107857458&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

**示例**:一个用于演示if-else语句的Java程序

文件名:IfElseExample.java

```java
public class IfElseExample {
    public static void main(String[] args) {
        // 定义一个变量
        int number = 133;
        // 检查数字是否可以被 2 整除？
        if (number % 2 == 0) {
            System.out.println(number + " 是一个偶数");
        } else {
            System.out.println(number + " 是一个奇数");
        }

        // 示例2
        int x = 30;

        if (x < 20) {
            System.out.println(x + " 是一个小于 20 的整数");
        } else {
            System.out.println(x + " 是一个大于 20 的整数");
        }

    }
}
```

```shell
cd ~/java && javac IfElseExample.java
java IfElseExample
```

康康

#### if…else if…else语句

`if`语句之后可以跟一个可选的`else if`语句，这对于使用`if...else if`语句测试各种条件非常有用。

当使用`if`，`else if`，`else`语句时，需要记住几点：

- 一个`if`语句之后可以有零个或一个`else`语句，但它必须在`else...if`之后。
- `if`可以有零或多个`else...if`，并且它们必须在`else`语句之前。
- 当有一个`else if`条件匹配成功，其余的`else...if`或者`else`都将不会执行。

**语法**

以下是`if...else`语句的语法 - 

```java
if(boolean_expression_1) {
   // 当 boolean_expression_1 结果为 true 时，执行这里的代码块
}else if(boolean_expression_2) {
   // 当 boolean_expression_2 结果为 true 时，执行这里的代码块
}else if(boolean_expression_3) {
   // 当 boolean_expression_3 结果为 true 时，执行这里的代码块
}else {
   // 当上面表达式都没有一个计算结果为 true 时，执行这里的代码块
}
```

**示例代码**

演示如何使用 if else-if 梯形。 
它是一个判断分数级别为：D级，C级，B级，A级和A+级 的程序。

文件名:IfElseIfExample.java

```java
public class IfElseIfExample {
    public static void main(String[] args) {
        int marks = 65;

        if (marks < 60) {
            System.out.println("D级");
        } else if (marks >= 60 && marks < 70) {
            System.out.println("C级");
        } else if (marks >= 70 && marks < 80) {
            System.out.println("B级");
        } else if (marks >= 80 && marks < 90) {
            System.out.println("A级");
        } else if (marks >= 90 && marks < 100) {
            System.out.println("A+级");
        } else {
            System.out.println("无效!");
        }
    }
}
```

```shell
cd ~/java && javac IfElseIfExample.java
java IfElseIfExample
```

康康
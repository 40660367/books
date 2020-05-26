# Java if语句

`if`语句由一个布尔表达式后跟一个或多个语句组成。

**语法**

以下是`if`语句的语法 - 

```java
if(boolean_expression) {
   // 如果布尔表达式为`true`，则将执行这里的语句
}
```

如果布尔表达式(`boolean_expression`)的计算结果为`true`，那么将执行`if`语句中的代码块。 如果计算结果为`false`，将执行`if`语句结束后(在结束大括号之后)的第一组代码。

执行流程图如下 

![if语句流程图](./images/if.jpg)

**示例代码**

文件名:IfExample.java

```java
public class IfExample {
    public static void main(String[] args) {
        int age = 20;
        if (age > 18) {
            System.out.println("年龄大于 18 岁");
        }
        if (age <= 20) {
            System.out.println("年龄小于或等于 20 岁");
        }

        if (age >= 20 && age < 30) {
            System.out.println("年龄小于或等于 20 岁，并且小于 30 岁");
        }
    }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac IfExample.java
java IfExample
```
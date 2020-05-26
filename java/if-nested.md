# Java 嵌套if语句 			

嵌套`if-else`语句总是合法有效的，可以在一个`if`或`else if`语句中使用另一个`if`或`else if`语句。

**语法**
嵌套`if...else`的语法如下 -

```java
if(boolean_expression_1) {
   // 当 boolean_expression_1 表示为：true 时，执行这里的代码块
   if(boolean_expression_2) {
      // 当 boolean_expression_2 表示为：true 时，执行这里的代码块
   }
}
```

可以使用类似于嵌套`if`语句的方式来嵌套`if else`。

**示例1**

文件名:JavaNestedIfExample.java

```java
public class JavaNestedIfExample {
    public static void main(String[] args) {
        // 创建两个变量： age 和 weight
        int age = 20;
        int weight = 80;
        // 适用年龄和体重的条件
        if (age >= 18) {
            if (weight > 50) {
                System.out.println("体重达标，有献血资格");
            }else {
                System.out.println("体重不达标，没有献血资格");
            }
        }
    }
}
```

```bash
cd ~/java && javac JavaNestedIfExample.java
java JavaNestedIfExample
```

康康

**示例2**

文件名:JavaNestedIfExample2.java

```java
public class JavaNestedIfExample2 {
    public static void main(String[] args) {
        //  创建两个变量： age 和 weight
        int age = 25;
        int weight = 48;
        // 适用年龄和体重的条件
        if (age >= 18) {
            if (weight > 50) {
                System.out.println("体重达标，有献血资格");
            }else {
                System.out.println("体重不达标，没有献血资格");
            }
        } else {
            System.out.println("年龄必须大于 18 岁");
        }
    }
}
```

```bash
cd ~/java && javac JavaNestedIfExample2.java
java JavaNestedIfExample2
```

康康
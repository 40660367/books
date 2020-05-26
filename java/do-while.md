# Java do...while循环 			

`do...while`循环类似于`while`循环，除了`do...while`循环保证至少执行一次。

**语法**
以下是`do...while`循环的语法 -

```java
do {
   // Statements
}while(boolean_expression);
Java
```

请注意，布尔表达式在循环的末尾，因此循环中的语句在测试布尔值之前已经执行了一次。

如果布尔表达(`boolean_expression`)式评估结果为`true`，则控制跳回到`do`语句，循环中的语句再次执行。 重复此过程，直到布尔表达式(`boolean_expression`)评估结果为`false`。

**执行流程图**

<img src="./images/loop-dowhile.jpg" alt="do...while循环执行流程图" style="zoom:80%;" />

<iframe src="//player.bilibili.com/player.html?aid=83626540&bvid=BV1eJ41177ec&cid=143065221&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
**示例1. do…while循环**

这是一个简单的java `do while`循环示例，用于打印`5`到`10`之间的数字。

文件名:JavaDoWhileLoop.java

```java
public class JavaDoWhileLoop {

    public static void main(String[] args) {

        int i = 5;
        do {
            System.out.println(i);
            i++;
        } while (i <= 10);
    }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac JavaDoWhileLoop.java
java JavaDoWhileLoop
```

**示例2. do…while无限循环**

通过在`do...while`循环中将布尔表达式使用`true`值来创建无限循环。下面是一个简单的做java无限循环的例子(伪代码)。

文件名:DoWhileTrueJava.java

```java
public class DoWhileTrueJava {

    public static void main(String[] args) throws InterruptedException {
        do {
            System.out.println("Start Processing inside do while loop");
            // 在指定目录中查找文件
            // 如果找到，则处理它，例如：将文件信息插入数据库
            System.out.println("End Processing of do while loop");

            Thread.sleep(5 * 1000); // 暂停5秒，接着执行
        } while (true);
    }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac DoWhileTrueJava.java
java DoWhileTrueJava
```

请注意，如果在终端中执行程序，则可使用`Ctrl + C`手动退出应用程序。 如果已在Eclipse IDE中执行程序，则会有一个红色按钮来终止程序。

**do…while与while循环比较**

当希望在循环内的语句至少执行一次时，则应该使用`do...while`循环。 否则，使用`while`循环总是更好选择。Java `while`循环看起来比`do...while`循环更干净。
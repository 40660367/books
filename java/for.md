# Java for循环

`for`循环是一种重复控制结构，用于有效地编写需要执行特定次数的循环。当知道要重复任务的次数时，`for`循环就很有用。

**语法**

`for`循环的语法是 -

```java
for(initialization; boolean_expression; update) {
   // Statements
}
```

在上面语法中，

- 首先执行初始化(`initialization`)步骤，并且仅执行一次。此步骤用于声明和初始化循环控制变量，此步骤以分号(`;`)结束。
- 接下来，计算布尔表达式(`boolean_expression`)。 如果结果为：`true`，则执行循环体。 如果为`false`，则不执行循环体，控制跳转到`for`循环之后的下一个语句。
- 在执行`for`循环体之后，控件跳回到`update`语句。 此语句用于更新任何循环控制变量。此语句可以留空，最后是分号(`;`)。
- 现在再次评估布尔表达式(`boolean_expression`)。 如果结果为：`true`，则循环执行并重复该过程(循环体，然后是更新步骤，然后是布尔表达式)。 布尔表达式为`false`后，`for`循环终止。

<iframe src="//player.bilibili.com/player.html?aid=68232568&bvid=BV15J41137AH&cid=118263758&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

**for循环的流程图如下**

![for循环流程](./images/for.jpg)

java中有三种类型的`for`循环，它们分别如下：

- 简单`for`循环
- `for-each`或增强`for`循环
- `for`循环与标签

**示例1:简单for循环实例**

Java中的简单`for`循环与C/C ++相同。可以初始化变量，检查条件和增量/减量值。
假设要打印`5`到`10`的整数，在这种情况下可以使用基本的`for`循环。

文件名:JavaForLoop.java

```java
public class JavaForLoop {

    public static void main(String[] args) {

        //print integers 5 to 10
        for (int i=5; i<=10; i++) {
            System.out.println("Java for loop example - " + i);
        }
    }
}
```

```shell
cd ~/java && javac JavaForLoop.java
java JavaForLoop
```

康康

**示例2. for增强型循环**

Java中的`for each`循环也称为增强型循环。可以使用`for each`迭代数组或集合元素。Java `for each`循环是推荐的循环方式，因为它的代码编写比较简单和紧凑。

文件名:JavaForEachLoopExample.java

```java
import java.util.ArrayList;
import java.util.List;

public class JavaForEachLoopExample {

    public static void main(String[] args) {
        int[] intArray = { 10, 20, 30, 40, 50 };

        for (int i : intArray)
            System.out.println("Java for each loop with array - " + i);

        List<String> fruits = new ArrayList<>();
        fruits.add("苹果");
        fruits.add("香蕉");
        fruits.add("橙子");

        for (String f : fruits)
            System.out.println("Java for each loop with collection - " + f);
    }
}
```

```shell
cd ~/java && javac JavaForEachLoopExample.java
java JavaForEachLoopExample
```

康康

从上面的例子中可以看出，如果`for`循环中只有一个语句，不需要将它们放在花括号`{}`中。

**示例3. for循环与标签**

可以在`for`循环中添加一个标签，它对`break`和`continue`语句有用，可以退出外循环。 请注意，默认情况下，`break`和`continue`语句仅适用于内部循环。 下面是带有标签的`for`循环的示例以及它如何与`continue`语句一起使用。

文件名:JavaForLoopWithLabel.java

```java
import  java.util.Arrays;
public class JavaForLoopWithLabel {
    public static void main(String[] args) {
        int[][] intArr = { { 1, -2, 3 }, { 0, 3 }, { 1, 2, 5 }, { 9, 2, 5 } };
        process: for (int i = 0; i < intArr.length; i++) {
            boolean allPositive = true;
            for (int j = 0; j < intArr[i].length; j++) {
                if (intArr[i][j] < 0) {
                    allPositive = false;
                    continue process;
                }
            }
            if (allPositive) {
                // process the array
                System.out.println("Processing " + Arrays.toString(intArr[i]));
            }
            allPositive = true;
        }
    }
}
```

```shell
cd ~/java && javac JavaForLoopWithLabel.java
java JavaForLoopWithLabel
```

康康
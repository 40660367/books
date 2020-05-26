# Java break语句

Java编程语言中的`break`语句有以下两种用法 - 

- 当在循环内遇到`break`语句时，循环立即终止，程序控制在循环体之后的下一个语句处重新开始。
- 它可以用于在`switch`语句中终止一个`case`(在下一章中介绍)。

**语法**

`break`的语法是循环内的单个语句 - 

```java
break;
```

**break语句流程图**

![break语句](./images/break.jpg)

<iframe src="//player.bilibili.com/player.html?aid=69116374&bvid=BV1kJ411T71u&cid=119786856&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
**示例1.  break简单示例**

文件名：SimpleBreak.java

```java
public class SimpleBreak {

   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};

      for(int x : numbers ) {
         if( x == 30 ) {
            break;
         }
         System.out.print( x );
         System.out.print("\n");
      }
   }
}
```

```bash
cd ~/java && javac SimpleBreak.java
java SimpleBreak
```

康康

**示例2. break语句示例**

在这个示例中，演示如何在java的`for`循环，while循环和`do-while`循环中使用`break`语句。

文件名:JavaBreaks.java

```java
public class JavaBreaks {

    public static void main(String[] args) {
        String[] arr = { "H", "E", "L", "L", "O", "!" };

        // 在 for 循环中使用 break
        for (int len = 0; len < arr.length; len++) {
            if (arr[len].equals("O")) {
                System.out.println("Array contains 'O' at index: " + len);
                // 当找到字母时使用`break`语句中断循环
                break;
            }
        }

        // 在 while 循环中使用  break
        int len = 0;
        while (len < arr.length) {
            if (arr[len].equals("L")) {
                System.out.println("Array contains 'L' at index: " + len);
                // 当找到字母时使用`break`语句中断循环
                break;
            }
            len++;
        }

        len = 0;
        // 在 do-while循环中使用 break
        do {
            if (arr[len].equals("E")) {
                System.out.println("Array contains 'E' at index: " + len);
                // 当找到字母时使用`break`语句中断循环
                break;
            }
            len++;
        } while (len < arr.length);
    }

}
```

```bash
cd ~/java && javac JavaBreaks.java
java JavaBreaks
```

康康

请注意，如果删除`break`语句，程序的输出将没有任何差异。 对于此示例中的小型迭代，没有的性能问题。 但是如果迭代器次数很大，那么它可以节省大量的处理时间。

**示例3. Java break标签**
`break`语句标签化用于终止外部循环，应该标记循环以使其起作用。这是一个演示java `break`标签语句用法的示例。

文件名:JavaBreakLabel.java

```java
public class JavaBreakLabel {

    public static void main(String[] args) {
        int[][] arr = { { 1, 2 }, { 3, 4 }, { 9, 10 }, { 11, 12 } };
        boolean found = false;
        int row = 0;
        int col = 0;
        // 查找第一个大于10的整数所在的索引值
        searchint:

        for (row = 0; row < arr.length; row++) {
            for (col = 0; col < arr[row].length; col++) {
                if (arr[row][col] > 10) {
                    found = true;
                    // 使用 break 标签来终止外部语句
                    break searchint;
                }
            }
        }
        if (found)
            System.out.println("First int greater than 10 is found at index: [" + row + "," + col + "]");
    }

}
```

```bash
cd ~/java && javac JavaBreakLabel.java
java JavaBreakLabel
```

康康

也可以使用break语句在`switch`语句块中，这个在接下来的章节中将详细讲解。




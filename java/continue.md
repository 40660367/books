# Java continue语句

Java **continue语句**用于继续循环。 它继续程序的当前流程，并在指定条件下跳过剩余的代码。在内循环的情况下，它仅继续内循环。

**语法：**

```java
jump-statement;    
continue;
```

<iframe src="//player.bilibili.com/player.html?aid=69116374&bvid=BV1kJ411T71u&cid=119786856&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## Java continue语句示例

**示例：**

文件名:ContinueExample.java

```java
public class ContinueExample {
    public static void main(String[] args) {
        for (int i = 1; i <= 10; i++) {
            if (i == 5) {
                continue;
            }
            System.out.println(i);
        }
    }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```bash
cd ~/java && javac ContinueExample.java
java ContinueExample
```

康康

## Java continue语句与内循环

如果在内循环中使用`continue`语句，它将继续内循环。

**示例：**

文件名:ContinueExample2.java

```java
public class ContinueExample2 {
    public static void main(String[] args) {
        for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= 3; j++) {
                if (i == 2 && j == 2) {
                    continue;
                }
                System.out.println(i + " " + j);
            }
        }
    }
}
```

```shell
cd ~/java && javac ContinueExample2.java
java ContinueExample2
```

康康
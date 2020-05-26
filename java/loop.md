# Java 循环控制

在程序执行过程中，存在需要多次执行代码块的情况。 通常，语句按顺序执行：首先执行函数中的第一个语句，然后执行第二个语句，依此类推。

编程语言提供各种控制结构，允许更复杂的执行路径。

循环语句用于多次执行一个语句或一组语句，以下是大多数编程语言中循环语句的一般形式 - 


Java编程语言提供以下类型的循环来处理循环要求，可通过单击以下每个链接来学习。

| 编号 | 循环                            | 描述                                                         |
| ---- | ------------------------------- | ------------------------------------------------------------ |
| 1    | [while循环](./while.html)       | 在给定条件为真时重复语句或语句组，它在执行循环体之前测试条件。 |
| 2    | [for循环](./for.html)           | 多次执行一系列语句，并缩写管理循环变量的代码。               |
| 3    | [do…while循环](./do-while.html) | 像`while`语句一样，但是它在末端测试循环体的条件。            |

## 循环控制语句

循环控制语句将执行从正常执行顺序更变。 当执行离开作用域时，将销毁在该作用域中创建的所有自动对象。

Java支持以下控制语句，可通过单击以下每个链接来了解和学习。

| 编号 | 控制语句                                                     | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | [break语句](/java/break.html) | 终止循环或`switch`语句，并立即将执行转移到在循环或`switch`之后的语句。 |
| 2    | [continue语句](/java/continue.html) | 使循环跳过其主体的其余部分，并在重复之前立即重新测试其状态。 |

## 增强Java循环

从Java 5开始，引入了增强的`for`循环。 这主要用于遍历元素的集合，包括数组。

**语法**
以下是增强`for`循环的语法 - 

```java
for(declaration : expression) {
   // Statements
}
```

在上面语法中，

- `declaration` - 新声明的块变量，是与要访问的数组元素兼容的类型。变量将在`for`块中可用，其值将与当前数组元素相同。
- `expression` - 这是要循环的数组。表达式(`expression`)可以是返回的数组变量或方法调用。

**示例**

文件名:LoopTest.java

```java
public class LoopTest {

   public static void main(String args[]) {
      int [] numbers = {10, 20, 30, 40, 50};

      for(int x : numbers ) {
         System.out.print( x );
         System.out.print(",");
      }
      System.out.print("\n");
      String [] names = {"James", "Curry", "Kobe", "Jordan"};

      for( String name : names ) {
         System.out.print( name );
         System.out.print(",");
      }
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac LoopTest.java
java LoopTest
```


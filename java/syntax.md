# Java 基本语法

当我们研究Java程序时，它一种定义为通过调用彼此的方法进行通信的对象集合。 下面简要地看一下：类，对象，方法和实例变量的含义。

- **类** - 类是用于描述其类型对象支持的行为/状态的模板/蓝图。
- **对象** - 对象具有状态和行为。 示例：狗有状态 - 颜色，名称，品种以及例如：摇尾巴，吠叫，吃东西等行为。对象是类的实例。
- **方法** - 方法是一种行为，一个类可以包含许多方法。它用于写入逻辑，操纵数据并执行所有操作。
- **实例变量** - 每个对象都有其唯一的实例变量集。 对象的状态由分配给这些实例变量的值来创建。

####  第一个Java程序

下面来看一个简单打印字符串：`Hello World`的Java代码。

文件名:HelloWorld.java

```java
public class HelloWorld {

   /* 这是第一个Java程序
    * 此程序执行后将打印输出：'Hello World' 
    */

   public static void main(String []args) {
      System.out.println("Hello World"); // 打印输出 Hello World
   }
}
```

- 打开命令提示符窗口并转到保存该类文件(*HelloWorld.java*)的目录。
- 输入`javac HelloWorld.java`并按*Enter*键编译代码。如果代码中没有错误，命令提示符将进入到下一行。
- 接下来，输入`java HelloWorld`来运行上面程序。
- 最后应该能在窗口上看到输出：`Hello World`。

```bash
#使用javac将java源文件进行编译，会生成HelloWorld.class文件
cd ~/java && javac HelloWorld.java

#使用Java执行HelloWorld
java HelloWorld
```

康康

#### 基本语法

关于Java程序，请务必牢记以下几点。

- **区分大小写** -  Java区分大小写，因此标识符`Hello`和`hello`在Java中具有不同的含义。
- **类名** - 对于所有类名，第一个字母应为大写。 如果使用多个单词来形成类的名称，则每个内部单词的第一个字母应为大写。
  示例：`class MyFirstJavaClass`
- **方法名称** - 所有方法名称都应以小写字母开头。如果使用多个单词来形成方法的名称，那么每个内部单词的第一个字母应该是大写字母。
  示例：`public void myMethodName()`
- **程序文件名** - 程序文件的名称应与类名完全匹配。保存文件时，应使用类名保存它(记住Java区分大小写)并在名称的末尾使用扩展名称：`.java`(如果文件名和类名不匹配，则程序将无法编译))。但请注意，如果代码文件中没有`public class`，则文件名可能与类名不同。在代码文件中也没有强制要求必须有`public class`。
  示例：假设`MyFirstJavaProgram`是类名，那么该文件应保存为：*MyFirstJavaProgram.java*。
- `public static void main(String args[])` − Java程序处理从`main()`方法开始，该方法是每个Java程序的必需部分。

#### Java标识符

所有Java组件都需要名称。 用于类，变量和方法的名称称为**标识符**。
在Java中，标识符的命名有几点要记住。 它们如下 - 

- 所有标识符都应以字母(`A`到`Z`或`a`到`z`)，货币字符(`$`)或下划线(`_`)开头。
- 在第一个字符之后，标识符可以是任何字符组合。
- 关键字不能用作标识符。
- 标识符区分大小写。
- 合法标识符的示例：`age`，`$salary`，`_value`，`__1_value`。
- 非法标识符的示例：`123abc`，`-salary`。

#### Java修饰符

与其他语言一样，可以通过使用修饰符来修改类，方法等。 修饰符分为两类 - 

- 访问修饰符 - `default`, `public` , `protected`, `private`；
- 非访问修饰符 -  `final`，`abstract`，`strictfp`；

在下一节中学习有关修饰符的更多细节。

#### Java变量

以下是Java中的变量类型 - 

- 局部变量
- 类变量(静态变量)
- 实例变量(非静态变量)

#### Java数组

数组是存储多个相同类型变量的对象。 但是，数组本身是堆上的对象。在接下来的章节中将学习如何声明，构造和初始化数组。

####  Java枚举

枚举是在Java 5.0中引入的。 枚举将变量限制为仅具有少数预定义值之一。此枚举列表中的值称为枚举。
通过使用枚举，可以减少代码中的错误数量。

例如，在新鲜果汁店中，可将玻璃杯大小限制为：*小杯*，*中杯*和*大杯*。 这将确保它不允许购买除了小杯，中杯或大杯之外的玻璃杯。

示例代码：

文件名:FreshJuiceTest.java

```java
class FreshJuice {
    // 定义枚举
    enum FreshJuiceSize{ SMALL, MEDIUM, LARGE }
    FreshJuiceSize size;
};

public class FreshJuiceTest {

   public static void main(String args[]) {
      FreshJuice juice = new FreshJuice();
      juice.size = FreshJuice.FreshJuiceSize.MEDIUM ;
      System.out.println("玻璃杯大小: " + juice.size);
   }
}
```

```bash
cd ~/java && javac FreshJuiceTest.java
java FreshJuiceTest
```

康康

> 注 - 枚举可以单独声明或在类中声明。 方法，变量，构造函数也可以在枚举内定义。

#### Java关键字

以下列表中列出了Java中的保留字(关键字)。这些保留字不能用作常量或变量或任何其他标识符名称。

| abstract | assert       | boolean  | break      |
| -------- | ------------ | -------- | ---------- |
| byte     | case         | catch    | char       |
| class    | const        | continue | default    |
| do       | double       | else     | enum       |
| extends  | final        | finally  | float      |
| for      | goto         | if       | implements |
| import   | instanceof   | int      | interface  |
| long     | native       | new      | package    |
| private  | protected    | public   | return     |
| short    | static       | strictfp | super      |
| switch   | synchronized | this     | throw      |
| throws   | transient    | try      | void       |
| volatile | while        |          |            |

#### 注释

Java支持与C和C++非常相似的单行和多行注释。Java编译器会忽略任何注释中可用的所有字符。

示例代码：

文件名:CommentsTest.java

```java
public class CommentsTest {

   /* This is my first java program.
    * This will print 'Hello World' as the output
    * This is an example of multi-line comments.
    */

   public static void main(String []args) {
      // 这是单行注释
      /* 这也是一个单行注释 */
      /* 这是一个
       多行的
       注释 
       */
      System.out.println("Hello World");
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```bash
cd ~/java && javac CommentsTest.java
java CommentsTest
```

#### 继承

在Java中，类可以从类派生(继承)。 如果需要创建一个新类，并且已经有一个包含需要的代码的类，那么可以直接从这个现有代码派生一个新类。

此概念可重用现有类的字段和方法，而无需在新类中重写代码。 在这种情况下，现有类称为超类，派生类称为子类。

#### 接口

在Java语言中，接口可以定义为对象之间如何相互通信的契约。 在涉及继承的概念时，接口起着至关重要的作用。

接口定义一些方法，在派生类(子类)应该使用这些方法。 但是这些方法的实现完全取决于子类。
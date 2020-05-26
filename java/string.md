# Java 字符串类(String)

字符串在Java编程中广泛使用，字符串就是一系列字符(由一个个的字符组成)。 在Java编程语言中，字符串被视为对象。

Java平台提供`String`类来创建和操作字符串。

## 1. 创建字符串

创建字符串的最直接方法是 - 

```java
String str = "Hello world!";
```

每当它在代码中遇到字符串文字时，编译器就会创建一个`String`对象，在本例中`str`对象的值为`Hello world!`。

与其他对象一样，可以使用`new`关键字和构造函数来创建`String`对象。`String`类有`11`个构造函数，方便使用不同的源(例如：字符数组)提供字符串的初始值。

**示例**

文件名:StringDemo.java

```java
public class StringDemo {
   public static void main(String args[]) {
      char[] helloArray = { 'H', 'e', 'l', 'l', 'o', '!' };
      String helloString = new String(helloArray);  
      System.out.println( helloString );
   }
}
```

```bash
cd ~/java && javac StringDemo.java
java StringDemo
```

康康

>注 -  `String`类是不可变的，因此一旦创建，就无法更改`String`对象。 如果想要对字符串进行大量修改，则应使用StringBuffer和StringBuilder。

## 字符串长度

用于获取对象信息的方法称为访问器方法。 可以与字符串一起使用来获取字符串长度的一个访问器方法是`length()`方法，它返回字符串对象中包含的字符数。

以下程序是`String`类的`length()`方法的示例。

文件名:StringDemo1.java

```java
public class StringDemo1 {
   public static void main(String args[]) {
      String greeting = "Hello World!";
      int len = greeting.length();
      System.out.println( greeting+" 字符串的长度是: " + len );
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？
```bash
cd ~/java && javac StringDemo1.java
java StringDemo1
```

## 连接字符串

`String`类包含一个用于连接两个字符串的方法 - 

```java
string1.concat(string2);
```

这将返回一个新字符串：`string1`，并且`string1`在结尾处添加了`string2`。 还可以将`concat()`方法与字符串文字一起使用，例如 - 

```java
"My name is ".concat("Maxsu");
```

字符串通常使用`+`运算符连接，如 - 

```java
"Hello," + " world" + "!"
```

上面代码执行后得到的结果是：

```shell
"Hello, world!"
```

下面再来看另一个例子

文件名:StringDemo2.java

```java
public class StringDemo2 {
   public static void main(String args[]) {
      String string1 = " Demo";
      System.out.println("String" + string1);
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```bash
cd ~/java && javac StringDemo2.java
java StringDemo2
```

## 创建格式化字符串

Java中使用`printf()`和`format()`方法来打印带有格式化数字的输出。 `String`类有一个等效的类方法`format()`，它返回一个`String`对象而不是一个`PrintStream`对象。

使用`String`的`static format()`方法可以创建重用的格式化字符串，而不是一次性打印语句。 例如 - 

```java
System.out.printf("The value of the float variable is " +
                  "%f, while the value of the integer " +
                  "variable is %d, and the string " +
                  "is %s", floatVar, intVar, stringVar);
```

上面打印语句可使用格式化写为：

```java
String fs;
fs = String.format("The value of the float variable is " +
                   "%f, while the value of the integer " +
                   "variable is %d, and the string " +
                   "is %s", floatVar, intVar, stringVar);
System.out.println(fs);
```
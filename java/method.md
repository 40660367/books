# Java 方法(method)

Java中的方法是一组语句，它们组合在一起以执行各种操作。 例如，当调用`System.out.println()`方法时，系统实际上会执行多个语句，以便在控制台上显示消息。

下面将学习如何使用或不使用返回值创建自己的方法，使用或不使用参数调用方法，以及在程序设计中应用方法抽象。

## 创建方法

下面来看看方法的语法 

```java
public static int methodName(int a, int b) {
   // body
}
```

在上面语法中，

- `public static` − 修辞符
- `int` − 返回值的类型
- `methodName` − 方法的名称
- `a, b` − 形式参数
- `int a, int b` − 参数列表

方法定义由方法头和方法体组成。以下语法中显示了相同的内容 - 

```java
modifier returnType nameOfMethod (Parameter List) {
   // method body
}
```

上面显示的语法包括 - 

- `modifier` - 它定义方法的访问类型，它可能是：`public`,`private`,`protected`或不指定。
- `returnType` -  方法可以返回一个值。
- `nameOfMethod` - 这是方法名称，方法签名由方法名称和参数列表组成。
- `Parameter List` - 参数列表，它是方法的类型，顺序和参数数量。 这些是可选的，方法可能包含零参数。
- `method body` - 方法体定义方法对语句的作用。

**示例**

以下代码中定义了`min()`方法。 这个方法有两个`int`类型的参数：`num1`和`num2`，并返回两者之间的最大值

文件名:MinFunction.java

```java
//返回两个数字之间的最小值
public static int MinFunction(int n1, int n2) {
   int min;
   if (n1 > n2)
      min = n2;
   else
      min = n1;

   return min; 
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac MinFunction.java
java MinFunction
```

## 方法调用

可通过调用方法来使用方法，调用方法有两种方式，即方法有返回值或无返回任何值。

方法调用的过程很简单。 当程序调用方法时，程序控制将转移到被调用的方法。 这个被调用的方法然后在两个条件下将控制权返回给调用者，即 - 

- `return`语句被执行。
- 它到达方法的结束，即右大括号(`}`)。

对返回`void`的方法的调用 - 

```java
System.out.println("This is Yiibai.com!");
```

对有返回值的方法的调用

```java
int result = sum(6, 9);
```

以下是演示如何定义方法以及如何调用方法的示例

文件名:ExampleMinNumber.java

```java
public class ExampleMinNumber {

   public static void main(String[] args) {
      int a = 111;
      int b = 125;
      int c = getMin(a, b);
      System.out.println("最小值 = " + c);
   }

   /** 返回两个 int 数值的最小值 */
   public static int getMin(int n1, int n2) {
      int min;
      if (n1 > n2)
         min = n2;
      else
         min = n1;

      return min; 
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac ExampleMinNumber.java
java ExampleMinNumber
```

## void关键字

`void`关键字允许创建不返回值的方法。在下面的例子中有一个返回值是`void`的方法`methodRankPoints`，它不返回任何值。 调用`void`方法必须是一个语句，即`methodRankPoints(245.67);`. 它是一个以分号结尾的Java语句，如以下示例所示

文件名:ExampleVoid.java

```java
public class ExampleVoid {

   public static void main(String[] args) {
      methodRankPoints(245.67);
   }

   public static void methodRankPoints(double points) {
      if (points >= 202.5) {
         System.out.println("Rank:A1");
      }else if (points >= 122.4) {
         System.out.println("Rank:A2");
      }else {
         System.out.println("Rank:A3");
      }
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac ExampleVoid.java
java ExampleVoid
```

## 按值传递参数

在按值传递参数时需要传递参数。它们的顺序应与方法规范中的参数顺序相同。参数可以通过值或引用传递。

通过值传递参数是使用参数调用方法。 通过这样将参数值将传递给参数。

**示例**

以下程序显示了按值传递参数的示例。 即使在方法调用之后，参数的值仍保持不变。

```java
public class SwappingExample {

   public static void main(String[] args) {
      int a = 30;
      int b = 45;
      System.out.println("Before swapping, a = " + a + " and b = " + b);

      // 调用交换方法
      swapFunction(a, b);
      System.out.println("Now, Before and After swapping values will be same here:");
      System.out.println("After swapping, a = " + a + " and b is " + b);
   }

   public static void swapFunction(int a, int b) {
      System.out.println("Before swapping(Inside), a = " + a + " b = " + b);
      // 交换 n1 和 n2
      int c = a;
      a = b;
      b = c;
      System.out.println("After swapping(Inside), a = " + a + " b = " + b);
   }
}
```

```shell
cd ~/java && javac SwappingExample.java
java SwappingExample
```

康康

## 方法重载

当一个类有两个或多个同名但方法不同参数的方法时，称为方法重载。 它与重写不同。 在重写中，方法具有相同的方法名称，类型，参数数量等。

在前面讨论的用于查找最小整数类型数的示例中，假设想要查找两个`double`类型的最小数值。 可引入重载的概念以创建具有相同名称但不同参数的两个或更多方法。

文件名: ExampleOverloading.java

```java
public class ExampleOverloading {

   public static void main(String[] args) {
      int a = 11;
      int b = 6;
      double c = 7.3;
      double d = 9.4;
      int result1 = getMin(a, b);

      // 具有相同函数名称，但数字不同参数
      double result2 = getMin(c, d);
      System.out.println("Minimum Value = " + result1);
      System.out.println("Minimum Value = " + result2);
   }

   // 处理 int 类型的数值(方法重载)
   public static int getMin(int n1, int n2) {
      int min;
      if (n1 > n2)
         min = n2;
      else
         min = n1;

      return min; 
   }

   //  处理 double 类型的数值(方法重载)
   public static double getMin(double n1, double n2) {
     double min;
      if (n1 > n2)
         min = n2;
      else
         min = n1;

      return min; 
   }
}
```

重载方法使程序可读。这里，两个方法由相同的名称给出但具有不同的参数类型。结果是求`int`类型和`double`类型的最小数。

```shell
cd ~/java && javac ExampleOverloading.java
java ExampleOverloading
```

康康

## 使用命令行参数

有时希望在运行程序时将一些信息传递给程序。它是通过将命令行参数传递给`main()`来实现的。

命令行参数是执行时在命令行上直接跟随程序名称的信息。 要访问Java程序中的命令行参数非常简单。 它们作为字符串存储在传递给`main()`的`String`类型数组中。

**示例**

以下程序显示传递给程序的所有命令行参数 - 

文件名:CommandLine.java

```java
public class CommandLine {

   public static void main(String args[]) { 
      for(int i = 0; i<args.length; i++) {
         System.out.println("args[" + i + "]: " +  args[i]);
      }
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac CommandLine.java
java CommandLine
```

## this 关键字

`this`是Java中的一个关键字，用作对当前类对象的引用，在实例方法或构造函数中。 使用它可以引用类的成员，例如：构造函数，变量和方法。

> 注 - `this`关键字仅在实例方法或构造函数中使用。

通常，`this`关键字用于 

如果实例变量在构造函数或方法中具有相同的名称，则将它们与局部变量区分开来。

```java
class Student {
 private int age;   
 Student(int age) {
    this.age = age;
 }
}
```

从类中的其他方法调用一种类型的构造函数(参数化构造函数或默认值)，称为显式构造函数调用。

```java
class Student {
 int age
 Student() {
    this(20);
 }

 Student(int age) {
    this.age = age;    
 }
}
```

以下是使用`this`关键字访问类成员的示例

文件名:ThisExample.java

```java
public class ThisExample {
   // 实例变量：num
   int num = 10;
   ThisExample() {
      System.out.println("This is an example program on keyword this");    
   }

   ThisExample(int num) {
      // 调用默认构造方法
      this();

      // 将局部变量 num 分配给实例变量 num 
      this.num = num;
   }

   public void greet() {
      System.out.println("Hi Welcome to Yiibai");
   }

   public void print() {
      // 局部变量：num
      int num = 20;

      // 打印局部变量
      System.out.println("value of local variable num is : "+num);

      // 打印实例变量
      System.out.println("value of instance variable num is : "+this.num);

      // 调用类方法 
      this.greet();     
   }

   public static void main(String[] args) {
      // 实例化该类
      ThisExample obj1 = new ThisExample();

      // 调用 print 方法
      obj1.print();

      //通过参数化构造函数将新值传递给 num 变量
      ThisExample obj2 = new ThisExample(30);

      // 再次调用 print 方法
      obj2.print(); 
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac ThisExample.java
java ThisExample
```

## 变量参数(var-args)

JDK 1.5允许将可变数量的相同类型的参数传递给方法。方法中的参数声明如下 - 

```java
typeName... parameterName
```

在方法声明中，指定类型后跟省略号(`...`)。 在方法中只能指定一个可变长度参数，并且此参数必须是最后一个参数。

文件名: VarargsDemo.java

```java
public class VarargsDemo {

   public static void main(String args[]) {
       // 使用变量参数调用方法
       printMax(314, 321, 213, 212, 356.5);
       printMax(new double[]{1, 2, 3});
   }

   public static void printMax( double... numbers) {
      if (numbers.length == 0) {
         System.out.println("No argument passed");
         return;
      }

      double result = numbers[0];

      for (int i = 1; i <  numbers.length; i++)
      if (numbers[i] >  result)
      result = numbers[i];
      System.out.println("参数列表中的最大值是：" + result);
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac VarargsDemo.java
java VarargsDemo
```

##  finalize()方法

finalize()方法在垃圾收集器对象最终销毁之前调用，它可用于确保对象完全终止。例如，可以使用`finalize()`来确保该对象拥有的打开文件已关闭。

要将终结器添加到类中，只需定义`finalize()`方法即可。只要Java方法要回收该类的对象，它就会调用该方法。

在`finalize()`方法中，将指定在销毁对象之前必须执行的操作。`finalize()`方法有这种一般形式 - 

```java
protected void finalize( ) {
   // finalization code here
}
```

这里，关键字`protected`是一个修辞符，它阻止通过类外部定义的代码访问`finalize()`。
我们无法知道Java何时或甚至是否将执行`finalize()`方法。如果程序在垃圾收集发生之前结束，则`finalize()`将不会执行。
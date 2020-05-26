# Java 非访问修饰符

Java提供了许多非访问修饰符来实现许多其他功能。

- `static`修饰符用于创建类方法和变量。
- `final`修饰符用于完成类，方法和变量的实现。
- `abstract`修饰符用于创建抽象类和方法。
- `synchronized`和`volatile`修饰符，用于线程。

下面来逐个了解和学习这些非访问修饰符。

#### static修饰符

静态变量**

`static`关键字用于创建独立于类实例的变量。无论类的实例数有多少个，都只存在一个静态变量副本。静态变量也称为类变量。局部变量不能声明为`static`。

静态方法**

`static`关键字用于创建独立于类实例的方法。
静态方法不能使用作为类的对象的实例变量，静态方法也叫作类方法。静态方法从参数中获取所有数据并从这些参数计算某些内容，而不引用变量。可以使用类名后跟一个点(`.`)以及变量或方法的名称来访问类变量或方法。

**示例**

- `static`修饰符用于创建类方法和变量，如下例所示

文件名:InstanceCounter.java

```java
public class InstanceCounter {

   private static int numInstances = 0;

   protected static int getCount() {
      return numInstances;
   }

   private static void addInstance() {
      numInstances++;
   }

   InstanceCounter() {
      InstanceCounter.addInstance();
   }

   public static void main(String[] arguments) {
      System.out.println("Starting with " + InstanceCounter.getCount() + " instances");

      for (int i = 0; i < 500; ++i) {
         new InstanceCounter();
      }
      System.out.println("Created " + InstanceCounter.getCount() + " instances");
   }
}
```

```shell
cd ~/java && javac InstanceCounter.java
java InstanceCounter
```

康康

## final修饰符

**final变量**

final变量只能显式地初始化一次，声明为`final`的引用变量永远不能重新分配以引用不同的对象。但是，可以更改对象内的数据。 因此，可以更改对象的状态，但不能更改引用。
对于变量，`final`修饰符通常与`static`一起使用，以使常量成为类变量。

**示例**

文件名:TestFinal.java

```java
public class TestFinal {
   final int value = 10;

   // 以下是声明常量的示例：
   public static final int BOXWIDTH = 6;
   static final String TITLE = "Manager";

   public void changeValue() {
      value = 12;   // 会出错，不能重新赋值
   }
}
```

```bash
cd ~/java && javac TestFinal.java
java TestFinal
```

康康

**final方法**

任何子类都不能覆盖`final`方法。 如前所述，`final`修饰符可防止在子类中修改方法。

声明`final`方法的主要目的是不让其它人改变方法的内容。

**示例**
可以在类声明中使用`final`修饰符声明方法，如下例所示 - 

```java
public class Test {
   public final void changeName() {
      // 方法主体
   }
}
```

**final类**

使用声明为`final`的类的主要目的是防止类被子类化。 如果一个类被标记为`final`，那么这个类不能被其它类继承。

**示例**

```java
public final class Test {
   // body of class
}
```

#### abstract饰符

**抽象类**

抽象(`abstract`)类不能实例化。如果一个类声明为抽象(`abstract`)，那么唯一的目的是扩展该类。

一个类不能是同时是`abstract`和`final`(因为`final`类不能被扩展)。 如果一个类包含抽象方法，那么该类应该被声明为`abstract`。 否则，将抛出编译错误。

抽象类可以包含抽象方法以及普通方法。

**示例**

```java
abstract class Caravan {
   private double price;
   private String model;
   private String year;
   public void getYear(String y){}；// 这是一个普通方法
   public abstract void goFast();   // 这是一个抽象方法
   public abstract void changeColor();// 这是一个抽象方法
}
```

**抽象方法**
抽象方法是在没有任何实现的情况下声明的方法。 方法体(实现)由子类提供。 抽象方法永远不会是最终的或严格的。

扩展抽象类的任何类都必须实现超类的所有抽象方法，除非子类也是抽象类。

如果一个类包含一个或多个抽象方法，那么该类必须声明为abstract。 抽象类不需要包含抽象方法。

抽象方法以分号结尾。 示例：public abstract sample();

**示例**

```java
public abstract class SuperClass {
   abstract void m();   // 抽象方法
}

class SubClass extends SuperClass {
   // 实现抽象方法
   void m() {
      // 实现代码.........
   }
}
```

### synchronized修饰符

`synchronized`关键字用于指示一次只能访问一个方法的方法。`synchronized`修饰符可以应用于四个访问级别修饰符中的任何一个。

**示例**

```java
public synchronized void showDetails() {
   .......
}
```

#### transient修饰符

实例变量标记为`transient`，表示JVM在序列化包含它的对象时跳过特定变量。

此修饰符包含在创建变量的语句中，位于变量的类或数据类型之前。

**示例**

```java
public transient int limit = 55;   // will not persist
public int b;   // will persist
```

#### volatile修饰符

`volatile`修饰符用于让JVM知道访问变量的线程必须始终将其自己的变量私有副本与内存中的主副本合并。

访问`volatile`变量会同步主内存中变量的所有缓存复制。 `volatile`只能应用于实例变量，类型为`private`。 `volatile`对象引用可以为`null`。

**示例**

文件名：MyRunnable.java

```java
public class MyRunnable implements Runnable {
   private volatile boolean active;

   public void run() {
      active = true;
      while (active) {   // line 1
         // some code here
      }
   }

   public void stop() {
      active = false;   // line 2
   }
}
```

通常，在一个线程(使用`Runnable`开始的线程)中调用`run()`，并从另一个线程调用`stop()`。 如果在第`1`行中使用了`active`的缓存值，那么当在第`2`行中将`active`设置为`false`时，循环可能不会停止。

```bash
cd ~/java && javac MyRunnable.java
java MyRunnable
```

康康
# Java 对象和类

Java是面向对象的语言。 作为具有面向对象功能的语言，Java支持以下基本概念 

- 多态性
- 继承
- 封装
- 抽象化
- 类
- 对象
- 实例
- 方法
- 消息传递

在本节中，我们将学习两个概念 - 类和对象。

- **对象** - 对象具有状态和行为。 例如：一只狗的状态有：颜色，名称，品种，它的行为有：摇尾巴，吠叫，吃东西。 对象是类的实例。
- **类** - 可以将类定义为描述其类型对象支持的行为/状态的模板/蓝图。

## Java对象

下面将深入了解什么是对象。 如果考虑现实世界，可以在我们周围找到许多对象，如：汽车，狗，人等等。所有这些对象都有状态和行为。

如果考虑一只狗，那么它的状态是 - 名称，品种，颜色，并且它的行为是 - 吠叫，摇尾巴，跑步。

如果将软件对象与实际对象进行比较，则它们具有非常相似的特征。
软件对象也具有状态和行为。 软件对象的状态存储在字段中，行为通过方法显示。
因此，在软件开发中，方法对对象的内部状态进行操作，并且对象到对象的通信是通过方法完成的。

## Java类

类是创建单个对象的蓝图(模板)。以下是一个类的示例代码。


```java
public class Dog {
   String breed;
   int age;
   String color;

   void barking() {
   }

   void hungry() {
   }

   void sleeping() {
   }
}
```

类可以包含以下任何变量类型。

- **局部变量** - 在方法，构造函数或块中定义的变量称为局部变量。 变量将在方法中声明和初始化，并且在方法完成时将销毁变量。
- **实例变量** - 实例变量是类中的变量，但在方法之外。 在实例化类时初始化这些变量。 可以从类的任何方法，构造函数或块内部访问实例变量。
- **类变量** - 类变量是使用`static`关键字修饰，它是在类中的方法之外声明的变量。

一个类可以有任意数量的方法。 在上面的例子中，`barking()`，`hungry()`和`sleeping()`都是类的方法。

以下是在学习Java语言类和对象时，需要了解的一些重要主题内容。

#### 构造函数

在讨论类时，最重要的子主题之一是构造函数。 每个类都有一个构造函数。 如果没有为类显式编写构造函数，Java编译器会自动为该类构建一个默认构造函数。

每次创建新对象时，都将至少调用一个构造函数。构造函数的主要规则是它与类具有相同的名称。 一个类可以有多个构造函数。

以下是构造函数的示例 - 

```java
public class Dog {
   // 无参数构造函数
   public Dog() {
   }
   // 有参数构造函数
   public Dog(String name) {
      // 此构造函数有一个参数：name。
   }
}
```

Java还支持单实例类，它是一种创建一个类只有一个实例设计模式。

> 注意 - 有两种不同类型的构造函数。 我们将在后续章节中详细讨论构造函数。

#### 创建对象

如前所述，类提供了对象的蓝图。一个对象是从一个类创建的。 在Java中，`new`关键字用于创建新对象。

从类创建对象时有三个步骤 - 

- 声明 - 具有变量名称和对象类型的变量声明。
- 实例化 - `new`关键字用于创建对象。
- 初始化 - `new`关键字后跟对构造函数的调用，此调用初始化新对象。

以下是创建对象的示例代码

文件名:Dog.java

```java
public class Dog {
   public Dog(String name) {
      // 这个构造函数有一个参数：anem
      System.out.println("传入的参数值是: " + name );
   }

   public static void main(String []args) {
      // 以下语句将创建一个对象: myDog
      Dog myDog = new Dog( "小屁狗" );
   }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac Dog.java
java Dog
```

#### 访问实例变量和方法

通过创建的对象访问实例变量和方法。 要访问实例变量，以下是完全限定的路径 - 

```java
/* 首先创建一个对象 */
ObjectReference = new Constructor();

/* 调用变量如下 */
ObjectReference.variableName;

/* 现在，可以按如下方式调用类方法 */
ObjectReference.MethodName();
```

下面示例说明如何访问类的实例变量和方法。

文件名:Dog1.java

```java
public class Dog1 {
    int dogAge;

    public Dog(String name) {
        // 此构造函数有一个参数：name
        System.out.println("设置的小狗名字是: " + name);
    }

    public void setAge(int age) {
        dogAge = age;
    }

    public int getAge() {
        System.out.println("小狗的年龄是: " + dogAge);
        return dogAge;
    }

    public static void main(String[] args) {
        /* 创建对象 */
        Dog myDog = new Dog("小屁狗");

        /* 调用方法来设置狗的年龄 */
        myDog.setAge(2);

        /* 调用另一个方法来获取狗的年龄 */
        myDog.getAge();

        /* 也可以按如下方式访问实例变量：dogAge */
        System.out.println("变量的值是:" + myDog.dogAge);
    }
}
```

```shell
cd ~/java && javac Dog1.java
java Dog1
```

康康

#### 源文件声明规则

在源文件中声明类，`import`语句和`package`语句时，这些规则是必不可少的。

- 每个源文件只能有一个`public`类。
- 源文件可以有多个非`public`类。
- `public`类名称也应该是源文件的名称，最后以`.java`作为扩展名。 例如：类名是`public class Employee{}`，那么源文件应该是：`Employee.java`。
- 如果在包内定义了类，则`package`语句应该是源文件中的第一个语句。
- 如果存在`import`语句，则必须在`package`语句和类声明之间写入它们。如果没有`package`语句，则`import`语句应该是源文件中的第一行。

类具有多个访问级别，并且有不同类型的类; 抽象类，`final`类等。我们将在访问修饰符章节中解释所有这些。

除了上面提到的类类型之外，Java还有一些特殊类：内部类和匿名类。

#### Java包

简而言之，它是一种对类和接口进行分类的方法。 在Java中开发应用程序时，将编写数百个类和接口，因此必须对这些类进行分类，以使生活变得更加容易。Java包也是用于解决命名冲突的问题。

#### import语句

在Java中，如果给出了包含包和类名的完全限定名称，则编译器可以快速地找到源代码或类。 `import`语句是一种为编译器提供正确位置以查找特定类的方法。

例如，以下行将要求编译器加载目录`java_installation/java/io`中可用的所有类 - 

```java
import java.io.*;
```

## 一个简单学习案例

在这个学习案例中，将创建两个类。 它们是：`Employee`和`EmployeeTest`。

首先打开记事本并添加以下代码。`Employee`类是公共(`public`)类。因此使用文件名称为：*Employee.java* 保存此源文件。

`Employee`类有四个实例变量 - `name`, `age`, `designation` 和 `salary`。 该类有一个显式定义的构造函数，它接受一个参数。

文件名:Employee.java

```java
import java.io.*;

public class Employee {

    String name;
    int age;
    String jobPosition;
    double salary;

    // 这是Employee类的构造函数
    public Employee(String name) {
        this.name = name;
    }

    // 设置员工的年龄，将empAge的分配给变量：age。
    public void empAge(int empAge) {
        age = empAge;
    }

    /* 设置员工的工作岗位. */
    public void setJobPosition(String jobPosit) {
        jobPosition = jobPosit;
    }

    /* 设置员工的薪水，将empSalary的分配给变量：salary。 */
    public void empSalary(double empSalary) {
        salary = empSalary;
    }

    /* 打印员工详细信息 */
    public void printEmployee() {
        System.out.println("------------------------------------");
        System.out.println("姓名:" + name);
        System.out.println("年龄:" + age);
        System.out.println("工作岗位:" + jobPosition);
        System.out.println("薪水:" + salary);
    }
}
```

如本教程前面所述，程序从`main`方法开始执行。 因此，要运行这个`Employee`类，应该有一个`main`方法，并且应该创建对象。接下来将为这些任务创建一个单独的类：`EmployeeTest`。

在`EmployeeTes`t类中，它创建`Employee`类的两个实例，并为每个对象调用方法以为每个变量赋值。将以下代码保存在*EmployeeTest.java* 文件中。

文件名:EmployeeTest.java

```java
import java.io.*;
public class EmployeeTest {

   public static void main(String args[]) {
      /* 使用构造函数创建两个对象 */
      Employee empOne = new Employee("Maxsu");
      Employee empTwo = new Employee("张小龙");

      // 为每个创建的对象调用方法
      empOne.empAge(26);
      empOne.setJobPosition("高级软件工程师");
      empOne.empSalary(15999);
      empOne.printEmployee();

      empTwo.empAge(42);
      empTwo.setJobPosition("产品经理");
      empTwo.empSalary(999999);
      empTwo.printEmployee();
   }
}
```

```bash
cd ~/java && javac Employee.java & javac EmployeeTest.java
java EmployeeTest
```

康康
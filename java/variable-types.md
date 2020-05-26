# Java 变量类型

变量提供了程序可以操作的命名存储。 Java中的每个变量都有一个类型，它决定了变量内存的大小和布局; 可以存储在该存储器中的值的范围; 以及可以应用于变量的操作集。

变量需要先声明才能使用，以下是变量声明的基本形式 - 

```java
data type variable [ = value][, variable [ = value] ...] ;
```

这里`data type`是Java的数据类型之一，`variable`是变量的名称。要声明具有相同类型的多个变量，可以使用逗号分隔列表。

以下是Java中变量声明和初始化的示例 - 

```java
int a, b, c;         // 声明三个int类型变量：a, b 和 c
int a = 10, b = 10;  // 初始化它们的值
byte B = 22;         // 声明并初始化一个 byte 类型的变量：B
double pi = 3.14159; // 声明并赋值一个 double 类型的变量：PI
char a = 'a';        // 声明char类型变量 a，并初始化值为：'a'
```

本章将解释Java语言中的各种变量类型。Java中有三种变量 - 

- 局部变量
- 实例变量
- 类/静态变量

## 1. 局部变量

- 局部变量一般在方法，构造函数或块中声明。
- 程序进入方法，构造函数或块时会创建局部变量，并且一旦退出方法，构造函数或块，变量就会销毁。
- 访问修饰符不能用于局部变量。
- 局部变量仅在声明的方法，构造函数或块中可见。
- 局部变量在内部实现堆栈级别。
- 局部变量没有默认值，因此应声明局部变量后，在第一次使用之前为它分配初始值。

**示例**

在这里，`age`是一个局部变量。 这是在`dogAge()`方法中定义的，它的范围仅限于此方法。

文件名:LocalVariableTest.java

```java
public class LocalVariableTest {
   public void dogAge() {
      int age = 0;
      age = age + 5;
      System.out.println("Dog age is : " + age);
   }

   public static void main(String args[]) {
      Test test = new Test();
      test.dogAge();
   }
}
```

```bash
cd ~/java && javac LocalVariableTest.java
java LocalVariableTest
```

康康

**示例**

下面示例中使用变量 `age` ，但不初始化它，因此在编译时会出错。

文件名:LocalVariableTest1.java

```java
public class LocalVariableTest1 {
   public void dogAge() {
      int age;
      age = age + 5;
      System.out.println("Dog age is : " + age);
   }

   public static void main(String args[]) {
      Test test = new Test();
      test.dogAge();
   }
}
```

```bash
cd ~/java && javac LocalVariableTest1.java
java LocalVariableTest1
```

康康

执行上面示例代码，得到以下结果(出错)：

```
Test.java:4:variable number might not have been initialized
age = age + 5;
         ^
1 error
```

## 实例变量

- 实例变量在类中声明，但在方法，构造函数或块之外。
- 为堆中的对象分配空间时，将为每个实例变量值创建一个槽。
- 使用关键字`new`创建对象时会创建实例变量，并在销毁对象时销毁实例变量。
- 实例变量包含由多个方法，构造函数或块引用的值，或者在整个类中存在的对象状态的基本部分。
- 实例变量可以在使用之前或之后在类级别中声明。
- 可以为实例变量给出访问修饰符。
- 实例变量对于类中的所有方法，构造函数和块都是可见的。 通常，建议将这些变量设为私有(访问级别)。 但是，可以使用访问修饰符为这些变量提供子类的可见性。
- 实例变量具有默认值。 对于数字，默认值为`0`，对于布尔值，它为`false`，对于对象引用，它为`null`。 可以在声明期间或构造函数中指定值。
- 可以通过调用类中的变量名来直接访问实例变量。 但是，在静态方法中(当实例变量具有可访问性时)，应使用完全限定名称调用它们，如：`ObjectReference.VariableName`。

**示例代码**

文件名:EmployeeInstanceVariable.java

```java
import java.io.*;
public class EmployeeInstanceVariable {

   // 此实例变量对于子类都是可见的。
   public String name;

   // salary 变量仅在Employee类中可见。
   private double salary;

   // name变量在构造函数中指定。
   public Employee (String empName) {
      name = empName;
   }

   // 为 salary 变量赋值
   public void setSalary(double empSal) {
      salary = empSal;
   }

   // 此方法打印员工详细信息。
   public void printEmp() {
      System.out.println("name  : " + name );
      System.out.println("salary :" + salary);
   }

   public static void main(String args[]) {
      Employee empOne = new Employee("Maxsu");
      empOne.setSalary(15999);
      empOne.printEmp();
   }
}
```

```shell
cd ~/java && javac EmployeeInstanceVariable.java
java EmployeeInstanceVariable
```

康康

## 类/静态变量

- 类变量(也称为静态变量)在类中使用`static`关键字声明，但在方法，构造函数或块之外。
- 每个类只有一个每个类变量的副本，无论从中创建多少个对象。
- 除了声明为常量之外，很少使用静态变量。常量是声明为`public/private`，`final`和`static`的变量。常量的初始值不能更改。
- 静态变量存储在静态存储器中。 除了声明的`final`之外，很少使用静态变量，并将其用作公共或私有常量。
- 程序启动时会创建静态变量，程序停止时会销毁静态变量。
- 可见性类似于实例变量。 但是，大多数静态变量都是公共的，因为它们必须可供该类用户使用。
- 默认值与实例变量相同。 对于数字，默认值为`0`; 对于布尔类型来说，默认值为`false`; 对于对象引用，默认值为`null`。 可以在声明期间或构造函数中指定值。 此外，可以在特殊的静态初始化程序块中分配值。
- 可以通过使用类名`ClassName.VariableName`调用来访问静态变量。
- 将类变量声明为`public static final`时，变量名(常量)都是大写的。 如果静态变量不是`public`和`final`，则命名语法与实例和局部变量命名规则相同。

**示例**

文件名:EmployeeStaticVariable.java

```java
import java.io.*;
public class EmployeeStaticVariable {

   // salary变量是一个私有静态变量
   private static double salary;

   // DEPARTMENT是一个常量
   public static final String DEPARTMENT = "研发部";

   public static void main(String args[]) {
      salary = 19999;
      System.out.println(DEPARTMENT + "平均薪水:" + salary);
   }
}
```

```shell
cd ~/java && javac EmployeeStaticVariable.java
java EmployeeStaticVariable
```

康康

> 注 - 如果从外部类访问变量，则应作为：`Employee.DEPARTMENT`。
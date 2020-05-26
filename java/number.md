# Java Number类

通常，当要在Java编程中使用数字时，可以使用原始数据类型，如：`byte`，`int`，`long`，`double`等。

**示例**

```java
int i = 5000;
float gpa = 13.65;
double mask = 0xaf;
```

但是，在开发过程中，我们遇到的是需要使用对象而不是原始数据类型的情况。要实现这一点，可使用Java提供的包装类。

所有包装类(如：`Integer`，`Long`，`Byte`，`Double`，`Float`，`Short`)都是抽象类`Number`的子类。

![Number类](./images/number.jpg)

包装类的对象包含或包装其各自的基本数据类型。将原始数据类型转换为对象称为**装箱**，编译器会对此进行处理。 因此，在使用包装器类时，只需将原始数据类型的值传递给包装类的构造函数就可以对它进行对应的操作。

并且包装对象将转换回原始数据类型，并且此过程称为**拆箱**。 `Number`类是`java.lang`包的一部分。

以下是装箱和拆箱的示例

文件名: NumberTest.java

```java
public class NumberTest {

   public static void main(String args[]) {
      Integer x = 5; // 装箱：将 int 添加到 Integer 对象
      x =  x + 1000;   // 拆箱：将Integer 对象转为 int 
      System.out.println(x); 
   }
}
```

当`x`赋予整数值时，编译器将整数装箱，因为`x`是整数对象。 之后，`x`又被拆箱，以便它们可以作为整数执行加法运算。

```bash
cd ~/java && javac NumberTest.java
java NumberTest
```

康康
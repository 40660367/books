# Scala 类和对象

本章将介绍如何在Scala编程中使用类和对象。类是对象的蓝图(或叫模板)。定义一个类后，可以使用关键字`new`来创建一个类的对象。 通过对象可以使用定义的类的所有功能。

下面的图通过一个包含成员变量(`name` 和 `rollNo`)和成员方法(`setName()`和`setRollNo()`)的`Student`类的例子来演示类和对象。最后都是类的成员。类是一个模板的东西，而对象是真实存在的。 在下图中，`Student`是一个类，而具体学生：*Harini*, *John*, 和 *Maria* 是学生类的对象，这此对象有是名字和注册号。

![img](./images\oob.jpg)

## 类基础

以下是在`Scala`中定义类的简单语法。这个类定义了两个变量`x`和`y`以及一个`move`方法，它没有返回值。

使用类的名称作为一个类构造函数，构造函数可以使用多个参数。 上面的代码定义了两个构造函数参数`xc`和`yc`; 它们在类的整个定义中都是可见的。

**语法**

```scala
class Point(xc: Int, yc: Int) {
   var x: Int = xc
   var y: Int = yc

   def move(dx: Int, dy: Int) {
      x = x + dx
      y = y + dy
      println ("Point x location : " + x);
      println ("Point y location : " + y);
   }
}
```

如本章前面所述，您可以使用关键字`new`来创建对象，然后访问类字段和方法，如下例所示：

文件名:oobNew.scala

```scala
import java.io._

class Point(val xc: Int, val yc: Int) {
   var x: Int = xc
   var y: Int = yc

   def move(dx: Int, dy: Int) {
      x = x + dx
      y = y + dy
      println ("Point x location : " + x);
      println ("Point y location : " + y);
   }
}

object oobNew {
   def main(args: Array[String]) {
      val pt = new Point(10, 20);

      // Move to a new location
      pt.move(10, 10);
   }
}
```

```bash
scala /share/lesson/scala/oobNew.scala
```

## 扩展类

在Scala中，我们可以扩展一个Scala类，使用与Java中相同的方式设计继承的类(使用`extends`关键字)，但有两个限制：方法重写需要`override`关键字，只有主构造函数可以通过参数调用基类构造函数。让我们扩展上面的类，并增加一个类的方法。

**例子**

让我们使用两个类`Point`作为一个例子(与上面一样)和`Location`类，`Location`类是一个使用`extends`关键字创建的继承类。 这样的“扩展”子句有两个效果：它使得`Location`类从`Point`类继承所有非私有成员，并且使类型`Location`成为`Point`类类型的子类型。 所以`Point`类被称为超类(父类)，`Location`类被称为子类。扩展一个类并继承父类的所有功能称为继承，但Scala允许只从一个类继承(不支持多继承)。

> 注意 - 在`Point`类中的`move()`方法和`Location`类中的`move()`方法不会覆盖`move`的相应定义，因为它们是不同的定义(例如，前者采用两个参数，后者采用三个参数)。

参考以下示例程序来实现继承

文件名:oobOverride.scala

```scala
import java.io._

class Point(val xc: Int, val yc: Int) {
   var x: Int = xc
   var y: Int = yc

   def move(dx: Int, dy: Int) {
      x = x + dx
      y = y + dy
      println ("Point x location : " + x);
      println ("Point y location : " + y);
   }
}

class Location(override val xc: Int, override val yc: Int,
   val zc :Int) extends Point(xc, yc){
   var z: Int = zc

   def move(dx: Int, dy: Int, dz: Int) {
      x = x + dx
      y = y + dy
      z = z + dz
      println ("Point x location : " + x);
      println ("Point y location : " + y);
      println ("Point z location : " + z);
   }
}

object oobOverride {
   def main(args: Array[String]) {
      val loc = new Location(10, 20, 15);

      // Move to a new location
      loc.move(10, 10, 5);
   }
}
```

```bash
scala /share/lesson/scala/oobOverride.scala
```

## 隐性类

当类在范围内时，隐式类允许与类的主构造函数进行隐式对话。隐式类是一个标有`'implicit'`关键字的类。此功能在*Scala 2.10*中引入。

> 语法 - 以下是隐式类的语法。这里，隐式类始终位于对象范围内，所有方法定义都被允许，因为隐式类不能是顶级类。

**语法**

```scala
object <object name> {
   implicit class <class name>(<Variable>: Data type) {
      def <method>(): Unit =
   }
}
```

**例子**

下面演示如何使用隐式类，创建一个名称为*IntTimes*的隐式类，并定义一个`times()`方法。`times()`包含一个循环事务，它将按给定的次数执行语句。假设要执行`4`次`println(“”Hello“)`语句。

以下是示例程序代码。在这个例子中，使用了两个对象类(*Run* 和 *Demo*)，将这两个类保存在不同的文件中，名称如下 - 

文件名:oobRun.scala

```scala
object oobRun {
   implicit class IntTimes(x: Int) {
      def times [A](f: =>A): Unit = {
         def loop(current: Int): Unit =

         if(current > 0){
            f
            loop(current - 1)
         }
         loop(x)
      }
   }
}
```

文件名:oobImplicit.scala

```scala
import oobRun._

object oobImplicit {
   def main(args: Array[String]) {
       println("hello")
   }
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobImplicit.scala
```

**注** - 

- 隐式类必须在另一个类/对象/特征中定义(不在顶层)。
- 隐式类在其构造函数中只能使用一个非默认参数。
- 隐式类作用域中不可以具有与隐式类相同名称的的任何方法，成员或对象。

## 单例对象

Scala比Java更面向对象，因为在Scala中不能拥有静态成员，Scala它使用单例对象。单例是一种只能有一个实例的对象。使用`object`关键字对象而不是类关键字创建单例。由于无法实例化单例对象，因此无法将参数传递给主构造函数。下面列出Scala使用单例对象的所有示例。

以下是实现单例的示例程序

文件名:oobSingle.scala

```scala
import java.io._

class Point(val xc: Int, val yc: Int) {
   var x: Int = xc
   var y: Int = yc

   def move(dx: Int, dy: Int) {
      x = x + dx
      y = y + dy
   }
}

object oobSingle {
   def main(args: Array[String]) {
      val point = new Point(10, 20)
      printPoint

      def printPoint{
         println ("Point x location : " + point.x);
         println ("Point y location : " + point.y);
      }
   }
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobSingle.scala
```
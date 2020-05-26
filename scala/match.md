# Scala 模式匹配

模式匹配是Scala函数值和闭包后第二大应用功能。Scala为模式匹配提供了极大的支持，处理消息。

模式匹配包括一系列备选项，每个替代项以关键字大小写为单位。每个替代方案包括一个模式和一个或多个表达式，如果模式匹配，将会进行评估计算。箭头符号`=>`将模式与表达式分离。

尝试以下示例程序，它显示匹配的整数值。

**示例**

文件名:match.scala

```scala
object match {
   def main(args: Array[String]) {
      println(matchTest(3))
   }

   def matchTest(x: Int): String = x match {
      case 1 => "one"
      case 2 => "two"
      case _ => "many"
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/match.scala
```



具有`case`语句的块定义了一个将整数映射到字符串的函数。*match*关键字提供了一种方便的方式来应用一个函数(如上面的模式匹配函数)到一个对象。

请尝试以下示例程序，其中的值与不同类型的模式相匹配。

文件名:matchCase.scala

```scala
object matchCase {
   def main(args: Array[String]) {
      println(matchTest("two"))
      println(matchTest("test"))
      println(matchTest(1))
   }

   def matchTest(x: Any): Any = x match {
      case 1 => "one"
      case "two" => 2
      case y: Int => "scala.Int"
      case _ => "many"
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/matchCase.scala
```



## 使用case类匹配

`case`类是用于与`case`表达式进行模式匹配的特殊类。在语法上，这些是带有特殊修饰符的标准类：`case`。

尝试以下，它是一个简单的模式匹配示例使用`case`类。

文件名:matchCaseClass.scala

```scala
object matchCaseClass {
   def main(args: Array[String]) {
      val alice = new Person("Alice", 25)
      val bob = new Person("Bob", 32)
      val charlie = new Person("Charlie", 32)

      for (person <- List(alice, bob, charlie)) {
         person match {
            case Person("Alice", 25) => println("Hi Alice!")
            case Person("Bob", 32) => println("Hi Bob!")
            case Person(name, age) => println(
               "Age: " + age + " year, name: " + name + "?")
         }
      }
   }
   case class Person(name: String, age: Int)
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/matchCaseClass.scala
```



添加`case`关键字会导致编译器自动添加一些有用的功能。该关键字表示与模式匹配中的`case`表达式的关联。

**首先**，编译器会自动将构造函数转换为不可变字段(`vals`)。 `val`关键字是可选的。 如果想要可变字段，请使用`var`关键字。 因此，构造函数参数列表更短。

**其次**，编译器会自动对类进行`equals`，`hashCode`和`toString`方法，该方法使用指定为构造函数参数的字段。 所以，我们不再需要自己的`toString()`方法。

最后，`Person`类的主体变为空，因为我们没有定义任何方法！
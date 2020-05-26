# Scala 柯里化函数(currying)

柯里化(*Currying*)函数是一个带有多个参数，并引入到一个函数链中的函数，每个函数都使用一个参数。 柯里化(*Currying*)函数用多个参数表定义，如下所示：

```scala
def strcat(s1: String)(s2: String) = s1 + s2
```

或者，还可以使用以下语法定义柯里化(*Currying*)函数 -

```scala
def strcat(s1: String) = (s2: String) => s1 + s2
```

以下是调用柯里化(*Currying*)函数的语法 -

```scala
strcat("foo")("bar")
```

您可以根据需要在柯里化(*Currying*)函数上定义两个以上的参数。

**示例:**

尝试下面一个简单的示例程序用来了解如何使用柯里化(*Currying*)函数

文件名:functionCurrying.scala

```scala
object functionCurrying {
   def main(args: Array[String]) {
      val str1:String = "Hello, "
      val str2:String = "Scala!"

      println( "str1 + str2 = " +  strcat(str1)(str2) )
   }

   def strcat(s1: String)(s2: String) = {
      s1 + s2
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/functionCurrying.scala
```


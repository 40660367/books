# Scala 可变参数的函数

Scala允许指定函数的最后一个参数可重复。 这允许客户端将可变长度参数列表传递给函数。 这里，打印字符串函数里面的`args`类型，被声明为类型`String *`，实际上是`Array [String]`。

尝试以下程序，这是一个简单的例子来演示如何使用带有可变参数的函数。

文件名:functionVariableArguments.scala

```scala
object functionVariableArguments {
   def main(args: Array[String]) {
      printStrings("Hello", "Scala", "Python");
   }

   def printStrings( args:String* ) = {
      var i : Int = 0;

      for( arg <- args ){
         println("Arg value[" + i + "] = " + arg );
         i = i + 1;
      }
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/functionVariableArguments.scala
```
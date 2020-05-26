# Scala 命名参数的函数

在正常的函数调用中，调用的参数按照被调用函数定义的参数顺序逐个匹配。命名参数允许您以不同的顺序将参数传递给函数。语法只是每个参数前面都有一个参数名称和一个等号。

尝试以下程序，它是一个简单的例子来显示具有命名参数的函数。

文件名:functionNamedArguments.scala

```scala
object functionNamedArguments {
   def main(args: Array[String]) {
      printInt(b = 11, a = 12);
   }

   def printInt( a:Int, b:Int ) = {
      println("Value of a : " + a );
      println("Value of b : " + b );
   }
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/functionNamedArguments.scala
```
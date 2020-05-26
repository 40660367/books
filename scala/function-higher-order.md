# Scala 高阶函数(high order function)

Scala允许定义高阶函数。它是将其他函数作为参数或其结果是函数的函数。

尝试以下示例程序，`apply()`函数接受另一个函数`f`和值`v`，并将函数`f`应用于`v`。

**示例**

文件名:functionHigherOrder.scala

```scala
object functionHigherOrder {
   def main(args: Array[String]) {
      println( apply( layout, 10) )
   }

   def apply(f: Int => String, v: Int) = f(v)

   def layout[A](x: A) = "[" + x.toString() + "]"
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/functionHigherOrder.scala
```
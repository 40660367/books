# Scala 嵌套函数(nested function)

Scala允许您定义函数内部的函数，而在其他函数中定义的函数称为局部函数。这是一个阶乘计算器的实现，我们使用传统的技术来调用第二个嵌套方法来完成工作。

尝试以下程序来了解如何实现嵌套函数。

**示例**

文件名:functioNested.scala

```scala
object functioNested {
   def main(args: Array[String]) {
      println( factorial(0) )
      println( factorial(1) )
      println( factorial(2) )
      println( factorial(3) )
   }

   def factorial(i: Int): Int = {
      def fact(i: Int, accumulator: Int): Int = {
         if (i <= 1)
            accumulator
         else
            fact(i - 1, i * accumulator)
      }
      fact(i, 1)
   }
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/functioNested.scala
```

像许多语言中的局部变量声明一样，嵌套方法仅在封闭方法中可见。如果您尝试在`factorial()`之外调用`fact()`，则会在编译器时出现错误。
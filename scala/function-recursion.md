# Scala 递归函数(recursion function)

递归在纯功能编程中起着重要作用，Scala支持递归函数。 递归表示一个函数可以重复调用自身。

尝试以下程序，它是一个很好的递归示例，它计算给定参数(数字)的阶乘。

**示例**

文件名:functionRecursion.scala

```scala
object functionRecursion {
   def main(args: Array[String]) {
      for (i <- 1 to 10)
         println( "Factorial of " + i + ": = " + factorial(i) )
   }

   def factorial(n: BigInt): BigInt = {  
      if (n <= 1)
         1  
      else    
      n * factorial(n - 1)
   }
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/functionRecursion.scala
```


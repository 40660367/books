# Scala 函数闭包(closure) 			

闭包是一个函数，它返回值取决于在此函数之外声明的一个或多个变量的值。

以下代码是一个匿名函数。

```scala
val multiplier = (i:Int) => i * 10
```

这里，函数体`i * 10`中使用的唯一变量是`i`，它被定义为该函数的一个参数。尝试以下代码 -

```scala
val multiplier = (i:Int) => i * factor
```

乘数有两个自由变量：`i`和`factor`。`i`是函数的一个正式参数。 因此，每当调用乘数时，它必然会有一个新的值。然而，`factor`不是一个正式的参数，那这是什么呢？ 再增加一行代码。

```scala
var factor = 3
val multiplier = (i:Int) => i * factor
```

现在`factor`参考了函数之外的变量，但是在闭合的范围内。函数引用`factor`，每次读取其当前值。 如果函数没有外部引用，那么它本身就会被简单地关闭，不需要外部上下文。

请尝试以下示例程序 - 

**例子**

文件名:functionClosure.scala

```scala
object functionClosure {
   def main(args: Array[String]) {
      println( "multiplier(1) value = " +  multiplier(1) )
      println( "multiplier(2) value = " +  multiplier(2) )
   }
   var factor = 3
   val multiplier = (i:Int) => i * factor
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/functionClosure.scala
```

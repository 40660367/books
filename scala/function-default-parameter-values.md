# Scala 指定默认参数值的函数

Scala 可以为函数参数指定默认参数值，使用了默认参数，你在调用函数的过程中可以不需要传递参数，这时函数就会调用它的默认参数值，如果传递了参数，则传递值会取代默认值。

**示例:**

文件名:functionDefaultParameterValues.scala

```scala
object functionDefaultParameterValues {
   def main(args: Array[String]) {
        println( "返回值 : " + addInt() );
   }
   def addInt( a:Int=6, b:Int=9 ) : Int = {
      var sum:Int = 0
      sum = a + b

      return sum
   }
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/functionDefaultParameterValues.scala
```
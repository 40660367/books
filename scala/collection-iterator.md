# Scala 迭代器(iterator)

迭代器不是集合，而是一种逐个访问集合元素的方法。 下一个迭代器的两个基本操作是`hasNext`。 对`it.next()`方法的调用将返回迭代器的下一个元素，并提高迭代器的状态。可以使用`Iterator`的`it.hasNext`方法判断是否还有更多元素返回。

迭代器返回的所有元素最直接的方法是使用`while`循环。让我们参考以下示例程序 - 

**示例**

文件名:iteratorAccess.scala

```scala
object iteratorAccess {
   def main(args: Array[String]) {
      val it = Iterator("a", "number", "of", "words")

      while (it.hasNext){
         println(it.next())
      }
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/iteratorAccess.scala
```

## 查找最小和最大值元素

可以使用`it.min`和`it.max`方法从迭代器中找出最小值和最大值元素。 在这里，我们使用`ita`和`itb`执行两个不同的操作，因为迭代器只能遍历一次。以下是示例程序。

文件名:iteratorMinMax.scala

```scala
object iteratorMinMax {
   def main(args: Array[String]) {
      val ita = Iterator(20,40,2,50,69, 90)
      val itb = Iterator(20,40,2,50,69, 90)

      println("Maximum valued element " + ita.max )
      println("Minimum valued element " + itb.min )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/iteratorMinMax.scala
```

## 查找迭代器的长度

可以使用`it.size`或`it.length`方法来查找迭代器中可用的元素数量。在这里，我们使用`ita`和`itb`执行两个不同的操作，因为迭代器只能遍历一次。 以下是示例程序的代码 - 

文件名:iteratorSize.scala

```scala
object iteratorSize {
   def main(args: Array[String]) {
      val ita = Iterator(20,40,2,50,69, 90)
      val itb = Iterator(20,40,2,50,69, 90)

      println("Value of ita.size : " + ita.size )
      println("Value of itb.length : " + itb.length )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/iteratorSize.scala
```

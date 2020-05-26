# Scala 集合(set)

Scala `Set`是相同类型成对的不同元素的集合。换句话说，一个集合是不包含重复元素的集合。 集合有两种：不可变(`immutable`)和可变(`mutable`)。可变对象和不可变对象之间的区别在于，当对象不可变时，对象本身无法更改。

默认情况下，Scala使用不可变的集合(`Set`)。 如果要使用可变集合(`Set`)，则必须明确导入`scala.collection.mutable.Set`类。 如果要在同一集合中使用可变集合和不可变集合，则可以继续引用不可变集作为集合(`Set`)，但可以将可变集合称为`mutable.Set`。

```scala
// Empty set of integer type
var s : Set[Int] = Set()

// Set of integer type
var s : Set[Int] = Set(1,3,5,7)
// 或者
var s = Set(1,3,5,7)
```

通过定义一个空集合，类型注释是必要的，因为系统需要将具体的类型分配给变量。

## 集合基本操作

所有对集合的操作都可以用以下三种方法来表示：

| 序号 | 方法    | 描述                                                |
| ---- | ------- | --------------------------------------------------- |
| 1    | head    | 此方法返回列表的第一个元素。                        |
| 2    | tail    | 此方法返回由除第一个之外的所有元素组成的列表。      |
| 3    | isEmpty | 如果列表为空，则此方法返回`true`，否则返回`false`。 |

以下示例显示如何使用上述方法。

**示例**

文件名:setAccess.scala

```scala
object setAccess {
   def main(args: Array[String]) {
      val fruit = Set("apples", "oranges", "pears")
      val nums: Set[Int] = Set()

      println( "Head of fruit : " + fruit.head )
      println( "Tail of fruit : " + fruit.tail )
      println( "Check if fruit is empty : " + fruit.isEmpty )
      println( "Check if nums is empty : " + nums.isEmpty )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/setAccess.scala
```

## 连接集合

您可以使用`++`运算符或`Set.++()`方法连接两个或多个集合，但是在添加集合时，它将删除重复的元素。

**示例**

以下是连接两个集合的例子 

文件名:setConcat.scala

```scala
object setConcat {
   def main(args: Array[String]) {
      val fruit1 = Set("apples", "oranges", "pears")
      val fruit2 = Set("mangoes", "banana")

      // use two or more sets with ++ as operator
      var fruit = fruit1 ++ fruit2
      println( "fruit1 ++ fruit2 : " + fruit )

      // use two sets with ++ as method
      fruit = fruit1.++(fruit2)
      println( "fruit1.++(fruit2) : " + fruit )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/setConcat.scala
```

## 在集合中查找最大值，最小元素

可以使用`Set.min`方法和`Set.max`方法来分别找出集合中元素的最大值和最小值。 以下是显示程序的示例。

文件名:setMinMax.scala

```scala
object setMinMax {
   def main(args: Array[String]) {
      val num = Set(5,6,9,20,30,45)

      // find min and max of the elements
      println( "Min element in Set(5,6,9,20,30,45) : " + num.min )
      println( "Max element in Set(5,6,9,20,30,45) : " + num.max )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/setMinMax.scala
```

## 查找交集值

可以使用`Set.＆`或`Set.intersect`方法来查找两个集合之间的交集(相交值)。尝试以下示例来显示用法。

文件名:setIntersect.scala

```scala
object setIntersect {
   def main(args: Array[String]) {
      val num1 = Set(5,6,9,20,30,45)
      val num2 = Set(50,60,9,20,35,55)

      // find common elements between two sets
      println( "num1.&(num2) : " + num1.&(num2) )
      println( "num1.intersect(num2) : " + num1.intersect(num2) )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/setIntersect.scala
```
# Scala 列表(list)

Scala列表与数组非常相似，列表的所有元素都具有相同的类型，但有两个重要的区别。 首先，列表是不可变的，列表的元素不能通过赋值来更改。 其次，列表表示一个链表，而数组是平的。

具有类型`T`的元素的列表的类型被写为`List[T]`。

尝试以下示例，这里列出了为各种数据类型定义的列表。

```scala
// List of Strings
val fruit: List[String] = List("apples", "oranges", "pears")

// List of Integers
val nums: List[Int] = List(1, 2, 3, 4)

// Empty List.
val empty: List[Nothing] = List()

// Two dimensional list
val dim: List[List[Int]] =
   List(
      List(1, 0, 0),
      List(0, 1, 0),
      List(0, 0, 1)
   )
```

所有列表都可以使用两个基本构建块定义，尾部为`Nil`和`::`，它的发音为`cons`。 `Nil`也代表空列表。以上列表可以定义如下。

```scala
// List of Strings
val fruit = "apples"::("oranges"::("pears"::Nil))

// List of Integers
val nums = 1::(2::(3::(4::Nil)))

// Empty List.
val empty = Nil

// Two dimensional list
val dim = (1::(0::(0::Nil))) ::
          (0::(1::(0::Nil))) ::
          (0::(0::(1::Nil)))::Nil
```

## 列表基本操作

列表上的所有操作都可以用以下三种方法表示。

| 序号 | 方法    | 描述                                                |
| ---- | ------- | --------------------------------------------------- |
| 1    | head    | 此方法返回列表的第一个元素。                        |
| 2    | tail    | 此方法返回由除第一个之外的所有元素组成的列表。      |
| 3    | isEmpty | 如果列表为空，则此方法返回`true`，否则返回`false`。 |

以下示例显示如何使用上述方法。

**示例**

文件名:listAccess.scala

```scala
object ListAccess {
   def main(args: Array[String]) {
      val fruit = "apples"::("oranges"::("pears"::Nil))
      val nums = Nil

      println( "Head of fruit : " + fruit.head )
      println( "Tail of fruit : " + fruit.tail )
      println( "Check if fruit is empty : " + fruit.isEmpty )
      println( "Check if nums is empty : " + nums.isEmpty )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/listAccess.scala
```

## 连接列表

可以使用`:::`操作符或`List.:::()`方法或`List.concat()`方法添加两个或多个列表。 请看下面给出的例子 - 

**示例**

文件名:listConcat.scala

```scala
object ListConcat {
   def main(args: Array[String]) {
      val fruit1 = "apples"::("oranges"::("pears"::Nil))
      val fruit2 = "mangoes"::("banana"::Nil)

      // use two or more lists with ::: operator
      var fruit = fruit1 ::: fruit2
      println( "fruit1 ::: fruit2 : " + fruit )

      // use two lists with Set.:::() method
      fruit = fruit1.:::(fruit2)
      println( "fruit1.:::(fruit2) : " + fruit )

      // pass two or more lists as arguments
      fruit = List.concat(fruit1, fruit2)
      println( "List.concat(fruit1, fruit2) : " + fruit  )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/listConcat.scala
```

## 创建统一列表

可以使用`List.fill()`方法创建由零个或多个相同元素的副本组成的列表。 请尝试以下示例程序。

**示例**

文件名:listFill.scala

```scala
object ListFill {
   def main(args: Array[String]) {
      val fruit = List.fill(3)("apples") // Repeats apples three times.
      println( "fruit : " + fruit  )

      val num = List.fill(10)(2)         // Repeats 2, 10 times.
      println( "num : " + num  )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/listFill.scala
```

## 制表函数

您可以使用一个函数与`List.tabulate()`方法在列表之前应用于列表的所有元素。它的参数与`List.fill`类似：第一个参数列表给出要创建的列表的维度，第二个参数列出了列表的元素。唯一的区别是，它不修复元素，而是从函数中计算。

请尝试以下示例程序 

文件名:listTabulate.scala

```scala
object ListTabulate {
   def main(args: Array[String]) {
      // Creates 5 elements using the given function.
      val squares = List.tabulate(6)(n => n * n)
      println( "squares : " + squares  )

      val mul = List.tabulate( 4,5 )( _ * _ )      
      println( "mul : " + mul  )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/listTabulate.scala
```

## 反向列表顺序

可以使用`List.reverse`方法来反转列表的所有元素。以下示例显示了使用情况 - 

文件名:listReverse.scala

```scala
object ListReverse {
   def main(args: Array[String]) {
      val fruit = "apples"::("oranges"::("pears"::Nil))

      println( "Before reverse fruit : " + fruit )
      println( "After reverse fruit : " + fruit.reverse )
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/listReverse.scala
```

## Scala列表方法

以下是使用列表时可以使用的重要方法。有关可用方法的完整列表，请查看Scala的官方文档。

| 序号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | `def +(elem: A): List[A]`                                    | 向列表中添加一个元素                                         |
| 2    | `def ::(x: A): List[A]`                                      | 向列表开头位置添加一具元素。                                 |
| 3    | `def :::(prefix: List[A]): List[A]`                          | 在此列表前添加给定列表中的元素。                             |
| 4    | `def ::(x: A): List[A]`                                      | 在列表的开头添加一个元素`x`                                  |
| 5    | `def addString(b: StringBuilder): StringBuilder`             | 将列表的所有元素附加到字符串构建器。                         |
| 6    | `def addString(b: StringBuilder, sep: String): StringBuilder` | 使用分隔符字符串将列表的所有元素附加到字符串构建器。         |
| 7    | `def apply(n: Int): A`                                       | 通过列表中的索引选择一个元素。                               |
| 8    | `def contains(elem: Any): Boolean`                           | 测试列表是否包含给定元素值。                                 |
| 9    | `def copyToArray(xs: Array[A], start: Int, len: Int): Unit`  | 将列表的元素复制到数组。在给定的数组`xs`中填充该列表的最多为长度(`len`)元素，从`start`位置开始。 |
| 10   | `def distinct: List[A]`                                      | 从列表中创建一个新的列表，而不会有任何重复的元素。           |
| 11   | `def drop(n: Int): List[A]`                                  | 返回除了前`n`个之外的所有元素。                              |
| 12   | `def dropRight(n: Int): List[A]`                             | 返回除最后`n`个之外的所有元素。                              |
| 13   | `def dropWhile(p: (A) => Boolean): List[A]`                  | 删除满足谓词的元素的最长前缀。                               |
| 14   | `def endsWith[B](that: Seq[B]): Boolean`                     | 测试列表是否以给定的顺序结束。                               |
| 15   | `def equals(that: Any): Boolean`                             | 任意序列的`equals`方法，将此序列与其他对象进行比较。         |
| 16   | `def exists(p: (A) => Boolean): Boolean`                     | 测试一个谓词是否适用于列表的某些元素。                       |
| 17   | `def filter(p: (A) => Boolean): List[A]`                     | 返回列表中满足谓词的所有元素。                               |
| 18   | `def forall(p: (A) => Boolean): Boolean`                     | 测试列表中所有元素的谓词是否成立。                           |
| 19   | `def foreach(f: (A) => Unit): Unit`                          | 将函数`f`应用于列表的所有元素。                              |
| 20   | `def head: A`                                                | 选择列表的第一个元素。                                       |
| 21   | `def indexOf(elem: A, from: Int): Int`                       | 在索引位置之后，查找列表中第一个出现值的索引。               |
| 22   | `def init: List[A]`                                          | 返回除上一个以外的所有元素。                                 |
| 23   | `def intersect(that: Seq[A]): List[A]`                       | 计算列表和另一个序列之间的多集合交集。                       |
| 24   | `def isEmpty: Boolean`                                       | 测试列表是否为空。                                           |
| 25   | `def iterator: Iterator[A]`                                  | 在可迭代对象中包含的所有元素上创建一个新的迭代器。           |
| 26   | `def last: A`                                                | 返回最后一个元素。                                           |
| 27   | `def lastIndexOf(elem: A, end: Int): Int`                    | 查找列表中某些值的最后一次出现的索引; 在给定的结束指数之前或之中。 |
| 28   | `def length: Int`                                            | 返回列表的长度。                                             |
| 29   | `def map[B](f: (A) => B): List[B]`                           | 通过将函数应用于此列表的所有元素来构建新集合。               |
| 30   | `def max: A`                                                 | 查找最大元素。                                               |
| 31   | `def min: A`                                                 | 查找最小元素。                                               |
| 32   | `def mkString: String`                                       | 显示字符串中列表的所有元素。                                 |
| 33   | `def mkString(sep: String): String`                          | 使用分隔符字符串显示字符串中列表的所有元素。                 |
| 34   | `def reverse: List[A]`                                       | 以相反的顺序返回带有元素的新列表。                           |
| 35   | `def sorted[B >: A]: List[A]`                                | 根据顺序规则对列表进行排序。                                 |
| 36   | `def startsWith[B](that: Seq[B], offset: Int): Boolean`      | 测试列表是否包含给定索引处的给定序列。                       |
| 37   | `def sum: A`                                                 | 将这个集合所有元素相加。                                     |
| 38   | `def tail: List[A]`                                          | 返回除第一个之外的所有元素。                                 |
| 39   | `def take(n: Int): List[A]`                                  | 返回第一个“n”个元素。                                        |
| 40   | `def takeRight(n: Int): List[A]`                             | 返回最后的“n”个元素。                                        |
| 41   | `def toArray: Array[A]`                                      | 将列表转换为数组。                                           |
| 42   | `def toBuffer[B >: A]: Buffer[B]`                            | 将列表转换为可变缓冲区。                                     |
| 43   | `def toMap[T, U]: Map[T, U]`                                 | 将此列表转换为映射。                                         |
| 44   | `def toSeq: Seq[A]`                                          | 将列表转换为序列。                                           |
| 45   | `def toSet[B >: A]: Set[B]`                                  | 将列表转换为一个集合。                                       |
| 46   | `def toString(): String`                                     | 将列表转换为字符串。                                         |
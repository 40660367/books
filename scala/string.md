# Scala 字符串(string)

本章将介绍Scala中的字符串。 在Scala中的字符串和Java中的一样，字符串是一个不可变的对象，也就是一个不能修改的对象。可以修改的对象，如数组，称为可变对象。字符串是非常有用的对象，在本节的最后部分，我们将介绍`java.lang.String`类的一些重要方法。

## 1.创建一个字符串

以下是创建一个字符串的代码 -

```scala
var greeting = "Hello world!";

// 或者

var greeting:String = "Hello world!";
```

每当编译器在代码中遇到一个字符串文字时，它会创建一个带有它的值的String对象，在这种情况下是`“Hello world！”`。`String`关键字也可以在如上所示的第二个声明中给出。

请尝试以下示例程序。

```scala
object Demo {
   val greeting: String = "Hello, world!"

   def main(args: Array[String]) {
      println( greeting )
   }
}
```

将上述程序保存在源文件：*Demo.scala*中，使用以下命令编译和执行此程序。

```scala
D:\> scalac Demo.scala
D:\> scala Demo

Hello, world!
```

如前所述，`String`类是不可变的。创建后的`String`对象是无法更改的。如果有必要对字符串进行大量修改，那么可考虑使用Scala中提供的`StringBuilder`类。

## 2. 字符串长度

用于获取有关对象的信息的方法称为访问器方法。一个可以与字符串一起使用的访问器方法是`length()`方法，它返回字符串对象中包含的字符数。

使用以下代码段来查找字符串的长度 - 

**例子**

```scala
object Demo {
   def main(args: Array[String]) {
      var palindrome = "Dot saw I was Tod";
      var len = palindrome.length();

      println( "String Length is : " + len );
   }
}
Scala
```

将上述程序保存在源文件：*Demo.scala*中，使用以下命令编译和执行此程序。

```scala
$ scalac Demo.scala
$ scala Demo

String Length is : 17
Scala
```

## 3. 连接字符串

String类包括一个连接两个字符串的方法 -

```scala
string1.concat(string2);
Scala
```

这将返回一个新的字符串，字符串`string1`的尾部添加字符串`string2`。您也可以使用`concat()`方法在字符串文字上操作，如下 -

```scala
"My name is ".concat("Zara");
Scala
```

字符串通常还使用`+`运算符连接，如 -

```scala
"Hello," + " world" + "!"
Scala
```

这将产生以下结果 -

```scala
"Hello, world!"
```

以下代码行将两个字符串相连接 - 

```scala
object Demo {
   def main(args: Array[String]) {
      var str1 = "Dot saw I was ";
      var str2 =  "Tod";

      println("Dot " + str1 + str2);
   }
}
```

将上述程序保存在源文件：*Demo.scala*中，使用以下命令编译和执行此程序。

```shell
D:\>scalac Demo.scala
D:\>scala Demo

Dot Dot saw I was Tod
```

## 4. 创建格式化字符串

您可以使用`printf()`和`format()`方法打印具有格式化数字或字符串的输出。 `String`类具有`format()`方法，它返回`String`对象而不是`PrintStream`对象。

尝试以下示例程序，它使用`printf()`方法 - 

**示例**

```scala
object Demo {
   def main(args: Array[String]) {
      var floatVar = 12.456
      var intVar = 2000
      var stringVar = "Hello, Scala!"

      var fs = printf("The value of the float variable is " + "%f, while the value of the integer " + "variable is %d, and the string" + "is %s", floatVar, intVar, stringVar);

      println(fs)
   }
}
```

将上述程序保存在源文件：*Demo.scala*中，以下命令用于编译和执行此程序。

```scala
D:\>scalac Demo.scala
D:\>scala Demo

The value of the float variable is 12.456000, 
while the value of the integer variable is 2000, 
and the string is Hello, Scala!()
```

## 5. 字符串插值

字符串插值是使用Scala编程语言创建字符串的新方法。此功能支持只在*Scala-2.10*及更高版本。字符串插值：直接在过程字符串文字中嵌入变量引用的机制。

字符串插值中有三种类型(插值器)实现。

### 5.1. ‘s’字符串插值器

文字`'s'`允许在处理字符串时直接使用变量。任何在范围中的String变量可以在字符串中使用。以下是`'s'`字符串插值器的不同用法。

在`println`语句中将`String`变量(`$name`)附加到普通字符串(`Hello`)中，以下示例代码片段用于实现`'s'`插值器。

```scala
val name = “James”
println(s “Hello, $name”) //output: Hello, James
```

字符串插入器还可以处理任意表达式。 使用`'s'`字符串插入器处理具有任意表达式(`${1 + 1}`)的字符串(`1 + 1`)的以下代码片段。任何表达式都可以嵌入到`${}`中。

```scala
println(s “1 + 1 = ${1 + 1}”) //output: 1 + 1 = 2
```

尝试实现`'s'`插值器的示例程序如下 - 

```scala
object Demo {
   def main(args: Array[String]) {
      val name = "James"

      println(s"Hello, $name")
      println(s"1 + 1 = ${1 + 1}")
   }
}
```

将上述程序保存在源文件：*Demo.scala*中，使用以下命令编译和执行此程序。

```scala
D:\>scalac Demo.scala
D:\>scala Demo

Hello, James
1 + 1 = 2
```

### 5.2 ‘f’插值器

文字`'f'`插值器允许创建一个格式化的字符串，类似于C语言中的`printf`。 在使用`'f'`插值器时，所有变量引用都应该是`printf`样式格式说明符，如`％d`，`％i`，`％f`等。

我们以一般的字符串为例附加浮点值(`height = 1.9d`)和字符串变量(`name =“James”`)。下面的代码片段实现`'f'`插值器。这里`$name％s`打印String变量`James`和`$height％2.2f`打印浮点值`1.90`。

```scala
val height = 1.9d
val name = "James"
println(f"$name%s is $height%2.2f meters tall") //James is 1.90 meters tall
```

它是类型安全的变量引用，以下格式说明符要匹配，否则显示错误。`'f'`插值器使用Java中可用`String`格式实用程序(格式说明符)。 默认情况下，变量引用后没有`％`字符。它将假定为`％s`的字符串。

### 5.3 “原始”插值器

`'raw'`内插器类似于`'s'`插值器，除了它不执行字符串内的文字转义。下表中的代码段将区别`'s'`和`'raw'`插值器的用法。 在使用`s`和`\n`效果的输出中，新行作为原始值输出，也就是`\n`将不起作用。它将使用转义字母打印完整的字符串。

- `'s'`的插值器使用，程序代码如下 - 

  ```scala
  object Demo {
   def main(args: Array[String]) {
      println(s"Result = \n a \n b")
   }
  }
  ```

  输出结果 -

  ```shell
  Result =
  a
  b
  ```

- `'raw'`的插值器使用，程序代码如下 - 

  ```scala
  object Demo {
   def main(args: Array[String]) {
      println(raw"Result = \n a \n b")
   }
  }
  ```

  输出结果 -

  ```shell
  Result = \n a \n b
  ```

## 字符串方法

以下是`java.lang.String`类定义的方法列表，可以直接在`Scala`程序中使用 -

| 编号 | 方法                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | char charAt(int index)                                       | 返回指定索引处的字符。                                       |
| 2    | int compareTo(Object o)                                      | 将此`String`与另一个对象进行比较。                           |
| 3    | int compareTo(String anotherString)                          | 按字典顺序比较两个字符串。                                   |
| 4    | int compareToIgnoreCase(String str)                          | 按字典顺序比较两个字符串，忽略大小写差异。                   |
| 5    | String concat(String str)                                    | 将指定的字符串连接到该字符串的末尾。                         |
| 6    | boolean contentEquals(StringBuffer sb)                       | 当且仅当此`String`表示与指定的`StringBuffer`的字符序列相同时，才返回`true`。 |
| 7    | static String copyValueOf(char[] data)                       | 返回一个字符串，表示指定的数组中的字符序列。                 |
| 8    | static String copyValueOf(char[] data, int offset, int count) | 返回一个字符串，表示指定的数组中的字符序列。                 |
| 9    | boolean endsWith(String suffix)                              | 测试此字符串是否以指定的字符串为后缀/结尾。                  |
| 10   | boolean equals(Object anObject)                              | 将此字符串与指定对象进行比较。                               |
| 11   | boolean equalsIgnoreCase(String anotherString)               | 将此String与另一个String进行比较，并忽略大小写。             |
| 12   | byte getBytes()                                              | 使用平台的默认字符集将此String编码为一系列字节，将结果存储到新的字节数组中。 |
| 13   | byte[] getBytes(String charsetName)                          | 使用命名的字符集将此String编码为一系列字节，将结果存储到新的字节数组中。 |
| 14   | void getChars(int srcBegin, int srcEnd, char[] dst, int dstBegin) | 将此字符串从`srcBegin`到`srcEnd`索引处的字符复制到目标字符数组(`dst`)中。 |
| 15   | int hashCode()                                               | 返回此字符串的哈希码。                                       |
| 16   | int indexOf(int ch)                                          | 返回指定字符第一次在字符串中出现的索引。                     |
| 17   | int indexOf(int ch, int fromIndex)                           | 返回指定字符以指定的索引开始搜索第一次在字符串内出现的索引。 |
| 18   | int indexOf(String str)                                      | 返回指定子字符串在字符串内第一次出现的索引。                 |
| 19   | int indexOf(String str, int fromIndex)                       | 返回从指定的索引开始，指定子串的第一次出现在给定字符串中的索引。 |
| 20   | String intern()                                              | 返回字符串对象的规范表示。                                   |
| 21   | int lastIndexOf(int ch)                                      | 返回指定字符在字符串中最后一次出现的索引。                   |
| 22   | int lastIndexOf(int ch, int fromIndex)                       | 返回指定字符在给定字符串中的最后一次出现的索引，它从指定的索引开始向后搜索。 |
| 23   | int lastIndexOf(String str)                                  | 返回指定子字符串在字符串内的最右边出现的索引。               |
| 24   | int lastIndexOf(String str, int fromIndex)                   | 返回指定子字符串在给定字符串中最后一次出现的索引，它从指定索引开始向后搜索。 |
| 25   | int length()                                                 | 返回此字符串的长度。                                         |
| 26   | boolean matches(String regex)                                | 测试这个字符串是否与给定的正则表达式匹配。                   |
| 27   | boolean regionMatches(boolean ignoreCase, int toffset, String other, int offset, int len) | 测试两个字符串区域是否相等。                                 |
| 28   | boolean regionMatches(int toffset, String other, int offset, int len) | 测试两个字符串区域是否相等。                                 |
| 29   | String replace(char oldChar, char newChar)                   | 返回一个新的字符串，此字符串是使用`newChar`替换此字符串中所有出现的`oldChar`的结果。 |
| 30   | String replaceAll(String regex, String replacement           | 使用`replacement`替换与给定正则表达式(`regex`)匹配的字符串中的每个子字符串。 |
| 31   | String replaceFirst(String regex, String replacement)        | 用给定的`replacement`替换与给定正则表达式(`regex`)匹配的字符串中的第一个子字符串。 |
| 32   | String[] split(String regex)                                 | 将此字符串拆分为给定正则表达式的匹配项。                     |
| 33   | String[] split(String regex, int limit)                      | 将此字符串拆分为给定正则表达式的匹配项。                     |
| 34   | boolean startsWith(String prefix)                            | 测试此字符串是否以指定的前缀开头。                           |
| 35   | boolean startsWith(String prefix, int toffset)               | 测试此字符串是否以指定的前缀开头，指定一个指定的索引。       |
| 36   | CharSequence subSequence(int beginIndex, int endIndex)       | 返回一个新的字符序列，该序列是该序列的子序列。               |
| 37   | String substring(int beginIndex)                             | 返回一个新字符串，该字符串是此字符串的子字符串。             |
| 38   | String substring(int beginIndex, int endIndex)               | 返回一个新字符串，该字符串是此字符串的子字符串。             |
| 39   | char[] toCharArray()                                         | 将此字符串转换为新的字符数组。                               |
| 40   | String toLowerCase()                                         | 使用默认语言环境的规则将此String中的所有字符转换为小写。     |
| 41   | String toLowerCase(Locale locale)                            | 使用给定的区域设置的规则将此String中的所有字符转换为小写。   |
| 42   | String toString()                                            | 此对象(已经是字符串)本身已被返回。                           |
| 43   | String toUpperCase()                                         | 使用默认语言环境的规则将此字符串中的所有字符转换为大写。     |
| 44   | String toUpperCase(Locale locale)                            | 使用给定的区域设置的规则将此String中的所有字符转换为大写。   |
| 45   | String trim()                                                | 返回字符串的副本，省略前导和尾随空格。                       |
| 46   | static String valueOf(primitive data type x)                 | 返回传递数据类型参数的字符串表示形式。                       |
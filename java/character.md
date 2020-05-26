# Java 字符类Character

通常，当处理字符时，使用原始数据类型`char`。

**示例**

```java
char ch = 'a';

// Unicode的大写字符
char uniChar = '\u039A'; 

// 字符数组
char[] charArray ={ 'a', 'b', 'c', 'd', 'e' };
```

但是在开发过程中，经常遇到的是需要使用对象而不是原始数据类型的情况。 为了实现这一点，Java为原始数据类型`char`提供了包装类`Character`。

`Character`类提供了许多用于操作字符的有用类(即静态)方法。 可以使用`Character`构造函数创建`Character`对象，例如 - 

```java
Character ch = new Character('a');
```

在某些情况下，Java编译器还会创建一个`Character`对象。 例如，如果将原始字符传递给需要对象的方法，则编译器会自动将`char`转换为`Character`。此功能称为自动装箱或拆箱。

**示例**

```java
// 这里是原始的char类型值：'a'
// 它被装入`Character`对象ch
Character ch = 'a';

// 这里原始char值'x'，装箱用于方法test，
// 拆箱到char类型值：'c'
char c = test('x');
```

## 转义序列

以反斜杠(`\`)开头的字符是转义序列，对编译器具有特殊含义。

在本教程中`System.out.println()`语句中经常使用换行符(`\n`)，以便在打印字符串后前进到下一行。

下表中列出了Java转义序列 - 

| 编号 | 转义序列 | 描述                         |
| ---- | -------- | ---------------------------- |
| 1    | `\t`     | 表示在文本中插入一个制表符。 |
| 2    | `\b`     | 表示在文本中插入退格符。     |
| 3    | `\n`     | 表示在文本中插入换行符。     |
| 4    | `\r`     | 表示在文本中插入回车符。     |
| 5    | `\f`     | 表示在文本中插入换页符。     |
| 6    | `\ '`    | 表示在文本中插入单引号字符。 |
| 7    | `\"`     | 表示在文本中插入双引号字符。 |
| 8    | `\\`     | 表示在文本中插入反斜杠字符。 |

当在`print`语句中遇到转义序列时，编译器会相应地解释它。

**示例**

如果要在引号内加引号，则必须在内部引号上使用转义序列`\"` - 

文件名:CharacterTest.java

```java
public class CharacterTest {

   public static void main(String args[]) {
      System.out.println("She said \"Hello!\" to me.");
   }
}
```

```bash
cd ~/java && javac CharacterTest.java
java CharacterTest
```

康康
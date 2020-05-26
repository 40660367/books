# Java 日期时间

Java的`java.util`包提供了`Date`类，该类封装了当前的日期和时间。`Date`类支持两个构造函数，如下表所示。

| 编号 | 构造函数              | 描述                                                         |
| ---- | --------------------- | ------------------------------------------------------------ |
| 1    | `Date()`              | 此构造函数使用当前日期和时间来初始化对象。                   |
| 2    | `Date(long millisec)` | 此构造函数接受一个参数，该参数等于自1970年1月1日午夜以来经过的毫秒数。 |

以下是`Date`类的方法列表 - 

| 编号 | 方法                          | 描述                                                         |
| ---- | ----------------------------- | ------------------------------------------------------------ |
| 1    | `boolean after(Date date)`    | 如果调用`Date`对象包含的日期晚于`date`指定的日期，则返回`true`，否则返回`false`。 |
| 2    | `boolean before(Date date)`   | 如果调用`Date`对象包含的日期早于`date`指定的日期，则返回`true`，否则返回`false`。 |
| 3    | `Object clone( )`             | 复制调用的`Date`对象。                                       |
| 4    | `int compareTo(Date date)`    | 将调用对象的值与`date`的值进行比较。 如果值相等则返回`0`。 如果调用对象早于`date`，则返回负值。 如果调用对象晚于`date`，则返回正值。 |
| 5    | `int compareTo(Object obj)`   | 如果`obj`对象是`Date`类对象，则与`compareTo(Date)`操作相同。 否则，它会抛出`ClassCastException`。 |
| 6    | `boolean equals(Object date)` | 如果调用`Date`对象包含与`date`指定的时间和日期相同的时间和日期，则返回`true`，否则返回`false`。 |
| 7    | `long getTime()`              | 返回自1970年1月1日以来经过的毫秒数。                         |
| 8    | `int hashCode()`              | 返回调用对象的哈希码。                                       |
| 9    | `void setTime(long time)`     | 设置时间指定的时间和日期，表示从1970年1月1日午夜开始的经过时间(以毫秒为单位)。 |
| 10   | `String toString( )`          | 将调用`Date`对象转换为字符串并返回结果。                     |

#### 获取当前日期和时间

这是一种在Java中获取当前日期和时间的简单方法。可以使用`Date`对象`toString()`方法来打印当前日期和时间，如下所示 - 

文件名:DatetimeTest.java

```java
import java.util.Date;
public class DatetimeTest {

   public static void main(String args[]) {
      // 实例化Date对象
      Date date = new Date();

      // display time and date using toString()
      System.out.println(date.toString());
   }
}
```

```shell
cd ~/java && javac DatetimeTest.java
java DatetimeTest
```

康康

#### 使用SimpleDateFormat设置日期格式

`SimpleDateFormat`是一个具体的类，用于以区域设置的方式格式化和解析日期。 `SimpleDateFormat`用于从为日期时间格式选择用户定义的模式。

**示例**

文件名:SimpleDateTest.java

```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class SimpleDateTest {

    public static void main(String args[]) {
        Date dNow = new Date();
        SimpleDateFormat ft = new SimpleDateFormat("yyyy.MM.dd (E)'at' hh:mm:ss a zzz");

        System.out.println("Current Date: " + ft.format(dNow));

        SimpleDateFormat ft2 = new SimpleDateFormat("yyyy-MM-dd hh:mm:ss");

        System.out.println("Current Datetime: " + ft2.format(dNow));

    }
}
```

康康

```shell
cd ~/java && javac SimpleDateTest.java
java SimpleDateTest
```

**DateFormat格式代码**

要指定时间格式，请使用时间模式字符串。 在此模式中，所有ASCII字母都保留为模式字母，其定义如下 - 

| 编号 | 字符 | 描述                      | 示全歼                  |
| ---- | ---- | ------------------------- | ----------------------- |
| 1    | G    | 时代指示符                | AD                      |
| 2    | y    | 四位数的年份值            | 2019                    |
| 3    | M    | 月份                      | July or 07              |
| 4    | d    | 日                        | 10                      |
| 5    | h    | 小时 A.M./P.M. (1~12)     | 12                      |
| 6    | H    | 24小时制的小时表示 (0~23) | 22                      |
| 7    | m    | 分钟                      | 30                      |
| 8    | s    | 秒钟                      | 55                      |
| 9    | S    | 毫秒                      | 234                     |
| 10   | E    | 星期几                    | Tuesday                 |
| 11   | D    | 一年中的第几天            | 360                     |
| 12   | F    | 一个月中的某一天          | 2 (second Wed. in July) |
| 13   | w    | 一年中的第几个星期        | 40                      |
| 14   | W    | 一月中的第几个星期        | 1                       |
| 15   | a    | A.M./P.M. 标记            | PM                      |
| 16   | k    | 小时 (1~24)               | 24                      |
| 17   | K    | 小时 A.M./P.M. (0~11)     | 10                      |
| 18   | z    | 时区                      | Eastern Standard Time   |
| 19   | ‘    | 转义文本                  | Delimiter               |
| 20   | `    | 单引号                    | `                       |

#### 3. 使用printf格式化日期

使用`printf`方法来完成日期和时间格式化。使用双字母格式，以`t`开头并以表格的一个字母结尾，如下面的代码所示。

文件名:DatePrintfTest.java

```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class DatePrintfTest {

    public static void main(String args[]) {
        // Instantiate a Date object
        Date date = new Date();

        // display time and date
        String str = String.format("Current Date/Time : %tc", date);

        System.out.printf(str);

    }
}
```

```shell
cd ~/java && javac DatePrintfTest.java
java DatePrintfTest
```

康康

如果多次提供日期来格式化每个部分，那多少会有点愚蠢。 格式字符串可以指示要格式化的参数的索引。

索引必须紧跟`%`，并且必须以`$`结尾。

**示例**

文件名:DatePrintfTest1.java

```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class DatePrintfTest1 {

    public static void main(String args[]) {
        // Instantiate a Date object
        Date date = new Date();

        // display time and date
        System.out.printf("%1$s %2$tB %2$td, %2$tY", "Due date:", date);
    }
}
```

快在右侧实验区使用下方命令执行上面代码，康康会得到什么结果？

```shell
cd ~/java && javac DatePrintfTest1.java
java DatePrintfTest1
```



或者，可以使用`<`标志。 它表示再次使用与前面的格式规范相同的参数。

**示例**

DatePrintfTest2.java

```java
import java.text.SimpleDateFormat;
import java.util.Date;

public class DatePrintfTest2 {

    public static void main(String args[]) {
        // Instantiate a Date object
        Date date = new Date();

        // display formatted date
        System.out.printf("%s %tB %<te, %<tY", "Due date:", date);
    }
}
```

```shell
cd ~/java && javac DatePrintfTest2.java
java DatePrintfTest2
```

康康

#### 日期和时间转换字符

**示例**

| 编号 | 字符 | 描述                                  | 示例                         |
| ---- | ---- | ------------------------------------- | ---------------------------- |
| 1    | c    | 完全日期和时间                        | Mon May 04 09:51:52 CDT 2019 |
| 2    | F    | ISO 8601 date                         | 2004-02-09                   |
| 3    | D    | U.S. formatted date (month/day/year)  | 02/09/2004                   |
| 4    | T    | 24小时时间                            | 18:05:19                     |
| 5    | r    | 12小时时间                            | 06:05:19 pm                  |
| 6    | R    | 24小时时间, 无秒钟。                  | 18:05                        |
| 7    | Y    | 四位数年份(前导零)                    | 2019                         |
| 8    | y    | 年份的最后两位数(带前导零)            | 19                           |
| 9    | C    | 年份的前两位数(带前导零)              | 20                           |
| 10   | B    | 月份全名称                            | February                     |
| 11   | b    | 缩写的月份名称                        | Feb                          |
| 12   | m    | 两位数月份(带前导零)                  | 02                           |
| 13   | d    | 两位数的日期(带前导零)                | 03                           |
| 14   | e    | 两位数的日期(没有前导零)              | 9                            |
| 15   | A    | 完整的工作日名称                      | Monday                       |
| 16   | a    | 缩写的工作日名称                      | Mon                          |
| 17   | j    | 一年中的三位数日(带前导零)            | 069                          |
| 18   | H    | 两位数小时(前导零)，介于00和23之间    | 18                           |
| 19   | k    | 两位数小时(不带前导零)，介于0和23之间 | 18                           |
| 20   | I    | 两位数小时(前导零)，介于01和12之间    | 06                           |
| 21   | l    | 两位数小时(不带前导零)，介于1和12之间 | 6                            |
| 22   | M    | 两位数分钟(带前导零)                  | 05                           |
| 23   | S    | 两位数秒(带前导零)                    | 19                           |
| 24   | L    | 三位数毫秒(带前导零)                  | 047                          |
| 25   | N    | 九位纳秒(带前导零)                    | 047000000                    |
| 26   | P    | 大写上午或下午标记                    | PM                           |
| 27   | p    | 小写上午或下午标记                    | pm                           |
| 28   | z    | GMT的RFC 822数字偏移量                | -0800                        |
| 29   | Z    | 时区                                  | PST                          |
| 30   | s    | 自1970-01-01 00:00:00 GMT以来的秒数   | 1078884319                   |
| 31   | Q    | 自1970-01-01 00:00:00 GMT以来的毫秒数 | 1078884319047                |

还有其他与日期和时间相关的有用类。 有关更多详细信息，请参阅Java标准文档。

#### 将字符串解析为日期

`SimpleDateFormat`类有一些额外的方法，特别是`parse()`，它用于根据存储在给定的`SimpleDateFormat`对象中的格式来解析字符串。

**示例**

文件名:ParseStringToDate.java

```java
import java.util.*;
import java.text.*;

public class ParseStringToDate {

    public static void main(String args[]) {
        SimpleDateFormat ft = new SimpleDateFormat("yyyy-MM-dd");
        String input = args.length == 0 ? "2019-11-11" : args[0];

        System.out.print(input + " 解析为：");
        Date t;
        try {
            t = ft.parse(input);
            System.out.println(t);
        } catch (ParseException e) {
            System.out.println("Unparseable using " + ft);
        }
    }
}
```

```shell
cd ~/java && javac ParseStringToDate.java
java ParseStringToDate
```

康康

#### 睡眠一段时间

可以在计算机生命周期的任何时间段内睡眠。 例如，以下程序将睡眠`3`秒钟 - 

文件名: SleepTest.java

```java
import java.util.*;
import java.text.*;

public class SleepTest {

    public static void main(String args[]) {
        try {
            System.out.println(new Date());
            Thread.sleep(5 * 60 * 10);
            System.out.println(new Date());
        } catch (Exception e) {
            System.out.println("Got an exception!");
        }
    }
}
```

```shell
cd ~/java && javac SleepTest.java
java SleepTest
```

康康

#### 测量经过的时间

有时，可能需要以毫秒为单位测量时间点。 

文件名:TimeMeasureTest.java

```java
import java.util.*;
import java.text.*;

public class TimeMeasureTest {
    public static void main(String args[]) {
        try {
            long start = System.currentTimeMillis();
            System.out.println(new Date());

            Thread.sleep(5 * 60 * 10);
            System.out.println(new Date());

            long end = System.currentTimeMillis();
            long diff = end - start;
            System.out.println("时间差为: " + diff);
        } catch (Exception e) {
            System.out.println("Got an exception!");
        }
    }
}
```

```shell
cd ~/java && javac TimeMeasureTest.java
java TimeMeasureTest
```

康康
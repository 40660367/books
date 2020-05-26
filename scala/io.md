# Scala 文件I/O

Scala可以使用任何Java对象，而`java.io.File`是Scala编程中可用于读取和写入文件的对象之一。

以下是写入文件的示例程序。

文件名:ioDemo.scala

```scala
import java.io._

object ioDemo {
   def main(args: Array[String]) {
      val writer = new PrintWriter(new File("test.txt" ))

      writer.write("Hello Scala")
      writer.close()
   }
}
```

使用以下命令编译和执行此程序。

```bash
cd ~
scala /share/lesson/scala/io.scala
cat test.txt
```

## 从命令行读一行

有时需要从屏幕上读取用户输入，然后继续进行进一步的处理。 以下示例程序显示如何从命令行读取输入。

文件名:ioReadConsole.scala

```scala
object ioReadConsole {
   def main(args: Array[String]) {
      print("Please enter your input : " )
      val line = Console.readLine

      println("Thanks, you just typed: " + line)
   }
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/ioReadConsole.scala
```

## 阅读文件内容

从文件读取真的很简单。可以使用Scala的`Source`类及其对象来读取文件。以下是从前面创建的`“Demo.txt”`文件中读取的示例。

文件名:ioReadFile.scala

```scala
import scala.io.Source

object ioReadFile {
   def main(args: Array[String]) {
      println("Following is the content read:" )

      Source.fromFile("demo.txt" ).foreach { 
         print 
      }
   }
}
```

使用以下命令编译和执行此程序。

```bash
cd ~
echo 'This is test content' > demo.txt

scala /share/lesson/scala/ioReadFile.scala
```

## 
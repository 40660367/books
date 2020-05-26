# Java 文件和输入和输出IO

`java.io`包几乎包含了在Java中执行输入和输出(I/O)所需的所有类。 所有这些流代表输入源和输出目的地。 `java.io`包中的流支持许多数据，如：原始，对象，本地化字符等。

## 流(Streams)

流(`Streams`)可以定义为数据序列，它有两种 - 

- `InPutStream`  -  它用于从源读取数据。
- `OutPutStream`  -  它用于将数据写入目标。

![Java流](./images/streams.png)

Java为与文件和网络相关的I/O提供强大而灵活的支持，但本教程只涵盖了流和I/O相关的非常基本的功能。下面将看到一些最常用的例子 - 

**字节流**
Java字节流用于执行`8`位字节的输入和输出。尽管有许多与字节流相关的类，但最常用的类是`FileInputStream`和`FileOutputStream`。以下示例使用这两个类将输入文件的内容复制到输出文件中

首先在课程目录创建一个`input.txt`

```bash
echo Java IO Source Text File input.txt > ~/java/input.txt
```

文件名:CopyFile.java

```java
import java.io.*;
public class CopyFile {

   public static void main(String args[]) throws IOException {  
      FileInputStream in = null;
      FileOutputStream out = null;

      try {
         in = new FileInputStream("input.txt");
         out = new FileOutputStream("output.txt");
         int c;
         while ((c = in.read()) != -1) {
            out.write(c);
         }
      }finally {
         if (in != null) {
            in.close();
         }
         if (out != null) {
            out.close();
         }
      }
   }
}
```

它将创建一个：`output.txt`文件，内容与`input.txt`中的相同。

```bash
cd ~/java && javac CopyFile.java
java CopyFile
```

康康

验证新生成的文件,看是否和预想的一样?

```bash
cat /course/java/output.txt
```

**字符流**

Java字节流用于执行`8`位字节的输入和输出，而Java字符流用于执行`16`位unicode的输入和输出。 尽管有许多与字符流相关的类，但最常用的类是`FileReader`和`FileWriter`。 虽然`FileReader`内部使用`FileInputStream`类，而`FileWriter`内部使用`FileOutputStream`类，但主要区别在于`FileReader`一次读取两个字节，而`FileWriter`一次写入两个字节。

可以重新编写上面的例子，它使用这两个类将输入文件(具有unicode字符)复制到输出文件中 - 

**示例**

首先在课程目录创建一个`input1.txt`

```bash
echo Java IO Source Text File input1.txt >> ~/java/input1.txt
```

文件名:CopyFile1.java

```java
import java.io.*;
public class CopyFile1 {

   public static void main(String args[]) throws IOException {
      FileReader in = null;
      FileWriter out = null;

      try {
         in = new FileReader("input1.txt");
         out = new FileWriter("output1.txt");

         int c;
         while ((c = in.read()) != -1) {
            out.write(c);
         }
      }finally {
         if (in != null) {
            in.close();
         }
         if (out != null) {
            out.close();
         }
      }
   }
}
```

```bash
cd ~/java && javac CopyFile1.java
java CopyFile1
```

康康

验证新生成的文件,看是否和预想的一样?

```bash
cat ~/java/output1.txt
```

## 标准流

所有编程语言都支持标准I/O，用户的程序可以从键盘输入，然后在计算机屏幕上产生输出。 如果您了解C或C++编程语言，那么应该了解三个标准流：`STDIN`，`STDOUT`和`STDERR`。 同样，Java提供以下三个标准流 - 

- **标准输入** - 用于将数据提供给用户程序，通常键盘用作标准输入流并表示为`System.in`。
- **标准输出** - 用于输出用户程序生成的数据，通常计算机屏幕用于标准输出流并表示为`System.out`。
- **标准错误** - 用于输出用户程序生成的错误数据，通常计算机屏幕用于标准错误流并表示为`System.err`。

以下是一个简单的程序，它使用`InputStreamReader`来读取标准输入流，直到用户键入：`q` - 

文件名:ReadConsole.java

```java
import java.io.*;
public class ReadConsole {

   public static void main(String args[]) throws IOException {
      InputStreamReader cin = null;

      try {
         cin = new InputStreamReader(System.in);
         System.out.println("Enter characters, 'q' to quit>");
         char c;
         do {
            c = (char) cin.read();
            System.out.print(c);
         } while(c != 'q');
      }finally {
         if (cin != null) {
            cin.close();
         }
      }
   }
}
```

```bash
cd ~/java && javac ReadConsole.java
java ReadConsole
```

康康

## 读写文件

如前所述，流可以定义为数据序列。 `InputStream`用于从源读取数据，`OutputStream`用于将数据写入目标。

以下是处理输入和输出流的类层次结构。

![输入和输出流](./images/io.jpg)

两个重要的流是：`FileInputStream`和`FileOutputStream`，将在本教程中讨论。

**FileInputStream**

此流用于从文件中读取数据。 可以使用关键字`new`创建对象，并且有几种类型的构造函数可用。

以下构造函数将文件名作为字符串来创建输入流对象以读取文件 - 

```java
InputStream f = new FileInputStream("hello.txt");
```

以下构造函数采用文件对象来创建输入流对象以读取文件。 首先，使用`File()`方法创建一个文件对象，如下所示 

```java
File f = new File("hello.txt");
InputStream f = new FileInputStream(f);
```

当创建了`InputStream`对象，就可以使用一些辅助方法来读取流或在流上执行其他操作。

| 编号 | 方法                                             | 描述                                                         |
| ---- | ------------------------------------------------ | ------------------------------------------------------------ |
| 1    | `public void close() throws IOException{}`       | 此方法关闭文件输出流。 释放与该文件关联的所有系统资源，抛出`IOException`。 |
| 2    | `protected void finalize()throws IOException {}` | 此方法清除与文件的连接。 确保在没有对此流的引用时调用此文件输出流的`close()`方法，抛出`IOException`。 |
| 3    | `public int read(int r)throws IOException{}`     | 此方法从`InputStream`读取指定的数据字节，并返回一个`int`值。 返回数据的下一个字节，如果它是文件的末尾，则返回`-1`。 |
| 4    | `public int read(byte[] r) throws IOException{}` | 此方法将输入流中的`r.length`个字节读入数组。返回读取的总字节数。 如果它到达文件的结尾，则返回`-1`。 |
| 5    | `public int available() throws IOException{}`    | 给出可以从此文件输入流中读取的字节数。 返回一个`int`值。     |

还有其他重要的输入流可用

- ByteArrayInputStream]
- DataInputStream

**FileOutputStream**

`FileOutputStream`用于创建文件并将数据写入文件。 如果文件尚不存在，则会在打开文件以进行输出之前创建该文件。

这里有两个构造函数，可用于创建`FileOutputStream`对象。

以下构造函数将文件名作为字符串来创建输入流对象以写入文件 - 

```java
OutputStream f = new FileOutputStream("hello.txt")
```

下面的构造函数接受一个文件对象来创建一个输出流对象来写入该文件。 首先，使用`File()`方法创建一个文件对象，如下所示 - 

```java
File f = new File("hello.txt");
OutputStream f = new FileOutputStream(f);
```

当创建了`OutputStream`对象，就使用它的一些辅助方法来写入流或在流上执行其他操作。

| 编号 | 方法                                             | 描述                                                         |
| ---- | ------------------------------------------------ | ------------------------------------------------------------ |
| 1    | `public void close() throws IOException{}`       | 此方法关闭文件输出流，释放与该文件关联的所有系统资源。抛出`IOException`。 |
| 2    | `protected void finalize()throws IOException {}` | 此方法清除与文件的连接，确保在没有对此流的引用时调用此文件输出流的`close()`方法。抛出`IOException`。 |
| 3    | `public void write(int w)throws IOException{}`   | 此方法将指定的字节写入输出流。                               |
| 4    | `public void write(byte[] w)`                    | 将长度为`w.length`的字节从字节数组写入`OutputStream`。       |

还有其他重要的输出流，有关更多详细信息，请参阅以下链接 - 

- ByteArrayOutputStream
- DataOutputStream

**示例**

以下是演示如何使用`InputStream`和`OutputStream`类对象的示例 - 

文件名:FileStreamTest.java

```java
import java.io.*;
public class FileStreamTest {

   public static void main(String args[]) {

      try {
         byte bWrite [] = {11,21,3,40,5};
         OutputStream os = new FileOutputStream("output.txt");
         for(int x = 0; x < bWrite.length ; x++) {
            os.write( bWrite[x] );   // writes the bytes
         }
         os.close();

         InputStream is = new FileInputStream("input.txt");
         int size = is.available();

         for(int i = 0; i < size; i++) {
            System.out.print((char)is.read() + "  ");
         }
         is.close();
      } catch (IOException e) {
         System.out.print("Exception");
      }    
   }
}
```

```shell
cd ~/java && javac ReadConsole.java
java ReadConsole
```

康康

上面的代码将创建文件`test.txt`并将以二进制格式写入给定的数字数据，同样也会在屏幕上输出。

## 文件导航和I/O

可通过其他几个类来了解文件导航和I/O的基础知识。如下 - 

#### 目录操作

目录是一个文件，它可以包含其他文件和目录的列表。 使用`File`对象创建目录，列出目录中可用的文件。 有关完整的详细信息，请查看在File对象上调用的所有方法的列表以及与目录相关的内容。

创建目录**

有两种`File`类的方法，可用于创建目录 - 

- `mkdir()`方法创建一个目录，创建成功时返回`true`，失败时返回`false`。 失败表示`File`对象中指定的路径已存在，或者由于整个路径尚不存在或权限问题而无法创建目录。
- `mkdirs()`方法创建目录和目录的所有上级目录。

以下示例创建一个目录：testdir在/course/java/

**示例**

文件名:CreateDir.java

```java
import java.io.File;
public class CreateDir {

   public static void main(String args[]) {
      String dirname = "/var/testdir";
      File d = new File(dirname);
      // 创建目录及父级目录
      d.mkdirs();
   }
}
```

```shell
cd ~/java && javac CreateDir.java
java CreateDir
```

康康

> 注 -  Java会根据约定自动处理UNIX和Windows上的路径分隔符。如果在Windows版本的Java上使用正斜杠(/)，则路径仍将正确解析。

**列出目录**

可以使用`File`对象的`list()`方法列出目录中可用的所有文件和目录

文件名:ReadDir.java

```java
import java.io.File;
public class ReadDir {

   public static void main(String[] args) {
      File file = null;
      String[] paths;

      try {      
         // 创建一个File对象
         file = new File("/var");

         // 文件和目录的数组
         paths = file.list();

         // 对于路径数组中的名称
         for(String path:paths) {
            // 打印文件名和目录名
            System.out.println(path);
         }
      } catch (Exception e) {
         // if any error occurs
         e.printStackTrace();
      }
   }
}
```

```bash
cd ~/java && javac ReadDir.java
java ReadDir
```

康康
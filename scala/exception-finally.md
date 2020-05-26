# Scala finally块

`finally`块用于在异常时释放资源。资源可能是文件，网络连接，数据库连接等，`finally`块执行代码运行保证。以下程序说明了`finally`块的用法。

**Scala finally块示例**

## finally子句

如果希望引发一些代码执行，无论表达式如何终止，都会执行在`finally`子句包装表达式。尝试以下程序。

文件名:exceptionFinally.scala

```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

object exceptionFinally {
   def main(args: Array[String]) {
      try {
         val f = new FileReader("input.txt")
      } catch {
         case ex: FileNotFoundException => {
            println("Missing file exception")
         }

         case ex: IOException => {
            println("IO Exception")
         }
      } finally {
         println("Exiting finally...")
      }
   }
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/exceptionFinally.scala
```



**示例:**

文件名:exceptionFinally2.scala

```scala
class ExceptionExample{  
    def divide(a:Int, b:Int) = {  
        try{  
            a/b  
            var arr = Array(1,2)  
            arr(10)  
        }catch{  
            case e: ArithmeticException => println(e)  
            case ex: Exception =>println(ex)  
            case th: Throwable=>println("found a unknown exception"+th)  
        }  
        finally{  
            println("Finaly block always executes")  
        }  
        println("Rest of the code is executing...")  
    }  
}  


object exceptionFinally2{  
    def main(args:Array[String]){  
        var e = new ExceptionExample()  
        e.divide(100,10)  

    }  
}
```
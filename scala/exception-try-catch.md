# Scala 捕获异常try-catch语句

## 捕获异常

Scala提供`try`和`catch`块来处理异常。`try`块用于包含可疑代码。`catch`块用于处理`try`块中发生的异常。可以根据需要在程序中有任意数量的`try...catch`块。

Scala允许在单个块中`try/catch`任何异常，然后使用`case`块对其进行模式匹配。尝试以下示例程序来处理异常。

当您想要处理异常时，要像Java一样使用`try {...} catch {...}`块，除了`catch`块使用匹配来识别和处理异常。

**Scala try catch示例1**

在下面的程序中，我们将可疑代码封装在`try`块中。 在`try`块之后使用了一个`catch`处理程序来捕获异常。如果发生任何异常，`catch`处理程序将处理它，程序将不会异常终止。

文件名:exceptionTryCatch1.scala

```scala
class ExceptionExample{  
    def divide(a:Int, b:Int) = {  
        try{  
            a/b  
        }catch{  
            case e: ArithmeticException => println(e)  
        }  
        println("Rest of the code is executing...")  
    }  
}  
object exceptionTryCatch1{  
    def main(args:Array[String]){  
        var e = new ExceptionExample()  
        e.divide(100,0)  

    }  
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/exceptionTryCatch1.scala
```

**Scala Try Catch示例2**

在这个例子中，`catch`处理程序有两种情况。 第一种情况将只处理算术类型异常。 第二种情况有`Throwable`类，它是异常层次结构中的超类。第二种情况可以处理任何类型的异常在程序代码中。有时当不知道异常的类型时，可以使用超类 - `Throwable`类。

文件名:exceptionTryCatch2.scala

```scala
class ExceptionExample{  
    def divide(a:Int, b:Int) = {  
        try{  
            a/b  
            var arr = Array(1,2)  
            arr(10)  
        }catch{  
            case e: ArithmeticException => println(e)  
            case ex: Throwable =>println("found a unknown exception"+ ex)  
        }  
        println("Rest of the code is executing...")  
    }  
}  
object exceptionTryCatch2{  
    def main(args:Array[String]){  
        var e = new ExceptionExample()  
        e.divide(100,10)  

    }  
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/exceptionTryCatch2.scala
```

**Scala try catch示例3**

文件名:exceptionTryCatch.scala

```scala
import java.io.FileReader
import java.io.FileNotFoundException
import java.io.IOException

object exceptionTryCatch {
   def main(args: Array[String]) {
      try {
         val f = new FileReader("input.txt")
      } catch {
         case ex: FileNotFoundException =>{
            println("Missing file exception")
         }

         case ex: IOException => {
            println("IO Exception")
         }
      }
   }
}
```

`try-catch`表达式的行为与其他具有异常的语言相同。它在主体中执行，如果它抛出一个异常，则会依次尝试每个`catch`子句。

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/exceptionTryCatch.scala

#创建input.txt后看看会不会触发异常
cd ~
echo 'this is test content' > input.txt
scala /share/lesson/scala/exceptionTryCatch.scala
```


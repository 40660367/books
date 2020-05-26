# Scala 引发异常throw关键字

可以在代码中明确地抛出异常。Scala提供`throw`关键字来抛出异常。 `throw`关键字主要用于抛出自定义异常。下面给出了使用scala `throw`异常关键字的例子。

**Scala Throw示例**

文件名:exceptionThrow.scala

```scala
class ExceptionExample2{  
    def validate(age:Int)={  
        if(age<18)  
            throw new ArithmeticException("You are not eligible")  
        else println("You are eligible")  
    }  
}  

object exceptionThrow{  
    def main(args:Array[String]){  
        var e = new ExceptionExample2()  
        e.validate(10)  

    }  
}
```


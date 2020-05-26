# Scala Case类和对象

Scala `Case`类只是常规类，默认情况下是不可变的，可通过模式匹配可分解。

它使用相等(`equal`)方法在结构上比较实例。它不使用`new`关键字实例化对象。

默认情况下，`case`类中列出的所有参数默认使用`public`和`immutable`修辞符。

**语法**

```scala
case class className(parameters)
```

**Scala Case类示例**

文件名:oobCase.scala

```scala
case class CaseClass(a:Int, b:Int)  

object oobCase{  
    def main(args:Array[String]){  
        var c =  CaseClass(10,10)       // Creating object of case class  
        println("a = "+c.a)               // Accessing elements of case class  
        println("b = "+c.b)  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobCase.scala
```

## Scala Case类和模式匹配示例

`Case`类支持模式匹配。 所以，可以在模式中使用它。以下是`Case`类和模式的示例。

没有参数的`case`类将被声明为`case`对象而不是`case`类。 默认情况下，`case`对象是可序列化的。

文件名:oobCaseSeq.scala

```scala
trait SuperTrait  
case class CaseClass1(a:Int,b:Int) extends SuperTrait  
case class CaseClass2(a:Int) extends SuperTrait         // Case class  
case object CaseObject extends SuperTrait               // Case object  
object oobCaseSeq{  
    def main(args:Array[String]){  
        callCase(CaseClass1(10,10))  
        callCase(CaseClass2(10))  
        callCase(CaseObject)  
    }  
    def callCase(f:SuperTrait) = f match{  
        case CaseClass1(f,g)=>println("a = "+f+" b ="+g)  
        case CaseClass2(f)=>println("a = "+f)  
        case CaseObject=>println("No Argument")  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobCaseSeq.scala
```

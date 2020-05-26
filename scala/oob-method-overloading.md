# Scala 方法重载(method overloading)

Scala提供了方法重载功能，使我们能够定义相同名称但使用不同参数或数据类型的方法。 它有助于优化代码。

**Scala方法通过使用不同的参数重载示例**

在下面的例子中，定义了两个具有不同数量的参数但具有相同数据类型的`add`方法。

文件名:oobMethodOverloading1.scala

```scala
class Arithmetic{  
    def add(a:Int, b:Int){  
        var sum = a+b  
        println(sum)  
    }  
    def add(a:Int, b:Int, c:Int){  
        var sum = a+b+c  
        println(sum)  
    }  
}  

object oobMethodOverloading1{  
    def main(args:Array[String]){  
        var a  = new Arithmetic();  
        a.add(10,20);  
        a.add(10,20,30);  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobMethodOverloading1.scala
```



**Scala通过使用不同的数据类型方法重载示例**

在下面的例子中，创建了一个使用两个相同数量的参数但是不同的数据类型的`add`方法。

文件名:oobMethodOverloading2.scala

```scala
class Arithmetic{  
    def add(a:Int, b:Int){  
        var sum = a+b  
        println(sum)  
    }  
    def add(a:Double, b:Double){  
        var sum = a+b  
        println(sum)  
    }  
}  
object oobMethodOverloading2{  
    def main(args:Array[String]){  
        var b = new Arithmetic()  
        b.add(10,20)  
        b.add(10.0,20.1)  

    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobMethodOverloading2.scala
```


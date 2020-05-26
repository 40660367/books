# Scala final关键字

`final`是一个关键字，用于防止超类成员继承为派生类。也可以声明`final`变量，方法和类。

## Scala final变量示例

不能覆盖子类中的`final`变量，我们来看下面一个例子。

**Scala单继承示例**

文件名:oobFinal1.scala

```scala
class Vehicle{  
     final val speed:Int = 60  
}  
class Bike extends Vehicle{  
   override val speed:Int = 100  
    def show(){  
        println(speed)  
    }  
}  

object oobFinal1{  
    def main(args:Array[String]){  
        var b = new Bike()  
        b.show()  
    }  
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/oobFinal1.scala
```

## Scala final方法

在父类中的`final`方法声明不能被覆盖。 如果不想让它被覆盖，则可以把方法定义成为`final`。尝试覆盖`final`方法将导致编译时错误。

**Scala final方法示例**

文件名:oobFinal2.scala

```scala
class Vehicle{  
     final def show(){  
         println("vehicle is running")  
     }  
}  
class Bike extends Vehicle{  
   //override val speed:Int = 100  
    override def show(){  
        println("bike is running")  
    }  
}  
object oobFinal2{  
    def main(args:Array[String]){  
        var b = new Bike()  
        b.show()  
    }  
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/oobFinal2.scala
```

**Scala final类示例**

也可以定义`final`类，`final`类不能继承。 如果定义了一个类为`final`类，那就不能进一步扩展了。

文件名:oobFinal3.scala

```scala
final class Vehicle{  
     def show(){  
         println("vehicle is running")  
     }  

}  

class Bike extends Vehicle{  
       override def show(){  
        println("bike is running")  
    }  
}  

object oobFinal3{  
    def main(args:Array[String]){  
        var b = new Bike()  
        b.show()  
    }  
}
```

使用以下命令编译和执行此程序。

```bash
scala /share/lesson/scala/oobFinal3.scala
```
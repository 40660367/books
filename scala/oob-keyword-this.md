# Scala this关键字

在scala中，`this`是一个关键字，用于引用当前对象。可以使用`this`关键字调用实例变量，方法，构造函数。

## Scala this示例

在以下示例中，这用于调用实例变量和主要构造方法。

文件名:oobThis.scala

```scala
class ThisExample{  
    var id:Int = 0  
    var name: String = ""  
    def this(id:Int, name:String){  
        this()  
        this.id = id  
        this.name = name  
    }  
    def show(){  
        println(id+" "+name)  
    }  
}  

object oobThis{  
    def main(args:Array[String]){  
        var t = new ThisExample(1010,"Maxsu")  
        t.show()  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobThis.scala
```



**Scala构造函数使用this关键字调用**

在下面的例子中，使用`this`关键字来调用构造函数。它演示了如何从其他构造函数调用构造函数。必须确保`this`必须放在构造函数中的第一个语句，同时调用其他构造函数，否则编译器会抛出错误。

文件名:oobThisInit.scala

```scala
class Student(name:String){  
    def this(name:String, age:Int){  
        this(name)  
        println(name+" "+age)  
    }      
}  

object oobThisInit{  
    def main(args:Array[String]){  
        var s = new Student("Maxsu",1000)  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobThisInit.scala
```
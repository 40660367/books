# Scala 构造函数

在scala中，构造函数不是特殊的方法。Scala提供主要和任意数量的辅助构造函数。我们将在下面的例子中逐一个详细解释。

## Scala默认主构造函数

在scala中，如果不指定主构造函数，编译器将创建一个主构造函数的构造函数。 所有类的主体的声明都被视为构造函数的一部分。它也被称为默认构造函数。

**Scala默认主构造函数示例**

```scala
class Student{  
    println("Hello from default constructor");  
}
```

## Scala主要构造函数

Scala提供了一个类的主构造函数的概念。如果代码只有一个构造函数，则可以不需要定义明确的构造函数。它有助于优化代码，可以创建具有零个或多个参数的主构造函数。

**Scala主构造函数示例**

文件名:oobConstructor.scala

```scala
class Student(id:Int, name:String){  
    def showDetails(){  
        println(id+" "+name);  
    }  
}  

object Demo{  
    def main(args:Array[String]){  
        var s = new Student(1010,"Maxsu");  
        s.showDetails()  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobConstructor.scala
```



## Scala次要(辅助)构造器

可以在类中创建任意数量的辅助构造函数，必须要从辅助构造函数内部调用主构造函数。`this`关键字用于从其他构造函数调用构造函数。当调用其他构造函数时，要将其放在构造函数中的第一行。

**Scala二次构造函数示例**

文件名:oobConstructorAux.scala

```scala
class Student(id:Int, name:String){  
    var age:Int = 0  
    def showDetails(){  
        println(id+" "+name+" "+age)  
    }  
    def this(id:Int, name:String,age:Int){  
        this(id,name)       // Calling primary constructor, and it is first line  
        this.age = age  
    }  
}  

object oobConstructorAux{  
    def main(args:Array[String]){  
        var s = new Student(1010,"Maxsu", 25);  
        s.showDetails()  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobConstructorAux.scala
```



## Scala示例：构造器重载

在scala中，可以重载构造函数。下面我们来看一个例子。

文件名:oobConstructorReload.scala

```scala
class Student(id:Int){  
    def this(id:Int, name:String)={  
        this(id)  
        println(id+" "+name)  
    }  
    println(id)  
}  

object oobConstructorReload{  
    def main(args:Array[String]){  
        new Student(101)  
        new Student(100,"Minsu")  
    }  
}
```

用于以下命令编译和执行这两个程序，输出结果如下 - 

```bash
scala /share/lesson/scala/oobConstructorReload.scala
```


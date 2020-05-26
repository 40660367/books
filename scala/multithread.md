# Scala 多线程(multi-thread)

多线程是同时执行多个线程的过程。 它允许您独立执行多个操作。可以通过使用多线程来实现多任务。线程是轻量级的子进程，占用较少的内存。多线程用于在Scala中开发并发应用程序。

Scala不提供用于创建线程的任何单独的库。如果您熟悉Java的多线程概念，那么将会了解到它与Scala语言本身的语法相似。

可以通过扩展`Thread`类或`Runnable`接口来创建线程。两者都提供了运行方法来提供具体的实现。

## Scala线程生命周期

线程生命周期是线程开始和终止的时间跨度。它有各种各样的阶段，如新，可运行，终止，阻止等。线程类提供了各种方法来监视线程的状态。

Scala线程状态如下：

- 新建(New)
- 可运行(Runnable)
- 运行(Running)
- 不可运行(Non-Runnable - 阻塞)
- 终止(Terminated)

![img](http://www.yiibai.com/uploads/images/201709/0409/316090902_46598.png)

**1. 新建(New)**

这是线程的第一个状态，在新线程开始之前。

**2. 可运行(Runnable)**

这是线程已经启动但是线程调度程序没有选择它作为正在运行的线程的状态。

**3. 运行(Running)**

如果线程调度程序选择了该线程，则该线程处于运行状态。

**4. 不可运行(Non-Runnable - 阻塞)**

这是线程仍然存在但由于等待输入或资源而无法运行的状态。

**5. 终止(Terminated)**

当`run()`方法退出时，线程处于终止或死亡状态。

## 创建多线程

在Scala中，创建线程有两种方法：

- 通过扩展`Thread`类
- 通过实现`Runnable`接口

**通过扩展Thread类的Scala线程示例**

以下示例扩展了`Thread`类并覆盖了`run`方法，`start()`方法用于启动线程。

文件名:multithreadDemo1.scala

```scala
class ThreadExample extends Thread{  
    override def run(){  
    println("Thread is running?");  
    }  
}  
object multithreadDemo1{  
    def main(args:Array[String]){  
        var t = new ThreadExample()  
        t.start()  
    }  
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/multithreadDemo1.scala
```



**通过扩展Runnable接口的Scala线程示例**

以下示例实现了`Runnable`接口并覆盖了`run`方法。 `start()`方法用于启动线程。

文件名:multithreadDemo2.scala

```scala
class ThreadExample extends Runnable{  
    override def run(){  
        println("Thread is running...")  
    }  
}  
object multithreadDemo2{  
    def main(args:Array[String]){  
        var e = new ThreadExample()  
        var t = new Thread(e)  
        t.start()  
    }  
}
```

使用以下命令编译和执行此程序。

```shell
scala /share/lesson/scala/multithreadDemo2.scala
```


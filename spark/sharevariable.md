# Spark RDD 共享变量(shared variable)

在Spark中，当任何函数传递给转换操作时，它将在远程集群节点上执行。它适用于函数中使用的所有变量的不同副本。这些变量将复制到每台计算机，并且远程计算机上的变量更新不会恢复到驱动程序。

## 广播变量

广播变量支持在每台机器上缓存的只读变量，而不是提供任务的副本。Spark使用广播算法来分发广播变量以降低通信成本。

spark动作的执行经过几个阶段，由分布式“shuffle”操作分开。Spark自动广播每个阶段中任务所需的公共数据。以这种方式广播的数据以序列化形式缓存并在运行每个任务之前反序列化。

要创建广播变量(比方说，`v`)，请调用`SparkContext.broadcast(v)`。让我们通过一个例子来理解。

```scale
val a=sc.longAccumulator("Accumulator")  
sc.parallelize(Array(2,5)).foreach(x=>a.add(x))  
a.value
```

## 累加器

累加器是用于执行关联和交换操作(例如计数器或总和)的变量。Spark为数字类型的累加器提供支持。但是，可以添加对新类型的支持。

要创建数字累加器，请调用`SparkContext.longAccumulator()`或`SparkContext.doubleAccumulator()`以累积`Long`或`Double`类型的值。

**示例**

```scale
val a=sc.longAccumulator("Accumulator")  
sc.parallelize(Array(2,5)).foreach(x=>a.add(x))  
a.value
```
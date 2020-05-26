# Spark RDD(弹性分布式数据集)		

RDD(弹性分布式数据集)是Spark的核心抽象。它是一组元素，在集群的节点之间进行分区，以便我们可以对其执行各种并行操作。

有两种方法可以用来创建RDD：

- 并行化驱动程序中的现有数据
- 引用外部存储系统中的数据集，例如：共享文件系统，HDFS，HBase或提供Hadoop InputFormat的数据源。

## 并行化集合

要创建并行化集合，请在驱动程序中的现有集合上调用`SparkContext`的`parallelize`方法。复制集合的每个元素以形成可以并行操作的分布式数据集。

```scala
val info = Array(1, 2, 3, 4)  
val distinfo = sc.parallelize(info)
```

现在，可以操作分布式数据集(distinguishedfo)，例如：`distinfo.reduce((a, b) => a + b)`。

## 外部数据集

在Spark中，可以从Hadoop支持的任何类型的存储源(如HDFS，Cassandra，HBase甚至本地文件系统)创建分布式数据集。Spark提供对文本文件，`SequenceFiles`和其他类型的Hadoop InputFormat的支持。

`SparkContext`的`textFile`方法可用于创建RDD的文本文件。此方法获取文件的URI(计算机上的本地路径或`hdfs://`)并读取文件的数据。

现在，可以通过数据集操作来操作数据，例如使用`map`和`reduceoperations`来添加所有行的大小，如下所示：`data.map(s => s.length).reduce((a, b) => a + b)`。

## RDD持久化	

Spark通过在操作中将其持久保存在内存中，提供了一种处理数据集的便捷方式。在持久化RDD的同时，每个节点都存储它在内存中计算的任何分区。也可以在该数据集的其他任务中重用它们。

我们可以使用`persist()`或`cache()`方法来标记要保留的RDD。Spark的缓存是容错的。在任何情况下，如果RDD的分区丢失，它将使用最初创建它的转换自动重新计算。

存在可用于存储持久RDD的不同存储级别。通过将`StorageLevel`对象(Scala，Java，Python)传递给`persist()`来使用这些级别。但是，`cache()`方法用于默认存储级别，即`StorageLevel.MEMORY_ONLY`。

以下是存储级别的集合：

| 存储级别                             | 描述                                                         |
| ------------------------------------ | ------------------------------------------------------------ |
| `MEMORY_ONLY`                        | 它将RDD存储为JVM中的反序列化Java对象。这是默认级别。如果RDD不适合内存，则每次需要时都不会缓存和重新计算某些分区。 |
| `MEMORY_AND_DISK`                    | 它将RDD存储为JVM中的反序列化Java对象。如果RDD不适合内存，请存储不适合磁盘的分区，并在需要时从那里读取它们。 |
| `MEMORY_ONLY_SER`                    | 它将RDD存储为序列化Java对象(即每个分区一个字节的数组)。这通常比反序列化的对象更节省空间。 |
| `MEMORY_AND_DISK_SER`                | 它类似于`MEMORY_ONLY_SER`，但是将内存中不适合的分区溢出到磁盘而不是重新计算它们。 |
| `DISK_ONLY`                          | 它仅将RDD分区存储在磁盘上。                                  |
| `MEMORY_ONLY_2`, `MEMORY_AND_DISK_2` | 它与上面的级别相同，但复制两个群集节点上的每个分区。         |
| `OFF_HEAP`                           | 它类似于`MEMORY_ONLY_SER`，但将数据存储在堆外内存中。必须启用堆外内存。 |

# Spark RDD操作	

RDD提供两种类型的操作：

- 转换Transform
- 执行Action

## 转换Transform

在Spark中，转换的作用是从现有数据集创建新数据集。转换是惰性的，因为它们仅在动作需要将结果返回到驱动程序时才计算。

下面来看看一些常用的RDD转换。

- `map(func)` - 它返回一个新的分布式数据集， 该数据集是通过函数`func`传递源的每个元素而形成的。
- `filter(func)` - 它返回一个新数据集， 该数据集是通过选择函数`func`返回`true`的源元素而形成的。
- `flatMap(func)` - 这里，每个输入项可以映射到零个或多个输出项， 因此函数`func`应该返回序列而不是单个项。
- `mapPartitions(func)` - 它类似于map，但是在RDD的每个分区(块)上单独运行， 因此当在类型T的RDD上运行时， `func`必须是`Iterator  => Iterator `类型。
- `mapPartitionsWithIndex(func)` - 它类似于`mapPartitions`，它为`func`提供了一个表示分区索引的整数值，因此当在类型T的RDD上运行时，`func`必须是类型`(Int，Iterator )=> Iterator `。
- `sample(withReplacement, fraction, seed)` - 它使用给定的随机数生成器种子对数据的分数部分进行采样，有或没有替换。
- `union(otherDataset)` - 它返回一个新数据集，其中包含源数据集和参数中元素的并集。
- `intersection(otherDataset)` - 它返回一个新的RDD，其中包含源数据集和参数中的元素的交集。
- `distinct([numPartitions]))` - 它返回一个新数据集，其中包含源数据集的不同元素。
- `groupByKey([numPartitions])` - 当在`(K，V)`对的数据集上调用时，它返回`(K，Iterable)`对的数据集。
- `reduceByKey(func, [numPartitions])` - 当调用`(K，V)`对的数据集时，返回`(K，V)`对的数据集，其中使用给定的`reduce`函数`func`聚合每个键的值，该函数必须是类型`(V，V)=>V`。
- `aggregateByKey(zeroValue)(seqOp, combOp, [numPartitions])` - 当调用`(K，V)`对的数据集时，返回`(K，U)`对的数据集，其中使用给定的组合函数和中性“零”值聚合每个键的值。
- `sortByKey([ascending], [numPartitions])` - 它返回按键按升序或降序排序的键值对的数据集，如在布尔`ascending`参数中所指定。
- `join(otherDataset, [numPartitions])`-当调用类型`(K，V)`和`(K，W)`的数据集时，返回`(K，(V，W))`对的数据集以及每个键的所有元素对。通过`leftOuterJoin`，`rightOuterJoin`和`fullOuterJoin`支持外连接。
- `cogroup(otherDataset, [numPartitions])`-当调用类型`(K，V)`和`(K，W)`的数据集时，返回`(K，(Iterable，Iterable))`元组的数据集。此操作也称为`groupWith`。
- `cartesian(otherDataset)`-当调用类型为T和U的数据集时，返回`(T，U)`对的数据集(所有元素对)。
- `pipe(command, [envVars])`-通过shell命令管道RDD的每个分区，例如， 一个Perl或bash脚本。
- `coalesce(numPartitions)`-它将RDD中的分区数减少到`numPartitions`。
- `repartition(numPartitions)` -它随机重新调整RDD中的数据，以创建更多或更少的分区，并在它们之间进行平衡。
- `repartitionAndSortWithinPartitions(partitioner)` - 它根据给定的分区器对RDD进行重新分区，并在每个生成的分区中键对记录进行排序。

## 执行Action

在Spark中，操作的作用是在对数据集运行计算后将值返回给驱动程序。

下面来看看一些常用的RDD操作。

| 操作                                       | 描述                                                         |
| ------------------------------------------ | ------------------------------------------------------------ |
| `reduce(func)`                             | 它使用函数func(它接受两个参数并返回一个)来聚合数据集的元素。该函数应该是可交换的和关联的，以便可以并行正确计算。 |
| `collect()`                                | 它将数据集的所有元素作为数组返回到驱动程序中。在过滤器或其他返回足够小的数据子集的操作之后，这通常很有用。 |
| `count()`                                  | 它返回数据集中的元素数。                                     |
| `first()`                                  | 它返回数据集的第一个元素(类似于`take(1)`)。                  |
| `take(n)`                                  | 它返回一个包含数据集的前n个元素的数组。                      |
| `takeSample(withReplacement, num, [seed])` | 它返回一个数组，其中包含数据集的num个元素的随机样本，有或没有替换，可选地预先指定随机数生成器种子。 |
| `takeOrdered(n, [ordering])`               | 它使用自然顺序或自定义比较器返回RDD的前n个元素。             |
| `saveAsTextFile(path)`                     | 它用于将数据集的元素作为文本文件(或文本文件集)写入本地文件系统，HDFS或任何其他Hadoop支持的文件系统的给定目录中。 |
| `saveAsSequenceFile(path)`                 | 它用于在本地文件系统，HDFS或任何其他Hadoop支持的文件系统中的给定路径中将数据集的元素编写为Hadoop SequenceFile。 |
| `saveAsObjectFile(path)`                   | 它用于使用Java序列化以简单格式编写数据集的元素，然后可以使用`SparkContext.objectFile()`加载。 |
| `countByKey()`                             | 它仅适用于类型(K，V)的RDD。因此，它返回(K，Int)对的散列映射与每个键的计数。 |
| `foreach(func)`                            | 它在数据集的每个元素上运行函数`func`以获得副作用，例如更新累加器或与外部存储系统交互。 |
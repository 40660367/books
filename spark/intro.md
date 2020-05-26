# Spark 简介

![spark](./images/spark.png)

Spark是加州大学伯克利分校AMP实验室（Algorithms, Machines, and People Lab）开发的**通用**内存并行计算框架

Spark使用Scala语言进行实现，它是一种面向对象、函数式编程语言，能够像操作本地集合对象一样轻松地操作分布式数据集，具有以下特点。

1.运行速度快：Spark拥有DAG执行引擎，支持在内存中对数据进行迭代计算。官方提供的数据表明，如果数据由磁盘读取，速度是Hadoop MapReduce的10倍以上，如果数据从内存中读取，速度可以高达100多倍。

2.易用性好：Spark不仅支持Scala编写应用程序，而且支持Java和Python等语言进行编写，特别是Scala是一种高效、可拓展的语言，能够用简洁的代码处理较为复杂的处理工作。

3.通用性强：Spark生态圈即BDAS（伯克利数据分析栈）包含了Spark Core、Spark SQL、Spark Streaming、MLLib和GraphX等组件，这些组件分别处理Spark Core提供内存计算框架、SparkStreaming的实时处理应用、Spark SQL的即席查询、MLlib或MLbase的机器学习和GraphX的图处理。

4.随处运行：Spark具有很强的适应性，能够读取HDFS、Cassandra、HBase、S3和Techyon为持久层读写原生数据，能够以Mesos、YARN和自身携带的Standalone作为资源管理器调度job，来完成Spark应用程序的计算

## Spark与Hadoop差异

Spark是在借鉴了MapReduce之上发展而来的，继承了其分布式并行计算的优点并改进了MapReduce明显的缺陷，具体如下：

首先，Spark把中间数据放到内存中，迭代运算效率高。MapReduce中计算结果需要落地，保存到磁盘上，这样势必会影响整体速度，而Spark支持DAG图的分布式并行计算的编程框架，减少了迭代过程中数据的落地，提高了处理效率。

其次，Spark容错性高。Spark引进了弹性分布式数据集RDD (Resilient Distributed Dataset)�0�2的抽象，它是分布在一组节点中的只读对象集合，这些集合是弹性的，如果数据集一部分丢失，则可以根据“血统”（即充许基于数据衍生过程）对它们进行重建。另外在RDD计算时可以通过CheckPoint来实现容错，而CheckPoint有两种方式：CheckPoint Data，和Logging The Updates，用户可以控制采用哪种方式来实现容错。

最后，Spark更加通用。不像Hadoop只提供了Map和Reduce两种操作，Spark提供的数据集操作类型有很多种，大致分为：Transformations和Actions两大类。Transformations包括Map、Filter、FlatMap、Sample、GroupByKey、ReduceByKey、Union、Join、Cogroup、MapValues、Sort和PartionBy等多种操作类型，同时还提供Count, Actions包括Collect、Reduce、Lookup和Save等操作。另外各个处理节点之间的通信模型不再像Hadoop只有Shuffle一种模式，用户可以命名、物化，控制中间结果的存储、分区等。

## Spark的适用场景

目前大数据处理场景有以下几个类型：

复杂的批量处理（Batch Data Processing），偏重点在于处理海量数据的能力，至于处理速度可忍受，通常的时间可能是在数十分钟到数小时；

基于历史数据的交互式查询（Interactive Query），通常的时间在数十秒到数十分钟之间

基于实时数据流的数据处理（Streaming Data Processing），通常在数百毫秒到数秒之间

目前对以上三种场景需求都有比较成熟的处理框架，第一种情况可以用Hadoop的MapReduce来进行批量海量数据处理，第二种情况可以Impala进行交互式查询，对于第三中情况可以用Storm分布式处理框架处理实时流式数据。以上三者都是比较独立，各自一套维护成本比较高，而Spark的出现能够一站式平台满意以上需求。

## Spark常用术语

| 术语            | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| Application     | Spark的应用程序，包含一个Driver program和若干Executor    |
| SparkContext    | Spark应用程序的入口，负责调度各个运算资源，协调各个Worker Node上的Executor |
| Driver Program  | 运行Application的main()函数并且创建SparkContext              |
| Executor        | 是为Application运行在Worker node上的一个进程，该进程负责运行Task，并且负责将数据存在内存或者磁盘上。每个Application都会申请各自的Executor来处理任务 |
| Cluster Manager | 在集群上获取资源的外部服务(例如：Standalone、Mesos、Yarn)    |
| Worker Node     | 集群中任何可以运行Application代码的节点，运行一个或多个Executor进程 |
| Task            | 运行在Executor上的工作单元                                   |
| Job             | SparkContext提交的具体Action操作，常和Action对应             |
| Stage           | 每个Job会被拆分很多组task，每组任务被称为Stage，也称TaskSet  |
| RDD             | 是Resilient distributed datasets的简称，中文为弹性分布式数据集;是Spark最核心的模块和类 |
| DAGScheduler    | 根据Job构建基于Stage的DAG，并提交Stage给TaskScheduler        |
| TaskScheduler   | 将Taskset提交给Worker node集群运行并返回结果                 |
| Transformations | 是Spark API的一种类型，Transformation返回值还是一个RDD，所有的Transformation采用的都是懒策略，如果只是将Transformation提交是不会执行计算的 |
| Action          | 是Spark API的一种类型，Action返回值不是一个RDD，而是一个scala集合；计算只有在Action被提交的时候计算才被触发。 |
# Hadoop 简介

Hadoop由Apache基金会开发的分布式系统基础架构，是利用集群对大量数据进行分布式处理和存储的软件框架。用户可以轻松地在Hadoop集群上开发和运行处理海量数据的应用程序。Hadoop有高可靠，高扩展，高效性，高容错等优点。

Hadoop 框架最核心的设计就是HDFS和MapReduce。HDFS为海量的数据提供了存储，MapReduce为海量的数据提供了计算。此外，Hadoop还包括了Hive，Hbase，ZooKeeper，Pig，Avro，Sqoop，Flume，Mahout等项目。



## Hadoop运行模式

Hadoop的运行模式分为3种：单机模式(standalone)，模拟分布运行模式，完全分布运行模式。

**1.单机模式(standalone)**

这种运行模式在一台单机上运行，没有HDFS分布式文件系统，而是直接读写本地操作系统中的文件系统。在本地运行模式（local mode）中不存在守护进程，所有进程都运行在一个JVM上。单机模式适用于开发阶段运行MapReduce程序，这也是最少使用的一个模式。

**2.模拟分布模式**

这种运行模式是在单台服务器上模拟Hadoop的完全分布模式，单机上的分布式并不是真正的分布式，而是使用线程模拟的分布式。在这个模式中，所有守护进程(NameNode，DataNode，ResourceManager，NodeManager，SecondaryNameNode)都在同一台机器上运行。因为伪分布运行模式的Hadoop集群只有一个节点，所以HDFS中的块复制将限制为单个副本，其secondary-master和slave也都将运行于本地主机。此种模式除了并非真正意义的分布式之外，其程序执行逻辑完全类似于完全分布式，因此，常用于开发人员测试程序的执行。本次实验就是在一台服务器上进行伪分布运行模式的搭建。

**3.完全分布模式**

这种模式通常被用于生产环境，使用N台主机组成一个Hadoop集群，Hadoop守护进程运行在每台主机之上。这里会存在Namenode运行的主机，Datanode运行的主机，以及SecondaryNameNode运行的主机。在完全分布式环境下，主节点和从节点会分开。

# Spark 安装及环境配置

## Spark运行模式概述

Spark主要支持三种分布式部署方式：分别是standalone、Spark on mesos和spark on YARN，其中，第一种类似于MapReduce 1.0所采用的模式，内部实现了容错性和资源管理，后两种则是未来发展的趋势，部分容错性和资源管理交由统一的资源管理系统完成：让Spark运行在一个通用的资源管理系统之上，这样可以与其他计算框架，比如MapReduce共用一个集群资源，最大的好处是降低运维成本和提高资源利用率（资源按需分配）。

## 安装配置

**安装JDK**

```bash
cp /share/tar/jdk-8u241-linux-x64.tar.gz  /usr/local/
#tar -xzvf 对文件进行解压缩，-C 指定解压后，将文件放到/usr/local目录下。
tar -xzvf /usr/local/jdk-8u241-linux-x64.tar.gz -C /usr/local/
mv /usr/local/jdk1.8.0_241 /usr/local/java
```

下面来修改环境变量：系统环境变量或用户环境变量。我们在这里修改用户环境变量。

```bash
echo 'export JAVA_HOME=/usr/local/java' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc  #生效环境变量
```

验证java安装，测试环境变量是否配置正确。如果出现正确的版本信息提示，则安装成功

```bash
java
```

**安装Spark**

```bash
cp /share/tar/spark-2.4.5-bin-hadoop2.7.tgz /usr/local
tar -xzvf /usr/local/spark-2.4.5-bin-hadoop2.7.tgz  -C /usr/local
mv /usr/local/spark-2.4.5-bin-hadoop2.7 /usr/local/spark
```


```bash
echo 'export SPARK_HOME=/usr/local/spark' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```
**启动spark**

```bash
cd $SPARK_HOME/sbin && /start-all.sh
```

**使用交互式命令行界面**

```bash
spark-shell
```

```
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.4.5
      /_/
         
Using Scala version 2.11.12 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_241)
Type in expressions to have them evaluated.
Type :help for more information.
scala>
```

在`scala>`提示符后便可交互式Scale语言而使用Spark了。

**使用UI界面**

实验区切换到VNC界面，在FireFox浏览器中打开以下网址：`localhost:4040`
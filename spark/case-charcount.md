# Spark 字符统计示例

## 环境准备

该示例需要[安装Hadoop](/hadoop/setup.html),以及[Spark](./setup.html)

在Spark字符统计示例中，将找出指定文件中每个字符的频率。在这里，使用Scala语言来执行Spark操作。

## 执行Spark字符计数示例的步骤

在此示例中，计算并显示每个字符的出现次数。在本地计算机中创建一个文本文件并在其中写入一些文本。

向sparkdata.txt 文件中写入的文本。

```bash
cd ~
echo 'spark char count test file now created!' > sparkdata.txt
```

在HDFS中创建一个目录，保存文本文件。

```bash
hdfs dfs -mkdir /spark
```

将HDD上的*sparkdata.txt* 文件上传到特定目录中。

```bash
hdfs dfs -put ~/sparkdata.txt /spark
```

现在，按照以下命令在Scala模式下打开spark。

```bash
cd ~ && spark-shell
```

使用以下命令创建一个RDD。

```scale
val data=sc.textFile("sparkdata.txt");
```

在这里，传递包含数据的任何文件名。现在，可以使用以下命令读取生成的结果。

```scale
data.collect;
```

在这里，使用以下命令以单个单词的形式拆分现有数据。

```scale
val splitdata = data.flatMap(line => line.split(""));
```

现在，可以使用以下命令读取生成的结果。

```bash
splitdata.collect;
```

执行映射操作，如下所示：

```scale
val mapdata = splitdata.map(word => (word,1));
```

在这里，我们为每个单词分配值`1`。现在，可以使用以下命令读取生成的结果。

```scale
mapdata.collect;
```

现在，执行`reduce`操作 -

```scale
val reducedata = mapdata.reduceByKey(_+_);
```

在这里，总结了生成的数据。可以使用以下命令读取生成的结果。

```scale
reducedata.collect;
```
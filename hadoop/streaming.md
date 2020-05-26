# Hadoop Streaming

Hadoop Streaming是一种编程工具，它是由hadoop提供的实用程序。该实用程序允许创建和运行Map/Reduce任务的**任何可执行文件或脚本**map函数或reduce函数。

## 为什么要用Hadoop Streaming呢？
Hadoop框架是用java语言写的，hadoop框架中运行的所有应用程序都要用java语言来写才能正常地在hadoop集群中运行。

那么问题来了，如果有些开发者就是不会java语言，但是又想使用mapreduce这个并行计算模型的话，那该怎么办？就是基于这样的考虑，所以hadoop提供了hadoop streaming这个编程工具，它支持用任何编程语言来编写mapreduce的map函数和reduce函数。

但是，map/reduce函数的数据流必须遵循相应编程语言的标准输入输出（stdin、stdout），即你用什么编程语言实现业务逻辑，就必须要通过该语言的标准输入stdin读取数据，通过该语言的标准输出stdout输出数据。

## Hadoop Streaming的数据流
hadoop streaming通过用户编写的map函数中标准输入读取数据（一行一行地读取），按照mapd函数的处理逻辑处理后，将处理后的数据由标准输出进行输出到下一个阶段，reduce函数也是按行读取数据，按照函数的处理逻辑处理完数据后将它们通过标准输出写到hdfs的指定目录中。

> 不管使用的是何种编程语言，在map函数中，原始数据会被处理成<key,value>的形式，但是key与value之间必须通过\t分隔符分隔，分隔符左边的是key，分隔符右边的是value,如果没有使用\t分隔符，那么整行都会被当作key处理。

## 案例1:shell命令作为mapper类以及 reducer类的实现
**准备HDFS文件系统**

```bash
hadoop fs -mkdir -p /streaming
hadoop fs -put /etc/passwd /streaming
```
>  注意：输入的文件必须在hdfs上，输出也是输出到hdfs上。

```undefined
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar \
-input /streaming/passwd \
-output /streaming-output1 \
-mapper /bin/cat \
-reducer /usr/bin/wc
```
**观察输出结果**

```bash
hadoop fs -ls /streaming-output1
hadoop fs -cat /streaming-output1/part-00000
```

## 案例2:shell脚本作为mapper类以及 reducer类的实现

使用Shell脚本处理较复杂的逻辑，如单词统计，每行都有多个单词

**准备HDFS文件系统**

```bash
hadoop fs -mkdir -p /streaming
hadoop fs -put /etc/passwd /streaming
```
**制作map阶段与reduce阶段的脚本**

```
cd ~
cat > mapper.sh <<  EOF
#!/bin/bash
while read line
do
    for word in $line
    do
        echo $word  1
    done
done
EOF

cat > reducer.sh << EOF
#!/bin/bash
count=0
read word1
reduce-word=`echo $word1 | awk  $1`
while read word2
do
    map-word=`echo $-word | awk  $1`
    if [ $reduce-word = $map-word ]
        count=count+1
    else
         echo $reduce-word  $count
         count=0
          reduce-word=map-word
          count=count+1
     fi
done
EOF
```
**提交任务**

```undefined
cd ~
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar \
-input /streaming/passwd \
-output /streaming-output3 \
-mapper mapper.sh \
-reducer reducer.sh \
-file mapper.sh \
-file reducer.sh
```

**观察输出结果**

```bash
hadoop fs -ls /streaming-output2
hadoop fs -cat /streaming-output2/part-0000
```

## Hadoop Stream帮助

```bash
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.10.0.jar --help
```

## 	重要的命令

| 参数                                           | 描述                                                         |
| ---------------------------------------------- | ------------------------------------------------------------ |
| -input directory/file-name                     | 输入位置映射。 （必填）                                      |
| -output directory-name                         | 输出位置的reducer。 （必填）                                 |
| -mapper executable or script or JavaClassName  | 映射器可执行文件。 （必填）                                  |
| -reducer executable or script or JavaClassName | reducer的可执行文件。 （必填）                               |
| -file file-name                                | 使现有的映射器，减速机，或组合的可执行本地计算节点上。       |
| -inputformat JavaClassName                     | 类，应该提供返回键/值对文字类。如果没有指定，使用TextInputFormat作为默认。 |
| -outputformat JavaClassName                    | 类，提供应采取键/值对文字类的。如果没有指定，使用TextOutputformat作为默认值。 |
| -partitioner JavaClassName                     | 类，确定哪个减少一个键被发送。                               |
| -combiner streamingCommand or JavaClassName    | 组合可执行文件映射输出。                                     |
| -cmdenv name=value                             | 通过环境变量数据流的命令。                                   |
| -inputreader                                   | 对于向后兼容性：指定记录读取器类（而不是输入格式类）。       |
| -verbose                                       | 详细的输出。                                                 |
| -lazyOutput                                    | 创建懒输出。例如，如果输出格式是基于FileOutputFormat，输出文件仅在第一次调用output.collect（或Context.write）创建。 |
| -numReduceTasks                                | 指定reducer的数目。                                          |
| -mapdebug                                      | 当map任务失败的脚本调用。                                    |
| -reducedebug                                   | 脚本调用时降低任务失败。                                     |

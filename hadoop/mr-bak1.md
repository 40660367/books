# Hadoop Mapreduce示例

## 示例说明

下面给出是关于一个组织的电消耗量的数据。它包含了每月的用电量，各年的平均。

|      | Jan  | Feb  | Mar  | Apr  | May  | Jun  | Jul  | Aug  | Sep  | Oct  | Nov  | Dec  | Avg  |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1979 | 23   | 23   | 2    | 43   | 24   | 25   | 26   | 26   | 26   | 26   | 25   | 26   | 25   |
| 1980 | 26   | 27   | 28   | 28   | 28   | 30   | 31   | 31   | 31   | 30   | 30   | 30   | 29   |
| 1981 | 31   | 32   | 32   | 32   | 33   | 34   | 35   | 36   | 36   | 34   | 34   | 34   | 34   |
| 1984 | 39   | 38   | 39   | 39   | 39   | 41   | 42   | 43   | 40   | 39   | 38   | 38   | 40   |
| 1985 | 38   | 39   | 39   | 39   | 39   | 41   | 41   | 41   | 00   | 40   | 39   | 39   | 45   |

如果上述数据作为输入，我们需要编写应用程序来处理它而产生的结果，如发现最大使用量，最低使用年份，依此类推。这是一个轻松取胜用于记录有限数目的编程器。他们将编写简单地逻辑，以产生所需的输出，并且将数据传递到写入的应用程序。

但是，代表一个特定状态下所有的大规模产业的电力消耗数据。

当我们编写应用程序来处理这样的大量数据，

- 他们需要大量的时间来执行。
- 将会有一个很大的网络流量，当我们将数据从源到网络服务器等。

为了解决这些问题，使用MapReduce框架。

## 依赖文件说明

#### 数据文件

上述数据被保存为 sample.txt 并作为输入。输入文件看起来如下所示。

文件名:/share/lesson/hadoop/sample.txt

```
1979   23   23   2   43   24   25   26   26   26   26   25   26  25 
1980   26   27   28  28   28   30   31   31   31   30   30   30  29 
1981   31   32   32  32   33   34   35   36   36   34   34   34  34 
1984   39   38   39  39   39   41   42   43   40   39   38   38  40 
1985   38   39   39  39   39   41   41   41   00   40   39   39  45 
```

使用MapReduce框架的样本数据的程序

#### 程序文件

文件名:/share/lesson/hadoop/ProcessUnits.java

```java
package hadoop; 

import java.util.*; 

import java.io.IOException; 
import java.io.IOException; 

import org.apache.hadoop.fs.Path; 
import org.apache.hadoop.conf.*; 
import org.apache.hadoop.io.*; 
import org.apache.hadoop.mapred.*; 
import org.apache.hadoop.util.*; 

public class ProcessUnits 
{ 
   //Mapper class 
   public static class E_EMapper extends MapReduceBase implements 
   Mapper<LongWritable ,/*Input key Type */ 
   Text,                /*Input value Type*/ 
   Text,                /*Output key Type*/ 
   IntWritable>        /*Output value Type*/ 
   { 
      
      //Map function 
      public void map(LongWritable key, Text value, 
      OutputCollector<Text, IntWritable> output,   
      Reporter reporter) throws IOException 
      { 
         String line = value.toString(); 
         String lasttoken = null; 
         StringTokenizer s = new StringTokenizer(line,"\t"); 
         String year = s.nextToken(); 
         
         while(s.hasMoreTokens())
            {
               lasttoken=s.nextToken();
            } 
            
         int avgprice = Integer.parseInt(lasttoken); 
         output.collect(new Text(year), new IntWritable(avgprice)); 
      } 
   } 
   
   
   //Reducer class 
   public static class E_EReduce extends MapReduceBase implements 
   Reducer< Text, IntWritable, Text, IntWritable > 
   {  
   
      //Reduce function 
      public void reduce( Text key, Iterator <IntWritable> values, 
         OutputCollector<Text, IntWritable> output, Reporter reporter) throws IOException 
         { 
            int maxavg=30; 
            int val=Integer.MIN_VALUE; 
            
            while (values.hasNext()) 
            { 
               if((val=values.next().get())>maxavg) 
               { 
                  output.collect(key, new IntWritable(val)); 
               } 
            } 
 
         } 
   }  
   

   //Main function 
   public static void main(String args[])throws Exception 
   { 
      Job job = Job.getInstance();
      conf.setJobName("max_eletricityunits"); 
      conf.setOutputKeyClass(Text.class);
      conf.setOutputValueClass(IntWritable.class); 
      conf.setMapperClass(E_EMapper.class); 
      conf.setCombinerClass(E_EReduce.class); 
      conf.setReducerClass(E_EReduce.class); 
      conf.setInputFormat(TextInputFormat.class); 
      conf.setOutputFormat(TextOutputFormat.class); 
      
      FileInputFormat.setInputPaths(conf, new Path(args[0])); 
      FileOutputFormat.setOutputPath(conf, new Path(args[1])); 
      
      JobClient.runJob(conf); 
   } 
} 
```

#### 依赖jar包：

程序运行还需要hadoop-core-1.2.1.jar，它用于编译和执行MapReduce程序。该文件[URL](https://mvnrepository.com/artifact/org.apache.hadoop/hadoop-core/1.2.1)地址

## 实验开始
### 	编译和执行

按照下面给出编译和执行上面程序的步骤。

下面的命令是创建一个目录来存储编译的Java类。并复制依赖的数据，java文件，jar包。

```bash
mkdir ~/units
cp /share/lesson/hadoop/sample.txt ~/units
cp /share/lesson/hadoop/hadoop-core-1.2.1.jar ~/units
cp /share/lesson/hadoop/ProcessUnits.java ~/units
```

编译ProcessUnits.java程序并创建一个jar程序

```bash
cd ~/units
javac -classpath hadoop-core-1.2.1.jar -d ~/units ProcessUnits.java 
jar -cvf units.jar -C ~/units/ . 
```

```bash
#下面的命令用来创建一个输入目录在HDFS中
hadoop fs -mkdir -p input_dir
#下面的命令用于复制命名sample.txt在HDFS输入目录中输入文件。
hadoop fs -put ~/units/sample.txt input_dir
#下面的命令用来验证在输入目录中的文件
hadoop fs -ls input_dir/ 
```

下面的命令用于通过从输入目录以输入文件来运行Eleunit_max应用。

```bash
cd ~/units
hadoop jar units.jar hadoop.ProcessUnits input_dir output_dir 
```

等待一段时间，直到执行文件。在执行后，如下图所示，输出将包含输入分割的数目，映射任务数，减速器任务的数量等。



下面的命令用来验证在输出文件夹所得文件。

```bash
hadoop fs -ls output_dir/ 
```

下面的命令是用来查看输出Part-00000文件。该文件由HDFS产生。

```bash
hadoop fs -cat output_dir/part-00000 
```

#### 查看作业的状态

**语法**

```
hadoop job -status <JOB-ID> 
```

#### 要查看作业历史在output-dir

**语法**

```
hadoop job -history <DIR-NAME> 
```

#### 终止任务

**语法**

```
hadoop job -kill <JOB-ID> 
hadoop job -kill job_201310191043_0004 
```


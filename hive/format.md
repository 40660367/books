# Hive 存储格式与数据格式

## 数据格式

当数据存储在文本文件中，必须按照一定格式区别行和列，并且在Hive中指明这些区分符。Hive默认使用了几个平时很少出现的字符，这些字符一般不会作为内容出现在记录中。

Hive默认的行和列分隔符如下表所示。

| 分隔符      | 描述                                                         |
| ----------- | ------------------------------------------------------------ |
| \n          | 对于文本文件来说，每行是一条记录，所以\n 来分割记录          |
| ^A (Ctrl+A) | 分割字段，也可以用\001 来表示                                |
| ^B (Ctrl+B) | 用于分割 Arrary 或者 Struct 中的元素，或者用于 map 中键值之间的分割，也可以用\002 分割。 |
| ^C          | 用于 map 中键和值自己分割，也可以用\003 表示。               |

## 存储格式

Hive会为每个创建的数据库在HDFS上创建一个目录，该数据库的表会以子目录形式存储，表中的数据会以表目录下的文件形式存储。对于default数据库，默认的缺省数据库没有自己的目录，default数据库下的表默认存放在/user/hive/warehouse目录下。

**textfile** 

textfile为默认格式，存储方式为行存储。数据不做压缩，磁盘开销大，数据解析开销大。 

**SequenceFile**

SequenceFile是Hadoop API提供的一种二进制文件支持，其具有使用方便、可分割、可压缩的特点。 

SequenceFile支持三种压缩选择：NONE, RECORD, BLOCK。 Record压缩率低，一般建议使用BLOCK压缩。 

**RCFile**

一种行列存储相结合的存储方式。 

**ORCFile**

数据按照行分块，每个块按照列存储，其中每个块都存储有一个索引。hive给出的新格式，属于RCFILE的升级版,性能有大幅度提升,而且数据可以压缩存储,压缩快 快速列存取。 

**Parquet**

Parquet也是一种行式存储，同时具有很好的压缩性能；同时可以减少大量的表扫描和反序列化的时间。

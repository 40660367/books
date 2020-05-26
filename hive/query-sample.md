# Hive 表格采样(table sample)

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

tablesample用于对表的数据采样，但是这个采样是将数据分成多个bucket，抽取其中一个bucket。

**其语句如下：**

```
TABLESAMPLE (BUCKET bucketId OUT OF bucketNum [ON colName])  
```

其中，`bucketId`为抽取的bucket的编号。`bucketNum`表示bucket的数量。如果基于某列来分桶，`colName`就是该列的列名，如果要随机分桶，那么`colName`可以用`rand()`来代替。

## 基于rand()抽样

举一个rand()分桶的例子。如下表示，将musics表中数据随机分为5个bucket，然后抽取编号为2的bucket的数据。因为是随机分的，所以每次执行的结果都不同。

```hql
select * from musics tablesample(bucket 2 out of 5 on rand()) s;
```

```hql
select * from musics tablesample(bucket 2 out of 5 on rand()) s;
```

## 基于列名抽样

举一个按列名分桶抽样的例子。对musics表基于singerid分桶，如果把也算上的话，一共有4位歌手。如果分成4个buckets。依次选择各个桶的数据，如下所示。可以发现，每个桶的数据刚好是各个歌手的歌曲记录。这就是按列名singerid分桶的效果。

```hql
select * from musics tablesample(bucket 1 out of 4 on singerid) s;
```

```hql
select * from musics tablesample(bucket 3 out of 4 on singerid) s;
```

```hql
select * from musics tablesample(bucket 4 out of 4 on singerid) s;
```

如果表在创建时已经使用cluster by分桶，而且tablesample指定的列正是用于分桶的列，那么在抽样时，可以只涉及到表相应的hash分区的数据，而无需扫描整张表。因为表中的数据已经按列的hash值分割到不同的分区。

## 基于百分比的数据块抽样

基于数据块抽样，是根据数据数据块大小的百分比进行抽样。比如输入400M，抽样百分比为25%，那么至少要抽样400*25%=100M的数据。

但是，因为这个抽样的最小单元是一个HDFS数据块。一般一个HDFS数据块大小为128M，那么返回的会是128M而不是100M。

如果表的数据少于一个HDFS数据块的大小，那么会返回所有的数。如下语句采样百分比为50%，但是会返回表中所有数据。

```hql
select * from musics tablesample(0.5 percent) s;
```

## 基于数据大小的数据块抽样

其实这个和基于百分比的数据块抽样类似，只是将百分比换成了数据大小。如下，抽样数据大小为10M，但是因为表数据量过小，未达到一个HDFS块大小，会输出全部的记录。

```hql
select * from musics tablesample(10M) s;
```

## 基于行数的抽样

这种采样的行数，假设行数为r，则其会对每个split的数据都r条数据。如下例子中，因为只存在一个split，则抽取2条数据。

```hql
select * from musics tablesample(2 rows) s;
```


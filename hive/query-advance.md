# Hive 高级查询

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

# sort by和order by

`order by`是将所有的记录都按`order by`后的字段进行排序。`sort by`是将每个reduce的数据进行排序，即局部地对每个分片的数据排序，而不是全局排序。因为`order by`全局排序可能会消耗非常长的时间，如果hive.mapred.mode=strict，hive要求order by的语句后面必须加上limit。如下，对musics表中歌名进行降序排序。因为默认为升序`asc`，因此在`order by`的语句后加上`desc`表示降序排列。`limit 2`表示只返回排名前2的记录。

```hql
select name from musics
order by name desc;
```

# distribute by

因为MR任务可能会包含多个reduce，数据被分成多个分片由不同的reduce处理。`distributed by`控制了这些map输出的数据是如何划分到reduce的。比如，需要将musics表的相同的音乐语种在一起处理，然后按语种、歌手和歌名依次排序。如果没有`distribute by languageid`的语句，就无法保证同样的languageid的记录被分到同一个reduce。

```hql
select singerid, languageid, name
from musics
where singerid not like '%unknow%' and languageid not like '%unknow%'
distribute by languageid
sort by languageid, singerid, name;
```

# cluster by

`cluster by col`其实相当于`distribute by col sort by col asc`。col为列名。在下面的语句也就相当于`distribute by languageid sort by languageid asc`。当然asc是可以省略的。这里加上asc只是为了表示cluster by的结果是升序排列的。

```hql
select singerid, languageid, name
from musics
where singerid not like '%unknow%' and languageid not like '%unknow%'
cluster by languageid;
```

# union/union all

union和union all都是将若干表的数据合并。但是，union会去除表数据重合的部分，但是union all会将所有数据完全保存下来。

union的语句如下，合并后数据没有重复。

```hql
select *  from
( select * from singers union select * from singers) s;
```

union all的语句如下，合并后数据是重复的。

```hql
select *  from
( select * from singers union all select * from singers) s;
```


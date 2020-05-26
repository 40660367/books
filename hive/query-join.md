# Hive 联接查询(Join)

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

##  内连接 inner join

连接musics和singers表。

```hql
select m.name,s.name
from musics m join singers s on m.singerid = s.id;
```

连接musics，singers和languages表。执行了一个MR job。

```hql
select m.name,s.name,l.type
from musics m join singers s on m.singerid = s.id join languages l on m.languageid = l.id;
```

Hive在执行表连接时，会默认最后那个表最大，将前面的表缓存起来，扫描最后的表。因此为了效率，从左到右表的大小应该逐渐增加。在上述的三张表中，如果是真实的数据，显然三张表的从小到大的顺序应该是languages、singers和musics。但是演示的数据只是非常小的人造数据，因此执行不会有什么区别。除了按序连接表，还可以通过`/*streamtable(m)*/`指定最大的驱动表。

```hql
select /*+STREAMTABLE (m)*/ m.name,s.name,l.type
from musics m join singers s on m.singerid = s.id join languages l on m.languageid = l.id;
```

## 笛卡儿积(cross join)

笛卡尔积就是将左边表的记录和右边表的记录两两组合。如果左表有m条记录，右表有n条，那么将产生m*n条记录。笛卡儿积会消耗大量的时间。如果设置hive.mapred.mode=strict，Hive会阻止笛卡儿积查询。

如下是一个例子，将singers和languages进行笛卡儿积。

```hql
select s.name, l.type
from singers s join languages l;
```

## 左连接 left outer join

如果A left outer join B，则A中所有记录都会被返回，如果B中无对应的记录，则相应列值为NULL。

如下，连接musics和singers，musics中音乐Fake Song对应的musicid为，在singers中无对应记录，所以返回的singer列为NULL。

```hql
select  m.name as music, s.name as singer
from musics m left outer join singers s on m.singerid = s.id;
```

如果添加了where语句，比如where singer则只返回符合where语句条件的musics的记录。比如，只选择日文歌，即languageid为L-0003。语句如下所示，其他语言的歌曲被过滤了。

```hql
select  m.name as music, s.name as singer
from musics m left outer join singers s on m.singerid = s.id
where languageid = 'L-0003';
```

尝试在on之后添加过滤的语句，发现输出结果如下。将条件改成m.language != ‘L-0002’，也依然输出一样的结果。没有过滤掉musics表中singerid为‘S-0002’的歌曲《A Step You Can’t Take Back》，而是使得其singers表对应的列为NULL。

```hql
select  m.name as music, s.name as singer
from musics m left outer join singers s on m.singerid = s.id and m.singerid != 'S-0002';
```

将条件改成m.singerid = ‘S-0002’，发现除了符合条件的歌曲《A Step You Can’t Take Back》以外，其他歌曲singer列全为NULL。

```hql
select  m.name as music, s.name as singer
from musics m left outer join singers s on m.singerid = s.id and m.singerid = 'S-0002';
```

这说明不管怎么在on部分设定条件，都不会改变返回的musics表的记录。如果要过滤表的记录，只能在where语句设置，但是where语句是在join完后才执行过滤的，实际上它是大表的过滤。如果想要在join之前就执行过滤，可以通过嵌套子查询的方式。如下：

```hql
select  m.name as music, s.name as singer from
(select * from musics where singerid = 'S-0002') m
left outer join
(select * from singers where id = 'S-0002') s
on m.singerid = s.id;
```

## 右连接 right outer join

返回join右边的表中所有符合条件的记录。左边表若无相应记录，则对应的列用NULL填充。

```hql
select  m.name as music, s.name as singer
from musics m right outer join singers s on m.singerid = s.id;
```

## 外连接 full outer join

返回所有表中所有符合条件的记录。连接的表若无相应记录，则对应的列用NULL填充。

```hql
select  m.name as music, s.name as singer
from musics m full outer join singers s on m.singerid = s.id;
```

## 左单连接 left semi join

eft semi join，只会返回左边的记录，但前提是右边的表必须满足on后面定义的判定条件。比如，现在需要查询rie fu这个歌手的所有歌曲。那么可以连接musics和singers这两张表。使用left semi join可以直接将s.name=’Rie fu’的判定条件添加在on后面的部分。

```hql
select  m.name as music
from musics m left semi join singers s on m.singerid = s.id and s.name = 'Rie fu';
```

如果去掉关于rie fu的判定条件，如下面的语句，查询的目的就变成了：如果musics表中某条记录的singerid存在于singers表中，那么可以返回这个记录。在sql中，这其实相当于in exists的结构，但是hive中并不支持这样的形式。left semi join比inner join更加高效，因为它只要查找到了相应的记录就可以停止扫描，因此不需要扫描整张表。

```hql
select  m.name as music
from musics m left semi join singers s on m.singerid = s.id;
```

其实这个on后面的语句可以理解为，如果在singers表中能找到一个记录的id和musics这条记录的singerid相同，那么这个musics记录可以返回。如果说，把on后面的语句设为s.id=’Rie fu’，因为在singers表中，存在Rie fu这位歌手，因此，这条语句一直都是true，musics表的每条记录都可以返回。

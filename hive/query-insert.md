# 通过insert查询插入数据

可以通过查询其他表中符合条件的数据，将查询结果插入目的表中。

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

## 单个查询插入

如下，将products表中来自中国的电子产品数据插入part_products表的(type=’electronics’, locality=’China’)分区中。
注意，这里使用的是insert into，写新数据前，不会删除旧的数据，即使新数据与旧数据相同，也不会对旧数据产生任何影响。into如果替换成overwrite，则会删掉掉旧数据，再写入新数据。

```hql
insert into table part_products
partition (type='electronics', locality='China')
select p.id, p.name, p.price from products p where p.locality='China' and p.type='electronics'; 
```

插入数据的操作由一个本地Hadoop MR任务执行。执行完成后，查看分区表part_products，发现数据已经成功插入。

```hql
select * from part_products;
```

最初执行插入语句时，出现了错误。后来在hive_env.sh中注释掉了有关jar包的配置即可成功执行。

## 多个查询插入

如果使用上述语句插入数据，则对每一个分区，都要扫描一遍原表products，效率非常低。因此，提供了另一种写法。扫描一遍products，即可将相应的数据插入不同分区。

```hql
from products p
insert overwrite table part_products
  partition (type='electronics', locality='China')
  select p.id, p.name, p.price  where p.locality='China' and p.type='electronics'
insert overwrite table part_products
  partition (type='food', locality='China')
  select p.id, p.name, p.price  where p.locality='China' and p.type='food';
```

## 动态分区插入

如果每次插入分区数据都要手动设定分区类型，操作实在非常麻烦。动态分区可以解决这个问题。为了方便演示，首先创建一张分区表part_id_price_prodcts。该分区表只包含2个普通字段和一个分区字段。

```hql
create table part_id_price_prodcts (id string, price string)
partitioned by (type string);
```

然后，查询products表中的数据，插入part_id_price_prodcts分区表中。查询时，仅选择了三个字段。Hive根据最后的字段p.type来确定分区字段type的值。

```hql
insert into table part_id_price_products
partition (type)
select p.id,p.price,p.type from products p;
```

执行完成后，查看分区表的分区情况。可见两个分区已经被创建成功。

```hql
show partitions part_id_price_products;
```

**注意：**在动态插入分区前，需设置如下参数。

```hql
set hive.exec.dynamic.partition=true;
set hive.exec.dynamic.partition.mode=nonstrict;
```

可通过`set 参数名`的形式查看参数是否正确。

```hql
set hive.exec.dynamic.partition;
```
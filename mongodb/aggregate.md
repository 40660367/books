# MongoDB 聚合(aggregate)

MongoDB中聚合(aggregate)主要用于处理数据(诸如统计平均值,求和等)，并返回计算后的数据结果。有点类似sql语句中的 count(*)。

## aggregate() 方法

MongoDB中聚合的方法使用aggregate()。

### 语法

aggregate() 方法的基本语法格式如下所示：

```sql
db.COLLECTION_NAME.aggregate(AGGREGATE_OPERATION)
```

### 实例

集合中的数据如下：

```sql
use testdb
db.c10.insert({
    title: '动手学Redis', 
    description: '极速内存数据库',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com/redis/',
    tags: ['redis'],
    likes: 200
})

db.c10.insert({title: '动手学Java', 
    description: 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com/java/',
    tags: ['java'],
    likes: 150
})

db.c10.insert({title: 'MongoDB 教程', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: 'mongodb',
    url: 'http://www.freeaihub.com/mongodb/',
    tags: ['mongodb'],
    likes: 100
})
```

现在我们通过以上集合计算每个作者所写的文章数，使用aggregate()计算结果如下：

```sql
db.c10.aggregate([{$group : {_id : "$by", num_tutorial : {$sum : 1}}}])
```

以上实例类似sql语句：`select by, count(*) from c10 group by by`

在上面的例子中，我们通过字段 by 字段对数据进行分组，并计算 by 字段相同值的总和。

下表展示了一些聚合的表达式:

| 表达式    | 描述                                           | 实例                                                         |
| :-------- | :--------------------------------------------- | :----------------------------------------------------------- |
| $sum      | 计算总和。                                     | db.c10.aggregate([{$group : {_id : "$by", num_tutorial : {$sum : "$likes"}}}]) |
| $avg      | 计算平均值                                     | db.c10.aggregate([{$group : {_id : "$by", num_tutorial : {$avg : "$likes"}}}]) |
| $min      | 获取集合中所有文档对应值得最小值。             | db.c10.aggregate([{$group : {_id : "$by", num_tutorial : {$min : "$likes"}}}]) |
| $max      | 获取集合中所有文档对应值得最大值。             | db.c10.aggregate([{$group : {_id : "$by", num_tutorial : {$max : "$likes"}}}]) |
| $push     | 在结果文档中插入值到一个数组中。               | db.c10.aggregate([{$group : {_id : "$by", url : {$push: "$url"}}}]) |
| $addToSet | 在结果文档中插入值到一个数组中，但不创建副本。 | db.c10.aggregate([{$group : {_id : "$by", url : {$addToSet : "$url"}}}]) |
| $first    | 根据资源文档的排序获取第一个文档数据。         | db.c10.aggregate([{$group : {_id : "$by", first_url : {$first : "$url"}}}]) |
| $last     | 根据资源文档的排序获取最后一个文档数据         | db.c10.aggregate([{$group : {_id : "$by", last_url : {$last : "$url"}}}]) |


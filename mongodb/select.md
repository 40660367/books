# MongoDB 查询文档

## 准备好数据
```sql
use testdb
db.c7.insert({
    title: '动手学Redis', 
    description: '极速内存数据库',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com',
    tags: ['redis'],
    likes: 200
})

db.c7.insert({title: '动手学Java', 
    description: 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com',
    tags: ['java'],
    likes: 150
})

db.c7.insert({title: '动手学mongoDB', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: 'mongo',
    url: 'http://www.freeaihub.com',
    tags: ['mongodb'],
    likes: 100
})
```

## MongoDB 查询文档

MongoDB 查询文档使用 find() 方法,以非结构化的方式来显示所有文档。

### 语法

MongoDB 查询数据的语法格式如下：

```sql
db.collection.find(query, projection)
```

- **query** ：可选，使用查询操作符指定查询条件
- **projection** ：可选，使用投影操作符指定返回的键。查询时返回文档中所有键值， 只需省略该参数即可（默认省略）。

如果你需要以易读的方式来读取数据，可以使用 pretty() 方法，语法格式如下：

```sql
db.col.find().pretty()
```

pretty() 方法以格式化的方式来显示所有文档。

### 实例

以下实例我们查询了集合c7中的数据：

```
use testdb
db.c7.find().pretty()
```

除了 find() 方法之外，还有一个 findOne() 方法，它只返回一个文档。

## MongoDB 与 RDBMS Where 语句比较

如果你熟悉常规的 SQL 数据，通过下表可以更好的理解 MongoDB 的条件语句查询：

| 操作       | 格式         | 范例                                        | RDBMS中的类似语句        |
| :--------- | :----------- | :------------------------------------------ | :----------------------- |
| 等于       | `{:`}        | `db.col.find({"by":"freeaihub"}).pretty()`  | `where by = 'freeaihub'` |
| 小于       | `{:{$lt:}}`  | `db.col.find({"likes":{$lt:50}}).pretty()`  | `where likes < 50`       |
| 小于或等于 | `{:{$lte:}}` | `db.col.find({"likes":{$lte:50}}).pretty()` | `where likes <= 50`      |
| 大于       | `{:{$gt:}}`  | `db.col.find({"likes":{$gt:50}}).pretty()`  | `where likes > 50`       |
| 大于或等于 | `{:{$gte:}}` | `db.col.find({"likes":{$gte:50}}).pretty()` | `where likes >= 50`      |
| 不等于     | `{:{$ne:}}`  | `db.col.find({"likes":{$ne:50}}).pretty()`  | `where likes != 50`      |

## MongoDB AND 条件

MongoDB 的 find() 方法可以传入多个键(key)，每个键(key)以逗号隔开，即常规 SQL 的 AND 条件。

语法格式如下：

```sql
db.col.find({key1:value1, key2:value2}).pretty()
```

### 实例

以下实例通过 **by** 和 **title** 键来查询 **FreeAIHub** 中 **动手学Redis** 的数据

```
db.c7.find({"by":"FreeAIHub", "title":"动手学Redis"}).pretty()
```

以上实例中类似于 WHERE 语句：`WHERE by='FreeAIHub' AND title='动手学Redis'`

## MongoDB OR 条件

MongoDB OR 条件语句使用了关键字 **$or**,语法格式如下：

```sql
db.col.find(
   {
      $or: [
         {key1: value1}, {key2:value2}
      ]
   }
).pretty()
```

### 实例

以下实例中，我们演示了查询键 **by** 值为 **FreeAIHub**或键 **title** 值为 **动手学mongoDB** 的文档。

```
db.c7.find({$or:[{"by":"mongo"},{"title": "mongo"}]}).pretty()
```

## AND 和 OR 联合使用

示例

```sql
db.c7.find({"likes": {$gt:50}, $or: [{"by": "freeaihub"},{"title": "动手学mongoDB"}]}).pretty()
```

## MongoDB 条件操作符


条件操作符用于比较两个表达式并从mongoDB集合中获取数据。

在本章节中，我们将讨论如何在MongoDB中使用条件操作符。

MongoDB中条件操作符有：

- (>) 大于 - $gt
- (<) 小于 - $lt
- (>=) 大于等于 - $gte
- (<= ) 小于等于 - $lte

**我们使用的数据库名称为"testdb" 我们的集合名称为"c7"，以下为我们插入的数据。**

使用find()命令查看数据：

```sql
use testdb
db.c7.find()
```

## MongoDB (>) 大于操作符 - $gt

如果你想获取 "c7" 集合中 "likes" 大于 100 的数据，你可以使用以下命令：

```sql
db.c7.find({likes : {$gt : 100}})
```

类似于SQL语句：`Select * from c7 where likes > 100;`

## MongoDB（>=）大于等于操作符 - $gte

如果你想获取"col"集合中 "likes" 大于等于 100 的数据，你可以使用以下命令：

```sql
db.c7.find({likes : {$gte : 100}})
```

类似于SQL语句：`Select * from c7 where likes >=100;`

## MongoDB (<) 小于操作符 - $lt

如果你想获取"col"集合中 "likes" 小于 150 的数据，你可以使用以下命令：

```sql
db.c7.find({likes : {$lt : 150}})
```

类似于SQL语句：`Select * from c7 where likes < 150;`

## MongoDB (<=) 小于等于操作符 - $lte

如果你想获取"col"集合中 "likes" 小于等于 150 的数据，你可以使用以下命令：

```sql
db.c7.find({likes : {$lte : 150}})
```

类似于SQL语句：`Select * from c7 where likes <= 150;`

## MongoDB 使用 (<) 和 (>) 查询 - $lt 和 $gt

如果你想获取"col"集合中 "likes" 大于100，小于 200 的数据，你可以使用以下命令：

```sql
db.c7.find({likes : {$lt :200, $gt : 100}})
```

类似于SQL语句：`Select * from c7 where likes>100 AND  likes<200;`
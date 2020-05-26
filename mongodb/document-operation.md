# MongoDB 文档操作

本章节中我们将向大家介绍如何将数据插入到 MongoDB 的集合中。

文档的数据结构和 JSON 基本一样。

所有存储在集合中的数据都是 BSON 格式。

BSON 是一种类似 JSON 的二进制形式的存储格式，是 Binary JSON 的简称。

## MongoDB 插入文档

MongoDB 使用 insert() 或 save() 方法向集合中插入文档，语法如下：

```mongodb
db.COLLECTION_NAME.insert(document)
```

### 实例

以下文档可以存储在 MongoDB 的 testdb数据库 的 col 集合中：

```mongodb
use testdb
db.c1.insert({title: '动手学MongoDB', 
    description: 'MongoDB 是一个 Nosql 数据库',
    tags: ['mongodb', 'database', 'NoSQL'],
})
```

以上实例中 c1是我们的集合名，如果该集合不在该数据库中， MongoDB 会自动创建该集合并插入文档。

查看已插入文档：

```sql
db.c1.find()
```

我们也可以将数据定义为一个变量，如下所示：

```sql
document=({title: '动手学MongoDB', 
    description: 'MongoDB 是一个 Nosql 数据库',
    tags: ['mongodb', 'database', 'NoSQL'],
});
```

```sql
#执行插入操作：
db.c2.insert(document)
```

```sql
db.c2.find()
```

插入文档你也可以使用 db.col.save(document) 命令。如果不指定 _id 字段 save() 方法类似于 insert() 方法。如果指定 _id 字段，则会更新该 _id 的数据。



## MongoDB 更新文档

MongoDB 使用 **update()** 和 **save()** 方法来更新集合中的文档。接下来让我们详细来看下两个函数的应用及其区别。

### update方法

update() 方法用于更新已存在的文档。语法格式如下：

```sql
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

**参数说明：**

- **query** : update的查询条件，类似sql update查询内where后面的。
- **update** : update的对象和一些更新的操作符（如$,$inc...）等，也可以理解为sql update查询内set后面的
- **upsert** : 可选，这个参数的意思是，如果不存在update的记录，是否插入objNew,true为插入，默认是false，不插入。
- **multi** : 可选，mongodb 默认是false,只更新找到的第一条记录，如果这个参数为true,就把按条件查出来多条记录全部更新。
- **writeConcern** :可选，抛出异常的级别。

### 实例

我们在集合 col 中插入如下数据：

```sql
db.c3.insert({
    title: '动手学MongoDB', 
    description: 'MongoDB 是一个 Nosql 数据库',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
})
```

接着我们通过 update() 方法来更新标题(title):

```sql
db.c3.update({'title':'动手学MongoDB'},{$set:{'title':'MongoDB动手学'}})
db.c3.find().pretty()
```

可以看到标题(title)由原来的 "动手学MongoDB" 更新为了 "MongoDB动手学"。

以上语句只会修改第一条发现的文档，如果你要修改多条相同的文档，则需要设置 multi 参数为 true。

```sql
db.col.update({'title':'动手学MongoDB'},{$set:{'title':'New Title you want'}},{multi:true})
```

### save() 方法

save() 方法通过传入的文档来替换已有文档。语法格式如下：

```sql
db.collection.save(
   <document>,
   {
     writeConcern: <document>
   }
)
```

**参数说明：**

- **document** : 文档数据。
- **writeConcern** :可选，抛出异常的级别。

### 实例

以下实例中我们先插入一条数据，查找到其ObjectId，再使用save方法，根据这个id替换数据：

```sql
db.c4.insert({
    title: '动手学MongoDB', 
    description: 'MongoDB 是一个 Nosql 数据库',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
})
db.c4.find()
```

```
db.c4.save({
    "_id" : ObjectId("在此处填写上面得到的ObjectID"),
    "title" : "MongoDB动手学"
})
```

替换成功后，我们可以通过 find() 命令来查看替换后的数据

```sql
db.c4.find().pretty()
```

### 更多实例

```
只更新第一条记录：
db.col.update( { "count" : { $gt : 1 } } , { $set : { "test2" : "OK"} } );

只添加第一条：
db.col.update( { "count" : { $gt : 4 } } , { $set : { "test5" : "OK"} },true,false );

只更新第一条记录：
db.col.update( { "count" : { $gt : 10 } } , { $inc : { "count" : 1} },false,false );

全部更新：
db.col.update( { "count" : { $gt : 15 } } , { $inc : { "count" : 1} },false,true );

全部添加进去:
db.col.update( { "count" : { $gt : 5 } } , { $set : { "test5" : "OK"} },true,true );

全部更新：
db.col.update( { "count" : { $gt : 3 } } , { $set : { "test2" : "OK"} },false,true );
```

## MongoDB 删除文档

在前面的几个章节中我们已经学习了MongoDB中如何为集合添加数据和更新数据。在本章节中我们将继续学习MongoDB集合的删除。

MongoDB remove()函数是用来移除集合中的数据。

MongoDB数据更新可以使用update()函数。在执行remove()函数前先执行find()命令来判断执行的条件是否正确，这是一个比较好的习惯。

### 语法

remove() 方法的基本语法格式如下所示：

```sql
db.collection.remove(
   <query>,
   <justOne>
)
```

如果你的 MongoDB 是 2.6 版本以后的，语法格式如下：

```sql
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>
   }
)
```

**参数说明：**

- **query** :（可选）删除的文档的条件。
- **justOne** : （可选）如果设为 true 或 1，则只删除一个文档，如果不设置该参数，或使用默认值 false，则删除所有匹配条件的文档。
- **writeConcern** :（可选）抛出异常的级别。

### 实例

以下文档我们执行两次插入操作：

```sql
use testdb
db.c5.insert({title: '动手学MongoDB', 
    description: 'MongoDB 是一个 Nosql 数据库',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
})
db.c5.insert({title: 'MongoDB动手学', 
    description: 'MongoDB 是一个 Nosql 数据库',
    tags: ['mongodb', 'database', 'NoSQL'],
    likes: 100
})
```

```sql
#使用 find() 函数查询数据：
db.c5.find()
```

接下来我们移除 title 为 'MongoDB动手学' 的文档：

```sql
db.c5.remove({'title':'MongoDB动手学'})
db.c5.find()
```

如果你想删除所有数据，可以使用以下方式（类似常规 SQL 的 truncate 命令）：

```sql
db.c5.remove({})
db.c5.find()
```




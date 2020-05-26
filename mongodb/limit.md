# MongoDB Limit与Skip方法

## MongoDB Limit() 方法

如果你需要在MongoDB中读取指定数量的数据记录，可以使用MongoDB的Limit方法，limit()方法接受一个数字参数，该参数指定从MongoDB中读取的记录条数。

### 语法

limit()方法基本语法如下所示：

```sql
db.COLLECTION_NAME.find().limit(NUMBER)
```

### 实例

集合 col 中的数据如下：

```sql
use testdb
db.c8.insert({
    title: '动手学Redis', 
    description: '极速内存数据库',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com/redis/',
    tags: ['redis'],
    likes: 200
})

db.c8.insert({title: '动手学Java', 
    description: 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com/java/',
    tags: ['java'],
    likes: 150
})

db.c8.insert({title: 'MongoDB 教程', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: 'freeaihub',
    url: 'http://www.freeaihub.com/mongodb/',
    tags: ['mongodb'],
    likes: 100
})
```

以下实例为显示查询文档中的两条记录：

```
db.c8.find({},{"title":1,_id:0}).limit(2)
```

注：如果你们没有指定limit()方法中的参数则显示集合中的所有数据。

## MongoDB Skip() 方法

我们除了可以使用limit()方法来读取指定数量的数据外，还可以使用skip()方法来跳过指定数量的数据，skip方法同样接受一个数字参数作为跳过的记录条数。

### 语法

skip() 方法脚本语法格式如下：

```sql
db.COLLECTION_NAME.find().limit(NUMBER).skip(NUMBER)
```

### 实例

以下实例只会显示第二条文档数据

```sql
db.c8.find({},{"title":1,_id:0}).limit(1).skip(1)
```
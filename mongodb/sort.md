# MongoDB 排序

## MongoDB sort() 方法

在 MongoDB 中使用 sort() 方法对数据进行排序，sort() 方法可以通过参数指定排序的字段，并使用 1 和 -1 来指定排序的方式，其中 1 为升序排列，而 -1 是用于降序排列。

### 语法

sort()方法基本语法如下所示：

```sql
db.COLLECTION_NAME.find().sort({KEY:1})
```

### 实例

将如下数据插入至c9集合中

```sql
use testdb
db.c9.insert({
    title: '动手学Redis', 
    description: '极速内存数据库',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com',
    tags: ['redis'],
    likes: 200
})

db.c9.insert({title: '动手学Java', 
    description: 'Java 是由Sun Microsystems公司于1995年5月推出的高级程序设计语言。',
    by: 'FreeAIHub',
    url: 'http://www.freeaihub.com',
    tags: ['java'],
    likes: 150
})

db.c9.insert({title: 'MongoDB 教程', 
    description: 'MongoDB 是一个 Nosql 数据库',
    by: 'freeaihub',
    url: 'http://www.freeaihub.com',
    tags: ['mongodb'],
    likes: 100
})
```

```sql
#以下实例演示了 col 集合中的数据按字段 likes 的降序排列：
db.c9.find({},{"title":1,_id:0}).sort({"likes":-1})
```

```sql
#以下实例演示了 col 集合中的数据按字段 likes 的升序排列：
db.c9.find({},{"title":1,_id:0}).sort({"likes":1})
```
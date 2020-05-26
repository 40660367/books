# MongoDB 集合操作

本章节我们为大家介绍如何使用 MongoDB 来创建集合。

## 创建集合

MongoDB 中使用 **createCollection()** 方法来创建集合。

语法格式：

```sql
db.createCollection(name, options)
```

参数说明：

- name: 要创建的集合名称
- options: 可选参数, 指定有关内存大小及索引的选项

options 可以是如下参数：

| 字段        | 类型 | 描述                                                         |
| :---------- | :--- | :----------------------------------------------------------- |
| capped      | 布尔 | （可选）如果为 true，则创建固定集合。固定集合是指有着固定大小的集合，当达到最大值时，它会自动覆盖最早的文档。 **当该值为 true 时，必须指定 size 参数。** |
| autoIndexId | 布尔 | （可选）如为 true，自动在 _id 字段创建索引。默认为 false。   |
| size        | 数值 | （可选）为固定集合指定一个最大值，以千字节计（KB）。 **如果 capped 为 true，也需要指定该字段。** |
| max         | 数值 | （可选）指定固定集合中包含文档的最大数量。                   |

在插入文档时，MongoDB 首先检查固定集合的 size 字段，然后检查 max 字段。

### 实例

在 testdb数据库中创建 c1集合：

```sql
use testdb
db.createCollection("c1")
```

如果要查看已有集合，可以使用 **show collections** 或 **show tables** 命令：

```sql
show collections
```

下面是带有几个关键参数的 createCollection() 的用法：

创建固定集合 mycol，整个集合空间大小 6142800 KB, 文档最大个数为 10000 个。

```
db.createCollection("c11", { capped : true, autoIndexId : true, size : 6142800, max : 10000 } )
```

在 MongoDB 中，你不需要创建集合。当你插入一些文档时，MongoDB 会自动创建集合。

```
db.c11.insert({"name" : "FreeAIHub"})
show collections
```

## MongoDB删除集合

MongoDB 中使用 drop() 方法来删除集合。

**语法格式：**

```sql
db.collection.drop()
```

**返回值**

如果成功删除选定集合，则 drop() 方法返回 true，否则返回 false。

### 实例

在数据库 testdb中，我们可以先通过 **show collections** 命令查看已存在的集合：

```
use testdb
show collections
```

接着删除集合 c1:

```
db.c1.drop()
```

通过 show collections 再次查看数据库 testdb中的集合：

```
show collections
```

从结果中可以看出 c1集合已被删除。
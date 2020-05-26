# MongoDB 数据库操作

### 语法

MongoDB 创建数据库的语法格式如下：

```sql
use DATABASE_NAME
```

如果数据库不存在，则创建数据库，否则切换到指定数据库。

### 实例

以下实例我们创建了数据库 testdb:

```sql
use testdb
db
```

如果你想查看所有数据库，可以使用 **show dbs** 命令：

```sql
show dbs
```

可以看到，我们刚创建的数据库 testdb 并不在数据库的列表中， 要显示它，我们需要向 testdb 数据库插入一些数据。

```localhost
db.testdb.insert({"name":"FreeAIHub"})
show dbs
```

MongoDB 中默认的数据库为 test，如果你没有创建新的数据库，集合将存放在 test 数据库中。

> **注意:** 在 MongoDB 中，集合只有在内容插入后才会创建! 就是说，创建集合(数据表)后要再插入一个文档(记录)，集合才会真正创建。

## MongoDB 删除数据库

### 语法

MongoDB 删除数据库的语法格式如下：

```sql
db.dropDatabase()
```

删除当前数据库，默认为 test，你可以使用 db 命令查看当前数据库名。

### 实例

以下实例我们删除了数据库 testdb。

首先，查看所有数据库：

```sql
show dbs
```

接下来我们切换到数据库 testdb：

```sql
use testdb
```

执行删除命令：

```sql
db.dropDatabase()
```

最后，我们再通过 show dbs 命令数据库是否删除成功：

```sql
show dbs
```


# MySQL 删除数据库

删除数据库意味着数据库中的所有数据和关联对象将被永久删除，并且无法撤消。 因此，用额外的注意事项执行此查询是非常重要的。

要删除数据库，请使用`DROP DATABASE`语句，遵循`DROP DATABASE`是要删除的数据库名称。

 与`CREATE DATABASE`语句类似，`IF EXISTS`是该语句的可选部分，以防止您删除数据库服务器中不存在的数据库。

如果要使用`DROP DATABASE`语句练习，可以创建一个新数据库`mytestdb`，然后将其删除。来看下面的查询：

```sql
CREATE DATABASE IF NOT EXISTS mytestdb;
SHOW DATABASES;
DROP DATABASE IF EXISTS mytestdb;
SHOW DATABASES;
```

三个语句的说明如下：

- 首先，使用`CREATE DATABASE`语句创建了一个名为`mytestdb`的数据库。
- 第二，使用`SHOW DATABASES`语句显示所有数据库。
- 第三，使用`DROP DATABASE`语句删除了名为`mytestdb`的数据库。

在本教程中，您学习了各种语句来管理MySQL中的数据库，包括创建新数据库，删除现有数据库，选择要使用的数据库，以及在MySQL数据库服务器中显示所有数据库。
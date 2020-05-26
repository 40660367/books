# MySQL 索引(index)

在本教程中，您将学习如何使用MySQL索引以及如何利用索引来加快数据检索。我们将介绍一些常用和方便的语句，让您可以有效地管理MySQL索引。

数据库索引或索引，有助于加速从表中检索数据。 当从表[查询数据](./select.html)时，首先MySQL会检查索引是否存在，然后MySQL使用索引来选择表的精确物理对应行，而不是扫描整个表。

数据库索引类似于书的目录。果果要查找某个主题，首先查找索引，然后打开具有该主题的页面(页码)，而不扫描整本书。

强烈建议您在经常查询数据的表的列上创建索引。 请注意，所有[主键](./primarykey.html)列都是表的主索引。

索引有助于加快查询数据，为什么我们不使用所有列的索引？ 如果为每列创建索引，MySQL必须构建和维护索引表。每当对表的行进行更改时，MySQL必须重建索引，这需要时间以及降低数据库服务器的性能。换句话说：使用索引可以加快查询数据，但是减慢了修改数据的速度。

## 创建MySQL索引

创建表时经常创建索引。MySQL自动将声明为`PRIMARY KEY`，`KEY`，`UNIQUE`或`INDEX`的任何列添加到索引。 另外，您可以向已经有数据的表添加索引。

要创建索引，可以使用`CREATE INDEX`语句。 下面说明了`CREATE INDEX`语句的语法：

```sql
CREATE [UNIQUE|FULLTEXT|SPATIAL] INDEX index_name
USING [BTREE | HASH | RTREE] 
ON table_name (column_name [(length)] [ASC | DESC],...)
```

首先，根据表类型或存储引擎指定索引： 

- 对于`UNIQUE`索引，MySQL创建一个约束，索引中的所有值都必须是唯一的。除了BDB之外，所有存储引擎都允许重复的`NULL`值。
- `FULLTEXT`索引仅由*MyISAM*存储引擎支持，仅在数据类型为`CHAR`，`VARCHAR`或`TEXT`的列中接受。
- `SPATIAL`索引支持空间列，可用于*MyISAM*存储引擎。另外，列值不能为`NULL`。

然后，在`USING`关键字之后命名索引及其类型。索引的名称可以是`BTREE HASH`或`RTREE`，但必须根据表的存储引擎遵循允许的索引。

以下是具有相应允许的索引类型的表的存储引擎：

| 存储引擎        | 允许的索引类型   |
| --------------- | ---------------- |
| `MyISAM`        | `BTREE`, `RTREE` |
| `InnoDB`        | `BTREE`          |
| `MEMORY`/`HEAP` | `HASH`, `BTREE`  |
| `NDB`           | `HASH`           |

**第三**，声明要添加到索引的表名称和列表列。

## 在MySQL中创建索引的示例

**[准备环境](./setup.html)**

在示例数据库中，可以使用`CREATE INDEX`语句将`employees`表的`officeCode`列添加索引，如下所示：

```sql
CREATE INDEX index_officeCode ON employees(officeCode)
```

## 删除索引

除了创建索引之外，还可以使用`DROP INDEX`语句来删除索引。 有趣的是，`DROP INDEX`语句也映射到[ALTER TABLE语句](./table-alter.html)。 以下是删除索引的语法：

```sql
DROP INDEX index_name ON table_name
```

例如，如果要删除`employees`表的索引`index_officeCode`，可以执行以下查询：

```sql
DROP INDEX index_officeCode ON employees
```

在本教程中，您已经了解了索引以及如何管理MySQL索引，包括创建和删除索引。
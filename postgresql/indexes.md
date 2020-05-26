# PostgreSQL 索引(index)

索引是用于加速从数据库检索数据的特殊查找表。数据库索引类似于书的索引(目录)。 索引为出现在索引列中的每个值创建一个条目。

## 数据库索引的重要特点

- 索引使用`SELECT`查询和`WHERE`子句加速数据输出，但是会减慢使用`INSERT`和`UPDATE`语句输入的数据。
- 您可以在不影响数据的情况下创建或删除索引。
- 可以通过使用`CREATE INDEX`语句创建索引，指定创建索引的索引名称和表或列名称。
- 还可以创建一个唯一索引，类似于唯一约束，该索引防止列或列的组合上有一个索引重复的项。

## PostgreSQL创建索引

`CREATE INDEX`语句用于创建PostgreSQL索引。

**语法**

```sql
CREATE INDEX index_name ON table_name;
```

## 索引类型

PostgreSQL中有几种索引类型，如`B-tree`，`Hash`，`GiST`，`SP-GiST`和`GIN`等。每种索引类型根据不同的查询使用不同的算法。 默认情况下，`CREATE INDEX`命令使用**B树**索引。

## 单列索引

如果仅在一个表列中创建索引，则将其称为单列索引。

**语法：**

```sql
CREATE INDEX index_name  
ON table_name (column_name);
```

**示例:**

表“`EMPLOYEES`”的“`name`”列上创建一个名为“`employees_index`”的索引。

执行以下创建语句：

```sql
CREATE INDEX employees_index  
ON EMPLOYEES (name);
```

## 多列索引

如果通过使用表的多个列创建索引，则称为多列索引。

**语法：**

```sql
CREATE INDEX index_name  
ON table_name (column1_name, column2_name);
SQL
```

**示例:**

让我们在同一个表“`EMPLOYEES`”上创建一个名为“`multicolumn_index`”的多列索引

执行以下创建查询语句：

```sql
CREATE INDEX multicolumn_index  
ON EMPLOYEES (name, salary);
```

## 唯一索引

创建唯一索引以获取数据的完整性并提高性能。它不允许向表中插入重复的值，或者在原来表中有相同记录的列上也不能创建索引。

**语法：**

```sql
CREATE UNIQUE INDEX index_name  
on table_name (column_name);
SQL
```

**示例:**

例如，在`employees`表的`name`字段上创建一个唯一索引，将会提示错误 -

```sql
CREATE UNIQUE INDEX unique_on_name  
on employees (name);
```

因为(`name`字段中有两个`Minsu`的值) -

## PostgreSQL删除索引

DROP INDEX方法用于删除PostgreSQL中的索引。 如果你放弃一个索引，那么它可以减慢或提高性能。

语法：

```sql
DROP INDEX index_name;
```

**示例:**

作为一个示例，我们现在来删除在前面创建的名为“`multicolumn_index`”的索引。

```sql
DROP INDEX multicolumn_index;
```

现在，您可以看到名为“`multicolumn_index`”的索引已被删除/删除。查看 `employees` 表的结构 -

## 什么时候应该避免使用索引？

- 应该避免在小表上使用索引。
- 不要为具有频繁，大批量更新或插入操作的表创建索引。
- 索引不应用于包含大量`NULL`值的列。
- 不要在经常操作(修改)的列上创建索引。
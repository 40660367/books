# SQLite 索引(index)

索引是特殊的查找表，数据库搜索引擎可以使用索引来加快数据检索的速度。简而言之，**索引**是指向表中数据的指针。数据库中的索引与书后的索引非常相似。

例如，如果要引用一本书中讨论某个主题的所有页面，则首先要参考索引，该索引按字母顺序列出所有主题，然后引用一个或多个特定的页码。

索引有助于加快SELECT查询和WHERE子句的速度，但它会通过UPDATE和INSERT语句减慢数据输入速度。可以创建或删除索引，而不会影响数据。

创建索引涉及CREATE INDEX语句，该语句使您可以命名索引，指定表以及要索引的列或列，并指示索引是升序还是降序。

索引也可以是唯一的，类似于UNIQUE约束，因为索引可以防止存在索引的列或列组合中的重复条目。

## CREATE INDEX命令

以下是**CREATE INDEX**的基本语法。

```sql
CREATE INDEX index_name ON table_name;
```

### 单列索引

单列索引是仅基于一个表列创建的索引。基本语法如下-

```sql
CREATE INDEX index_name
ON table_name (column_name);
```

### 唯一索引

唯一索引不仅用于提高性能，而且还用于数据完整性。唯一索引不允许将任何重复的值插入表中。基本语法如下-

```sql
CREATE UNIQUE INDEX index_name
on table_name (column_name);
```

### 综合指数

复合索引是表的两个或多个列上的索引。基本语法如下-

```sql
CREATE INDEX index_name
on table_name (column1, column2);
```

无论是创建单列索引还是复合索引，都应考虑在查询的WHERE子句中可能经常使用的列作为过滤条件。

如果只使用一列，则应选择单列索引。如果WHERE子句中经常使用两个或多个列作为过滤器，则复合索引将是最佳选择。

### 隐式索引

隐式索引是创建对象时由数据库服务器自动创建的索引。为主键约束和唯一约束自动创建索引。

**例**

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

以下是我们将在表中为薪水列创建索引的示例

```sql
CREATE INDEX salary_index ON COMPANY (salary);
```

现在，让我们使用**.indices**命令列出COMPANY表中可用的所有索引，如下所示-

```sql
.indices COMPANY
```

康康，其中*sqlite_autoindex_COMPANY_1*是在创建表本身时创建的隐式索引。

您可以列出所有索引数据库范围，如下所示：

```
SELECT * FROM sqlite_master WHERE type = 'index';
```

康康

## DROP INDEX命令

可以使用SQLite **DROP**命令删除索引。删除索引时应小心，因为性能可能会减慢或提高。

以下是基本语法如下-

```sql
DROP INDEX index_name;
```

**例**

您可以使用以下语句删除上方创建的索引。

```sql
DROP INDEX salary_index;
SELECT * FROM sqlite_master WHERE type = 'index';
```

康康

### 什么时候应该避免索引？

尽管索引旨在增强数据库的性能，但有时应避免使用它们。以下准则指示何时应重新考虑使用索引。

索引不得用于

- 小数据量的表格。
- 具有频繁，大量批处理更新或插入操作的表。
- 包含大量NULL值的列。
- 经常操作的列。
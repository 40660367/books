# PostgreSQL 视图(view)

在PostgreSQL中，视图(VIEW)是一个**伪表**。 它不是物理表，而是作为普通表选择查询。
视图也可以表示连接的表。 它可以包含表的所有行或来自一个或多个表的所选行。

**视图便于用户执行以下操作：**

- 它以自然和直观的方式构建数据，并使其易于查找。
- 它限制对数据的访问，使得用户只能看到有限的数据而不是完整的数据。
- 它归总来自各种表中的数据以生成报告。

## PostgreSQL创建视图

可以使用`CREATE VIEW`语句来在PostgreSQL中创建视图。 您可以从单个表，多个表以及另一个视图创建它。

**语法**

```sql
CREATE [TEMP | TEMPORARY] VIEW view_name AS  
SELECT column1, column2.....  
FROM table_name  
WHERE [condition];
```

## PostgreSQL创建视图示例

[准备环境及数据](./setup.html)

考虑一个表“`EMPLOYEES`”，具有以下数据。

现在，我们从“`EMPLOYEES`”表创建一个视图。 此视图将仅包含`EMPLOYEES`表中的几个列：

执行以下查询语句：

```sql
CREATE VIEW current_employees AS  
SELECT NAME, ID, SALARY 
FROM EMPLOYEES;
```

现在，您可以从视图“`current_employees`”中使用简单的查询语句检索数据。会看到下表：

```sql
SELECT * FROM current_employees;
```

## PostgreSQL DROP视图

按着下面这些次序操作删除就好了：

- 选择视图“`current_employees`”并右键点击。
- 您将看到一个**删除/移除**选项，点击它。

视图是永久删除的。所以一但删除了以后，在数据库中就不会存在了。
您还可以使用`DROP VIEW`命令删除或删除视图。

**语法**

```sql
DROP VIEW view_name;
```

要删除上面的例子中创建的视图，可执行以下SQL语句：

```sql
DROP VIEW current_employees;
```
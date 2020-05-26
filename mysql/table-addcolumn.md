# MySQL 添加列

在本教程中，我们将向您展示如何使用MySQL `ADD COLUMN`语句将列添加到表中。

## MySQL ADD COLUMN语句简介

要向现有表添加新列，请按如下所示使用[ALTER TABLE](./table-alter.html) `ADD COLUMN`语句：

- 首先，在`ALTER TABLE`子句之后指定表名。
- 其次，将新列及其定义放在`ADD COLUMN`子句之后。 请注意，`COLUMN`关键字是可选的，因此可以省略它。
- 第三，MySQL允许通过指定`FIRST`关键字将新列添加到表的第一列。 它还允许您使用`AFTER existing_column`子句在现有列之后添加新列。如果没有明确指定新列的位置，MySQL会将其添加为最后一列。

要同时向表中添加两个或多个列，请使用以下语法：

```sql
ALTER TABLE table
ADD [COLUMN] column_name_1 column_1_definition [FIRST|AFTER existing_column],
ADD [COLUMN] column_name_2 column_2_definition [FIRST|AFTER existing_column],
...;
```

我们来看一些向现有表添加新列的示例。

## MySQL ADD COLUMN示例

首先，作为演示目的我们使用以下语句，创建一个名为`vendor`的表：

```sql
USE testdb;

CREATE TABLE IF NOT EXISTS vendors (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
```

**第二**，在`vendors`表中添加一个名为`phone`的新列。 因为在`name`列之后明确指定了`phone`列的位置，MySQL将会遵守这一点。

```sql
ALTER TABLE vendors
ADD COLUMN phone VARCHAR(15) AFTER name;
```

**第三**，在`vendors`表中添加一个名为`vendor_group`的新列。 此时，不指定新列的位置，因此MySQL将`vendor_group`列添加为`vendors`表的最后一列。

```sql
ALTER TABLE vendors
ADD COLUMN vendor_group INT NOT NULL;
```

让我们插入一些行数据到`vendors`表。

```sql
INSERT INTO vendors(name,phone,vendor_group)
VALUES('IBM','(408)-298-2987',1);

INSERT INTO vendors(name,phone,vendor_group)
VALUES('Microsoft','(408)-298-2988',1);
```

可以查询`vendors`表的数据来查看更改。

```sql
SELECT 
    id, name, phone,vendor_group
FROM
    vendors;

+----+-----------+----------------+--------------+
| id | name      | phone          | vendor_group |
+----+-----------+----------------+--------------+
|  1 | IBM       | (408)-298-2987 |            1 |
|  2 | Microsoft | (408)-298-2988 |            1 |
+----+-----------+----------------+--------------+
2 rows in set
```

**第四**，同时向`vendors`表格添加两列：`email`和`hourly_rate`。

```sql
ALTER TABLE vendors
ADD COLUMN email VARCHAR(100) NOT NULL,
ADD COLUMN hourly_rate decimal(10,2) NOT NULL;
```

请注意，`email`和`hourly_rate`列都分配给`NOT NULL`值。但是，`vendors`表已经有数据。 在这种情况下，MySQL将为这些新列使用默认值。

现在，我们来查看`vendors`表中的数据，如下 - 

```sql
SELECT 
    id, name, phone, vendor_group, email, hourly_rate
FROM
    vendors;
```

`email`列填充有空白字符值，而不是`NULL`值。`hourly_rate`列填充`0.00`值。

如果不小心添加了表中已经存在的列，MySQL将发出错误。 例如，如果执行以下语句：

```sql
ALTER TABLE vendors
ADD COLUMN vendor_group INT NOT NULL;
```

MySQL发出错误消息。

对于具有几列的表，很容易看出哪些列已经存在。 但是，有一个大表中有一百个列，这是比较困难的。

在某些情况下，您需要在添加表之前检查一列是否已经存在。 但是，没有像`ADD COLUMN IF NOT EXISTS`这样的声明。 但是可以从`information_schema`数据库的`columns`表中获取以下信息：

```sql
SELECT 
    IF(count(*) = 1, 'Exist','Not Exist') AS result
FROM
    information_schema.columns
WHERE
    table_schema = 'testdb'
        AND table_name = 'vendors'
        AND column_name = 'phone';
```

在[WHERE子句](./where.html)中，我们传递了三个参数：表模式或数据库，表名和列名。使用IF函数]返回列是否存在。

在本教程中，已经学习了如何使用MySQL `DROP COLUMN`语句将一个或多个列添加到表中。
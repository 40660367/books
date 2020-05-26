# MySQL replace语句

在本教程中，您将学习如何使用MySQL `REPLACE`语句向数据库表插入或更新数据。

## MySQL REPLACE语句简介

MySQL `REPLACE`语句是标准SQL的MySQL扩展。 MySQL `REPLACE`语句的工作原理如下：

- 如果给定行数据不存在，那么MySQL REPLACE语句会[插入一个新行](./insert.html)。
- 如果给定行数据存在，则`REPLACE`语句首先[删除](./delete.htmll)旧行，然后[插入](./insert.html)一个新行。 在某些情况下，`REPLACE`语句仅更新现有行。

MySQL使用[PRIMARY KEY](./primarykey.html)或`UNIQUE KEY`索引来要确定表中是否存在新行。如果表没有这些索引，则`REPLACE`语句等同于[INSERT语句](./insert.html)。

要使用MySQL `REPLACE`语句，至少需要具有`INSERT`和`DELETE`权限。

> 请注意，有一个REPLACE字符串函数，它不是本教程中说述的`REPLACE`语句。

## MySQL REPLACE语句示例

我们来看一下使用`REPLACE`语句来更好地了解它的工作原理的例子。

首先，创建一个名为`cities`的新表，如下所示：

```sql
USE testdb;

CREATE TABLE cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    population INT NOT NULL
);
```

接下来，在`cities`表中插入一些行记录：

```sql
INSERT INTO cities(name,population)
VALUES('New York',8008278),
   ('Los Angeles',3694825),
   ('Shanghai',1923400);
```

下面查询`cities`表中的数据，以验证插入操作 - 

```sql
SELECT * FROM cities;
```

现在，在`cities`表中有三个城市数据。

那么，假设我们要将纽约市的人口更新为`1008256`，可以使用UPDATE语句如下：

```sql
UPDATE cities 
SET 
    population = 1008256
WHERE
    id = 1;
```

再次查询`cities`表中的数据来验证更新结果 - 

```sql
mysql> UPDATE cities 
SET 
    population = 1008256
WHERE
    id = 1;
```

`UPDATE`语句的确按照预期更新了数据。

之后，使用`REPLACE`声明将洛杉矶市的人口更新为`3696820`。

```sql
REPLACE INTO cities(id,population) VALUES(2,3696820);
Query OK, 2 rows affected
```

上面执行返回结果中提示：*2 rows affected*，说明有两行数据受影响。

最后，再次查询城市表的数据来验证替换的结果。

```sql
SELECT  * FROM  cities;
```

现在`name`列为`NULL`。 您可能期望`name`列的值保持不变。但是，`REPLACE`语句不这样做。 在这种情况下，`REPLACE`语句的工作原理如下：

- `REPLACE`语句首先使用列列表提供的信息将新行插入到`cities`表中。但是插入失败，因为在`cities`表中已经存在`ID`为`2`的行记录，因此，MySQL引发了重复键错误。
- 然后，`REPLACE`语句更新具有`id`列值为`2`指定的行记录。在正常进程中，它将先删除具有冲突`id`为`2`的旧行，然后插入一个新行。

## MySQL REPLACE和INSERT

`REPLACE`语句的第一种形式类似于`INSERT`语句，除了`INSERT`关键字换成`REPLACE`关键字以外，如下所示：

```sql
REPLACE INTO table_name(column_list)
VALUES(value_list);
```

例如，如果要在`cities`表中插入新行，请使用以下查询：

```sql
REPLACE INTO cities(name,population)
VALUES('Phoenix',1321523);
```

请注意，没有出现在`REPLACE`语句中的列将使用默认值插入相应的列。 如果列具有`NOT NULL`属性并且没有默认值，并且您如果没有在`REPLACE`语句中指定该值，则MySQL将引发错误。这是`REPLACE`和`INSERT`语句之间的区别。

例如，在以下语句中，仅指定`name`列的值，而没有指定`population`列。MySQL引发错误消息。 因为`population`列不接受`NULL`值，而我们定义`cities`表时，也没有指定`population`列的默认值。

```sql
REPLACE INTO cities(name)
VALUES('Houston');
```

执行上面语句后，MySQL发出如下的错误消息：

```sql
Error Code: 1364. Field 'population' doesn't have a default value
```

## MySQL REPLACE和UPDATE

`REPLACE`语句的第二种形式类似于`UPDATE`语句，如下所示：

```sql
REPLACE INTO table
SET column1 = value1,
    column2 = value2;
```

请注意，`REPLACE`语句中没有[WHERE子句](./where.html)。

例如，如果要将`Phoenix`城市的人口更新为`1768980`，请使用`REPLACE`语句，如下所示：

```sql
REPLACE INTO cities
SET id = 4,
    name = 'Phoenix',
    population = 1768980;
```

与`UPDATE`语句不同，如果不在`SET`子句中指定列的值，则`REPLACE`语句将使用该列的默认值。

```sql
SELECT * FROM cities;
```

## MySQL REPLACE INTO和SELECT

`REPLACE`语句的第三种形式类似于INSERT INTO SELECT语句：

```sql
REPLACE INTO table_1(column_list)
SELECT column_list
FROM table_2
WHERE where_condition;
```

假设要复制`ID`为`1`的城市行记录，可以使用`REPLACE INTO SELECT`语句，如下查询示例：

```sql
REPLACE INTO cities(name,population)
SELECT name,population FROM cities 
WHERE id = 1;
```

## MySQL REPLACE语句用法

使用`REPLACE`语句时需要知道几个重点：

- 如果您开发的应用程序不仅支持MySQL数据库，而且还支持其他关系数据库管理系统(RDBMS)，则应避免使用`REPLACE`语句，因为其他RDBMS可能不支持。代替的作法是在[事务](./tx.html)中使用[DELETE](./delete.html)和INSERT语句的组合。
- 如果在具有触发器的表中使用了`REPLACE`语句，并且发生了重复键错误的删除，则[触发器](./trigger.html)将按以下顺序触发：在删除前删除，删除之后，删除后，如果`REPLACE`语句删除当前 行并插入新行。 如果`REPLACE`语句更新当前行，则触发`BEFORE UPDATE`和`AFTER UPDATE`触发器。

在本教程中，您学习了不同形式的`REPLACE`语句来插入或更新表中的数据。
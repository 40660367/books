# MySQL DISTINCT语句

在本教程中，您将学习如何使用MySQL `DISTINCT`子句与`SELECT`语句一起组合来消除结果集中的重复行。

## MySQL DISTINCT子句简介

从表中查询数据时，可能会收到重复的行记录。为了删除这些重复行，可以在`SELECT`语句中使用`DISTINCT`子句。

`DISTINCT`子句的语法如下：

```sql
SELECT DISTINCT
    columns
FROM
    table_name
WHERE
    where_conditions;
SQL
```

## MySQL DISTINCT示例

**[准备环境](./setup.html)**

下面来看看一个使用`DISTINCT`子句从`employees`表中选择员工的唯一姓氏(`lastName`)的简单示例。

首先，使用`SELECT`语句从`employees`表中查询员工的姓氏(`lastName`)，如下所示：

```sql
SELECT 
    lastname
FROM
    employees
ORDER BY lastname;
```

可看到上面结果中，有好些结果是重复的，比如：`Bondur`，`Firrelli`等，那如何做到相同的结果只显示一个呢？要删除重复的姓氏，请将`DISTINCT`子句添加到`SELECT`语句中，如下所示：

```sql
SELECT DISTINCT
    lastname
FROM
    employees
ORDER BY lastname;
```

当使用`DISTINCT`子句时，重复的姓氏(`lastname`)在结果集中被消除。

## MySQL DISTINCT和NULL值

如果列具有`NULL`值，并且对该列使用`DISTINCT`子句，MySQL将保留一个`NULL`值，并删除其它的`NULL`值，因为`DISTINCT`子句将所有`NULL`值视为相同的值。

例如，在`customers`表中，有很多行的州(`state`)列是`NULL`值。 当使用`DISTINCT`子句来查询客户所在的州时，我们将看到唯一的州和`NULL`值，如下查询所示：

```sql
SELECT DISTINCT
    state
FROM
    customers;
```

## MySQL DISTINCT在多列上的使用

可以使用具有多个列的`DISTINCT`子句。 在这种情况下，MySQL使用所有列的组合来确定结果集中行的唯一性。

例如，要从`customers`表中获取城市(`city`)和州(`state`)的唯一组合，可以使用以下查询：

```sql
SELECT DISTINCT
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY state , city;
```

没有`DISTINCT`子句，将查询获得州(`state`)和城市(`city`)的重复组合如下：

```sql
SELECT 
    state, city
FROM
    customers
WHERE
    state IS NOT NULL
ORDER BY state , city;
```

## DISTINCT子句与GROUP BY子句比较

如果在`SELECT`语句中使用`GROUP BY`子句，而不使用聚合函数，则`GROUP BY`子句的行为与`DISTINCT`子句类似。

以下语句使用`GROUP BY`子句来选择`customers`表中客户的唯一`state`列的值。

```sql
SELECT 
    state
FROM
    customers
GROUP BY state;
```

可以通过使用`DISTINCT`子句来实现类似的结果：

```sql
SELECT DISTINCT state FROM customers;
```

一般而言，`DISTINCT`子句是`GROUP BY`子句的特殊情况。 `DISTINCT`子句和`GROUP BY`子句之间的区别是`GROUP BY`子句可对[结果集进行排序](./orderby.html)，而`DISTINCT`子句不进行排序。

如果将[ORDER BY子句](./order-by.html)添加到使用`DISTINCT`子句的语句中，则结果集将被排序，并且与使用`GROUP BY`子句的语句返回的结果集相同。

```sql
SELECT DISTINCT
    state
FROM
    customers
ORDER BY state;
```

## MySQL DISTINCT和聚合函数

可以使用具有[聚合函数](./agg.html)(例如[SUM](./sum.html)，[AVG](./avg.html)和[COUNT](./count.html))的`DISTINCT`子句中，在MySQL将聚合函数应用于结果集之前删除重复的行。

例如，要计算美国客户的唯一`state`列的值，可以使用以下查询：

```sql
SELECT 
    COUNT(DISTINCT state)
FROM
    customers
WHERE
    country = 'USA';
```

## MySQL DISTINCT与LIMIT子句

如果要将`DISTINCT`子句与[LIMIT子句](./limit.html)一起使用，MySQL会在查找`LIMIT`子句中指定的唯一行数时立即停止搜索。

以下查询`customers`表中的前`3`个非空(NOT NULL)唯一`state`列的值。

```sql
SELECT DISTINCT state FROM customers WHERE state IS NOT NULL LIMIT 3;
```

在本教程中，我们学习了使用MySQL `DISTINCT`子句的各种方法，例如消除重复行和计数非`NULL`值。
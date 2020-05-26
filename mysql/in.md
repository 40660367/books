# MySQL IN运算符 			

在本教程中，您将学习如何使用MySQL `IN`运算符来确定指定列的值是否匹配列表中的值或子查询中的任何值。

## MySQL IN操作符介绍

IN运算符允许您确定指定的值是否与列表中的值或子查询中的任何值匹配。 下面说明了`IN`操作符的语法。

```sql
SELECT 
    column1,column2,...
FROM
    table_name
WHERE 
 (expr|column_1) IN ('value1','value2',...);
```

下面我们更详细的来看看上面的查询：

- 可以在WHERE子句中与`IN`运算符一起使用，可使用列或表达式(`expr`)。
- 列表中的值必须用逗号(`，`)分隔。
- `IN`操作符也可以用在其他语句(如INSERT，UPDATE，DELETE等)的WHERE子句中。

如果`column_1`的值或`expr`表达式的结果等于列表中的任何值，则`IN`运算符返回`1`，否则返回`0`。

当列表中的值都是常量时：

- 首先，MySQL根据`column_1`的类型或`expr`表达式的结果来计算值。
- 第二步，MySQL排序值。
- 第三步，MySQL使用二进制搜索算法搜索值。因此，使用具有常量列表的`IN`运算符的查询将执行得非常快。

> 请注意，如果列表中的`expr`或任何值为`NULL`，则`IN`运算符计算结果返回`NULL`。

可以将`IN`运算符与`NOT`运算符组合，以确定值是否与列表或子查询中的任何值不匹配。

## MySQL IN示例

**[准备环境](./setup.html)**

下面练习一些使用`IN`操作符的例子。首先来看看办事处表：`offices` 的结构 - 

如果您想查找位于美国和法国的办事处，可以使用`IN`运算符作为以下查询：

```shell
SELECT 
    officeCode, city, phone, country
FROM
    offices
WHERE
    country IN ('USA' , 'France');
```

也可以使用`OR`运算符执行得到与上面查询相同的结果，如下所示：

```shell
SELECT 
    officeCode, city, phone
FROM
    offices
WHERE
    country = 'USA' OR country = 'France';
```

如果列表中有很多值，使用多个`OR`运算符则会构造一个非常长的语句。 因此，使用`IN`运算符则会缩短查询并使查询更易读。

要获得不在美国和法国的办事处，请在`WHERE`子句中使用`NOT IN`如下：

```shell
SELECT 
    officeCode, city, phone
FROM
    offices
WHERE
    country NOT IN ('USA' , 'France');
```

## MySQL IN与子查询

`IN`运算符通常用于子查询。子查询不提供常量值列表，而是提供值列表。

我们来看看两张表：`orders`和`orderDetails`表的结构以及它们之间的关系：

![img](./images/in.png)

例如，如果要查找总金额大于`60000`的订单，则使用`IN`运算符查询如下所示：

```sql
SELECT 
    orderNumber, customerNumber, status, shippedDate
FROM
    orders
WHERE
    orderNumber IN (SELECT 
            orderNumber
        FROM
            orderdetails
        GROUP BY orderNumber
        HAVING SUM(quantityOrdered * priceEach) > 60000);
```

上面的整个查询可以分为`2`个查询。

首先，子查询使用`orderDetails`表中的GROUP BY和HAVING子句返回总额大于`60000`的订单号列表。

```sql
SELECT 
    orderNumber
FROM
    orderdetails
GROUP BY orderNumber
HAVING SUM(quantityOrdered * priceEach) > 60000;
```

其次，主查询从`orders`表中获取数据，并在`WHERE`子句中应用`IN`运算符。

```sql
SELECT 
    orderNumber, customerNumber, status, shippedDate
FROM
    orders
WHERE
    orderNumber IN (10165,10287,10310);
```

在本教程中，我们向您展示了如何使用MySQL `IN`运算符来确定值是否匹配列表或子查询中的任何值。
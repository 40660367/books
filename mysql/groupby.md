# MySQL Group By子句

在本教程中，您将学习如何使用MySQL `GROUP BY`根据指定列或表达式的值将行进行分组到子组。

## MySQL GROUP BY子句简介

`GROUP BY`子句通过列或表达式的值将一组行分组为一个小分组的汇总行记录。 `GROUP BY`子句为每个分组返回一行。换句话说，它减少了结果集中的行数。

经常使用`GROUP BY`子句与聚合函数一起使用，如SUM，MAX，COUNT等。SELECT子句中使用聚合函数来计算有关每个分组的信息。

$$
abc^2\sum
$$
`GROUP BY`子句是SELECT语句的可选子句。 下面是`GROUP BY`子句语法：

```sql
SELECT 
    c1, c2,..., cn, aggregate_function(ci)
FROM
    table
WHERE
    where_conditions
GROUP BY c1 , c2,...,cn;
SQL
```

`GROUP BY`子句必须出现在`FROM`和`WHERE`子句之后。 在`GROUP BY`关键字之后是一个以逗号分隔的列或表达式的列表，这些是要用作为条件来对行进行分组。

## MySQL GROUP BY示例

**[准备环境](./setup.html)**

我们来看看`orders`表，其结构如下所示 - 

```sql
desc orders;
```

假设要将订单状态的值分组到子组中，则要使用`GROUP BY`子句并指定按`status`列来执行分组，如下查询：

```sql
SELECT 
    status
FROM
    orders
GROUP BY status;
```

可以看到，`GROUP BY`子句返回状态(`status`)值是唯一的。它像DISTINCT运算符一样工作，如下面的查询所示：

```sql
SELECT DISTINCT
    status
FROM
    orders;
```

**MySQL GROUP BY与聚合函数**

可使用聚合函数来执行一组行的计算并返回单个值。 `GROUP BY`子句通常与聚合函数一起使用以执行计算每个分组并返回单个值。

例如，如果想知道每个状态中的订单数，可以使用`COUNT`函数与`GROUP BY`子句查询语句，如下所示：

```sql
SELECT 
    status, COUNT(*) AS total_number
FROM
    orders
GROUP BY status;
```

请参阅以下订单(`orders`)和订单详细(`orderdetails`)表，它们的*ER*图如下所示 - 

![img](./images/groupby.png)

要按状态获取所有订单的总金额，可以使用`orderdetails`表连接`orders`表，并使用`SUM`函数计算总金额。请参阅以下查询：

```sql
SELECT 
    status, SUM(quantityOrdered * priceEach) AS amount
FROM
    orders
        INNER JOIN
    orderdetails USING (orderNumber)
GROUP BY status;
```

类似地，以下查询返回订单号和每个订单的总金额。

```sql
SELECT 
    orderNumber,
    SUM(quantityOrdered * priceEach) AS total
FROM
    orderdetails
GROUP BY orderNumber;
```

MySQL GROUP BY用表达式示例**

除了列之外，可以按表达式对行进行分组。以下查询获取每年的总销售额。

```sql
SELECT 
    YEAR(orderDate) AS year,
    SUM(quantityOrdered * priceEach) AS total
FROM
    orders
        INNER JOIN
    orderdetails USING (orderNumber)
WHERE
    status = 'Shipped'
GROUP BY YEAR(orderDate);
```

在这个例子中，我们使用YEAR函数从订单日期(`orderDate`)中提取年份数据。只包括已发货(`Shipped`)状态的订单。 请注意，`SELECT`子句中出现的表达式必须与`GROUP BY`子句中的相同。

## MySQL GROUP BY与HAVING子句

可使用HAVING子句过滤`GROUP BY`子句返回的分组。以下查询使用`HAVING`子句来选择`2013`年以后的年销售总额。

```sql
SELECT 
    YEAR(orderDate) AS year,
    SUM(quantityOrdered * priceEach) AS total
FROM
    orders
        INNER JOIN
    orderdetails USING (orderNumber)
WHERE
    status = 'Shipped'
GROUP BY year
HAVING year > 2013;
```

## GROUP BY子句 MySQL与标准SQL

标准SQL不允许使用`GROUP BY`子句中的别名，但MySQL支持此选项。以下查询从订单日期提取年份，并对每年的订单进行计数。该`year`用作表达式`YEAR(orderDate)`的别名，它也用作`GROUP BY`子句中的别名，此查询在标准SQL中无效。
参考以下查询 - 

```sql
SELECT 
    YEAR(orderDate) AS year, COUNT(orderNumber)
FROM
    orders
GROUP BY year;
```

MySQL还允许您以升序或降序(标准SQL不能提供)对组进行排序。默认顺序是升序。例如，如果要按状态获取订单数量并按降序对状态进行排序，则可以使用带有`DESC`的`GROUP BY`子句，如下查询语句：

```sql
SELECT 
    status, COUNT(*)
FROM
    orders
GROUP BY status DESC;
```

请注意，在`GROUP BY`子句中使用`DESC`以降序对状态进行排序。我们还可以在`GROUP BY`子句中明确指定`ASC`，按状态对分组进行升序排序。

在本教程中，我们向您演示了如何使用MySQL `GROUP BY`子句根据列或表达式的值将行分组到子组中。
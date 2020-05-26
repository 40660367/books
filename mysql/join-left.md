# MySQL 左连接(LEFT JOIN)

在本教程中，您将了解MySQL `LEFT JOIN`子句以及如何将其应用于从两个或多个数据库表查询数据。

## MySQL LEFT JOIN简介

MySQL `LEFT JOIN`子句允许您从两个或多个数据库表查询数据。`LEFT JOIN`子句是[SELECT](./select.html)语句的可选部分，出现在`FROM`子句之后。

我们假设要从两个表`t1`和`t2`查询数据。以下语句说明了连接两个表的`LEFT JOIN`子句的语法：

```sql
SELECT 
    t1.c1, t1.c2, t2.c1, t2.c2
FROM
    t1
        LEFT JOIN
    t2 ON t1.c1 = t2.c1;
```

当使用`LEFT JOIN`子句将`t1`表加入`t2`表时，如果来自左表`t1`的行与基于连接条件(`t1.c1 = t2.c1`)的右表`t2`匹配，则该行将被包含在结果集中。

如果左表中的行与右表中的行不匹配，则还将选择左表中的行并与右表中的“*假*”行组合。“*假*”行对于`SELECT`子句中的所有相应列都包含`NULL`值。

换句话说，`LEFT JOIN`子句允许您从匹配的左右表中查询选择行记录，连接左表(`t1`)中的所有行，即使在右表(`t2`)中找不到匹配的行也显示出来，但使用`NULL`值代替。

下图可帮助您可视化`LEFT JOIN`子句的工作原理。 两个圆圈之间的交点是两个表中匹配的行，左圆的剩余部分(白色部分)是`t1`表中不存在`t2`表中任何匹配行的行。 因此，左表中的所有行都包含在结果集中。

![img](./images/join-left.png)

请注意，如果这些子句在查询中可用，返回的行也必须与[WHERE](./where.html)和[HAVING](./having.html)子句中的条件相匹配。

## MySQL LEFT JOIN示例

**[准备环境](./setup.html)**

**使用MySQL LEFT JOIN子句来连接两个表**

下面来看看示例数据库中的两个表：订单表和客户表，两个表的 *ER* 图如下所示 - 

![img](./images/joinleft-table.png)

在上面的数据库图中：

- 订单(`orders`)表中的每个订单必须属于客户(`customers`)表中的客户。
- 客户(`customers`)表中的每个客户在订单(`orders`)表中可以有零个或多个订单。

要查询每个客户的所有订单，可以使用`LEFT JOIN`子句，如下所示：

```sql
SELECT
 c.customerNumber,
 c.customerName,
 orderNumber,
 o.status
FROM
 customers c
LEFT JOIN orders o ON c.customerNumber = o.customerNumber;
```

左表是`customers`表，因此，所有客户都包含在结果集中。 但是，结果集中有一些行具有客户数据，但没有订单数据。如：`customerNumber`列值为：`477`，`480`等。这些行中的订单数据为`NULL`。也就是说这些客户在`orders`表中没有任何订单(未购买过任何产品)。

因为我们使用相同的列名(`orderNumber`)来连接两个表，所以可以使用以下语法使查询更短：

```sql
SELECT
 c.customerNumber,
 customerName,
 orderNumber,
 status
FROM
 customers c
LEFT JOIN orders USING (customerNumber);
```

在上面查询语句中，下面的子句 - 

```sql
USING (customerNumber)
```

相当于 - 

```sql
ON c.customerNumber = o.customerNumber
```

如果使用[INNER JOIN](./join-inner.html)子句替换`LEFT JOIN`子句，则只能获得至少有下过一个订单的客户。

**使用MySQL LEFT JOIN子句来查找不匹配的行**

当您想要找到右表中与不匹配的左表中的行时，`LEFT JOIN`子句非常有用。要查询两个表之间的不匹配行，可以向SELECT语句添加一个[WHERE子句](./where.html)，以仅查询右表中的列值包含`NULL`值的行。

例如，要查找没有下过订单的所有客户，请使用以下查询：

```sql
SELECT 
    c.customerNumber, 
    c.customerName, 
    orderNumber, 
    o.status
FROM
    customers c
        LEFT JOIN
    orders o ON c.customerNumber = o.customerNumber
WHERE
    orderNumber IS NULL;
```

## WHERE子句与ON子句中的条件

```sql
SELECT 
    o.orderNumber, 
    customerNumber, 
    productCode
FROM
    orders o
        LEFT JOIN
    orderDetails USING (orderNumber)
WHERE
    orderNumber = 10123;
```

在本示例中，我们使用`LEFT JOIN`子句来查询`orders`表和`orderDetails`表中的数据。 该查询返回订单号为`10123`的订单及其购买产品明细信息(如果有的话)。

但是，如果将条件从`WHERE`子句移动到`ON`子句：

```sql
SELECT 
    o.orderNumber, 
    customerNumber, 
    productCode
FROM
    orders o
        LEFT JOIN
    orderDetails d ON o.orderNumber = d.orderNumber
        AND o.orderNumber = 10123;
```

想想上面代码将会输出什么结果 - 

请注意，对于[INNER JOIN](./join-inner.html)子句，`ON`子句中的条件等同于`WHERE`子句中的条件。

在本教程中，我们解释了MySQL `LEFT JOIN`子句，并向您展示了如何将使用它来从多个数据库表中查询数据。
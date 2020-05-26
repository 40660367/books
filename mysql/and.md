# MySQL AND语句

在本教程中，将学习如何使用MySQL `AND`运算符组合多个布尔表达式以形成多个条件来过滤数据。

## MySQL AND运算符简介

`AND`运算符是组合两个或多个布尔表达式的逻辑运算符，只有当两个表达式求值为`true`时才返回`true`。如果两个表达式中的一个求值为`false`，则`AND`运算符返回`false`。

```sql
WHERE boolean_expression_1 AND boolean_expression_2
```

以下说明`AND`运算符组合`true`，`false`和`null`时的结果。

|       | TRUE  | FALSE | NULL  |
| ----- | ----- | ----- | ----- |
| TRUE  | TRUE  | FALSE | NULL  |
| FALSE | FALSE | FALSE | FALSE |
| NULL  | NULL  | FALSE | NULL  |

`AND`运算符通常用在`SELECT`，`UPDATE`，`DELETE`语句的`WHERE`子句中以形成布尔表达式。`AND`运算符也用于[INNER JOIN](./join-inner.html)或[LEFT JOIN](./join-left.html)子句的连接条件。

当求值具有`AND`运算符的表达式时，MySQL会计算表达式的其余部分，直到可以确定结果为止。该功能称为短路求值。请参见以下示例。

```sql
SELECT 1 = 0 AND 1 / 0 ;
```

> 请注意，在MySQL中，`0`被认为是`false`，非零被视为`true`。

MySQL只计算表达式`1 = 0 AND 1/0`的第一部分`1 = 0`，因为表达式`1 = 0`返回`false`，所以MySQL得出结论：整个表达式的结果是`false`。 MySQL不对表达式的剩余部分求值，即不对`1/0`进行求值; 如果对`1/0`进行求值，它将发出一个错误消息，因为除以零错误。

## MySQL AND运算符示例

下面使用示例数据库中的`customers`表进行演示。`customers`表的结构如下所示 - 

```shell
desc customers;
```

以下声明选择国家是`USA`和`CA`的客户。我们在`WHERE`子句中使用`AND`运算符。

```sql
SELECT customername, country, state FROM customers WHERE country = 'USA' AND state = 'CA';
```

使用`AND`运算符，可以组合两个以上的布尔表达式。例如，以下查询返回位于美国加州的客户，并且信用额度大于`100K`。

```sql
SELECT   customername,
         country,
         state,
         creditlimit
FROM customers
WHERE country = 'USA'
        AND state = 'CA'
        AND creditlimit > 100000;
```

在本教程中，我们向您展示了如何使用MySQL `AND`运算符组合两个或多个表达式以形成`WHERE`子句的复合条件语句。
# MySQL 自连接(self join)

在本教程中，您将了解如何使用连接语句将表连接到表自身，即，在同一张表上自己连接自己。

在之前的教程中，已经学习了如何使用[INNER JOIN](./join-inner.html)，[LEFT JOIN](./join-left.html) 或 [CROSS JOIN](./join-cross.html)子句将表连接到其他表。 但是，有一个特殊情况，需要将表自身连接，这被称为自连接。

当您想将表中行与同一表中的其他行组合时，可以使用自连接。要执行自联接操作必须使用[表别名](./alias.html)来帮助MySQL在单个查询中区分左表与同一张表的右表。

## MySQL自连接的例子

**[准备环境](./setup.html)**

我们来看看示例数据库中的`employees`表，其表结构如下所示

```sql
desc employees;
```

要获得整个组织结构，可以使用`employeeNumber`和`reportsTo`列将`employees`表连接自身。`employees`表有两个角色：一个是经理，另一个是直接报告者(即，下属员工)。

```sql
SELECT 
    CONCAT(m.lastname, ', ', m.firstname) AS 'Manager',
    CONCAT(e.lastname, ', ', e.firstname) AS 'Direct report'
FROM
    employees e
        INNER JOIN
    employees m ON m.employeeNumber = e.reportsto
ORDER BY manager;
```

在上述输出中，只能看到有经理的员工。 但是，由于`INNER JOIN`子句，所以看不到总经理。总经理是没有任何经理的员工，或者他的经理人是`NULL`。

我们将上述查询中的`INNER JOIN`子句更改为`LEFT JOIN`子句，以包括总经理。 如果管理员名称为`NULL`，则还需要使用IFNULL函数来显示总经理。

```sql
SELECT 
    IFNULL(CONCAT(m.lastname, ', ', m.firstname),
            'Top Manager') AS 'Manager',
    CONCAT(e.lastname, ', ', e.firstname) AS 'Direct report'
FROM
    employees e
        LEFT JOIN
    employees m ON m.employeeNumber = e.reportsto
ORDER BY manager DESC;
```

通过使用MySQL自连接，可以通过将`customers`表连接自身来显示位于同一个城市的客户列表。参考以下查询语句 - 

```sql
SELECT 
    c1.city, c1.customerName, c2.customerName
FROM
    customers c1
        INNER JOIN
    customers c2 ON c1.city = c2.city
        AND c1.customername > c2.customerName
ORDER BY c1.city;
```

我们通过以下连接条件连接了`customers`表：

- 指定 `c1.city = c2.city` 以确保两个表的客户都是来自相同的城市。
- `c.customerName> c2.customerName`以确保不要得到相同的客户。

在本教程中，我们向您介绍了MySQL自连接，可以通过使用`INNER JOIN`或`LEFT JOIN`子句将一个表连接到自身。
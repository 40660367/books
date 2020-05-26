# MySQL 视图(view)

在本教程中，您将学习如何使用`CREATE VIEW`语句在MySQL中创建视图。

## CREATE VIEW语句简介

要在MySQL中创建一个新视图，可以使用`CREATE VIEW`语句。 在MySQL中创建视图的语法如下：

```sql
CREATE 
   [ALGORITHM = {MERGE  | TEMPTABLE | UNDEFINED}]
VIEW [database_name].[view_name] 
AS
[SELECT  statement]
```

下面我们来详细的查看上面的语法。

### 查看名称

在数据库中，视图和表共享相同的命名空间，因此视图和表不能具有相同的名称。 另外，视图的名称必须遵循表的命名规则。

### SELECT语句

在`SELECT`语句中，可以从数据库中存在的任何表或视图查询数据。`SELECT`语句必须遵循以下几个规则：

- `SELECT`语句可以在[WHERE子句](./where.html)中包含[子查询](./subquery.html)，但`FROM`子句中的不能包含子查询。
- `SELECT`语句不能引用任何变量，包括局部变量，用户变量和会话变量。
- `SELECT`语句不能引用准备语句的参数。

> 请注意，`SELECT`语句不需要引用任何表。

## 创建MySQL视图示例

**[准备环境](./setup.html)**

**创建简单的视图**

我们来看看`orderDetails`表。基于`orderDetails`表来创建一个表示每个订单的总销售额的视图。

```sql
CREATE VIEW SalePerOrder AS
    SELECT 
        orderNumber, SUM(quantityOrdered * priceEach) total
    FROM
        orderDetails
    GROUP by orderNumber
    ORDER BY total DESC;
```

如果使用`SHOW TABLES`命令来查看示例数据库中的所有表，我们还会看到`SalesPerOrder`视图也显示在表的列表中。

```sql
show tables;
```

这是因为视图和表共享相同的命名空间。要知道哪个对象是视图或表，请使用`SHOW FULL TABLES`命令，如下所示：

```sql
SHOW FULL TABLES
```

结果集中的`table_type`列指定哪个对象是视图，哪个对象是一个表(基表)。如上所示，`saleperorder`对应`table_type`列的值为：`VIEW`。

如果要查询每个销售订单的总销售额，只需要对`SalePerOrder`视图执行一个简单的SELECT语句，如下所示：

```sql
SELECT 
    *
FROM
    salePerOrder;
```

**基于另一个视图创建视图**

MySQL允许您基于另一个视图创建一个视图。例如，可以根据`SalesPerOrder`视图创建名为大销售订单(`BigSalesOrder`)的视图，以显示总计大于`60,000`的每个销售订单，如下所示：

```sql
CREATE VIEW BigSalesOrder AS
    SELECT 
        orderNumber, ROUND(total,2) as total
    FROM
        saleperorder
    WHERE
        total > 60000;
```

现在，我们可以从`BigSalesOrder`视图查询数据，如下所示：

```sql
SELECT 
    orderNumber, total
FROM
    BigSalesOrder;
```

**使用连接表创建视图**

以下是使用[INNER JOIN](./join-inner.html)创建视图的示例。 该视图包含客户编号和客户支付的总金额。

```sql
CREATE VIEW customerOrders AS
    SELECT 
        c.customerNumber,
        p.amount
    FROM
        customers c
            INNER JOIN
        payments p ON p.customerNumber = c.customerNumber
    GROUP BY c.customerNumber
    ORDER BY p.amount DESC;
```

要查询`customerOrders`视图中的数据，请使用以下查询：

```sql
SELECT  * FROM customerOrders;
```

**使用子查询创建视图**

以下说明如何使用[子查询](./subquery.html)创建视图，该视图包含价格高于所有产品的平均价格的产品。

```sql
CREATE VIEW aboveAvgProducts AS
    SELECT 
        productCode, productName, buyPrice
    FROM
        products
    WHERE
        buyPrice > 
 (SELECT 
                AVG(buyPrice)
            FROM
                products)
    ORDER BY buyPrice DESC;
SQL
```

查询上述视图：`aboveAvgProducts`的数据简单如下：

```sql
SELECT 
    *
FROM
    aboveAvgProducts;
```

在本教程中，我们向您展示了如何使用`CREATE VIEW`语句创建视图。
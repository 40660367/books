# MySQL 临时表(temporary table)

在本教程中，我们将讨论MySQL临时表，并演示如何创建，使用和删除临时表。

## MySQL临时表简介

在MySQL中，临时表是一种特殊类型的表，它允许您存储一个临时结果集，可以在单个会话中多次重用。

当使用[JOIN](./join-inner.html)子句查询需要单个[SELECT](./select.html)语句的数据是不可能或遇到瓶颈的时候，临时表非常方便。 在这种情况下，我们就可以使用临时表来存储直接结果，并使用另一个查询来处理它。

MySQL临时表具有以下特殊功能：

- 使用`CREATE TEMPORARY TABLE`语句创建临时表。请注意，在`CREATE`和`TABLE`关键字之间添加`TEMPORARY`关键字。
- 当会话结束或连接终止时，MySQL会自动删除临时表。当您不再使用临时表时，也可以使用DROP TABLE语句来显式删除临时表。
- 一个临时表只能由创建它的客户机访问。不同的客户端可以创建具有相同名称的临时表，而不会导致错误，因为只有创建临时表的客户端才能看到它。 但是，在同一个会话中，两个临时表不能共享相同的名称。
- 临时表可以与数据库中的普通表具有相同的名称。 例如，如果在示例数据库中创建一个名为`employees`的临时表，则现有的`employees`表将变得无法访问。 对`employees`表发出的每个查询现在都是指`employees`临时表。 当删除`您`临时表时，永久`employees`表可以再次访问。

> 注意：即使临时表可以与永久表具有相同的名称，但不推荐。 因为这可能会导致混乱，并可能导致意外的数据丢失。例如，如果与数据库服务器的连接丢失，并且您自动重新连接到服务器，则不能区分临时表和永久性表。 然后，你又发出一个`DROP TABLE`语句，这个时候删除的可能是永久表而不是临时表，这种结果是不可预料的。

## 示例 

**[准备环境](./setup.html)**

### 创建MySQL临时表

要创建临时表，只需要将`TEMPORARY`关键字添加到`CREATE TABLE`语句的中间。

例如，以下语句创建一个临时表，按照收入存储前`10`名客户：

```sql
CREATE TEMPORARY TABLE top10customers
SELECT p.customerNumber, 
       c.customerName, 
       FORMAT(SUM(p.amount),2) total
FROM payments p
INNER JOIN customers c ON c.customerNumber = p.customerNumber
GROUP BY p.customerNumber
ORDER BY total DESC
LIMIT 10;
```

现在，可以从`top10customers`临时表中查询数据，例如：

```sql
SELECT * FROM top10customers;
```

### 删除MySQL临时表

您可以使用`DROP TABLE`语句来删除临时表，但最好添加`TEMPORARY`关键字如下：

```sql
DROP TEMPORARY TABLE table_name;
```

`DROP TEMPORARY TABLE`语句仅删除临时表，而不是永久表。 当将临时表命名为永久表的名称相同时，它可以避免删除永久表的错误

例如，要删除`top10customers`临时表，请使用以下语句：

```sql
DROP TEMPORARY TABLE top10customers;
SQL
```

请注意，如果尝试使用`DROP TEMPORARY TABLE`语句删除永久表，则会收到一条错误消息，指出您尝试删除的表是未知的。

如果开发使用连接池或持久连接的应用程序，则不能保证临时表在应用程序终止时自动删除。

因为应用程序使用的数据库连接可能仍然打开并放置在其他客户端使用的连接池中。 因此，当不再使用它们时马上删除临时表，这是一个很好的做法。

在本教程中，您已经了解了MySQL临时表以及如何管理临时表，例如创建和删除新临时表。
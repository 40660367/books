# MySQL 事务 			

在本教程中，您将了解MySQL事务以及如何使用MySQL `COMMIT`语句和MySQL `ROLLBACK`语句来管理MySQL中的事务。

## MySQL事务介绍

要了解MySQL中的事务是什么，我们先来看看在示例数据库中添加新的销售订单的示例。添加销售订单的步骤如下所述：

- 从`orders`表中查询最新的销售订单编号，并使用下一个销售订单编号作为新的销售订单编号。
- 在指定客户的`orders`表中插入新的销售订单。
- 将新的销售订单项目插入`orderdetails`表中。
- 从`orders`表和`orderdetails`中获取数据以确认更改。

现在想象如果由于数据库故障而导致上述一个或多个步骤失败，那么数据会发生什么？ 如果将订单项添加到`orderdetails`表中的步骤失败，系统中将会有空的销售订单(只有订单号，不知道这个订单卖了什么)。数据可能不完整，那么必须花费的精力来解决这个问题。

如何解决这个问题？ 这就是为什么事务来处理。 MySQL事务使您能够执行一组MySQL操作，以确保数据库从不包含部分操作的结果。 在一组操作中，如果其中一个失败，则会恢复回滚数据库。 如果没有发生错误，则将整个语句集合提交到数据库。

## 使用MySQL事务

在上述示例中，我们将使用它们添加销售订单之前，先来看看MySQL事务语句。

要启动事务，请使用`START TRANSACTION`语句。要撤消MySQL语句执行，请使用`ROLLBACK`语句。

请注意，有一些SQL语句，主要是数据定义语句，不能在事务中使用以下语句：

```sql
CREATE / ALTER / DROP DATABASE
CREATE /ALTER / DROP / RENAME / TRUNCATE TABLE
CREATE / DROP INDEX
CREATE / DROP EVENT
CREATE / DROP FUNCTION
CREATE / DROP PROCEDURE
…
```

要将更改写入事务中的数据库，请使用`COMMIT`语句。要注意的是，默认情况下，MySQL自动提交对数据库的更改。

要强制MySQL不会自动提交更改，请使用以下语句：

```sql
SET autocommit = 0
```

## MySQL事务的例子

**[准备环境](./setup.html)**

要使用MySQL事务，首先必须将MySQL语句分解成逻辑部分，并确定何时应该提交或回滚数据。

下面来看一下使用MySQL事务在上面的示例数据库中添加新的销售订单并添加事务处理步骤的例子：

- 使用START TRANSACTION语句启动事务。
- 从`orders`表中获取最新的销售订单编号，并使用下一个销售订单编号作为新的销售订单编号。
- 在指定`orders`表中插入新的销售订单。
- 将新的销售订单项目插入`orderdetails`表中。
- 使用`COMMIT`语句提交更改。
- 从`orders`表和`orderdetails`表中获取数据以确认更改。

以下是执行上述步骤的脚本：

```sql
-- start a new transaction
start transaction;

-- get latest order number
select @orderNumber := max(orderNUmber) 
from orders;
-- set new order number
set @orderNumber = @orderNumber  + 1;

-- insert a new order for customer 145
insert into orders(orderNumber,
                   orderDate,
                   requiredDate,
                   shippedDate,
                   status,
                   customerNumber)
values(@orderNumber,
       now(),
       date_add(now(), INTERVAL 5 DAY),
       date_add(now(), INTERVAL 2 DAY),
       'In Process',
        145);
-- insert 2 order line items
insert into orderdetails(orderNumber,
                         productCode,
                         quantityOrdered,
                         priceEach,
                         orderLineNumber)
values(@orderNumber,'S18_1749', 30, '136', 1),
      (@orderNumber,'S18_2248', 50, '55.09', 2); 
-- commit changes    
commit;       

-- get the new inserted order
select * from orders a 
inner join orderdetails b on a.ordernumber = b.ordernumber
where a.ordernumber = @ordernumber;
```

在本教程中，您学习了如何使用`START TRANSACTION COMMI`和`ROLLBACK`的MySQL事务语句来管理MySQL中的事务以保护数据完整性。
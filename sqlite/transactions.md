# SQLite 事务(transaction)

事务是针对数据库执行的工作单元。事务是以逻辑顺序完成的单位或工作顺序，无论是由用户手动完成还是由某种数据库程序自动完成。

事务是将一个或多个更改传播到数据库。例如，如果您要在表中创建，更新或删除记录，那么您将在表上执行事务。控制事务以确保数据完整性和处理数据库错误很重要。

实际上，您会将许多SQLite查询组成一个组，并将它们作为事务的一部分一起执行。

## 事务性质

事务具有以下四个标准属性，通常由首字母缩写ACID指代。

- **原子性** -确保工作单元内的所有操作均成功完成；否则，事务将在失败点中止，并且先前的操作将回滚到其先前的状态。
- **一致性** -确保数据库在成功提交事务后正确更改状态。
- **隔离** -使事务能够独立运行并且彼此透明。
- **持久性** -确保在系统故障的情况下持久化已提交事务的结果或效果。

## 事务控制

以下是用于控制事务的以下命令：

- **BEGIN TRANSACTION*** -开始事务。
- **COMMIT-**要保存更改，也可以使用**END TRANSACTION**命令。
- **ROLLBACK-**回滚更改。

事务控制命令仅与DML命令INSERT，UPDATE和DELETE一起使用。在创建表或删除表时不能使用它们，因为这些操作是在数据库中自动提交的。

### BEGIN TRANSACTION命令

可以使用BEGIN TRANSACTION或简单地使用BEGIN命令来启动事务。这样的事务通常会持续到遇到下一个COMMIT或ROLLBACK命令为止。但是，如果数据库关闭或发生错误，则事务也将回滚。以下是启动事务的简单语法。

```sql
BEGIN;
or 
BEGIN TRANSACTION;
```

### COMMIT命令

COMMIT命令是用于将事务调用的更改保存到数据库的事务性命令。

自上一个COMMIT或ROLLBACK命令以来，COMMIT命令将所有事务保存到数据库中。

以下是COMMIT命令的语法。

```sql
COMMIT;
or
END TRANSACTION;
```

### ROLLBACK命令

ROLLBACK命令是用于撤消尚未保存到数据库的事务的事务性命令。

自上次发出COMMIT或ROLLBACK命令以来，ROLLBACK命令只能用于撤消事务。

以下是ROLLBACK命令的语法。

```
ROLLBACK;
```

**例**

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

现在，让我们开始一个事务并从age = 25的表中删除记录。然后，使用ROLLBACK命令撤消所有更改。

```
BEGIN;
DELETE FROM COMPANY WHERE AGE = 25;
ROLLBACK;
```

现在检查COMPANY表，

```SQL
SELECT * FROM COMPANY
```

康康

让我们开始另一个事务，并从年龄= 25的表中删除记录，最后我们使用COMMIT命令来提交所有更改。

```
BEGIN;
DELETE FROM COMPANY WHERE AGE = 25;
sqlite> COMMIT;
```

现在检查COMPANY表，

```sql
SELECT * FROM COMPANY
```

康康
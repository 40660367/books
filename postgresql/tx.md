# PostgreSQL 事务(transaction)	

事务是对数据库执行的工作单元。事务是以逻辑顺序完成的工作的单位或顺序，无论是用户手动的方式还是通过某种数据库程序自动执行。

## 事务性质

事务具有以下四个标准属性，一般是由首字母缩写词`ACID`简称：

- **原子性(Atomicity)**：确保工作单位内的所有操作成功完成; 否则事务将在故障点中止，以前的操作回滚到其以前的状态。
- **一致性(Consistency)**：确保数据库在成功提交的事务时正确更改状态。
- **隔离性(Isolation)**：使事务能够独立运作并相互透明。
- **持久性(Durability)**：确保在系统发生故障的情况下，提交的事务的结果或效果仍然存在。

## 事务控制

以下命令用于控制事务：

- `BEGIN TRANSACTION`：开始事务。
- `COMMIT`：保存更改，或者您可以使用`END TRANSACTION`命令。
- `ROLLBACK`：回滚更改。

事务控制命令仅用于DML命令`INSERT`，`UPDATE`和`DELETE`。 创建表或删除它们时不能使用它们，因为这些操作会在数据库中自动提交。

## BEGIN TRANSACTION命令：

可以使用`BEGIN TRANSACTION`或简单的`BEGIN`命令来开始事务。 这样的事务通常会持续下去，直到遇到下一个`COMMIT`或`ROLLBACK`命令。 但如果数据库关闭或发生错误，则事务也将`ROLLBACK`。

以下是启动/开始事务的简单语法：

```sql
BEGIN;
```

## COMMIT命令

`COMMIT`命令是用于将事务调用的更改保存到数据库的事务命令。
`COMMIT`命令自上次的`COMMIT`或`ROLLBACK`命令后将所有事务保存到数据库。
`COMMIT`命令的语法如下：

```sql
COMMIT;
```

## ROLLBACK命令

`ROLLBACK`命令是用于还原尚未保存到数据库的事务的事务命令。自上次发出`COMMIT`或`ROLLBACK`命令以来，`ROLLBACK`命令只能用于撤销事务。
`ROLLBACK`命令的语法如下：

```sql
ROLLBACK;
```

## 示例

[准备环境及数据](./setup.html)

查看`COMPANY`表中的数据

现在，我们开始一个事务，并删除表中`age = 25`的记录，最后使用`ROLLBACK`命令撤消所有的更改。

```sql
BEGIN;
DELETE FROM COMPANY WHERE AGE = 25;
ROLLBACK;
```

这时查看`COMPANY`表应该什么查看到什么内容？



现在，让我们开始另一个事务，并从表中删除`age = 25`的记录，最后使用`COMMIT`命令提交所有的更改。

```sql
BEGIN;
DELETE FROM COMPANY WHERE AGE = 25;
COMMIT;
```



这时查看`COMPANY`表应该什么查看到什么内容？
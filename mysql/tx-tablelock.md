# MySQL 表锁定(table lock)

在本教程中，您将学习如何使用MySQL锁来协调会话之间的表访问。

MySQL允许客户端会话明确获取表锁，以防止其他会话在特定时间段内访问表。客户端会话只能为自己获取或释放表锁。它不能获取或释放其他会话的表锁。

在详细介绍之前，我们将创建一个名为`sampledb`的示例数据库，其中包含一个简单的`tbl`表来模拟练习表锁定语句。

```sql
CREATE DATABASE IF NOT EXISTS testdb;

USE testdb;
CREATE TABLE tbl (
  id int(11) NOT NULL AUTO_INCREMENT,
  col int(11) NOT NULL,
  PRIMARY KEY (id)
);
```

## LOCK和UNLOCK TABLES语法

获取表的锁的简单形式如下：

```sql
LOCK TABLES table_name [READ | WRITE]
```

可将表的名称放在`LOCK TABLES`关键字后面，后跟一个锁类型。 MySQL提供两种锁类型：`READ`和`WRITE`。 我们将在下一节详细介绍这两种锁类型。

要释放表的锁，请使用以下语句：

```sql
UNLOCK TABLES;
```

### 表锁定为READ

表的READ锁具有以下功能：

- 同时可以通过多个会话获取表的`READ`锁。此外，其他会话可以从表中读取数据，而无需获取锁定。
- 持有`READ`锁的会话只能从表中读取数据，但不能写入。此外，其他会话在释放`READ`锁之前无法将数据写入表中。来自另一个会话的写操作将被放入等待状态，直到释放`READ`锁。
- 如果会话正常或异常终止，MySQL将会隐式释放所有锁。这也与`WRITE`锁相关。

## 示例

下面我们来看看在以下情况下`READ`锁如何工作。

首先，连接到`testdb1`数据库。要查找当前的连接ID，请使用`CONNECTION_ID()`函数，如下所示：

```sql
create database testdb1;
use database testdb1;
SELECT CONNECTION_ID();
```

然后，在向`tbl`表中插入一个新行

```sql
INSERT INTO tbl(col) VALUES(10);
```

接下来，从上表`tbl`中检索所有行。

```sql
SELECT * FROM tbl;
```

之后，要获取锁，可以使用`LOCK TABLE`语句。
最后，在同一个会话中，如果您尝试在`tbl`表中插入一个新行，将收到一条错误消息。

```sql
LOCK TABLE tbl READ;

INSERT INTO tbl(col) VALUES(11);
```

`1099 - Table 'tbl' was locked with a READ lock and can't be updated`

所以一旦获得了`READ`锁定，就不能在同一个会话中的表中写入数据。让我们从不同的会话中来查看`READ`锁。

首先，打开另一个终端并连接到数据库`testdb`，然后检查连接ID：

```sql
SELECT CONNECTION_ID();
```

然后，从`tbl`检索数据，如下所示 - 

```sql
SELECT * FROM tbl;
```

接下来，从第二个会话(会话ID为第二个会话中得到的ID)插入一个新行到`tbl`表中。

第二个会话的插入操作处于等待状态，因为第一个会话已经在`tbl`表上获取了一个`RE`AD锁，并且尚未释放。

可以使用`SHOW PROCESSLIST`语句查看详细信息，如下所示 - 

```sql
SHOW PROCESSLIST;
```

之后，返回第一个会话并使用`UNLOCK TABLES`语句来释放锁。从第一个会话释放`READ`锁之后，在第二个会话中执行`INSERT`操作。

最后，查看`tbl`表中的数据，以查看第二个会话中的`INSERT`操作是否真的执行。

```sql
SELECT * FROM tbl;
```

### 将MySQL表锁定WRITE

表锁为`WRITE`具有以下功能：

- 只有拥有表锁定的会话才能从表读取和写入数据。
- 在释放`WRITE`锁之前，其他会话不能从表中读写。

详细了解`WRITE`锁的工作原理。

首先，从第一个会话获取一个`WRITE`锁。

```sql
LOCK TABLE tbl WRITE;
```

然后，在`tbl`表中插入一个新行。

```sql
INSERT INTO tbl(col) VALUES(11);
```

没有问题，上面语句可能正常执行。接下来，从`tbl`表读取数据。

```sql
SELECT * FROM tbl;
```

之后，打开第二个连接到MySQL的会话，尝试写和读数据：

MySQL将这些操作置于等待状态。可以在第一个会话中，使用`SHOW PROCESSLIST`语句来查看它。

```sql
SHOW PROCESSLIST;
```

最后，从第一个会话释放锁。执行以下语句 - 

```sql
UNLOCK TABLES;
```

执行上面语句后，将看到第二个会话中的所有待处理已经执行操作。

```sql
SELECT * FROM tbl;
```

在本教程中，我们向您展示了如何锁定和解锁：`READ`和`WRITE`操作，以便在会话之间配合表访问。
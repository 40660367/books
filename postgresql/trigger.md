# PostgreSQL 触发器(trigger)

PostgreSQL触发器是一组动作或数据库回调函数，它们在指定的表上执行指定的数据库事件(即，`INSERT`，`UPDATE`，`DELETE`或`TRUNCATE`语句)时自动运行。 触发器用于验证输入数据，执行业务规则，保持审计跟踪等。

## 触发器的重点知识

1. PostgreSQL在以下情况下执行/调用触发器：在尝试操作之前(在检查约束并尝试`INSERT`，`UPDATE`或`DELETE`之前)。或者在操作完成后(在检查约束并且`INSERT`，`UPDATE`或`DELETE`完成后)。或者不是操作(在视图中`INSERT`，`UPDATE`或`DELETE`的情况下)
2. 对于操作修改的每一行，都会调用一个标记为`FOR EACH ROWS`的触发器。 另一方面，标记为`FOR EACH STATEMENT`的触发器只对任何给定的操作执行一次，而不管它修改多少行。
3. 您可以为同一事件定义同一类型的多个触发器，但条件是按名称按字母顺序触发。
4. 当与它们相关联的表被删除时，触发器被自动删除。

## PostgreSQL触发器的使用

PostgreSQL触发器可用于以下目的：

- 验证输入数据。
- 执行业务规则。
- 为不同文件中新插入的行生成唯一值。
- 写入其他文件以进行审计跟踪。
- 从其他文件查询交叉引用目的。
- 访问系统函数。
- 将数据复制到不同的文件以实现数据一致性。

## 使用触发器的优点

- 它提高了应用程序的开发速度。 因为数据库存储触发器，所以您不必将触发器操作编码到每个数据库应用程序中。
- 全局执法业务规则。定义触发器一次，然后将其重用于使用数据库的任何应用程序。
- 更容易维护 如果业务策略发生变化，则只需更改相应的触发程序，而不是每个应用程序。
- 提高客户/服务器环境的性能。 所有规则在结果返回之前在服务器中运行。

## PostgreSQL创建触发器语法说明

`CREATE TRIGGER`语句用于在PostgreSQL表中创建一个新的触发器。 当表发生特定事件(即`INSERT`，`UPDATE`和`DELETE`)时，它被激活。

**语法**

```sql
CREATE  TRIGGER trigger_name [BEFORE|AFTER|INSTEAD OF] event_name  
ON table_name  
[  
 -- Trigger logic goes here....  
];
```

在这里，`event_name`可以是`INSERT`，`UPDATE`，`DELETE`和`TRUNCATE`数据库操作上提到的表`table_name`。 您可以选择在表名后指定`FOR EACH ROW`。

下面来看看看如何在`INSERT`操作中创建触发器的语法。

```sql
CREATE  TRIGGER trigger_name AFTER INSERT ON column_name  
ON table_name  
[  
 -- Trigger logic goes here....  
];
```

## 触发器示例

[准备环境及数据](./setup.html)

下面举个例子来演示PostgreSQL在`INSERT`语句之后创建触发器。在以下示例中，我们对每个记录插入到`COMPANY`表中进行审核(审计)。

使用以下查询创建一个名为`COMPANY`的表：

```sql
CREATE TABLE COMPANY(  
   ID INT PRIMARY KEY     NOT NULL,  
   NAME           TEXT    NOT NULL,  
   AGE            INT     NOT NULL,  
   ADDRESS        CHAR(50),  
   SALARY         REAL  
);
SQL
```

为了保存审计/审核，我们将创建一个名为`AUDIT`的新表，只要在`COMPANY`表中有一个新记录的条目，就会插入日志消息。

使用以下查询语句创建另一个表`Audit`：

```sql
CREATE TABLE AUDIT(  
    EMP_ID INT NOT NULL,  
    ENTRY_DATE TEXT NOT NULL  
);
```

在`COMPANY`表上创建触发器之前，首先创建一个名为`auditlogfunc()`的函数/过程。

执行以下查询语句来创建函数/过程：

```sql
CREATE OR REPLACE FUNCTION auditlogfunc() RETURNS TRIGGER AS $example_table$  
    BEGIN  
        INSERT INTO AUDIT(EMP_ID, ENTRY_DATE) VALUES (new.ID, current_timestamp);  
        RETURN NEW;   
    END;  
$example_table$ LANGUAGE plpgsql;
```

现在通过使用以下查询语句在`COMPANY`表上创建一个触发器：

```sql
CREATE TRIGGER example_trigger AFTER INSERT ON COMPANY  
FOR EACH ROW EXECUTE PROCEDURE auditlogfunc();
```

向`COMPANY`表中插入一些数据记录，以验证触发器执行情况。

```sql
INSERT INTO COMPANY VALUES(1, 'JD', 8, '北京市', 9999);
INSERT INTO COMPANY VALUES(2, 'TENCENT', 6, '广州市', 8999);
```

在执行上面两条插入语句后，现我们来看`AUDIT`表是否有自动插入两条审核记录。

```SQL
select * from company;
```

可以确定的是在插入数据后触发了触发器，PostgreSQL也自动向`AUDIT`表中创建/插入两个记录。 这些记录是触发的结果，这是因为我们在`AFTER INSERT on COMPANY`表上创建了这些记录。
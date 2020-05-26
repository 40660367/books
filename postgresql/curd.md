# PostgreSQL 查询(curd)

## PostgreSQL插入数据（INSERT语句） 			

在PostgreSQL中，`INSERT`查询用于在表中插入新行。 您可以一次插入单行或多行到表中。

**语法：**

```sql
INSERT INTO TABLE_NAME (column1, column2, column3,...columnN)  
VALUES (value1, value2, value3,...valueN);
```

> 注意：`column1`, `column2`, `column3`,`...columnN`是要插入数据的表中的列的名称。

**示例:**

[准备环境及数据](./setup.html)

打开查询工具并执行以下查询以在表中插入多个值：

```sql
CREATE TABLE COMPANYTEST(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL,
   JOIN_DATE      DATE
);

INSERT INTO COMPANYTEST(  ID, NAME, AGE, ADDRESS, SALARY)  
VALUES
(1, 'Maxsu', 25, 'London', 109990.00 ), 
(2, 'minsu', 25, 'Moscow', 125000.00 ), 
(3, 'Manisha', 24, 'Mumbai', 65000.00), 
(4, 'Larry', 21, 'Paris', 85000.00);
```

## PostgreSQL查询数据（SELECT语句）

在PostgreSQL中，SELECT语句用于从数据库表中检索数据。 数据以结果表格的形式返回。 这些结果表称为结果集。

**语法：**

```sql
SELECT "column1", "column2".."column" FROM "table_name";
```

这里，`column1，column2，.. columnN`指定检索哪些数据的列。 如果要从表中检索所有字段，则必须使用以下语法：

```sql
SELECT * FROM "table_name"
```

**示例:**

```sql
SELECT id,name FROM COMPANYTEST;
```

或者 

```sql
SELECT ID, NAME, AGE, SALARY  FROM COMPANYTEST;
```

## PostgreSQL更新数据（UPDATE语句） 			

在PostgreSQL中，UPDATE语句用于修改表中现有的记录。 要更新所选行，您必须使用WHERE子句，否则将更新所有行。

**语法：**

以下是`update`语句的基本语法：

```sql
UPDATE table_name  
SET column1 = value1, column2 = value2...., columnN = valueN  
WHERE [condition];
```

## PostgreSQL删除数据（DELETE语句） 			

DELETE语句用于从表中删除现有记录。 “WHERE”子句用于指定删除所选记录的条件，如是不指定条件则将删除所有记录。

**语法：**

以下是DELETE语句的基本语法：

```sql
DELETE FROM table_name  
WHERE [condition];
```

**示例**

从“`EMPLOYEES`”中删除“ID”为`1`的记录。执行以下查询语句：

```sql
DELETE FROM COMPANYTEST WHERE ID = 1;
```

> 注意：如果不使用“WHERE”条件，整个表中的记录都将被删除。

```SQL
DELETE FROM COMPANYTEST;
SELECT * FROM COMPANYTEST;
```


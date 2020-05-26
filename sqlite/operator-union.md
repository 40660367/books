# SQLite UNION运算符

SQLite `UNION`运算符用于使用`SELECT`语句组合两个或多个表的结果集。 `UNION`操作符仅显示唯一的行(删除重复的行)。

在使用`UNION`运算符时，每个`SELECT`语句必须在结果集中具有相同数量的字段。

**语法：**

```sql
SELECT expression1, expression2, ... expression_n  
FROM tables  
[WHERE conditions]  
UNION  
SELECT expression1, expression2, ... expression_n  
FROM tables  
[WHERE conditions];
```

### 示例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

查看以下两个表：`COMPANY`和`DEPARTMENT`。

`student`表中具有以下数据：

```sql
SELECT * FROM COMPANY;
```

康康

`DEPARTMENT`表中具有以下数据：

```sql
SELECT * FROM DEPARTMENT;
```

康康

**示例1：**

使用`union`操作符返回单个字段 - 

```sql
SELECT ID FROM COMPANY  
UNION  
SELECT ID FROM DEPARTMENT;
```

康康



**示例2：** 

联合内部和外部连接，按照以下条件和UNION子句，将上述两个表：`COMPANY`和`DEPARTMENT`作为内部联接和外部联接。

```sql
SELECT EMP_ID, NAME, DEPT FROM COMPANY JOIN DEPARTMENT  
ON COMPANY.ID = DEPARTMENT.EMP_ID  
UNION  
SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT  
ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

康康
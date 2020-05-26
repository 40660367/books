# SQLite 表达式(expression)

SQLite表达式是一个或多个值，运算符和SQL函数的组合。表达式用于评估示值。

SQLite表达式用查询语言(SQL)编写，并与`SELECT`语句一起使用。

**语法：**

```sql
SELECT column1, column2, columnN   
FROM table_name   
WHERE [CONDITION | EXPRESSION];
```

SQLite中主要有三种类型的表达式：

### 1. SQLite布尔表达式

SQLite布尔表达式用于在匹配单个值的基础上获取数据。

**语法：**

```sql
SELECT column1, column2, columnN   
FROM table_name   
WHERE SINGLE VALUE MATCHTING EXPRESSION;
```

**示例：**

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

有一个名称为“COMPANY”的表，具有以下数据：

使用SQLite布尔表达式的简单示例，如下所示 -

```sql
SELECT * FROM COMPANY WHERE SALARY > 20000;
```

康康

### 2. SQLite数字表达式

SQLite数字表达式用于在查询中用来执行数学运算。

**语法：**

```sql
SELECT numerical_expression as  OPERATION_NAME  
[FROM table_name WHERE CONDITION] ;
```

**示例**

```sql
SELECT (25 + 15) AS ADDITION;
SELECT (250 + 255) AS ADDITION;
```

康康



数字表达式包含一些内置函数，如`avg()`，`sum()`，`count()`等。这些函数称为聚合数据计算函数。

**例如**

```sql
SELECT COUNT(*) AS "number of PEOPLE" FROM COMPANY;
SELECT SUM(SALARY) AS "Sum SALARY of PEOPLE" FROM COMPANY;
```

康康

### 3. SQlite日期表达式

SQlite日期表达式用于获取当前系统日期和时间值。

**语法：**

```sql
SELECT CURRENT_TIMESTAMP;
```

康康
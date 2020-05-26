# PostgreSQL 表达式

表达式是由一个或多个的值、运算符、PostgresSQL 函数组成的。

PostgreSQL 表达式类似一个公式，我们可以将其应用在查询语句中，用来查找数据库中指定条件的结果集。

## 实例

[准备环境及数据](./setup.html)

**SELECT 语句语法:**

```sql
SELECT column1, column2, columnN
FROM table_name
WHERE [CONDITION | EXPRESSION];
```

PostgreSQL 的表达式可以有不同类型，我们接下来会讲到。

### 布尔表达式

布尔表达式是根据一个指定条件来读取数据：

```sql
SELECT column1, column2, columnN
FROM table_name
WHERE SINGLE VALUE MATCHTING EXPRESSION;
```

以下使用了布尔表达式（**SALARY=10000**）来查询数据：

```sql
SELECT * FROM COMPANY WHERE SALARY = 10000;
```

### 数字表达式

数字表达式常用于查询语句中的数学运算：

```sql
SELECT numerical_expression as  OPERATION_NAME
[FROM table_name WHERE CONDITION] ;
```

**实例:**

**numerical_expression** 是一个数学运算表达式，实例如下：

```sql
SELECT (17 + 6) AS ADDITION ;
```

此外 PostgreSQL 还内置了一些数学函数，如：

- avg() ： 返回一个表达式的平均值
- sum() ： 返回指定字段的总和
- count() ： 返回查询的记录总数

以下实例查询 COMPANY 表的记录总数：

```sql
SELECT COUNT(*) AS "RECORDS" FROM COMPANY;
```

### 日期表达式

日期表达式返回当前系统的日期和时间，可用于各种数据操作。

**实例:**

```sql
SELECT CURRENT_TIMESTAMP;
```
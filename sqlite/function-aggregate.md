# SQLite 聚合函数(aggregate function)

SQLite聚合函数是将多行的值组合在一起作为某些条件的输入并形成单个值作为输出结果的函数。 以下是SQLite中的一些聚合函数的列表：

- SQLite `MIN()`函数
- SQLite `MAX()`函数
- SQLite `AVG()`函数
- SQLite `COUNT()`函数
- SQLite `SUM()`函数
- SQLite `RANDOM()`函数
- SQLite `ABS()`函数
- SQLite `UPPER()`函数
- SQLite `LOWER()`函数
- SQLite `LENGTH()`函数
- SQLite `sqlite_version()`函数

| 序号 | 函数                   | 描述说明                                                     |
| ---- | ---------------------- | ------------------------------------------------------------ |
| 1    | `MIN()`函数            | SQLite MIN()函数用于查询某列的最低(最小)值。                 |
| 2    | `MAX()`函数            | SQLite MAX()函数用于查询某列的最高(最大)值。                 |
| 3    | `AVG()`函数            | SQLite MAX()函数用于查询某列的平均值。                       |
| 4    | `COUNT()`函数          | SQLite COUNT()函数用于计算数据库表中的行数。                 |
| 5    | `SUM()`函数            | SQLite SUM()函数用于查询指定数字列的总数(相加的总和)。       |
| 6    | `RANDOM()`函数         | SQLite RANDOM()函数返回`-9223372036854775808`与`+9223372036854775807`之间的伪随机整数。 |
| 7    | `ABS()`函数            | SQLite ABS()函数用于获取给定参数的绝对值。                   |
| 8    | `UPPER()`函数          | SQLite UPPER()函数用于将给定字符串参数转换为大写字母。       |
| 9    | `LOWER()`函数          | SQLite LOWER()函数用于将给定字符串参数转换为小写字母。       |
| 10   | `LENGTH()`函数         | SQLite LENGTH()函数用于获取给定字符串的长度。                |
| 11   | `sqlite_version()`函数 | SQLite sqlite_version()函数用于获取SQLite库的版本。          |

## SQLite AVG()函数 			

SQLite `AVG()`函数用于检索表达式或给定列的平均值。

**语法**

```sql
SELECT AVG(aggregate_expression)  
FROM tables  
[WHERE conditions];
```

在`GROUP BY`子句中使用`AVG()`函数时的语法：

```sql
SELECT expression1, expression2, ... expression_n  
AVG(aggregate_expression)  
FROM tables  
[WHERE conditions]  
GROUP BY expression1, expression2, ... expression_n;
```

**示例：**

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)，如果已经配置好请忽略。

```sql
SELECT AVG(SALARY) AS "SALARY AVG"  FROM COMPANY   
```

康康

```sql
SELECT NAME, AVG(SALARY) AS "SALARY AVG BY AGE"
FROM COMPANY  
GROUP BY AGE;
```

康康

## SQLite COUNT()函数 			

SQLite `COUNT()`函数用于检索表达式或给定列的行数。

**语法**

```sql
SELECT COUNT(aggregate_expression)  
FROM tables  
[WHERE conditions];
```

在`GROUP BY`子句中使用`COUNT()`函数时的语法：

```sql
SELECT expression1, expression2, ... expression_n  
COUNT(aggregate_expression)  
FROM tables  
[WHERE conditions]  
GROUP BY expression1, expression2, ... expression_n;
```

**示例1：**

导入库<>

从`COMPANY`表中检索`AGE`大于`22`的人数：

```sql
SELECT COUNT(*) AS "Number of PEOPLE"  FROM COMPANY  WHERE AGE > 22;
```

康康

**示例2：**

计算`AGE`大于`22`岁的学生人数，并按学生名字分组。

```sql
SELECT COUNT(*) AS "Number of PEOPLE GROUP BY ADDRESS"
FROM COMPANY  
WHERE AGE > 22  
GROUP BY ADDRESS;
```

康康

## SQLite MAX()函数 			

SQLite `MAX()`函数用于获取表达式或给定列的最大值。

**语法**

```sql
SELECT MAX(aggregate_expression)  
FROM tables  
[WHERE conditions];
SQL
```

在`GROUP BY`子句中使用`Max()`函数时的语法：

```sql
SELECT expression1, expression2, ... expression_n  
MAX(aggregate_expression)  
FROM tables  
[WHERE conditions]  
GROUP BY expression1, expression2, ... expression_n;
SQL
```

**示例1：**

导入库<>

从`COMPANY`表中检索人员的最高薪资(`SALARY`)：

```sql
SELECT MAX(SALARY) AS "Highest SALARY"  FROM COMPANY ; 
```

**示例2：**

使用具有的`GROUP BY`子句的`MAX()`函数：

从`COMPANY`表中检索`NAME`,`ADDRESS`和`MAX(SALARY)`，并按`ADDRESS`的数据排序：

```sql
SELECT NAME, ADDRESS, MAX(SALARY) AS "Highest SALARY"  
FROM COMPANY  
WHERE ID >= 2  
GROUP BY ADDRESS;
```

## SQLite SUM()函数 			

SQLite `SUM()`函数用于返回表达式或给定数字列的总和。

**语法**

```sql
SELECT SUM(aggregate_expression)  
FROM tables  
[WHERE conditions];
```

在`SUM()`函数中使用`GROUP BY`子句时的语法：

```sql
SELECT expression1, expression2, ... expression_n  
SUM(aggregate_expression)  
FROM tables  
[WHERE conditions]  
GROUP BY expression1, expression2, ... expression_n;
```

**示例1：**

导入库<>

从`COMPANY`表中检索`AGE`小于`24`的人员总薪资：

```sql
SELECT SUM(SALARY) AS "Total SALARY"  
FROM STUDENT  
WHERE AGE < 24;
```

康康

**示例2：**

使用具有数学公式的`SUM()`函数，求每个月的学生总费用 - 

```sql
SELECT SUM(SALARY / 12) AS "Total Monthly SALARY"  
FROM COMPANY;
```

康康

**示例3：**

计算每个地址的学生总人数，按学生地址(`Address`)分组。

从`student`表中检索地址，并按地址分组并查找相应费用的总和。

```sql
SELECT ADDRESS, SUM(Salary) AS "Total Salary"  
FROM COMPANY  
GROUP BY ADDRESS;
```

康康
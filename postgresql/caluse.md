# PostgreSQL 子句(caluse)

## PostgreSQL ORDER BY子句

PostgreSQL `ORDER BY`子句用于按升序或降序对数据进行排序。数据在一列或多列的基础上进行排序。

**语法：**

```sql
SELECT column-list  
FROM table_name  
[WHERE condition]  
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
```

**参数说明：**

- `column_list`：它指定要检索的列或计算。
- `table_name`：它指定要从中检索记录的表。FROM子句中必须至少有一个表。
- `WHERE conditions`：可选。 它规定必须满足条件才能检索记录。
- `ASC`：也是可选的。它通过表达式按升序排序结果集(默认，如果没有修饰符是提供者)。
- `DESC`：也是可选的。 它通过表达式按顺序对结果集进行排序。

**示例：**

[准备环境及数据](./setup.html)

升序排序 - ORDER BY [field] ASC

执行以下查询以按升序`ORDER BY AGE`数据记录：

```sql
SELECT *   FROM COMAPNY  
ORDER BY AGE ASC;
```

**示例：**

降序排序 - ORDER BY [field] DESC

执行以下查询以按降序`ORDER BY name DESC`数据的记录：

```sql
SELECT *   FROM COMAPNY 
ORDER BY name DESC;
```

按照 `name` 字段降序排序

## PostgreSQL GROUP BY子句 			

PostgreSQL `GROUP BY`子句用于将具有相同数据的表中的这些行分组在一起。 它与`SELECT`语句一起使用。

`GROUP BY`子句通过多个记录收集数据，并将结果分组到一个或多个列。 它也用于减少输出中的冗余。

**语法：**

```sql
SELECT column-list  
FROM table_name  
WHERE [conditions ]  
GROUP BY column1, column2....columnN  
ORDER BY column1, column2....columnN
SQL
```

> 注意：在`GROUP BY`多个列的情况下，您使用的任何列进行分组时，要确保这些列应在列表中可用。

**示例1** 

```sql
SELECT NAME, SUM(SALARY)   
FROM COMAPNY   
GROUP BY NAME;
```

**示例2 **：如何减少冗余数据：

我们在“`COMAPNY`”表中插入一些重复的记录。添加以下数据：

```sql
INSERT INTO COMAPNY VALUES (6, 'Nancy', 24, 'New York', 135000);  
INSERT INTO COMAPNY VALUES (7, 'Manisha', 19, 'Noida', 125000);  
INSERT INTO COMAPNY VALUES (8, 'Larry', 45, 'Texas', 165000);
```

执行以下查询以消除冗余：

```sql
SELECT NAME, SUM(SALARY)   FROM COMAPNY   
GROUP BY NAME;
```

在上面的例子中，当我们使用`GROUP BY NAME`时，可以看到重复的名字数据记录被合并。 它指定`GROUP BY`减少冗余。

## PostgreSQL Having子句 			

在PostgreSQL中，HAVING子句与GROUP BY子句组合使用，用于选择函数结果满足某些条件的特定行。

**语法：**

```sql
SELECT column1, column2  
FROM table1, table2  
WHERE [ conditions ]  
GROUP BY column1, column2  
HAVING [ conditions ]  
ORDER BY column1, column2
```

**示例1：**

```sql
SELECT NAME   
FROM COMAPNY  
GROUP BY NAME HAVING COUNT (NAME) < 2;
```

**示例2：**

我们在“`COMAPNY`”表中插入一些重复的记录，首先添加以下数据：

```sql
INSERT INTO COMAPNY VALUES (7, 'Minsu', 24, 'Delhi', 135000);  
INSERT INTO COMAPNY VALUES (8, 'Manisha', 19, 'Noida', 125000);
```

执行以下查询表“`COMAPNY`”中`name`字段值计数大于`1`的名称。

```sql
SELECT NAME,COUNT (NAME) 
FROM COMAPNY  
GROUP BY NAME HAVING COUNT (NAME) > 1;
```

这是因为名字为 `Minsu`和 `Manisha` 有两条记录。

## PostgreSQL WHERE 子句

在 PostgreSQL 中，当我们需要根据指定条件从单张表或者多张表中查询数据时，就可以在 SELECT 语句中添加 WHERE 子句，从而过滤掉我们不需要数据。

WHERE 子句不仅可以用于 SELECT 语句中，同时也可以用于 UPDATE，DELETE 等等语句中。

**语法**

以下是 SELECT 语句中使用 WHERE 子句从数据库中读取数据的通用语法：

```sql
SELECT column1, column2, columnN
FROM table_name
WHERE [condition1]
```

**示例：**

找出 **AGE(年龄)** 字段大于等于 25，并且 **SALARY(薪资)** 字段大于等于 65000 的数据：

```sql
SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000;
```

找出 **AGE(年龄)** 字段大于等于 25，或者 **SALARY(薪资)** 字段大于等于 65000 的数据：

```sql
SELECT * FROM COMPANY WHERE AGE >= 25 OR SALARY >= 65000;
```

在公司表中找出 **AGE(年龄)** 字段不为空的记录：

```sql
SELECT * FROM COMPANY WHERE AGE IS NOT NULL;
```

在 COMPANY 表中找出 **NAME(名字)** 字段中以 Pa 开头的的数据：

```sql
SELECT * FROM COMPANY WHERE NAME LIKE 'Pa%';
```

以下 SELECT 语句列出了 **AGE(年龄)** 字段为 25 或 27 的数据：

```sql
SELECT * FROM COMPANY WHERE AGE IN ( 25, 27 );
```

以下 SELECT 语句列出了 **AGE(年龄)** 字段不为 25 或 27 的数据：

```sql
SELECT * FROM COMPANY WHERE AGE NOT IN ( 25, 27 );
```

以下 SELECT 语句列出了 **AGE(年龄)** 字段在 25 到 27 的数据：

```sql
SELECT * FROM COMPANY WHERE AGE BETWEEN 25 AND 27;
```

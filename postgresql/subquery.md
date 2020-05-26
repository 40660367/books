# PostgreSQL 子查询(subquery)

子查询或内部查询或嵌套查询是一个PostgreSQL查询中的查询，它可以嵌入到`WHERE`子句中。子查询用于返回将在主查询中使用的数据作为进一步限制要检索的数据的条件。
子查询可以与`SELECT`，`INSERT`，`UPDATE`和`DELETE`语句以及运算符(如`=`，`<`，`>`，`>=`，`<=`，`IN`等)一起使用。

子查询必须遵循以下规则：

- 子查询必须括在括号中。
- 子查询在SELECT子句中只能有一列，除非主查询中有多个列用于比较其所选列的子查询。
- `ORDER BY`不能用于子查询，尽管主查询可以使用`ORDER BY`。`GROUP BY`可用于执行与子查询中的`ORDER BY`相同的功能。
- 返回多行的子查询只能与多个值运算符一起使用，例如：`IN`，`EXISTS`，`NOT IN`，`ANY / SOME`，`ALL`运算符。
- `BETWEEN`运算符不能与子查询一起使用; 但是，`BETWEEN`可以在子查询中使用。

## 带SELECT语句的子查询

子查询最常用于SELECT语句。基本语法如下：

```sql
SELECT column_name [, column_name ]
FROM   table1 [, table2 ]
WHERE  column_name OPERATOR
      (SELECT column_name [, column_name ]
      FROM table1 [, table2 ]
      [WHERE])
```

**示例:**

[准备环境及数据](./setup.html)

考虑`COMPANY`表有以下记录：

```sql
SELECT * FROM COMPANY
```

现在，我们用SELECT语句检查以下子查询：

```sql
SELECT *
FROM COMPANY
WHERE ID IN (SELECT ID
			FROM COMPANY
			WHERE SALARY > 45000) ;
```

## 带INSERT语句的子查询

子查询也可以用于INSERT语句。INSERT语句使用从子查询返回的数据插入另一个表。可以使用任何字符，日期或数字函数修改子查询中选定的数据。

**基本语法如下：**

```sql
INSERT INTO table_name [ (column1 [, column2 ]) ]
           SELECT [ *|column1 [, column2 ]
           FROM table1 [, table2 ]
           [ WHERE VALUE OPERATOR ]
```

**示例：**

考虑一个表`COMPANY_BKP`，其结构与`COMPANY`表类似，可以使用`COMPANY_BKP`作为表名使用相同的`CREATE TABLE`数据结构来创建。现在要将完整的`COMPANY`表复制到`COMPANY_BKP`中，以下是语句：

```sql
INSERT INTO COMPANY_BKP
SELECT * FROM COMPANY
WHERE ID IN (SELECT ID FROM COMPANY) ;
```

## 带UPDATE语句的子查询：

子查询可以与`UPDATE`语句一起使用。当使用具有`UPDATE`语句的子查询时，可以更新表中的单列或多列。

```sql
UPDATE table
SET column_name = new_value
[ WHERE OPERATOR [ VALUE ]
   (SELECT COLUMN_NAME
   FROM TABLE_NAME)
   [ WHERE) ]
```

**示例：**

假设我们有一个名为`COMPANY_BKP`表，它是`COMPANY`表的备份。

以下示例将所有客户(其`AGE`大于或等于`27`)在`COMPANY`表中的`SALARY`更新为`0.50`倍：

```sql
UPDATE COMPANY
     SET SALARY = SALARY * 0.50
     WHERE AGE IN (SELECT AGE FROM COMPANY_BKP
                   WHERE AGE >= 27 );
```

这将影响两行，最后`COMPANY`表中将具有以下记录：

## 带有DELETE语句的子查询：

子查询可以与DELETE语句一起使用，就像上面提到的任何其他语句一样。

基本语法如下：

```sql
DELETE FROM TABLE_NAME
[ WHERE OPERATOR [ VALUE ]
   (SELECT COLUMN_NAME
   FROM TABLE_NAME)
   [ WHERE) ]
```

**示例：**

假设我们有一个`COMPANY_BKP`表，它是`COMPANY`表的备份。

以下示例从`COMPANY` 表中删除所有客户的记录，其`AGE`大于或等于`27`数据记录：

```sql
testdb=# DELETE FROM COMPANY
     WHERE AGE IN (SELECT AGE FROM COMPANY_BKP
                   WHERE AGE >= 27 );
```

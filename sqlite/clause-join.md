# SQLite JOIN(表联接)子句

SQLite **Joins**子句用于合并数据库中两个或多个表中的记录。JOIN是一种通过使用每个表的公用值来组合两个表中的字段的方法。

SQL定义了三种主要的联接类型-

- 交叉联接 CROSS JOIN
- 内部联接 INNER JOIN
- 外连接 OUTTER JOIN

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](./setup.html)，如果已经配置好请忽略。

在继续之前，让我们考虑两个表COMPANY和DEPARTMENT。

```sql
SELECT * FROM COMPANY
```
除了COMPANY表，我们要在再看下DEPARTMENT表中有以下可用的记录

```sql
SELECT * FROM DEPARTMENT
```

康康

## 交叉联接

CROSS JOIN将第一个表的每一行与第二个表的每一行匹配。如果输入表分别具有x和y行，则结果表将具有x * y行。由于CROSS JOINs可能会生成非常大的表，因此必须注意仅在适当的时候使用它们。

以下是CROSS JOIN的语法:

```sql
SELECT ... FROM table1 CROSS JOIN table2 ...
```

### 示例：

基于上面的语法和数据表，您可以编写CROSS JOIN，如下所示：

```sql
SELECT EMP_ID, NAME, DEPT FROM COMPANY CROSS JOIN DEPARTMENT;
```

康康

## 内部联接

INNER JOIN通过基于连接谓词组合两个表（table1和table2）的列值来创建新的结果表。该查询将table1的每一行与table2的每一行进行比较，以找到满足联接谓词的所有行对。当满足连接谓词时，A和B的每对匹配行对的列值将合并为结果行。

INNER JOIN是最常见的默认联接类型。您可以选择使用INNER关键字。

以下是INNER JOIN的语法

```sql
SELECT ... FROM table1 [INNER] JOIN table2 ON conditional_expression ...
```

为了避免冗余并缩短短语，可以**使用USING**表达式声明INNER JOIN条件。此表达式指定一个或多个列的列表。

```sql
SELECT ... FROM table1 JOIN table2 USING ( column1 ,... ) ...
```

NATURAL JOIN类似于**JOIN ... USING**，只是它自动测试两个表中存在的每个列的值之间是否相等-

```sql
SELECT ... FROM table1 NATURAL JOIN table2...
```

### 示例：

基于上面的语法和数据表，您可以编写一个INNER JOIN，如下所示：

```sql
SELECT EMP_ID, NAME, DEPT FROM COMPANY INNER JOIN DEPARTMENT
   ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

康康

## 外连接

OUTER JOIN是INNER JOIN的扩展。尽管SQL标准定义了三种类型的外部联接：LEFT，RIGHT和FULL，但是SQLite仅支持**LEFT OUTER JOIN**。

外部联接的条件与内部联接的条件相同，使用ON，USING或NATURAL关键字表示。初始结果表的计算方法相同。一旦计算了主JOIN，OUTER JOIN将从一个或两个表中获取所有未连接的行，将它们填充为NULL，并将其附加到结果表中。

以下是LEFT OUTER JOIN的语法-

```sql
SELECT ... FROM table1 LEFT OUTER JOIN table2 ON conditional_expression ...
```

为了避免冗余并缩短短语，可以使用USING表达式声明OUTER JOIN条件。此表达式指定一个或多个列的列表。

```sql
SELECT ... FROM table1 LEFT OUTER JOIN table2 USING ( column1 ,... ) ...
```

### 示例：

基于上面的语法和数据表，您可以编写内部联接，如下所示：

```sql
SELECT EMP_ID, NAME, DEPT FROM COMPANY LEFT OUTER JOIN DEPARTMENT
   ON COMPANY.ID = DEPARTMENT.EMP_ID;
```

康康

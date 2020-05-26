# MySQL 查询SELECT

使用`SELECT`语句从表或视图获取数据。表由行和列组成，如电子表格。 通常，我们只希望看到子集行，列的子集或两者的组合。`SELECT`语句的结果称为结果集，它是行列表，每行由相同数量的列组成。

请参阅示例数据库(`mysqlstudy`)中的以下`employees`表的结构。它有`8`列：员工人数，姓氏，名字，分机，电子邮件，办公室代码，报告，职位等。

`SELECT`语句控制要查看哪些列和行。例如，如果只对所有员工的名字，姓氏和职位感兴趣，或者您只想查看其职位是销售代表的每位员工的信息，则`SELECT`语句可帮助您执行这些操作。

我们来看一下`SELECT`语句的语法：

```sql
SELECT 
    column_1, column_2, ...
FROM
    table_1
[INNER | LEFT |RIGHT] JOIN table_2 ON conditions
WHERE
    conditions
GROUP BY column_1
HAVING group_conditions
ORDER BY column_1
LIMIT offset, length;
```

`SELECT`语句由以下列表中所述的几个子句组成：

- `SELECT`之后是逗号分隔列或星号(`*`)的列表，表示要返回所有列。
- `FROM`指定要查询数据的表或视图。
- `JOIN`根据某些连接条件从其他表中获取数据。
- `WHERE`过滤结果集中的行。
- `GROUP BY`将一组行组合成小分组，并对每个小分组应用聚合函数。
- `HAVING`过滤器基于`GROUP BY`子句定义的小分组。
- `ORDER BY`指定用于排序的列的列表。
- `LIMIT`限制返回行的数量。

语句中的`SELECT`和`FROM`语句是必须的，其他部分是可选的。

> 在随后的教程中将更详细地了解每个子句。在本教程中，我们将重点介绍`SELECT`语句的简单形式用法。

## MySQL SELECT语句示例

**[准备环境](./setup.html)**

`SELECT`语句允许通过在`SELECT`子句中指定逗号分隔列的列表来查询表的部分数据。 

本节的学习依赖示例数据库。如还未导入该数据库，请在第二节课程的提示下导入示例数据库`classicmodels`后再进行本节的学习。

准备数据

例如，如果要仅查看员工的名字，姓氏和职位，请使用以下查询：

```sql
SELECT 
    lastname, firstname, jobtitle
FROM
    employees;
```

即使员工表中有很多列，`SELECT`语句只返回表中所有行的三列数据

### 注意比较以下两个语句返回列有什么区别

*语句-1*

```sql
SELECT lastname, firstname, jobtitle FROM employees;
```
*语句-2*

```sql
SELECT * FROM employees;
```

如果要获取`employees`表中所有列的数据，可以列出`SELECT`子句中的所有列名，或者只需使用星号(`*`)表示您想要从表的所有列获取数据，如下查询：

它返回`employees`表中的所有列和行。应该使用星号(`*`)进行测试。建议显式获取数据的列，原因如下：

- 使用星号(`*`)可能会返回不使用的列的数据。 它在MySQL数据库服务器和应用程序之间产生不必要的*I/O*磁盘和网络流量。
- 如果明确指定列，则结果集更可预测并且更易于管理。 想象一下，当您使用星号(`*`)并且有人通过添加更多列来更改表格数据时，将会得到一个与预期不同的结果集。
- 使用星号(`*`)可能会将敏感信息暴露给未经授权的用户。

在本教程中，您已经了解并熟悉了MySQL `SELECT`语句的用法，并通过`SELECT`语句从MySQL表中查询数据。



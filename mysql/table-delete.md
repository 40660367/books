# MySQL 删除表数据

在本教程中，您将学习如何使用MySQL `DELETE`语句从单个表中删除数据。

## MySQL DELETE语句介绍

要从表中删除数据，请使用MySQL `DELETE`语句。下面说明了`DELETE`语句的语法：

```sql
DELETE FROM table_name
WHERE condition;
```

在上面查询语句中 - 

- 首先，指定删除数据的表(`table_name`)。
- 其次，使用条件来指定要在`WHERE`子句中删除的行记录。如果行匹配条件，这些行记录将被删除。

> 请注意，`WHERE`子句是可选的。如果省略`WHERE`子句，`DELETE`语句将删除表中的所有行。

除了从表中删除数据外，`DELETE`语句返回删除的行数。

## MySQL DELETE的例子

**[准备环境](./setup.html)**

我们将使用`employees`表进行演示。

> 请注意，一旦删除数据，它就会永远消失。因此，在执行`DELETE`语句之前，应该先备份数据库以防万一要找回删除过的数据。

假设要删除`officeNumber`为`4`的员工，则使用`DELETE`语句与`WHERE`子句作为以下查询：

```shell
DELETE FROM employees 
WHERE
    officeCode = 4;
```

要删除`employees`表中的所有行，请使用不带WHERE子句的`DELETE`语句，如下所示：

```shell
DELETE FROM employees;
```

在执行上面查询语句后，`employees`表中的所有行都被删除。

执行SELECT进行验证：

```shell
SELECT * FROM employees;
```

## MySQL DELETE和LIMIT子句

如果要限制要删除的行数，则使用LIMIT子句

**语法：**

```sql
DELETE FROM table
LIMIT row_count;
```

请注意，表中的行顺序未指定，因此，当您使用`LIMIT`子句时，应始终使用`ORDER BY`子句，不然删除的记录可能不是你所预期的那样。

```sql
DELETE FROM table_name
ORDER BY c1, c2, ...
LIMIT row_count;
```

**示例:**

**[准备环境](./setup.html)及[导入示例数据][./database-import.html]**

考虑在示例数据库中的`customers`表，其表结构如下：

```sql
desc customers;
```

例如，以下语句按客户名称按字母排序客户，并删除前`10`个客户：

```sql
DELETE FROM customers
ORDER BY customerName
LIMIT 10;
```

类似地，以下`DELETE`语句选择法国(*France*)的客户，按升序按信用额度(`creditLimit`)进行排序，并删除前`5`个客户：

```shell
DELETE FROM customers
WHERE country = 'France'
ORDER BY creditLimit
LIMIT 5;
```

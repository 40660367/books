# SQLite AND与OR运算符

SQLite **AND**＆**OR**运算符用于编译多个条件以缩小SQLite语句中的所选数据。这两个运算符称为合**取运算符**。

这些运算符提供了在同一SQLite语句中与不同运算符进行多次比较的方法。

## and 运算符

在**与**运营商允许多个条件中存在一个SQLite语句的WHERE子句。使用AND运算符时，当所有条件都为真时，将假定完全条件为真。例如，仅当condition1和condition2都为true时，[condition1] AND [condition2]才为true。

### 句法

以下是带有WHERE子句的AND运算符的基本语法。

```sql
SELECT column1, column2, columnN 
FROM table_name
WHERE [condition1] AND [condition2]...AND [conditionN];
```

您可以使用AND运算符组合**N**个条件。对于要由SQLite语句执行的操作（无论是事务还是查询），用AND分隔的所有条件必须为TRUE。

### 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

在SELECT语句之后列出了AGE大于或等于25 **并且**薪水大于或等于65000.00的所有记录。

```
SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000;
```

康康

## or 运算符

OR运算符还用于在SQLite语句的WHERE子句中组合多个条件。使用OR运算符时，如果至少有一个条件为true，则将假定完全条件为true。例如，如果condition1或condition2为true，则[condition1]或[condition2]将为true。

### 句法

以下是带有WHERE子句的OR运算符的基本语法。

```
SELECT column1, column2, columnN 
FROM table_name
WHERE [condition1] OR [condition2]...OR [conditionN]
```

您可以使用OR运算符组合**N**个条件。对于要通过SQLite语句执行的操作（无论是事务还是查询），仅由OR分隔的条件之一必须为TRUE。

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

### 例

在SELECT语句之后列出了AGE大于或等于25 **或**薪金大于或等于65000.00的所有记录。

```
SELECT * FROM COMPANY WHERE AGE >= 25 OR SALARY >= 65000;
```

康康
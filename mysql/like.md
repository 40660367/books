# MySQL LIKE运算符

在本教程中，您将了解如何使用MySQL `LIKE`运算符根据模式查询选择数据。

`LIKE`操作符通常用于基于模式查询选择数据。以正确的方式使用`LIKE`运算符对于增加/减少查询性能至关重要。

`LIKE`操作符允许您根据指定的模式从表中查询选择数据。 因此，`LIKE`运算符通常用在SELECT语句的WHERE子句中。

MySQL提供两个通配符，用于与`LIKE`运算符一起使用，它们分别是：百分比符号 - `%`和下划线 - `_`。

- 百分比(`%`)通配符允许匹配任何字符串的零个或多个字符。
- 下划线(`_`)通配符允许匹配任何单个字符。

## MySQL LIKE运行符示例

**[准备环境](./setup.html)**

下面让我们来学习一些使用`LIKE`操作符的例子。请参阅以下`employees`表。

```sql
desc employees;
```

MySQL LIKE使用百分比(％)通配符**

假设要搜索名字以字符`a`开头的员工信息，可以在模式末尾使用百分比通配符(`％`)，如下所示：

```sql
SELECT 
    employeeNumber, lastName, firstName
FROM
    employees
WHERE
    firstName LIKE 'a%';
```

MySQL将扫描整个`employees`表以找到每个其名字以字符`a`开头，后跟任意数量的字符的员工信息。

要搜索员工以`on`字符结尾的姓氏，例如，`Patterson`，`Thompson`，可以使用模式开头的`％`通配符，如下查询：

```sql
SELECT 
    employeeNumber, lastName, firstName
FROM
    employees
WHERE
    lastName LIKE '%on';
```

如果知道要搜索包含指定字符串，则可以在模式的开头和结尾使用百分比(`%`)通配符。

例如，要查找 `lastname` 字段值中包含`on`字符串的所有员工，可使用带有`%on%`条件，如下所示 - 

```sql
SELECT 
    employeeNumber, lastName, firstName
FROM
    employees
WHERE
    lastname LIKE '%on%';
```

**MySQL LIKE带下划线(_)通配符**

要查找名字以`T`开头的员工，以`m`结尾，并且包含例如`Tom`，`Tim`之间的任何单个字符，可以使用下划线通配符来构建模式，如下所示：

```sql
SELECT 
    employeeNumber, lastName, firstName
FROM
    employees
WHERE
    firstname LIKE 'T_m';
```

**具有NOT运算符的MySQL LIKE运算符**

MySQL允许将`NOT`运算符与`LIKE`运算符组合，以找到不匹配特定模式的字符串。

假设要搜索姓氏(`lastname`)不以字符`B`开头的员工，则可以使用`NOT LIKE`作为以下查询：

```sql
SELECT 
    employeeNumber, lastName, firstName
FROM
    employees
WHERE
    lastName NOT LIKE 'B%';
```

> 请注意，使用`LIKE`运算符，该模式不区分大小写，因此，`b%`和`B%`模式产生相同的结果。

## MySQL LIKE与ESCAPE子句

有时想要匹配的模式包含通配符，例如`10%`，`_20`等这样的字符串时。在这种情况下，您可以使用`ESCAPE`子句指定转义字符，以便MySQL将通配符解释为文字字符。如果未明确指定转义字符，则反斜杠字符`\`是默认转义字符。

如下语句，将查询`productCode`字段中包含`_20`字符串的值。

```sql
SELECT 
    productCode, productName
FROM
    products
WHERE
    productCode LIKE '%\_20%';
```

或者，也可以使用`ESCAPE`子句指定一个不同的转义字符，例如`$`：

```sql
SELECT 
    productCode, productName
FROM
    products
WHERE
    productCode LIKE '%$_20%' ESCAPE '$';
```

以上语句查询结果与上一个语句得到的结果相同。

模式`%$_20%`匹配任何包含`_20`字符串的字符串。

`LIKE`操作符强制MySQL扫描整个表以找到匹配的行记录，因此，它不允许数据库引擎使用索引进行快速搜索。因此，当要从具有大量行的表查询数据时，使用`LIKE`运算符来查询数据的性能会大幅降低。

在本教程中，您已经学习了如何使用`LIKE`运算符根据模式查询数据，这比使用比较运算符更灵活。
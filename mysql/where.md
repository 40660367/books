# MySQL WHERE子句

在本教程中，我们将学习如何在`SELECT`语句中使用MySQL `WHERE`子句来过滤结果集中的行记录。

## MySQL WHERE子句简介

如果使用SELECT语句但不使用WHERE子句在表中查询数据，则会获取表中的所有行记录，这些行记录中大部分是不想要的行记录。例如，在一些表中存放商业交易中的数据。 从这些表中获取所有行，尤其是对于诸如员工，销售订单，采购订单，生产订单等的大型表格来说，这是没有意义的，因为我们经常想要的是一些特定的数据，例如本季度的销售额 ，今年销量比去年同期的销量等等。

`WHERE`子句允许根据指定的过滤表达式或条件来指定要选择的行。

> 您还将学习如何使用LIMIT子句来限制`SELECT`语句返回的行数。

## MySQL WHERE子句示例

**[准备环境](./setup.html)**

假设只想从`employees`表中获取销售代表员工，可使用以下查询：

```sql
SELECT     lastname, firstname, jobtitle
FROM       employees
WHERE      jobtitle = 'Sales Rep';
```

执行上面查询，得到以下结果 - 

即使`WHERE`子句出现在语句的末尾，但MySQL会首先使用`WHERE`子句中的表达式来选择匹配的行。它选择具有职位名称为销售代表的行记录。

```sql
jobtitle = 'Sales Rep';
```

MySQL从`SELECT`子句中的选择列表中选择列。

可以像上面的查询一样形成一个简单的条件，或者是将多个表达式与逻辑运算符(如AND，OR等)组合在一起的一个非常复杂的例子。例如，要在办公室代码(`officeCode`)等于`1`中查找所有销售代表，请使用以下查询：

```sql
SELECT lastname, firstname, jobtitle FROM employees WHERE jobtitle = 'Sales Rep' AND officeCode = 1;
```

下表列出了可用于在`WHERE`子句中形成过滤表达式的比较运算符。

| 操作符       | 描述                                    |
| ------------ | --------------------------------------- |
| `=`          | 等于，几乎任何数据类型都可以使用它。    |
| `<>` 或 `!=` | 不等于                                  |
| `<`          | 小于，通常使用数字和日期/时间数据类型。 |
| `>`          | 大于，                                  |
| `<=`         | 小于或等于                              |
| `>=`         | 大于或等于                              |

以下查询使用不等于(`!=`)运算符来获取不是销售代表的其它所有员工：

```sql
SELECT lastname, firstname, jobtitle FROM employees WHERE jobtitle <> 'Sales Rep';
```

以下查询将获得办公室代码大于`5`的每位员工：

```sql
SELECT lastname, firstname, officeCode FROM employees WHERE officecode > 5;
```

办公室代码小于或等于`4`(`<= 4`)的员工呢？

```sql
SELECT lastname, firstname, officeCode FROM employees WHERE officecode <= 4;
```

**更多关于MySQL WHERE子句…**

还有一些有用的运算符可以在`WHERE`子句中使用来形成复杂的条件，例如：

- BETWEEN选择在给定范围值内的值。
- LIKE匹配基于模式匹配的值。
- IN指定值是否匹配列表中的任何值。
- `IS NULL`检查该值是否为`NULL`。

在本教程中，我们学习了如何使用MySQL `WHERE`子句来根据条件过滤行记录。

# MySQL BETWEEN运算符

`BETWEEN`运算符允许指定要测试的值范围。 我们经常在`SELECT`，`INSERT`，`UPDATE`和`DELETE`语句的`WHERE`子句中使用`BETWEEN`运算符。

下面说明了`BETWEEN`运算符的语法：

```sql
expr [NOT] BETWEEN begin_expr AND end_expr;
```

`expr`是在由`begin_expr`和`end_expr`定义的范围内测试的表达式。

所有三个表达式：`expr`，`begin_expr`和`end_expr`必须具有相同的数据类型。

如果`expr`的值大于或等于(`>=`)`begin_expr`的值且小于等于(`<=`)`end_expr`的值，则`BETWEEN`运算符返回`true`，否则返回`0`。

如果`expr`的值小于(`<`)`begin_expr`的值或大于`end_expr`的值的值，则`NOT BETWEEN`将返回`true`，否则返回`0`。

如果任何表达式为`NULL`，则`BETWEEN`运算符返回`NULL`值。如果想指定一个不含边界值的范围，则使用大于(`>`)和小于(`<`)运算符。

## MySQL BETWEEN示例

下面我们来练习一些使用`BETWEEN`运算符的例子。

**[准备环境](./setup.html)**

**MySQL BETWEEN与数字示例**

```sql
use classicmodels
```
请参见示例数据库中的以下产品(`products`)表，desc为描述命令，后边跟表名。

```sql
desc products;
```

假设您想要查找价格在`90`和`100`(含`90`和`100`)元范围内的商品，可以使用`BETWEEN`运算符作为以下查询：

```sql
SELECT 
    productCode, productName, buyPrice
FROM
    products
WHERE
    buyPrice BETWEEN 90 AND 100;
```

也可以通过使用大于或等于(`>=`)和小于或等于(`<=`)运算符来实现相同的结果，如以下查询：

```sql
SELECT 
    productCode, productName, buyPrice
FROM
    products
WHERE
    buyPrice >= 90 AND buyPrice <= 100;
```

要查找购买价格不在`20`到`100`(含`20`到`100`)之间的产品，可将`BETWEEN`运算符与`NOT`运算符组合使用，如下：

```sql
SELECT 
    productCode, productName, buyPrice
FROM
    products
WHERE
    buyPrice NOT BETWEEN 20 AND 100;
```

您也可以使用少于(`>`)，大于(`>`)和逻辑运算符(`AND`)重写上述查询，如下所示 -

```sql
SELECT 
    productCode, productName, buyPrice
FROM
    products
WHERE
    buyPrice < 20 OR buyPrice > 100;
```

执行上面查询语句，得到以下结果 -

```sql
SELECT 
    productCode, productName, buyPrice
FROM
    products
WHERE
    buyPrice < 20 OR buyPrice > 100;
```

## MySQL BETWEEN与日期类型数据示例

当使用`BETWEEN`运算符与日期类型值时，要获得最佳结果，应该使用类型转换将列或表达式的类型显式转换为DATE类型。

例如，要查询获取所需日期(`requiredDate`)从`2013-01-01`到`2013-01-31`的所有订单，请使用以下查询：

```sql
SELECT orderNumber,
         requiredDate,
         status
FROM orders
WHERE requireddate
    BETWEEN CAST('2013-01-01' AS DATE)
        AND CAST('2013-01-31' AS DATE);
```

因为`requiredDate`列的数据类型是`DATE`，所以我们使用转换运算符将文字字符串“`2013-01-01`”和“`2013-12-31`”转换为`DATE`数据类型。

在本教程中，您已经学会了如何使用`BETWEEN`运算符来测试值是否在值的范围内。

# MySQL 基于正则表达式的搜索(regexp)

在本教程中，您将学习如何使用MySQL `REGEXP`运算符执行基于正则表达式的复杂搜索。

## 正则表达式简介

正则表达式是描述搜索模式的特殊字符串。 它是一个强大的工具，为您提供一种简洁灵活的方法来识别基于模式的文本字符，例如字符，单词等。

例如，可以使用正则表达式来搜索电子邮件，IP地址，电话号码，社会安全号码或具有特定模式的任何内容。

正则表达式使用其可以由正则表达式处理器解释的自己的语法。 正则表达式广泛应用于从编程语言到数据库(包括MySQL)大部分平台。

使用正则表达式的优点是，不限于在[Like](./like.html)运算符中基于具有百分号(`%`)和下划线(`_`)的固定模式搜索字符串。 使用正则表达式，有更多的元字符来构造灵活的模式。

正则表达式的缩写是`regex`或`regexp`。

## MySQL REGEXP运算符

MySQL适应了[Henry Spencer](http://garyhouston.github.io/regex/)实现的正则表达式。MySQL允许使用`REGEXP`运算符在SQL语句中匹配模式。

下面说明了[WHERE子句](./where.html)中`REGEXP`运算符的语法：

```sql
SELECT 
    column_list
FROM
    table_name
WHERE
    string_column REGEXP pattern;
```

此语句执行`string_column`与模式`pattern`匹配。

如果`string_column`中的值与模式`pattern`匹配，则`WHERE`子句中的表达式将返回`1`，否则返回`0`。

如果`string_column`或`pattern`为`NULL`，则结果为`NULL`。

除了`REGEXP`运算符之外，可以使用`RLIKE`运算符，这是`REGEXP`运算符的同义词。

`REGEXP`运算符的否定形式是`NOT REGEXP`。

## MySQL REGEXP示例

**[准备环境](./setup.html)**

假设想找出名字以字母`A`，`B`或`C`开头的产品。可以使用[SELECT语句](./select.html)中的正则表达式如下：

```sql
SELECT 
    productname
FROM
    products
WHERE
    productname REGEXP '^(A|B|C)'
ORDER BY productname;
```

该模式允许查询名称以`A`，`B`或`C`开头的产品。

- 字符`^`表示从字符串的开头匹配。
- 字符`|`如果无法匹配，则搜索替代方法。

下表说明了正则表达式中一些常用的元字符和构造。

| 元字符  | 行为                             |
| ------- | -------------------------------- |
| `^`     | 匹配搜索字符串开头处的位置       |
| `$`     | 匹配搜索字符串末尾的位置         |
| `.`     | 匹配任何单个字符                 |
| `[…]`   | 匹配方括号内的任何字符           |
| `[^…]`  | 匹配方括号内未指定的任何字符     |
| `*`     | 匹配前面的字符零次或多次         |
| `+`     | 匹配前一个字符一次或多次         |
| `{n}`   | 匹配前几个字符的`n`个实例        |
| `{m,n}` | 从`m`到`n`个前一个字符的实例匹配 |

要查找名称以`a`开头的产品，您可以在名称开头使用“`^`”进行匹配，如下查询语句：

```sql
SELECT 
    productname
FROM
    products
WHERE
    productname REGEXP '^a';
```

如果要使`REGEXP`运算符以区分大小写的方式比较字符串，可以使用`BINARY`运算符将字符串转换为二进制字符串。

因为MySQL比较二进制字节逐字节而不是逐字符。 这允许字符串比较区分大小写。

例如，以下语句只匹配开头为大写“`C`”的产品名称。

```sql
SELECT 
    productname
FROM
    products
WHERE
    productname REGEXP BINARY '^C';
```

要找到以`f`结尾的产品，您可以使用’`$f`‘来匹配字符串的末尾。

```sql
SELECT 
    productname
FROM
    products
WHERE
    productname REGEXP 'f$';
```

要查找其名称包含“`ford`”的产品，请使用以下查询：

```sql
SELECT 
    productname
FROM
    products
WHERE
    productname REGEXP 'ford';
```

要查找名称只包含`10`个字符的产品，可以使用’`^`‘和’`$`‘来匹配产品名称的开头和结尾，并重复`{10}`次任何字符`.`，作为以下查询：

```sql
SELECT 
    productname
FROM
    products
WHERE
    productname REGEXP '^.{10}$';
```

在本教程中，您已学习如何使用具有正则表达式的MySQL `REGEXP`运算符查询数据。
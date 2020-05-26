# MySQL 自然语言全文搜索

在本教程中，您将通过使用`MATCH()`和`AGAINST()`函数来了解MySQL自然语言全文搜索。

在自然语言全文搜索中，MySQL查找与自由文本自然人类语言查询相关的行或文档，例如“如何使用MySQL自然语言全文搜索”。

相关性是一个正浮点数。 当相关性为零时，这意味着没有相似性。MySQL根据各种因素计算相关性，包括文档中的字数，文档中的唯一字数，集合中的单词总数以及包含特定单词的文档数(行)。

要执行自然语言全文搜索，您可以使用`MATCH()`和`AGAINST()`函数。 `MATCH()`函数指定要搜索的列，`AGAINST()`函数确定要使用的搜索表达式。

## MySQL自然语言全文搜索示例

**[准备环境](./setup.html)**

我们将使用示例数据库中的`products`表进行演示。

```sql
desc products;
```

*首先*，需要使用`ALTER TABLE ADD FULLTEXT`语句在`products`表的`productLine`列中启用全文搜索：

```sql
ALTER TABLE products 
ADD FULLTEXT(productline);
```

*其次*，可以搜索产品系列包含`Classic`的产品，使用`MATCH()`和`AGAINST()`函数，如下查询：

```sql
SELECT productName, productline
FROM products
WHERE MATCH(productline) AGAINST('Classic');
```

`AGAINST()`函数默认使用`IN NATURAL LANGUAGE MODE`搜索修饰符，因此您可以在查询中省略它。还有其他搜索修饰符，例如`IN BOOLEAN MODE`用于布尔文本搜索。

可以在查询中显式使用`IN NATURAL LANGUAGE MODE`搜索修饰符，如下所示：

```sql
SELECT productName, productline
FROM products
WHERE MATCH(productline) 
AGAINST('Classic,Vintage' IN NATURAL LANGUAGE MODE);
```

默认情况下，MySQL以不区分大小写的方式执行搜索。但是，您可以指示MySQL使用二进制排序规则对索引列进行区分大小写搜索。

**按相关性排序结果集**

全文搜索的一个非常重要的特征是MySQL根据其相关性对结果集中的行进行排序。 当[WHERE](./where.html)子句中使用`MATCH()`函数时，MySQL返回首先更相关的行。

以下示例显示了MySQL如何根据相关性对结果集进行排序。

*首先*，可以为`products`表的`productName`列启用全文搜索功能。

```sql
ALTER TABLE products 
ADD FULLTEXT(productName);
```

*其次*，使用以下查询搜索名称包`Ford`和/或`1932`的产品：

```sql
SELECT productName, productline
FROM products
WHERE MATCH(productName) AGAINST('1932,Ford');
```

首先返回其名称包含`1932`和`Ford`的产品，然后返回名称包含唯一`Ford`关键字的产品。

使用全文搜索时，应该记住一些重点：

- MySQL全文搜索引擎中定义的搜索项的最小长度为`4`，这意味着如果搜索长度小于`4`的关键字，例如`car`，`cat`等，则不会得到任何结果。
- 停止词被忽略，MySQL定义了MySQL源代码分发`storage/myisam/ft_static.c`中的停止词列表。

在本教程中，向您展示了如何使用`MATCH()`和`AGAINST()`函数在MySQL中执行自然语言搜索。
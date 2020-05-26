# MySQL Order By自然排序

在本教程中，您将使用`ORDER BY`子句了解MySQL中的各种自然排序技术。

下面让我们使用一个示例数据来开始学习自然排序技术。

假设我们有一个`items`的表，其中包含两列：`id`和`item_no`。使用以下[CREATE TABLE语句](./table-create.html)创建`items`表，如下：

```sql
CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    item_no VARCHAR(255) NOT NULL
);
```

我们使用[INSERT](./insert.html)语句将一些数据插入到`items`表中：

```sql
INSERT INTO items(item_no)
VALUES ('1'),
       ('1C'),
       ('10Z'),
       ('2A'),
       ('2'),
       ('3C'),
       ('20D');
```

当我们查询选择数据并按`item_no`排序时，不是我们的预期的结果，我们想要看到的结果如下：

```sql
+---------+
| item_no |
+---------+
| 1       |
| 1C     |
| 2      |
| 2A       |
| 3C     |
| 10Z      |
| 20D      |
+---------+
```

这被称为自然排序。不幸的是，MySQL不提供任何内置的自然排序语法或函数。 [ORDER BY](./orderby.html)子句以线性方式排序字符串，即从第一个字符开始的每个字符一次。

为了克服这个问题，首先我们将`item_no`列分成两列：`prefix` 和 `suffix`。 `prefix`列存储`item_no`的数字部分，`suffix`列存储字母部分。然后根据这些列对数据进行排序，如下所示：

```sql
SELECT 
    CONCAT(prefix, suffix)
FROM
    items
ORDER BY prefix , suffix;
```

查询首先对数据进行数字排序，并按字母顺序对数据进行排序。我们就得到预期的结果。

这个解决方案的缺点是必须在插入或更新之前将`item_no`值分成两部分。 此外，当查询数据时，必须将这两列组合成一列。

如果`item_no`数据格式相当标准，则可以使用以下查询执行自然排序，而无需更改表的结构。

```sql
SELECT 
    item_no
FROM
    items
ORDER BY CAST(item_no AS UNSIGNED) , item_no;
```

在这个查询中，首先使用[类型转换](./cast.html)将`item_no`数据转换为无符号整数。 其次，使用`ORDER BY`子句对数字进行数字排序，然后按字母顺序排列。

下面来看看经常要处理的另一个常见的数据。

```sql
TRUNCATE TABLE items;

INSERT INTO items(item_no)
VALUES('A-1'),
      ('A-2'),
      ('A-3'),
      ('A-4'),
      ('A-5'),
      ('A-10'),
      ('A-11'),
      ('A-20'),
      ('A-30');
```

排序后的预期结果如下：

![img](D:\Books\books\mysql\images\orderby-nature.jpg)

为了得到上面这个结果，可以使用LENGTH函数。 请注意，LENGTH函数返回字符串的长度。 这个做法是首先对`item_no`数据进行排序，然后按列值排序，如以下查询：

```sql
SELECT 
    item_no
FROM
    items
ORDER BY LENGTH(item_no) , item_no;
```

所看到数据就是自然排序的。

但是，如果所有上述解决方案都不适合。 则需要在应用程序层执行自然排序。 一些语言支持自然排序功能，例如，PHP提供了使用自然排序算法对数组进行排序的natsort()函数。

在本教程中，我们已经演示了如何在MySQL中执行自然排序的各种技术。
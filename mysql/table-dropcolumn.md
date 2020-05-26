# MySQL 删除列

在本教程中，我们将向您展示如何使用MySQL `DROP COLUMN`语句从表中删除列。

## MySQL DROP COLUMN语句简介

在某些情况下，要从表中删除一个或多个列。 在这种情况下，可以使用[ALTER TABLE ](./table-alter.html)DROP COLUMN语句：

```sql
ALTER TABLE table
DROP COLUMN column;
```

下面让我们更详细地学习上面的语法：

- 首先，在`ALTER TABLE`子句之后，指定将要删除的列的表。
- 其次，将列的名称放在`DROP COLUMN`子句之后。

请注意，关键字`COLUMN`是可选的，因此可以使用更短语句书写形式，如下：

```sql
ALTER TABLE table
DROP column;
```

要同时从表中删除多个列，请使用以下语法：

```sql
ALTER TABLE table
DROP COLUMN column_1,
DROP COLUMN column_2,
```

在从表中删除列之前，应该要记住一些重要的事情：

- 从表中删除列会使所有数据库对象(如[存储过程](./sp.html)，[视图](./view.html)，[触发器](./trigger.html)等)依赖于列无效。 例如，您可能有一个引用列的存储过程。 删除列时，存储过程将变为无效。 要修复它，必须手动更改存储过程的代码。
- 取决于已删除列的其他应用程序的代码也必须更改，这需要时间和精力。
- 从大型表中删除列可能会影响数据库的性能。

## MySQL DROP COLUMN示例

首先，为了演示创建一个名为`posts`的表。

```sql
USE testdb;

CREATE TABLE posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    excerpt VARCHAR(400),
    content TEXT,
    created_at DATETIME,
    updated_at DATETIME
);
```

**第二**，假设要删除`excerpt`列，请使用`ALTER TABLE`语句如下：

```sql
ALTER TABLE posts
DROP COLUMN excerpt;
SQL
```

**第三**，要同时删除`created_at`和`updated_at`列，请使用以下语句：

```sql
ALTER TABLE posts
DROP COLUMN created_at,
DROP COLUMN updated_at;
```

**MySQL删除一列是外键示例**

如果您删除作为[外键](./foreignkey.html)的列，MySQL将发出错误。下面我们来一步步演示这个想法。

**首先**，创建一个名为`categories`的表：

```sql
USE testdb;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);
```

**第二**，将`categories_id`列添加到`posts`表中。

```sql
ALTER TABLE posts ADD COLUMN category_id INT NOT NULL;
```

**第三**，将`category_id`列引用`categories`表的`id`列作为外键。

```sql
ALTER TABLE posts 
ADD CONSTRAINT fk_cat 
FOREIGN KEY (category_id) 
REFERENCES categories(id) ON DELETE CASCADE;
```

**第四**，从`posts`表中删除`category_id`列。

```sql
ALTER TABLE posts
DROP COLUMN category_id;
```

MySQL发出错误消息：

为避免此错误，必须删除外键约束才能删除该列。

在本教程中，我们向您展示了如何使用MySQL `DROP COLUMN`语句从表中删除一个或多个列。
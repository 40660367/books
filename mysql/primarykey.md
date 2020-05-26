# MySQL 主键(Primary Key)		

MySQL主键(*Primary Key*)是唯一标识表中每行的列或一组列。当定义表的主键时，必须遵循以下规则：

- 主键必须包含唯一值。如果主键由多个列组成，则这些列中的值的组合必须是唯一的。
- 主键列不能包含`NULL`值。 这意味着必须使用`NOT NULL`属性声明主键列。如果没有指定`NOT NULL`，MySQL将强制为主键列为`NOT NULL`。
- 一张表只有一个主键。

因为MySQL使用整数工作更快，所以主键列的[数据类型](./datatype.html)应该是整数类型，例如：`INT`，`BIGINT`。可以选择一个较小的整数类型：`TINYINT`，`SMALLINT`等。但是，应该确保值的范围的主键的整数类型足以存储表可能所具有最大行数。

主键列通常具有自动生成键的唯一序列的`AUTO_INCREMENT`属性。下一行的主键值大于前一个行的主键值。

MySQL为表中的主键创建一个名为`PRIMARY`的`PRIMARY`索引类型。

## 定义MySQL主键约束

MySQL允许通过在创建或修改表时定义主键约束来创建主键。

**使用CREATE TABLE语句定义MySQL PRIMARY KEY约束**

当使用[CREATE TABLE](./table-create.html)语句创建表时，MySQL允许创建主键。要为表创建`PRIMARY KEY`约束，请在主键列的定义中指定`PRIMARY KEY`。

以下示例将为`users`表的`user_id`列上创建主键：

```sql
CREATE DATABASE testdb;
USE testdb;

CREATE TABLE users(
   user_id INT AUTO_INCREMENT PRIMARY KEY,
   username VARCHAR(40),
   password VARCHAR(255),
   email VARCHAR(255)
);
```

还可以在`CREATE TABLE`语句的末尾指定`PRIMARY KEY`，如下所示：

```sql
USE testdb;

CREATE TABLE roles(
   role_id INT AUTO_INCREMENT,
   role_name VARCHAR(50),
   PRIMARY KEY(role_id)
);
```

如果主键由多个列组成，则必须在`CREATE TABLE`语句的末尾指定它们。在`PRIMARY KEY`关键字之后，将逗号分隔的主键列的列表在括号内。

```sql
CREATE TABLE userroles(
   user_id INT NOT NULL,
   role_id INT NOT NULL,
   PRIMARY KEY(user_id,role_id),
   FOREIGN KEY(user_id) REFERENCES users(user_id),
   FOREIGN KEY(role_id) REFERENCES roles(role_id)
);
```

除了创建由`user_id`和`role_id`列组成的主键之外，该语句还创建了两个[外键约束](foreignkey.html)。

**使用ALTER TABLE语句定义MySQL PRIMARY KEY约束**

如果表由于某些原因没有主键，可以使用[ALTER TABLE](./table-alter.html)语句将具有所有主键的列添加到主键中，如下语句：

```sql
ALTER TABLE table_name
ADD PRIMARY KEY(primary_key_column);
```

以下示例将`id`列添加到主键。
**首先**，创建`t1`表但不定义主键。

```sql
CREATE TABLE t1(
   id int,
   title varchar(255) NOT NULL
);
```

**其次**，将`id`列作为`t1`表的主键。

```sql
ALTER TABLE t1
ADD PRIMARY KEY(id);
```

## PRIMARY KEY与UNIQUE KEY对比

`KEY`是`INDEX`的同义词。当要为列创建[索引](./indexing.html)，但不是主键或唯一键时使用`KEY`。

`UNIQUE`索引为其值必须是唯一的列创建约束。与`PRIMARY`索引不同，MySQL在`UNIQUE`索引中允许有`NULL`值。 一个表也可以有多个`UNIQUE`索引。

例如，`users`表中的用户的`email`和`username`必须是唯一的。可以为`email`和`username`列定义UNIQUE索引，如下语句所示：

在`username`列上添加`UNIQUE`索引。

```sql
ALTER TABLE users
ADD UNIQUE INDEX username_unique (username ASC) ;
```

在`email`列上添加`UNIQUE`索引。

```sql
ALTER TABLE users
ADD UNIQUE INDEX  email_unique (email ASC) ;
```

在本教程中，您已经学习了如何为新表创建主键或为现有表添加主键。
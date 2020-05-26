# MySQL truncate table语句

在本教程中，您将学习如何使用MySQL `TRUNCATE TABLE`语句删除表中的所有数据。

## MySQL TRUNCATE TABLE语句简介

MySQL `TRUNCATE TABLE`语句允许您删除表中的所有数据。 因此，在功能方面，`TRUNCATE TABLE`语句就像没有[WHERE子句](./where.html)的[DELETE](./delete.html)语句。 但是，在某些情况下，MySQL `TRUNCATE TABLE`语句比`DELETE`语句更有效。

MySQL `TRUNCATE TABLE`语句的语法如下：

```sql
TRUNCATE TABLE table_name;
```

在`TRUNCATE TABLE`子句后面指定要删除所有数据的表名称。

`TABLE`关键字是可选的。 但是，应该使用它来区分`TRUNCATE TABLE`语句和`TRUNCATE`函数。

如果您使用InnoDB表，MySQL将在删除数据之前检查表中是否有可用的外键约束。 以下是一些情况：

- 如果表具有任何外键约束，则`TRUNCATE TABLE`语句会逐个删除行。如果外键约束具有`DELETE CASCADE`动作，则子表中的相应行也将被删除。
- 如果外键约束没有指定[DELETE CASCADE](./on-delete-cascade.html)动作，则`TRUNCATE TABLE`将逐个删除行，并且遇到由子表中的行引用的行时，它将停止并发出错误。
- 如果表没有任何外键约束，则`TRUNCATE TABLE`语句将删除该表并重新创建一个具有相同结构的新表，这比使用`DELETE`语句特别是对于大表更快更有效。

如果您使用其他存储引擎，则`TRUNCATE TABLE`语句将删除并重新创建一个新表。

> 请注意，如果表具有`AUTO_INCREMENT`列，则`TRUNCATE TABLE`语句将自动递增值重置为零

此外，`TRUNCATE TABLE`语句不使用`DELETE`语句，因此与表关联的[DELETE触发器](./trigger.html)将不被调用。

## MySQL TRUNCATE TABLE示例

首先，创建一个名为`books`的新表：

```sql
CREATE DATABASE IF NOT EXISTS testdb;

USE testdb;

CREATE TABLE books(
 id int auto_increment primary key,
        title varchar(255) not null
)ENGINE=InnoDB;
```

接下来，使用以下存储过程填充`books`表的数据：

```sql
DELIMITER $$

CREATE PROCEDURE load_book_data(IN num int(10))
BEGIN
 DECLARE counter int(10) default 0;
 DECLARE book_title varchar(255) default '';

 WHILE counter < num DO
   SET book_title = concat('Book title #',counter);
   SET counter = counter + 1;

   INSERT INTO books(title) VALUES(book_title);
 END WHILE;
END$$

DELIMITER ;
```

然后，将`10,000`行数据插入到`books`表，执行上面语句将需要一段时间。

```sql
CALL load_book_data(10000);
```

执行上面语句之后，查看`books`表中的数据：

```sql
SELECT * FROM books;
```

最后，使用`TRUNCATE TABLE`语句来与`DELETE`语句相比执行的速度。

```sql
select now() as start_time;
TRUNCATE TABLE books;
select now() as end_time;
```

可以看到整个过程也就差不多 `1` 秒钟完成，下面再次调用`CALL load_book_data(10000);`，完成插入数据后使用`DELETE`语句，查看执行的时间 - 

```sql
select now() as start_time;
DELETE FROM books;
select now() as end_time;
```

在本教程中，我们向您展示了如何使用MySQL `TRUNCATE TABLE`语句从表中有效地删除所有数据，特别是对于拥有大量数据的表。
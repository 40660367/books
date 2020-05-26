# MySQL 字符集与排序规则

在本教程中，您将了解MySQL中的字符集。 在本教程之后，您将了解如何获取MySQL中的所有字符集，如何在字符集之间转换字符串以及如何为客户端连接配置正确的字符集。了解MySQL排序规则以及如何设置MySQL服务器，数据库，表和列的字符集和排序规则。

## MySQL字符集简介

MySQL字符集是一组在字符串中合法的字符。 例如，我们有一个从`a`到`z`的字母。要为每个字母分配一个数字，例如`a = 1`，`b = 2`等。字母`a`是一个符号，数字`1`与字母`a`相关联就是一种编码。 从`a`到`z`的所有字母和它们相应的编码的组合是一个字符集。

每个字符集具有一个或多个排序规则，其定义用于比较字符集中的字符的一组规则。 

MySQL支持各种字符集，允许您几乎可将每个字符存储在字符串中。 要获取MySQL数据库服务器中的所有可用字符集，请使用`SHOW CHARACTER SET`语句如下：

```sql
SHOW CHARACTER SET;
```

MySQL中的默认字符集是`latin1`。如果要在单列中存储多种语言的字符，可以使用`Unicode`字符集，即`utf8`或`ucs2`。

`Maxlen`列中的值指定字符集中的字符持有的字节数。一些字符集包含单字节字符，例如：`latin1`，`latin2`，`cp850`等，而其他字符集包含多字节字符。

MySQL提供了`LENGTH`函数来获取字节的长度，以字节为单位，`CHAR_LENGTH`函数用于获取字符串的长度。如果字符串包含多字节字符，则`LENGTH`函数的结果大于`CHAR_LENGTH()`函数的结果。 请参阅以下示例：

```sql
SET @str = CONVERT('我的MySQL' USING ucs2);

SELECT LENGTH(@str), CHAR_LENGTH(@str);
```

`CONVERT`函数将字符串转换为指定的字符集。在这个例子中，它将MySQL字符集字符串的字符集转换为`ucs2`。 因为`ucs2`字符集包含`2`个字节的字符，因此`@str`字符串的长度(以字节为单位)大于其字符长度。

请注意，某些字符集包含多字节字符，但其字符串可能只包含单字节字符，例如`utf8`，如以下语句所示：

```sql
SET @str = CONVERT('MySQL Character Set' USING utf8);
SELECT LENGTH(@str), CHAR_LENGTH(@str);
```



但是，如果`utf8`字符串包含特殊字符，例如`ü`在`pingüino`字符串中; 其字节长度不同，请参见以下示例：

```sql
SET @str = CONVERT('pingüino' USING utf8);
SELECT LENGTH(@str), CHAR_LENGTH(@str);
```

一个使用中文的示例 - 

```sql
SET @str = CONVERT('中文示例' USING utf8);
SELECT LENGTH(@str), CHAR_LENGTH(@str);
SQL
```

在使用`utf8`字符集编码时，中文字占`3`个长度。

## 转换不同的字符集

MySQL提供了两个函数，允许您在不同字符集之间转换字符串：`CONVERT`和`CAST`。 在上面的例子中，我们多次使用了`CONVERT`函数。

**`CONVERT`函数的语法如下：**

```sql
CONVERT(expression USING character_set_name)
```

CAST函数类似于`CONVERT`函数。它将字符串转换为不同的字符集：

```sql
CAST(string AS character_type CHARACTER SET character_set_name)
```

看一下使用`CAST`函数的以下示例：

```sql
SELECT CAST(_latin1'MySQL character set' AS CHAR CHARACTER SET utf8);
```



## MySQL排序规则简介

MySQL排序规则是用于比较特定字符集中的字符的一组规则。 MySQL中的每个字符集可以有多个排序规则，并且至少具有一个默认排序规则。两个字符集不能具有相同的归类。

MySQL提供了`SHOW CHARACTER SET`语句，查看字符集的默认排序规则。

默认排序规则列的值指定字符集的默认排序规则。

按照惯例，字符集的排序规则以字符集名称开头，以`_ci`(不区分大小写)`_cs`(区分大小写)或`_bin`(二进制文件)结尾。

要获取给定字符集的所有排序规则，请使用`SHOW COLLATION`语句如下：

```sql
SHOW COLLATION LIKE 'character_set_name%';
```

例如，要获取`latin1`字符集的所有排序规则，请使用以下语句：

```sql
SHOW COLLATION LIKE 'latin1%';
```

执行上面语句，得到用于`latin1`字符集的MySQL排序规则，如下结果 - 

```sql
SHOW COLLATION LIKE 'latin1%';
```

如上所述，每个字符集都具有默认排序规则，例如`latin1_swedish_ci`是`latin1`字符集的默认排序规则。

## 设置字符集和排序规则

MySQL允许您在四个级别指定字符集和排序规则：服务器，数据库，表和列。

**在服务器级别设置字符集和排序规则**

注意MySQL使用`latin1`作为默认字符集，因此，其默认排序规则为`latin1_swedish_ci`。 您可以在服务器启动时更改这些设置。

如果在服务器启动时仅指定一个字符集，MySQL将使用字符集的默认排序规则。 如果您明确指定了一个字符集和排序规则，MySQL将使用数据库服务器中的字符集和排序规则来创建的所有数据库。

以下语句通过命令行启动并设置服务器使用`utf8`字符集和`utf8_unicode_cs`排序规则：

```bash
mysqld --character-set-server=utf8 --collation-server=utf8_unicode_ci
```

**在数据库级别设置字符集和排序规则**

创建数据库时，如果不指定其字符集和排序规则，MySQL将使用数据库的服务器的默认字符集和排序规则。

可以使用CREATE DATABASE或ALTER DATABASE语句来覆盖数据库级的默认设置，如下所示：

```sql
CREATE DATABASE database_name
CHARACTER SET character_set_name
COLLATE collation_name

-- 修改排序规则
ALTER  DATABASE database_name
CHARACTER SET character_set_name
COLLATE collation_name
```

MySQL在数据库级使用数据库中创建的所有表的字符集和排序规则。

**在表级别设置字符集和排序规则**

数据库可能包含与默认数据库的字符集和排序规则不同的字符集和排序规则的表。

当您通过使用`CREATE TABLE`语句创建表或使用`ALTER TABLE`语句更改表的结构时，可以指定表的默认字符集和排序规则。

```sql
CREATE TABLE table_name(
)
CHARACTER SET character_set_name
COLLATE collation_name
```

**在列级别设置字符集和排序规则**

`CHAR`，`VARCHAR`或`TEXT`类型的列可以使用与表的默认字符集和排序规则不同的，自己指定的字符集和排序规则。

可以按照`CREATE TABLE`或`ALTER TABLE`语句的列定义中的列指定字符集和排序规则，如下所示：

```sql
column_name [CHAR | VARCHAR | TEXT] (length)
CHARACTER SET character_set_name
COLLATE collation_name
```

以下是设置字符集和排序规则的规则：

- 如果显式指定字符集和排序规则，则使用字符集和排序规则。
- 如果指定一个字符集并忽略排序规则，则使用字符集的默认排序规则。
- 如果指定没有字符集的排序规则，则使用与排序规则相关联的字符集。
- 如果省略字符集和排序规则，则使用默认字符集和排序规则。

我们来看一些设置字符集和排序规则的例子。

## 设置字符集和排序规则的示例

**首先**，我们使用`utf8`作为字符集创建一个新数据库，将`utf8_unicode_ci`作为默认排序规则：

```sql
CREATE DATABASE mydbdemo
CHARACTER SET utf8
COLLATE utf8_unicode_ci;
```

因为明确指定`mydbdemo`数据库的字符集和排序规则，所以`mydbdemo`数据库不会在服务器级别采用默认字符集和排序规则。

**其次**，我们在`mydbdemo`数据库中创建一个名为`t1`的新表，但不指定字符集和排序规则：

```sql
USE mydbdemo; 
CREATE TABLE t1(
    c1 char(25)
);
```

如上所示，我们并没有为`t1`表指定字符集和排序规则; MySQL将检查数据库级别以确定`t1`表的字符集和排序规则。 在这种情况下，`t1`表将使用`utf8`作为默认字符集，`utf8_unicode_ci`作为默认排序规则。

**第三**，对于`t1`表，我们将其字符集更改为`latin1`，并将其排序规则改为`latin1_german1_ci`：

```sql
ALTER TABLE t1
CHARACTER SET latin1
COLLATE latin1_german1_ci;
```

`t1`表中的`c1`列使用`latin1`作为字符集，`latin1_german1_ci`作为排序规则。

**第四**，将`c1`列的字符集更改为`latin1`：

```sql
ALTER TABLE t2
MODIFY c1 VARCHAR(25)
CHARACTER SET latin1;
```

现在，`c1`列使用`latin1`字符集，但是它的排序规则呢？ 是否从表的排序规则继承了`latin1_german1_ci`排序规则？ 不是的，因为`latin1`字符集的默认排序规则是`latin1_swedish_ci`，所以`c1`列具有`latin1_swedish_ci`排序规则。

在本教程中，您已经了解了MySQL排序规则以及如何为MySQL服务器，数据库，表和列指定字符集和排序规则。
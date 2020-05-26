# MySQL 创建用户

在本教程中，您将学习如何使用MySQL的`CREATE USER`语句在MySQL中创建一个用户帐户。

## MySQL中的用户帐户简介

在MySQL中，不仅可以指定谁可以连接到数据库服务器，还可以指定用户连接的主机。因此，MySQL中的用户帐号由用户名，以及使用`@`字符分隔的主机名组成。

例如，如果`admin`用户从`localhost`主机连接到MySQL数据库服务器，则用户帐户是书写形式是：`admin@localhost`，其中`@`符号是一个固定的分隔符。

`admin`用户只能从本地主机(`localhost`)连接到MySQL数据库服务器，而不是远程主机这使得MySQL数据库服务器更加安全。

> 注意：如要限制`admin`用户只能从`mysql.com`主机登录，那么可以书写为：`admin@mysql.com` ， 如果想要允许从任意主机登录，那么可以书写为：`admin@%`。

此外，通过组合用户名和主机，可以设置多个具有相同名称的帐户，但可以从具有不同权限的不同主机进行连接。

MySQL将用户帐户授权存储在`mysql`数据库的`user`表中。

## 使用MySQL CREATE USER语句创建用户帐户

MySQL提供了`CREATE USER`语句，允许您创建一个新的用户帐户。 `CREATE USER`语句的语法如下：

```sql
CREATE USER user_account IDENTIFIED BY password;
```

用户帐号(`user_account`)是以`username@hostname`格式跟在`CREATE USER`子句之后。

密码(`password`)在`IDENTIFIED BY`子句中指定。`password`必须是明文。 在将用户帐户保存到用户表之前，MySQL将加密明文密码。

例如，要创建一个新的用户`dbadmin`，这个用户只允许从`localhost`主机并使用密码为`pwd123`连接到MySQL数据库服务器，使用`CREATE USER`语句，如下所示：

```sql
CREATE USER dbadmin@localhost 
IDENTIFIED BY 'pwd123';
```

如果用户`dbadmin`还可以从IP为`192.168.1.100`的主机连接到MySQL数据库服务器，使用`CREATE USER`语句，如下所示：

```sql
CREATE USER dbadmin@192.168.1.100 
IDENTIFIED BY 'pwd123';
```

要查看用户帐户的权限，请使用`SHOW GRANTS`语句，如下所示：

```sql
SHOW GRANTS FOR dbadmin@localhost;
```

执行上面查询语句，得到以下结果 - 

```sql
SHOW GRANTS FOR dbadmin@localhost;
```

上面结果中的`*.*`显示`dbadmin`用户帐户只能登录到数据库服务器，没有其他权限。 要授予用户权限，您可以使用[GRANT语句](./grant.html)。

请注意，点(`.`)之前的部分表示数据库，点(`.`)后面的部分表示表，例如`database.table`，`testdb.offices`等等。

要允许用户帐户从任何主机连接，请使用百分比(`%`)通配符，如以下示例所示：

```
CREATE USER superadmin@'%' IDENTIFIED BY 'mypassword';
```

百分比通配符`%`与[LIKE](./like.html)运算符中使用的效果相同，例如，要允许`mysqladmin`用户帐户从`mysql.com`主机的任何子域连接到数据库服务器，请使用百分比通配符`%`，如下所示：

```sql
CREATE USER mysqladmin@'%.mysql.com'
IDENTIFIED by 'mypassword';
SQL
```

> 请注意，也可以在`CREATE USER`语句中使用下划线通配符`_`。

如果您省略了用户帐户的主机名部分，MySQL也会接受它，并允许用户从任何主机进行连接。 例如，以下语句创建一个名为`remote_user`的新用户帐户，可以从任何主机连接到数据库服务器：

```sql
CREATE USER remote_user;
SQL
```

可以看到授予远程用户帐户(`remote_user`)的权限如下：

```sql
SHOW GRANTS FOR remote_user;
```

执行上面查询语句，得到以下结果 - 

```sql
SHOW GRANTS FOR remote_user;
```

要注意，引用是非常重要的，特别是当用户帐户包含特殊字符(如`_`或`%`)时。

如果您不小心引用`"username@hostname"`这样的用户帐户，MySQL将创建一个`username@hostname`的用户，并允许用户从任何主机进行连接，这可能不是您预期的。

例如，以下语句创建可以从任何主机连接到MySQL数据库服务器的新用户`api@localhost`(这是用户名，并非用户账号)。

```sql
-- 常用创建用户为：CREATE USER api@'localhost' 与下面语句不同 -
CREATE USER 'api@localhost';
```

查看上面创建的用户的权限 - 

```sql
HOW GRANTS FOR 'api@localhost';
```

如果创建一个已经存在的用户，MySQL会发出一个错误。 例如，以下语句创建一个名为`remote_user`的用户帐户已经存在：

```sql
CREATE USER remote_user;
```

上面语句执行后，MySQL发出以下错误信息：

```sql
1396 - Operation CREATE USER failed for 'remote_user'@'%'
```

请注意，`CREATE USER`语句只是创建一个没有任何权限的新用户帐户。如果要[向用户授予使用权限](./grant.html)，则使用`GRANT`语句。
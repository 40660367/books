# MySQL Grant语句

在本教程中，您将学习如何使用MySQL中的`GRANT`语句向MySQL用户授予权限。

## MySQL GRANT语句简介

[创建新的用户帐户](./user-create.html)后，用户没有任何权限。如要向用户帐户授予权限，请使用`GRANT`语句。

下面说明`GRANT`语句的语法：

```sql
GRANT privilege,[privilege],.. ON privilege_level 
TO user [IDENTIFIED BY password]
[REQUIRE tsl_option]
[WITH [GRANT_OPTION | resource_option]];
```

下面让我们来详细地看看`GRANT`语句 - 

- *首先*，在`GRANT`关键字之后指定一个或多个特权。如果要授予用户多个权限，则每个权限都将以逗号分隔(见下表中的特权列表)。
- *接下来*，指定确定特权应用级别的`privilege_level`。MySQL支持全局(`*.*`)，数据库(`database.*`)，表(`database.table`)和列级别。 如果您使用列权限级别，则必须在每个权限之后使用逗号分隔列的列表。
- *然后*，放置要授予权限的用户。如果用户已经存在，则`GRANT`语句修改其特权。如不存在，则`GRANT`语句将创建一个新用户。可选的条件`IDENTIFIED BY`允许为用户设置新密码。
- *之后*，可指定用户是否必须通过安全连接(如`SSL`，`X059`等)连接到数据库服务器。
- *最后*，可选的`WITH GRANT OPTION`子句允许此用户授予其他用户或从其他用户删除您拥有的权限。此外，可以使用`WITH`子句来分配MySQL数据库服务器的资源，例如，设置用户每小时可以使用多少个连接或语句。这在MySQL共享托管等共享环境中非常有用。

请注意，要使用`GRANT`语句，您必须具有[GRANT OPTION](http://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_grant-option)权限和您授予其它用户的权限。 如果启用了[read_only](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_read_only)系统变量，则需要具有[SUPER](http://dev.mysql.com/doc/refman/5.7/en/privileges-provided.html#priv_super)权限才能执行`GRANT`语句授权。

我们来练习一些使用MySQL中的`GRANT`语句的例子来更好的理解。

## MySQL GRANT示例

通常，我们首先使用`CREATE USER`语句创建新的用户帐户，然后再使用`GRANT`语句向用户授予权限。

例如，以下`CREATE USER`语句创建一个新的超级用户帐户。

```sql
CREATE USER super@localhost IDENTIFIED BY 'newpasswd';
```

要查看已分配给`super@localhost`用户帐户的权限，请使用`SHOW GRANTS`语句。

```sql
SHOW GRANTS FOR super@localhost;
```

上面代码执行结果如下 - 

```sql
SHOW GRANTS FOR super@localhost;
```

要向`super@localhost`用户帐户授予所有权限，请使用以下语句。

```sql
GRANT ALL ON *.* TO 'super'@'localhost' WITH GRANT OPTION;
```

`ON *.*`子句表示MySQL中的所有数据库和所有对象。`WITH GRANT OPTION`允许`super@localhost`向其他用户授予权限。

现在，如果再次执行`SHOW GRANTS FOR super@localhost`语句，您将看到`super@localhost`的权限已被更新。

```sql
SHOW GRANTS FOR super@localhost;
SQL
```

执行上面查询语句，得到以下结果 - 

```sql
HOW GRANTS FOR super@localhost;
```

要创建一个用户:`auditor`，并所有示例数据库中的所有权限，请使用以下语句：

```sql
CREATE USER auditor@localhost IDENTIFIED BY 'newpasswd';
GRANT ALL ON classicmodels.* TO auditor@localhost;
```

您可以在单个`GRANT`语句中授予多个权限。 例如，创建一个针对示例数据classicmodels库执行[SELECT](./select.html)，[INSERT](./insert.html)和[UPDATE](./update.html)语句的权限的用户，如下语句：

```sql
CREATE USER rfc IDENTIFIED BY 'mypasswd';
GRANT SELECT, UPDATE, DELETE ON classicmodels.* TO rfc;
```

现在，如果您使用`rfc`用户帐户登录到MySQL服务器并发出以下查询语句：

```sql
CREATE TABLE city(
   id INT PRIMARY KEY AUTO_INCREMENT, 
   name VARCHAR(255)
);
```

MySQL将发出错误信息.

## GRANT允许的特权

下表说明了可用于`GRANT`和`REVOKE`语句的所有可用权限：

| 权限                      | 含义                                                         | 全局 | 数据库 | 表   | 列   | 过程 | 代理 |
| ------------------------- | ------------------------------------------------------------ | ---- | ------ | ---- | ---- | ---- | ---- |
| `ALL [PRIVILEGES]`        | 授予除了`GRANT OPTION`之外的指定访问级别的所有权限           |      |        |      |      |      |      |
| `ALTER`                   | 允许用户使用`ALTER TABLE`语句                                | x    | x      | x    |      |      |      |
| `ALTER ROUTINE`           | 允许用户更改或删除存储程序                                   | x    | x      |      |      | x    |      |
| `CREATE`                  | 允许用户创建数据库和表                                       | x    | x      | x    |      |      |      |
| `CREATE ROUTINE`          | x                                                            | x    |        |      |      |      |      |
| `CREATE TABLESPACE`       | 允许用户创建，更改或删除表空间和日志文件组                   | x    |        |      |      |      |      |
| `CREATE TEMPORARY TABLES` | 允许用户使用`CREATE TEMPORARY TABLE`创建临时表               | x    | x      |      |      |      |      |
| `CREATE USER`             | 允许用户使用`CREATE USER`，`DROP USER`，`RENAME USER`和`REVOKE ALL PRIVILEGES`语句。 | x    |        |      |      |      |      |
| `CREATE VIEW`             | 允许用户创建或修改视图                                       | x    | x      | x    |      |      |      |
| `DELETE`                  | 允许用户使用`DELETE`                                         | x    | x      | x    |      |      |      |
| `DROP`                    | 允许用户删除数据库，表和视图                                 | x    | x      | x    |      |      |      |
| `EVENT`                   | 能够使用事件计划的事件                                       | x    | x      |      |      |      |      |
| `EXECUTE`                 | 允许用户执行存储过程/存储函数                                | x    | x      |      |      |      |      |
| `FILE`                    | 允许用户读取数据库目录中的任何文件                           | x    |        |      |      |      |      |
| `GRANT OPTION`            | 允许用户有权授予或撤销其他帐户的权限                         | x    | x      | x    |      | x    | x    |
| `INDEX`                   | 允许用户创建或删除索引                                       | x    | x      | x    |      |      |      |
| `INSERT`                  | 允许用户使用`INSERT`语句                                     | x    | x      | x    | x    |      |      |
| `LOCK TABLES`             | 允许用户在具有`SELECT`权限的表上使用`LOCK TABLES`            | x    | x      |      |      |      |      |
| `PROCESS`                 | 允许用户使用`SHOW PROCESSLIST`语句查看所有进程               | x    |        |      |      |      |      |
| `PROXY`                   | 启用用户代理                                                 |      |        |      |      |      |      |
| `REFERENCES`              | 允许用户创建外键                                             | x    | x      | x    | x    |      |      |
| `RELOAD`                  | 允许用户使用`FLUSH`操作                                      | x    |        |      |      |      |      |
| `REPLICATION CLIENT`      | 允许用户查询主服务器或从服务器的位置                         | x    |        |      |      |      |      |
| `REPLICATION SLAVE`       | 允许用户使用复制从站从主机读取二进制日志事件                 | x    |        |      |      |      |      |
| `SELECT`                  | 允许用户使用`SELECT`语句                                     | x    | x      | x    | x    |      |      |
| `SHOW DATABASES`          | 允许用户显示所有数据库                                       | x    |        |      |      |      |      |
| `SHOW VIEW`               | 允许用户使用`SHOW CREATE VIEW`语句                           | x    | x      | x    |      |      |      |
| `SHUTDOWN`                | 允许用户使用`mysqladmin shutdown`命令                        | x    |        |      |      |      |      |
| `SUPER`                   | 允许用户使用其他管理操作，如`CHANGE MASTER TO`，`KILL`，`PURGE BINARY LOGS`，`SET GLOBAL`和`mysqladmin`命令 | x    |        |      |      |      |      |
| `TRIGGER`                 | 允许用户使用`TRIGGER`操作                                    | x    | x      | x    |      |      |      |
| `UPDATE`                  | 允许用户使用`UPDATE`语句                                     | x    | x      | x    | x    |      |      |
| `USAGE`                   | 相当于“无权限”                                               |      |        |      |      |      |      |

在本教程中，您已经学会了如何使用MySQL的`GRANT`语句向用户授予权限。
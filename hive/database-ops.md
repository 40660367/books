# Hive 数据库相关操作

Hive是一种数据库技术，可以定义数据库和表来分析结构化数据。主题结构化数据分析是以表方式存储数据，并通过查询来分析。本章介绍如何创建Hive 数据库。配置单元包含一个名为 default 默认的数据库。

[环境准备](./setup.html)

## 显示数据库 show database 语句

通过`show databases`来显示已有数据库。如果想要模糊匹配，则可以用`like`关键字实现。

```hive
show databases like 'd*';
```

## 创建数据库 create database语句

创建数据库是用来创建数据库在Hive中语句。在Hive数据库是一个命名空间或表的集合。此语法声明如下：

```
CREATE DATABASE|SCHEMA [IF NOT EXISTS] <database name>
```

在这里，IF NOT EXISTS是一个可选子句，通知用户已经存在相同名称的数据库。可以使用SCHEMA 在DATABASE的这个命令。

下面的查询执行创建一个名为`userdb`数据库，并使用comment设置描述信息。

```
create database userdb comment 'userdb database with commnets'; 
```

用dfs查看/user/hive/warehouse目录，可发现多出了一个userdb的文件夹。

```
dfs -ls /user/hive/warehouse/;
```

## 描述数据库 describe database 语句

用`describe` 查看数据库描述。显示数据库描述和存放目录。

```hive
describe database userdb;
```

## 使用数据库 use database 语句

使用数据库。使用`use dbname`的语句切换到相应的数据库。

```hive
set hive.cli.print.current.db=true; 
use userdb;
```

## 删除数据库 drop database 语句

DROP DATABASE是删除所有的表并删除数据库的语句。

**它的语法如下：**

```
DROP DATABASE StatementDROP (DATABASE|SCHEMA) [IF EXISTS] database_name 
[RESTRICT|CASCADE];
```

下面的查询用于删除数据库。假设要删除的数据库名称为userdb。

```
DROP DATABASE IF EXISTS userdb;
```

但使用`drop database dbname`的方式删除时，如果当数据库存在表时会提示删除失败。

这时可以使用使用CASCADE关键字来删除数据库。这意味着要全部删除相应的表在删除数据库之前。以下使用SCHEMA查询删除数据库。

```hive
DROP DATABASE IF EXISTS userdb CASCADE;
```


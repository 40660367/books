# PostgreSQL 创建数据库

在PostgreSQL中，可以使用`CREATE DATABASE`命令创建数据库。

**语法：**

```sql
CREATE DATABASE database_name;
```

这里，`database_name`是指定要创建的数据库的名称。

## PostgreSQL使用UI创建数据库

在您的系统中安装PostgreSQL后，打开开始菜单，然后单击**pgAdmin**。会得到一个这样的页面：

打开**pgAdmin**，第一次打开可能需要你输入密码，结果如下 -

右键单击`PostgreSQL 9.6`并将PostgreSQL连接到本地主机服务器。

右键单击数据库(**Databases**)，转到新数据库，将出现一个弹出框，如下图所示 -

然后键入您要的数据库名称，这里创建的数据库名称是：**testdb**，如下图所示 -

点击保存(Save)就可以了。

## PostgreSQL使用查询工具创建数据库

打开**SQL Shell(psql)**，执行以下创建语句 -

```sql
create database testdb;
```

```sql
\l
```

或者在 **pgAdmin** 的

## 使用SQL删除数据库

```sql
drop database testdb;
```


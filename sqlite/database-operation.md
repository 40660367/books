# SQLite 数据库操作			

## 创建数据库

在SQLite中，`sqlite3`命令用于创建新的数据库。

**语法**

```sql
sqlite3 database.db
```

数据库名称(`DatabaseName.db`)在RDBMS中应该是唯一的。

> 注意：`sqlite3`命令用于创建数据库。 但是，如果数据库不存在，则将自动创建具有给定名称的新数据库文件。

**如何创建数据库：**

首先打开命令提示符并进入创建数据库的目录。之后，可以使用“`dir`”命令查看`sqlite`目录。

**示例：**

创建一个名称为`test.db`的数据库：

```sql
sqlite3 test.db
```

执行上面命令后，应该就创建了数据库。 可以使用“`.databases`”命令检查创建的数据库。

```sql
.databases
```

也可以在SQLite根文件夹中看到创建的数据库。

### 导出数据库

**.dump命令**

`.dump`命令用于在命令提示符下使用SQlite命令导出完整数据库在文本文件中。

```shell
sqlite3 test.db .dump > test.sql
```

## SQLite附加/选择数据库 			

**什么是附加数据库？**

假设有多个数据库，但是一次只能使用其中的一个。 这就要使用`ATTACH DATABASE`语句了。 它有助于您选择特定的数据库，并且在使用此命令后，所有SQLite语句将在附加/选择的数据库下执行。

**语法**

```sql
ATTACH DATABASE 'DatabaseName' As 'Alias-Name';
```

> 注意：如果数据库不存在，上述语法也将创建一个数据库，否则它只会将数据库文件名与逻辑数据库`Alias-Name`相连接。

下面来举个例子，假设已以有一个存在的数据库：`db1.db` 。

使用以下语句：

```sql
ATTACH DATABASE 'db1.db' as 'db1';
```

现在可以通过使用`.databases`命令看到数据库：

## SQLite分离数据库 			

SQLite `DETACH DATABASE`语句用于将别名命名的数据库与先前使用`ATTACH`语句附加的数据库连接进行分离。

如果同一数据库文件已附加多个别名，则`DETACH`命令将仅断开给定的名称，其余的附件仍将继续。 主数据库和临时数据库无法分离。

> **注意**：内存或临时数据库中的数据库将被完全销毁，内容将丢失。

**语法：**

```sql
DETACH DATABASE 'Alias-Name'
```

下面举个例子来演示如何分离附加的别名数据库。 在这里，假设有一个附加的数据库：“`db1`”。

从db1.db`分离“`db1`”：

```sql
DETACH DATABASE 'db1';
```

执行上面命令后，数据库就分离了。可以使用“`.databases`”命令查看数据库的情况。

```sql
.database
```


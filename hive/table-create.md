# Hive 创建内部表(create table)

本章将介绍如何创建一个表以及如何将数据插入。创造表的约定在Hive中非常类似于使用SQL创建表。

## 创建内部表

Hive中的表分为内部表（管理表）和外部表。删除内部表时，内部表的元数据和目录上的数据均被删除；删除外部表时，只删除元数据，目录上数据不被删除。内部表不适合共享数据。因为表被删除时，数据也被删除。

## 	CREATE TABLE语句

Create Table是用于在Hive中创建表的语句。语法和示例如下：

### 语法

```
CREATE [TEMPORARY] [EXTERNAL] TABLE [IF NOT EXISTS] [db_name.] table_name

[(col_name data_type [COMMENT col_comment], ...)]
[COMMENT table_comment]
[ROW FORMAT row_format]
[STORED AS file_format]
```

### 示例

假设需要使用CREATE TABLE语句创建一个名为employee表。下表列出了employee表中的字段和数据类型：

| Sr.No | 字段名称    | 数据类型 |
| ----- | ----------- | -------- |
| 1     | Eid         | int      |
| 2     | Name        | String   |
| 3     | Salary      | Float    |
| 4     | Designation | string   |

下面的数据是一个注释，行格式字段，如字段终止符，行终止符，并保存的文件类型。

```
COMMENT ’Employee details‘
FIELDS TERMINATED BY ‘\t’
LINES TERMINATED BY ‘\n’
STORED IN TEXT FILE
```

### Hive Shell方式完成

下面的查询创建使用上述数据的表名为 employeeTest1。

```
CREATE TABLE IF NOT EXISTS employeeTest1 ( eid int, name String,
salary String, destination String)
ROW FORMAT DELIMITED;
show tables;
```

如果添加选项IF NOT EXISTS，Hive 忽略大小写，万一表已经存在的声明。

### 通过导入HQL文件完成

在hive shell中，通过`source`执行创建表的语句。

```hive
source /share/lesson/hive/data-import.hql;
show tables;
```

### 通过拷贝表的方式创建表

```shell
create table if not exists employeeTest2 like employees;
show tables;
```


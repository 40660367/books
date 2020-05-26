# Hive 数据表相关操作

本章将介绍如何修改表的属性，如，修改表名，修改列名，添加列，并删除或替换列。

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

## 使用describe查看表定义

```hive
describe employees;
```

**describe extended**

通过过`extended`关键字查看表结构及描述信息。

```hive
describe extended employees;
```

**describe formatted**

通过`formatted`查看表结构及描述信息。

```hive
describe formatted employees;
```

### tblproperties

查看tblproperties。发现多出了一个transient_lastDdlTime属性。

```hive
show tblproperties employees;
```

## 修改表

### 表重命名

将表etlemlpyees修改为etl_employees。

```hql
alter table employees rename to employees1;
```

### 修改列

将employees1的列`level`修改成`loggerlevel`，添加`comment`描述，并将其调整到hms列后面。不过level本来就在hms后面，因此产生更改。

```hql
alter table employees1
change column destination dept string
comment 'Department'
after eid;
desc employees1;
```

### 添加列

通过`add columns(colname datatype, ...)`来添加列。

```hql
alter table employees1 add columns(age int,address string);
desc employees1;
```

### 修改表属性
改变表的tblproperties。之前的employees表中，定义了部分属性，下面的语句为其添加了新的属性depart。注意，属性只能添加和修改，不能删除。

```hql
alter table employees1 set tblproperties ('depart'='Cloud'); 
show tblproperties employees1; 
```

### 替换列(危险操作)

通过`replace columns(colname datatype, ...)`来实现。()中定义的新列会替代原表结构中除了分区列之外的所有列。如下所示，原本的列都被删除，仅有一个新列一个`name string`。

```hql
alter table employees1 replace columns (name string);
desc employees1;
```

## 删除表(危险操作)

删除内部表employees表。元数据和表中数据都被删除。

```hive> 
drop table if exists employees1;
show tables;
```

# SQLite 表格操作 			

## SQLite 创建表

在SQLite中，`CREATE TABLE`语句用于创建新表。 在创建表时，需要为表指定一个名称并定义表的每列和数据类型。

**语法：**

```sql
CREATE TABLE database_name.table_name(  
   column1 datatype  PRIMARY KEY(one or more columns),  
   column2 datatype,  
   column3 datatype,  
   .....  
   columnN datatype,  
);
```

### 示例：

下面举个例子来创建SQLite数据库中的表：

```sql
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

使用SQLite的`.tables`命令查看表是否已成功创建。

```sql
.tables
```

康康

下面再创建另一个表：`DEPARTMENT`。

```sql
CREATE TABLE DEPARTMENT(
   ID INT PRIMARY KEY      NOT NULL,
   DEPT           CHAR(50) NOT NULL,
   EMP_ID         INT      NOT NULL
);
```

```sql
.tables
```

康康

## SQLite 删除表 			

在SQLite中，`DROP TABLE`语句用于删除表定义以及与该表关联的所有关联数据，索引，触发器，约束和权限规范。

**语法**

```sql
DROP TABLE database_name.table_name;
SQL
```

注意：使用`DROP TABLE`命令时必须**非常小心**，因为一旦删除了表，那么表中的所有可用信息都将被破坏，再无法恢复了。

### 示例：

下面举个例子来演示如何在SQLite中删除一个表。在上面我们成功地创建了有两个表：`DEPARTMENT`和`COMPANY`。下面使用`.tables`命令来查看数据库现有表信息。

```sql
.tables
```

康康

现在，使用以下语句来删除`student`表 -

```sql
DROP TABLE COMPANY;
```

```sql
.tables
```

康康
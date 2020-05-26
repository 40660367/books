# SQLite 主键(primary key)

SQLite主键是用于唯一定义行记录的一个简单字段或多个字段的组合。一个表只能有一个主键。

主键的值不可以是一个`NULL`值。

## 创建主键

主键通常在创建表时一同创建。在执行`CREATE TABLE`语句时可以直接定义主键。

**语法：**

```sql
CREATE TABLE table_name  
(  
    column1 datatype [ NULL | NOT NULL ],  
    column2 datatype [ NULL | NOT NULL ],  
    ......  
    CONSTRAINT constraint_name PRIMARY KEY (pk_col1, pk_col2, ... pk_col_n)  
);
```

**参数说明：**

- *table_name*：指定要创建的表的名称。
- *column1*，*column2*：指定要在表中创建的列。
- *constraint_name*：指定主键的名称。
- *pk_col1*，*pk_col2*，*… pk_col_n*：它指定构成主键的列。

**示例：**

创建一个“`workers`”表，其中`worker_id`列是表的主键。

```sql
CREATE TABLE workers  
(
    worker_id INTEGER PRIMARY KEY,  
    last_name VARCHAR NOT NULL,  
    first_name VARCHAR,  
    join_date DATE  
);
```

## 添加主键

当没有在`CREATE TABLE`语句中定义主键时，也可以在创建表后再添加主键。

需要注意的是，不能使用`ALTER TABLE`语句来创建主键。在SQLite中需要先创建一个与原表一样的新表，并在这个新表上创建主键，然后复制旧表中的所有数据到新表中就可以了。

**语法**

```sql
PRAGMA foreign_keys=off;  
BEGIN TRANSACTION;  
ALTER TABLE table_name RENAME TO old_table;  
CREATE TABLE table_name  
(  
    column1 datatype [ NULL | NOT NULL ],  
    column2 datatype [ NULL | NOT NULL ],  
    ...  
    CONSTRAINT constraint_name PRIMARY KEY (pk_col1, pk_col2, ... pk_col_n)  
);  
INSERT INTO table_name SELECT * FROM old_table;  
COMMIT;  
PRAGMA foreign_keys=on;
```

**参数说明：**

- *table_name*：指定要创建含有主键的表的名称。
- *old_table*：指定要被修表的名称。
- *column1*，*column2*：指定要在表中创建的列。
- *constraint_name*：指定主键的名称。
- *pk_col1*，*pk_col2*，*… pk_col_n*：它指定构成主键的列。

**示例：**

首先创建一个没有主键的表：`employees`，如下语句 - 

```sql
CREATE TABLE employees  
(
    employee_id INTEGER,  
    last_name VARCHAR NOT NULL,  
    first_name VARCHAR,  
    hire_date DATE  
);
```

现在，运行以下命令将“`employee_id`”列设置成为主键。

```sql
PRAGMA foreign_keys=off;  
BEGIN TRANSACTION;  
ALTER TABLE employees RENAME TO old_employees;  
CREATE TABLE employees  
(  
    employee_id INTEGER,  
    last_name VARCHAR NOT NULL,  
    first_name VARCHAR,  
    hire_date DATE,  
    CONSTRAINT employees_pk PRIMARY KEY (employee_id)  
);  
INSERT INTO employees SELECT * FROM old_employees;  
COMMIT;  
PRAGMA foreign_keys=on;
```

现在，它会将`employees`表重命名为`old_employees`，然后创建一个新表`employees`并创建主键，然后从`old_employees`表中将所有数据传输到新表 `employees`中。

最后删除旧表：`old_employees`。

```sql
DROP TABLE old_employees;
```

## 删除主键

与添加主键一样，不能使用`ALTER TABLE`语句来删除主键。需要创建一个没有(删除)主键的新表，并将数据复制到此新表中。

**语法**

```sql
PRAGMA foreign_keys=off;  
BEGIN TRANSACTION;  
ALTER TABLE table_name RENAME TO old_table;  
CREATE TABLE table_name  
(  
    column1 datatype [ NULL | NOT NULL ],  
    column2 datatype [ NULL | NOT NULL ],  
    ...  
);  
INSERT INTO table_name SELECT * FROM old_table;  
COMMIT;  
PRAGMA foreign_keys=on;
```

**参数说明**

- *table_name* - 指定要从中删除主键的表的名称。
- *old_table* - 指定在删除主键后再创建新表时，将要删除拥有主键的表名称。

**示例：**

假设有一个表`engineers`，并有一个主键：`engineer_id`，现在要删除这个`engineer_id`主键。

```sql
CREATE TABLE engineers  
(
    engineer_id INTEGER,  
    engineerr_name VARCHAR NOT NULL,  
    address VARCHAR,  
    city VARCHAR,  
    CONSTRAINT engineers_pk PRIMARY KEY (engineer_id)  
);
```

现在，运行以下命令删除主键。

```sql
PRAGMA foreign_keys=off;  
BEGIN TRANSACTION;  
ALTER TABLE engineers RENAME TO old_engineers;  
CREATE TABLE engineers  
(  
    engineer_id INTEGER,  
    engineer_name VARCHAR NOT NULL,  
    address VARCHAR,  
    city VARCHAR  
);  
INSERT INTO engineers SELECT * FROM old_engineers;  
COMMIT;  
PRAGMA foreign_keys=on;
```

执行上面语句后，主键现在从`engineers`表中删除。 但是原来的表现在被重命名为`old_engineers`。

现在删除`old_engineers`表，如下语句 - 

```sql
DROP TABLE old_engineers;
```
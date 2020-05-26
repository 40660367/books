# MySQL插入INSERT 			

在本教程中，您将学习如何使用MySQL `INSERT`语句将数据插入到数据库表中。

## 简单的MySQL INSERT语句

MySQL `INSERT`语句用于将一行或多行插入到表中。下面说明了`INSERT`语句的语法：

```sql
INSERT INTO table(column1,column2...)
VALUES (value1,value2,...);
```

**首先**，在`INSERT INTO`子句之后，在括号内指定表名和逗号分隔列的列表。
**然后**，将括号内的相应列的逗号分隔值放在`VALUES`关键字之后。

在执行插入语句前，需要具有执行`INSERT`语句的`INSERT`权限。

## 准备本节练习的数据

让我们创建一个名为`tasks`的新表来本节的`INSERT`语句练习

```sql
create database testdb;
use testdb;
CREATE TABLE IF NOT EXISTS tasks (
    task_id INT(11) AUTO_INCREMENT,
    subject VARCHAR(45) DEFAULT NULL,
    start_date DATE DEFAULT NULL,
    end_date DATE DEFAULT NULL,
    description VARCHAR(200) DEFAULT NULL,
    PRIMARY KEY (task_id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
例如，如果要将任务插入到`tasts`表中，则使用`INSERT`语句如下：

```sql
INSERT INTO tasks(subject,start_date,end_date,description)
VALUES('Learning MySQL INSERT COMMAND','2020-1-1','2020-1-2','Start learning..');
```
执行该语句后，MySQL返回一条消息以通知受影响的行数。在这种情况下，有一行受到影响。
现在使用以下语句查询 `tasks` 中的数据，如下所示 - 

```sql
SELECT * FROM tasks;
```
## MySQL INSERT - 插入多行

想要在表中一次插入多行，可以使用具有以下语法的`INSERT`语句：

**语法：**

```sql
INSERT INTO table(column1,column2...)
VALUES (value1,value2,...),
       (value1,value2,...),
...;
```

**示例：**

在这种形式中，每行的值列表用逗号分隔。例如，要将多行插入到`tasks`表中，请使用以下语句：

```sql
INSERT INTO tasks(subject,start_date,end_date,description)
VALUES ('task-1','2020-01-01','2020-01-02','Description 1'),
       ('task-2','2020-01-01','2020-01-02','Description 2'),
       ('task-3','2020-01-01','2020-01-02','Description 3');
```
现在查询`tasks`表中的数据，如下所示 - 

```sql
select * from tasks;
```

如果为表中的所有列指定相应列的值，则可以忽略`INSERT`语句中的列列表，如下所示语法：

```sql
INSERT INTO table
VALUES (value1,value2,...);

INSERT INTO table
VALUES (value1,value2,...),
       (value1,value2,...),
...;
```
> 请注意，不必为自动递增列(例如`taskid`列)指定值，因为MySQL会自动为自动递增列生成值。

## 具有SELECT子句的MySQL INSERT

在MySQL中，可以使用SELECT语句返回的列和值来填充`INSERT`语句的值。此功能非常方便，因为您可以使用`INSERT`和`SELECT`子句完全或部分复制表

**语法：**

```sql
INSERT INTO table_1
SELECT c1, c2, FROM table_2;
```

假设要将`tasks`表复制到`tasks_bak`表。

**示例：**

**首先**，通过复制`tasks`表的结构，创建一个名为`tasks_bak`的新表，如下所示：

```sql
CREATE TABLE tasks_bak LIKE tasks;
```

**第二步**，使用以下`INSERT`语句将`tasks`表中的数据插入`tasks_bak`表：

```sql
INSERT INTO tasks_bak SELECT * FROM tasks;
```

**第三步**，检查`tasks_bak`表中的数据，看看是否真正从`tasks`表复制完成了。

```sql
select * from tasks_bak;
```

## MySQL INSERT与ON DUPLICATE KEY UPDATE

如果新行违反主键(PRIMARY KEY)或`UNIQUE`约束，MySQL会发生错误。例如，如果执行以下语句：MySQL很不高兴，并向你扔来一个错误消息：

```sql
INSERT INTO tasks(task_id,subject,start_date,end_date,description)
VALUES (4,'Test ON DUPLICATE KEY UPDATE','2017-01-01','2017-01-02','Next Priority');
```
因为表中的主键`task_id`列已经有一个值为 `4` 的行了，所以该语句违反了`PRIMARY KEY`约束。

但是，如果在`INSERT`语句中指定ON DUPLICATE KEY UPDATE选项，MySQL将插入新行或使用新值更新原行记录

例如，以下语句使用新的`task_id`和`subject`来更新`task_id`为`4`的行。

```sql
INSERT INTO tasks(task_id,subject,start_date,end_date,description)
VALUES (4,'Test ON DUPLICATE KEY UPDATE','2017-01-01','2017-01-02','Next Priority')
ON DUPLICATE KEY UPDATE 
   task_id = task_id + 1, 
   subject = 'Test ON DUPLICATE KEY UPDATE';
```
执行上面语句后，MySQL发出消息说`2`行受影响。现在，我们来看看`tasks`表中的数据：
```sql
select * from tasks;
```

新行没有被插入，但是更新了`task_id`值为`4`的行。上面的`INSERT ON DUPLICATE KEY UPDATE`语句等效于以下UPDATE语句

```sql
UPDATE tasks 
SET 
    task_id = task_id + 1,
    subject = 'Test ON DUPLICATE KEY UPDATE'
WHERE
    task_id = 4;
```

在本教程中，我们向您展示了如何使用各种形式的MySQL `INSERT`语句将数据插入到表中。
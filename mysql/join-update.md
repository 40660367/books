# MySQL update join语句

在本教程中，您将学习如何使用MySQL `UPDATE JOIN`语句来执行跨表更新。我们将逐步介绍如何使用`INNER JOIN`子句和`LEFT JOIN`子句与`UPDATE`语句一起使用。

## MySQL UPDATE JOIN语法

我们经常使用`join`子句来查询表中的行(在[INNER JOIN](./join-inner.html)的情况下)，或者可能没有(在[LEFT JOIN](./join-left.html)的情况下)另一个表中的相应行。 在MySQL中，可以在[UPDATE语句](./update.html)中使用`JOIN`子句执行跨表更新。

MySQL `UPDATE JOIN`的语法如下：

```sql
UPDATE T1, T2,
[INNER JOIN | LEFT JOIN] T1 ON T1.C1 = T2. C1
SET T1.C2 = T2.C2, 
    T2.C3 = expr
WHERE condition
```

让我们更详细地看看MySQL `UPDATE JOIN`语法：

- 首先，在`UPDATE`子句之后，指定主表(`T1`)和希望主表连接表(`T2`)。 请注意，必须在`UPDATE`子句之后至少指定一个表。`UPDATE`子句后未指定的表中的数据未更新。
- 第二，指定一种要使用的连接，即`INNER JOIN`或`LEFT JOIN`和连接条件。`JOIN`子句必须出现在`UPDATE`子句之后。
- 第三，要为要更新的`T1`和/或`T2`表中的列分配新值。
- 第四，[WHERE子句](./where.html)中的条件用于指定要更新的行。

如果您学习过了[UPDATE语句](./update.html)，您可能会注意到使用以下语法更新数据交叉表的另一种方法：

```sql
UPDATE T1, T2
SET T1.c2 = T2.c2,
      T2.c3 = expr
WHERE T1.c1 = T2.c1 AND condition
```

在这个`UPDATE`语句与具有隐式`INNER JOIN`子句的`UPDATE JOIN`工作相同。这意味着可以如下重写上述语句：

```sql
UPDATE T1,T2
INNER JOIN T2 ON T1.C1 = T2.C1
SET T1.C2 = T2.C2,
      T2.C3 = expr
WHERE condition
```

让我们来看一些使用`UPDATE JOIN`语句来更好地理解的例子。

## MySQL UPDATE JOIN示例

我们将在这些例子中使用一个新的示例数据库(*empdb*)。示例数据库包含`2`个表：

- `employees`表将存储在员工编号，姓名，工作表现和工资的数据。
- `merits`表存储员工绩效和绩效百分比。

以下语句在`empdb`示例数据库中创建表并导入数据：

```sql
CREATE DATABASE IF NOT EXISTS empdb;

USE empdb;
-- create tables
CREATE TABLE merits (
    performance INT(11) NOT NULL,
    percentage FLOAT NOT NULL,
    PRIMARY KEY (performance)
);

CREATE TABLE employees (
    emp_id INT(11) NOT NULL AUTO_INCREMENT,
    emp_name VARCHAR(255) NOT NULL,
    performance INT(11) DEFAULT NULL,
    salary FLOAT DEFAULT NULL,
    PRIMARY KEY (emp_id),
    CONSTRAINT fk_performance FOREIGN KEY (performance)
        REFERENCES merits (performance)
);
-- insert data for merits table
INSERT INTO merits(performance,percentage)
VALUES(1,0),
      (2,0.01),
      (3,0.03),
      (4,0.05),
      (5,0.08);
-- insert data for employees table
INSERT INTO employees(emp_name,performance,salary)      
VALUES('Mary Doe', 1, 50000),
      ('Cindy Minsu', 3, 65000),
      ('Sue Greenspan', 4, 75000),
      ('Grace Dell', 5, 125000),
      ('Nancy Johnson', 3, 85000),
      ('John Doe', 2, 45000),
      ('Lily Bush', 3, 55000);
```

**使用INNER JOIN子句的MySQL UPDATE JOIN示例**

假设想根据员工的工作表现来调整员工的工资。

因此，优点百分比存储在`merits`表中，您必须使用`UPDATE INNER JOIN`语句根据存储在`merits`表中的百分比来调整`employees`表中员工的工资。

`employees`和`merits`表之间以是`performance`字段相关联的。 请参阅以下查询：

```sql
UPDATE employees
        INNER JOIN
    merits ON employees.performance = merits.performance 
SET 
    salary = salary + salary * percentage;
```

上面查询语句的工作原理是什么？

我们仅在`UPDATE`子句之后指定`employees`表，因为我们只想更新`employees`表中的数据。

对于`employees`表中的每一行，查询根据`merits`表中`performance`列中的值来检查`employees`表中的`performance`列中的值。 如果找到一个匹配，它将获得`merits`表中的百分比，并更新`employees`表中的`salary`列。

```sql
select * from employees; -- 更新之前的数据
```

```sql
UPDATE employees
        INNER JOIN
    merits ON employees.performance = merits.performance 
SET 
    salary = salary + salary * percentage; -- 执行连接更新
```

因为省略了`UPDATE`语句中的`WHERE`子句，所以`employees`表中的所有记录都被更新。

**具有LEFT JOIN的MySQL UPDATE JOIN示例**

假设公司又雇用了两名新员工：

```sql
INSERT INTO employees(emp_name,performance,salary)
VALUES('Jack William',NULL,43000),
      ('Ricky Bond',NULL,52000);
```

因为这些员工是新员工，所以他们的绩效(`performance`)数据不可用或为`NULL`。现在 `employees`表中的数据，如下所示 - 

```sql
SELECT * FROM employees;
```

要计算新员工的工资，不能使用`UPDATE INNER JOIN`语句，因为它们的绩效数据在`merits`表中不可用。这就是为什么要使用`UPDATE LEFT JOIN`来实现了。

当`UPDATE LEFT JOIN`语句在另一个表中没有相应行时，就会更新表中的一行。

例如，您可以使用以下语句将新雇员的工资增加`1.5％`：

```sql
UPDATE employees
        LEFT JOIN
    merits ON employees.performance = merits.performance 
SET 
    salary = salary + salary * 0.015
WHERE
    merits.percentage IS NULL;
```

上面语句执行后，得到以下结果 - 

```sql
SELECT * FROM employees;
```

```sql
UPDATE employees
        LEFT JOIN
    merits ON employees.performance = merits.performance 
SET 
    salary = salary + salary * 0.015
WHERE
    merits.percentage IS NULL;
```

```sql
SELECT * FROM employees;
```
# MySQL 触发器(trigger)

在本教程中，您将学习如何使用`CREATE TRIGGER`语句在MySQL中创建触发器。

## MySQL触发语法

为了创建一个新的触发器，可以使用`CREATE TRIGGER`语句。 下面说明了`CREATE TRIGGER`语句的语法：

```sql
CREATE TRIGGER trigger_name trigger_time trigger_event
 ON table_name
 FOR EACH ROW
 BEGIN
 ...
 END;
```

下面，我们来更详细的检查上面的语法。

- 将触发器名称放在`CREATE TRIGGER`语句之后。触发器名称应遵循命名约定`[trigger time]_[table name]_[trigger event]`，例如before_employees_update。
- 触发激活时间可以在之前或之后。必须指定定义触发器的激活时间。如果要在更改之前处理操作，则使用`BEFORE`关键字，如果在更改后需要处理操作，则使用`AFTER`关键字。
- 触发事件可以是`INSERT`，`UPDATE`或`DELETE`。此事件导致触发器被调用。 触发器只能由一个事件调用。要定义由多个事件调用的触发器，必须定义多个触发器，每个事件一个触发器。
- 触发器必须与特定表关联。没有表触发器将不存在，所以必须在`ON`关键字之后指定表名。
- 将SQL语句放在`BEGIN`和`END`块之间。这是定义触发器逻辑的位置。

## MySQL触发器示例

**[准备环境](./setup.html)**

下面我们将在MySQL中创建触发器来记录`employees`表中行数据的更改情况。

```sql
DESC employees;
```

首先，创建一个名为`employees audit`的新表，用来保存`employees`表中数据的更改。 以下语句创建`employee_audit`表。

```sql
CREATE TABLE employees_audit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    employeeNumber INT NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    changedat DATETIME DEFAULT NULL,
    action VARCHAR(50) DEFAULT NULL
);
```

接下来，创建一个`BEFORE UPDATE`触发器，该触发器在对`employees`表中的行记录更改之前被调用。

```sql
DELIMITER $$
CREATE TRIGGER before_employee_update 
    BEFORE UPDATE ON employees
    FOR EACH ROW 
BEGIN
    INSERT INTO employees_audit
    SET action = 'update',
     employeeNumber = OLD.employeeNumber,
        lastname = OLD.lastname,
        changedat = NOW(); 
END$$
DELIMITER ;
```

在触发器的主体中，使用`OLD`关键字来访问受触发器影响的行的`employeeNumber`和`lastname`列。

请注意，在为[INSERT](./insert.html)定义的触发器中，可以仅使用`NEW`关键字。不能使用`OLD`关键字。但是，在为`DELETE`定义的触发器中，没有新行，因此您只能使用`OLD`关键字。在[UPDATE](./update.html)触发器中，`OLD`是指更新前的行，而`NEW`是更新后的行。

然后，要查看当前数据库中的所有触发器，请使用`SHOW TRIGGERS`语句，如下所示：

```sql
SHOW TRIGGERS;
```

之后，更新`employees`表以检查触发器是否被调用。

```sql
UPDATE employees 
SET 
    lastName = 'Maxsu'
WHERE
    employeeNumber = 1056;
```

最后，要检查触发器是否被`UPDATE`语句调用，可以使用以下查询来查询`employees_audit`表：

```sql
SELECT * FROM employees_audit;
```

如上面输出结果所示，触发器被真正调用，并在`employees_audit`表中插入一个新行。

在本教程中，您已经学会了如何在MySQL中创建一个触发器。我们还向您展示了如何开发触发器来审计员工(`employees`)表的更改。
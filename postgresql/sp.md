# PostgreSQL 存储过程(storage procedure)

PostgreSQL函数也称为PostgreSQL存储过程。 PostgreSQL函数或存储过程是存储在数据库服务器上并可以使用SQL界面调用的一组SQL和过程语句(声明，分配，循环，控制流程等)。 它有助于您执行通常在数据库中的单个函数中进行多次查询和往返操作的操作。

您可以在许多语言(如SQL，PL/pgSQL，C，Python等)中创建PostgreSQL函数。

**语法：**

```sql
CREATE [OR REPLACE] FUNCTION function_name (arguments)   
RETURNS return_datatype AS $variable_name$  
  DECLARE  
    declaration;  
    [...]  
  BEGIN  
    < function_body >  
    [...]  
    RETURN { variable_name | value }  
  END; LANGUAGE plpgsql;
```

### 参数说明

- `function_name`：指定函数的名称。
- `[OR REPLACE]`：是可选的，它允许您修改/替换现有函数。
- `RETURN`：它指定要从函数返回的数据类型。它可以是基础，复合或域类型，或者也可以引用表列的类型。
- `function_body`：`function_body`包含可执行部分。
- `plpgsql`：它指定实现该函数的语言的名称。

## 例子：

[准备环境及数据](./setup.html)

在`EMPLOYEES`表上创建一个名为`total records()`的函数。
函数的定义如下：

```sql
CREATE OR REPLACE FUNCTION totalRecords ()  
RETURNS integer AS $total$  
declare  
    total integer;  
BEGIN  
   SELECT count(*) into total FROM EMPLOYEES;  
   RETURN total;  
END;  
$total$ LANGUAGE plpgsql;
```

您可以看到一个名为“`totalrecords`”的函数被创建。

现在，来执行一个调用这个函数并检查`EMPLOYEES`表中的记录，如下所示 -

```sql
select totalRecords();
```
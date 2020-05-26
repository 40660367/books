# SQLite SELECT查询(query SELECT)

SQLite **SELECT**语句用于从SQLite数据库表中获取数据，该表以结果表的形式返回数据。这些结果表也称为**结果集**。

### 句法

以下是SQLite SELECT语句的基本语法。

```sql
SELECT column1, column2, columnN FROM table_name;
```

在这里，column1，column2 ...是表的字段，您要获取其值。如果要获取该字段中可用的所有字段，则可以使用以下语法-

```sql
SELECT * FROM table_name;
```

### 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

考虑带有以下记录的COMPANY表-

```
ID          NAME        AGE         ADDRESS     SALARY
----------  ----------  ----------  ----------  ----------
1           Paul        32          California  20000.0
2           Allen       25          Texas       15000.0
3           Teddy       23          Norway      20000.0
4           Mark        25          Rich-Mond   65000.0
5           David       27          Texas       85000.0
6           Kim         22          South-Hall  45000.0
7           James       24          Houston     10000.0
```

以下是使用SELECT语句获取并显示所有这些记录的示例。在这里，前三个命令已用于设置正确格式的输出。

```
.header on
.mode column
SELECT * FROM COMPANY;
```

康康

如果您只想获取COMPANY表的选定字段，则使用以下查询-

```
SELECT ID, NAME, SALARY FROM COMPANY;
```

康康

## 设置输出列宽

有时，在**.mode列的**情况下，由于要显示的列的默认宽度，您会遇到与截断输出有关的问题。您可以做的是，您可以使用**.width num，num ....**命令设置列的可显示列宽**，**如下所示：

```
.width 10, 20, 10
SELECT * FROM COMPANY;
```

上面的**.width**命令将第一列的宽度设置为10，第二列的宽度设置为20，第三列的宽度设置为10。

康康

## 模式信息

由于所有**点命令**都在SQLite提示符下可用，因此在使用SQLite进行编程时，您将对**sqlite_master**表使用以下SELECT语句来列出数据库中创建的所有表。

```
SELECT tbl_name FROM sqlite_master WHERE type = 'table';
```

假设您的testDB.db中只有COMPANY表，

康康

您可以列出有关COMPANY表的完整信息，如下所示：

```
SELECT sql FROM sqlite_master WHERE type = 'table' AND tbl_name = 'COMPANY';
```

康康


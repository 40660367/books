# SQLite 更新查询(query UPDATE)

SQLite **UPDATE**查询用于修改表中的现有记录。您可以将WHERE子句与UPDATE查询一起使用来更新选定的行，否则所有行都将被更新。

## 句法

以下是带有WHERE子句的UPDATE查询的基本语法。

```
UPDATE table_name
SET column1 = value1, column2 = value2...., columnN = valueN
WHERE [condition];
```

您可以使用AND或OR运算符组合**N**个条件。

## 例

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

下面是一个示例，它将为ID为6的客户更新ADDRESS。

```
UPDATE COMPANY SET ADDRESS = 'Texas' WHERE ID = 6;
```

康康

如果要修改COMPANY表中的所有ADDRESS和SALARY列值，则无需使用WHERE子句，并且UPDATE查询将如下所示-

```
UPDATE COMPANY SET ADDRESS = 'Texas', SALARY = 20000.00;
```

康康 
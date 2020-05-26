# SQLite LIMIT(限制返回记录数)子句

SQLite **LIMIT**子句用于限制SELECT语句返回的数据量。

## 句法

以下是带有LIMIT子句的SELECT语句的基本语法。

```sql
SELECT column1, column2, columnN 
FROM table_name
LIMIT [no of rows]
```

以下是LIMIT子句与OFFSET子句一起使用时的语法。

```sql
SELECT column1, column2, columnN 
FROM table_name
LIMIT [no of rows] OFFSET [row num]
```

SQLite引擎将返回从下一行开始到给定OFFSET的行，如上一个示例所示。

## 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

先康康COMPANY表

```sql
SELECT * FROM COMPANY
```

该示例根据要从表中获取的行数来限制表中的行。

```
SELECT * FROM COMPANY LIMIT 6;
```

康康

但是，在某些情况下，您可能需要从特定偏移量中拾取一组记录。下面是一个例子，其拾取3个记录从3开始第三位置。

```sql
SELECT * FROM COMPANY LIMIT 3 OFFSET 2;
```

康康


# SQLite 删除查询(query DELETE)

在SQLite中，`DELETE`查询语句用于从表中删除已经存在的记录。 可以将其与WHERE子句或不与WHERE子句一起使用。 WHERE子句用于指定删除特定记录(选定的行)，否则所有记录将被删除。

**语法**

```sql
DELETE FROM table_name  
WHERE [conditions....................];;
SQL
```

> 注意：可以使用多个“`AND`”或“`OR`”运算符在“WHERE”子句中。

**示例：**

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

下面是一个示例，它将删除ID为7的客户。

```sql
DELETE FROM COMPANY WHERE ID = 7;
```

现在使用select，查询现有COMPANY表中内容

```sql
SELETE FROM COMPANY;
```

康康

如果要删除COMPANY表中的所有记录，则无需将WHERE子句与DELETE查询一起使用，如下所示-

```
DELETE FROM COMPANY;
```

现在使用select，查询现有COMPANY表中内容。现在COMPANY表没有任何记录，因为所有记录已被DELETE语句删除。

```sql
SELETE FROM COMPANY;
```

康康


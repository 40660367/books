# SQLite 关键字DISTINCT(消除重复)

SQLite `DISTINCT`子句与`SELECT`语句一起使用，用来消除所有重复记录，并仅获取唯一记录。

当在表中有多个重复记录时可使用它来过滤重复的记录。

**语法：**

```sql
SELECT DISTINCT column1, column2,.....columnN   
FROM table_name  
WHERE [condition]
```

## 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

首先，让我们看看下面的SELECT查询返回重复名字的薪水记录。

```
SELECT name FROM COMPANY;
```

康康



现在，让我们在上面的SELECT查询中使用**DISTINCT**关键字，然后查看结果。

```
SELECT DISTINCT name FROM COMPANY;
```

康康


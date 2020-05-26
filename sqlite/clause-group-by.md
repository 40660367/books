# SQLite GROUP BY(分组)子句

SQLite `GROUP BY`子句与`SELECT`语句一起使用，将相同的相同元素合并成一个组。

`GROUP BY`子句与`SELECT`语句中的`WHERE`子句一起使用，并且`WHERE`子句在`ORDER BY`子句之前。

**语法：**

```sql
SELECT column-list  
FROM table_name  
WHERE [ conditions ]  
GROUP BY column1, column2....columnN  
ORDER BY column1, column2....columnN
SQL
```

## 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)，如果已经配置好请忽略。

如果您想知道每个客户的工资总额，那么GROUP BY查询将如下所示-

```sql
SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME;
```

康康

现在，让我们使用以下INSERT语句在COMPANY表中再创建三个记录。

```sql
INSERT INTO COMPANY VALUES (8, 'Paul', 24, 'Houston', 20000.00 );
INSERT INTO COMPANY VALUES (9, 'James', 44, 'Norway', 5000.00 );
INSERT INTO COMPANY VALUES (10, 'James', 45, 'Texas', 5000.00 );
```

现在，康康我们的表具有以下重名的记录。

```sql
SELECT * FROM COMPANY;
```

再次，让我们使用相同的语句使用NAME列对所有记录进行分组，如下所示：

```sql
SELECT NAME, SUM(SALARY) FROM COMPANY GROUP BY NAME ORDER BY NAME;
```

康康

让我们如下使用ORDER BY子句和GROUP BY子句-

```sql
SELECT NAME, SUM(SALARY) 
   FROM COMPANY GROUP BY NAME ORDER BY NAME DESC;
```

康康
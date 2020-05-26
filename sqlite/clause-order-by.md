# SQLite ORDER BY(排序)子句 			

SQLite `ORDER BY`子句用于根据一个或多个列对所获取的数据按升序或降序进行排序(排序)。

**语法**

```sql
SELECT column-list   
FROM table_name   
[WHERE condition]   
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
```

可以在`ORDER BY`子句中使用一个或多个列。所使用的列必须在列的列表中显示。

您可以在ORDER BY子句中使用多个列。确保要用于排序的任何列，该列都应在column-list中可用。

## 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

下面是一个示例，它将按SALARY降序对结果进行排序。

```
SELECT * FROM COMPANY ORDER BY SALARY ASC;
```

这将产生以下结果。

下面是一个示例，它将按NAME和SALARY的降序对结果进行排序。

```
SELECT * FROM COMPANY ORDER BY NAME, SALARY ASC;
```

这将产生以下结果。

以下是一个示例，它将按照NAME的降序对结果进行排序。

```
SELECT * FROM COMPANY ORDER BY NAME DESC;
```

这将产生以下结果。
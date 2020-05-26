# SQLite HAVING(分组过滤)子句 			

HAVING子句使您可以指定条件，以过滤哪些组结果出现在最终结果中。

WHERE子句在所选列上放置条件，而HAVING子句在GROUP BY子句创建的组上放置条件。

## 句法

以下是HAVING子句在SELECT查询中的位置。

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```

HAVING子句必须在查询中的GROUP BY子句之后，并且也必须在ORDER BY子句之前（如果使用）。以下是SELECT语句的语法，包括HAVING子句。

```sql
SELECT column1, column2
FROM table1, table2
WHERE [ conditions ]
GROUP BY column1, column2
HAVING [ conditions ]
ORDER BY column1, column2
```

## 示例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)，如果已经配置好请忽略。

下面将显示名称计数小于2的记录。

```
SELECT * FROM COMPANY GROUP BY name HAVING count(name) < 2;
```

康康



下面将显示名称计数大于2的记录。

```
sqlite > SELECT * FROM COMPANY GROUP BY name HAVING count(name) > 2;
```

康康
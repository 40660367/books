# SQLite 视图(view)

视图无非是一个SQLite语句，该语句以关联的名称存储在数据库中。它实际上是以预定义的SQLite查询的形式组成的表。

一个视图可以包含一个表的所有行或一个或多个表中的选定行。可以从一个或多个表创建视图，这取决于编写的SQLite查询来创建视图。

作为虚拟表的视图，允许用户-

- 以用户或用户类别自然或直观的方式构造数据。
- 限制对数据的访问，以便用户只能看到有限的数据，而不是完整的表。
- 汇总各种表中的数据，这些数据可用于生成报告。

SQLite视图是只读的，因此您可能无法在视图上执行DELETE，INSERT或UPDATE语句。但是，您可以在视图上创建触发器，该触发器将在尝试删除，插入或更新视图时触发，并在触发器主体中执行所需的操作。

## 创建视图

SQLite视图是使用**CREATE VIEW**语句创建的。可以从一个表，多个表或另一个视图创建SQLite视图。

以下是基本的CREATE VIEW语法。

```sql
CREATE [TEMP | TEMPORARY] VIEW view_name AS
SELECT column1, column2.....
FROM table_name
WHERE [condition];
```

您可以像在普通SQL SELECT查询中使用多个表一样，在SELECT语句中包括多个表。如果存在可选的TEMP或TEMPORARY关键字，则将在temp数据库中创建该视图。

### 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

以下是从COMPANY表创建视图`COMPANY_VIEW`的示例。该视图将仅用于COMPANY表中的几列。

```sql
CREATE VIEW COMPANY_VIEW AS
SELECT ID, NAME, AGE
FROM  COMPANY
WHERE ARE > 25;
```

现在，您可以通过查询实际表的类似方式查询COMPANY_VIEW。

```sql
SELECT * FROM COMPANY_VIEW;
```

康康

## 删除视图

要删除视图，只需将DROP VIEW语句与**view_name一起使用**。基本的DROP VIEW语法如下-

```sql
DROP VIEW view_name;
```

以下命令将删除我们在上一节中创建的COMPANY_VIEW视图。

例：删除上面刚刚创建的视图`COMPANY_VIEW`

```sql
DROP VIEW COMPANY_VIEW;
```
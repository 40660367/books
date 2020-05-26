# SQLite 关键字explain(分析执行计划)

在SQLite语句之前可以使用关键字“ EXPLAIN”或用于描述表详细信息的短语“ EXPLAIN QUERY PLAN”。

两种修改都会使SQLite语句充当查询，并返回有关如果省略EXPLAIN关键字或短语则SQLite语句将如何操作的信息。

- EXPLAIN和EXPLAIN QUERY PLAN的输出仅用于交互式分析和故障排除。
- 输出格式的详细信息可能会从一个版本的SQLite更改为下一个版本。
- 应用程序不应使用EXPLAIN或EXPLAIN QUERY PLAN，因为它们的确切行为是可变的，并且仅部分记录在案。

## 句法

**EXPLAIN的**语法如下-

```sql
EXPLAIN [SQLite Query]
```

**EXPLAIN QUERY PLAN的**语法如下-

```sql
EXPLAIN QUERY PLAN [SQLite Query]
```

## 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

现在，让我们使用SELECT语句检查以下子查询

```sql
EXPLAIN SELECT * FROM COMPANY WHERE Salary >= 20000;
```

康康



现在，让我们使用SELECT语句检查以下**解释查询计划**

```sql
EXPLAIN QUERY PLAN SELECT * FROM COMPANY WHERE Salary >= 20000;
```

康康
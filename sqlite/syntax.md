# SQLite 语法(syntax)			

语法是一组独特的规则和约定。 以下是SQLite的语法列表。

**区分大小写：**

- SQLite不区分大小写。但是，有一些区分大小写的命令。例如：`GLOB`和`glob`在SQLite语句中有不同的含义。

**注释：**

- 注释用于在SQLite代码中增加代码的可读性。
- 注释不能嵌套。
- 注释以两个连续的“ `-` ”字符。
- 也可使用“`/*`”字符开始，并延伸至下一个“`*/`”字符对所包括的内容视为注释。

**SQLite语句**

所有的SQLite语句都是以关键字(如：`SELECT`，`INSERT`，`UPDATE`，`DELETE`，`ALTER`，`DROP`等)开始的。所有语句都以分号(`;`)结尾。

**SQLite ANALYZE语句的语法：**

```sql
ANALYZE;  
-- or  
ANALYZE database_name;  
-- or  
ANALYZE database_name.table_name;
```

**SQLite AND/OR子句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  CONDITION-1 {AND|OR} CONDITION-2;
```

**SQLite ALTER TABLE语句的语法**

```sql
ALTER TABLE table_name ADD COLUMN column_def...;
```

**SQLite ALTER TABLE语句(Rename)语句的语法**

```sql
ALTER TABLE table_name RENAME TO new_table_name;
```

**SQLite ATTACH DATABASE语句的语法：**

```sql
ATTACH DATABASE 'DatabaseName' As 'Alias-Name';
```

**SQLite BEGIN TRANSACTION语句的语法：**

```sql
BEGIN;  
-- or  
BEGIN EXCLUSIVE TRANSACTION;
```

**SQLite BETWEEN语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  column_name BETWEEN val-1 AND val-2;  
SQLite COMMIT Statement:  
COMMIT;
```

**SQLite CREATE INDEX语句的语法：**

```sql
CREATE INDEX index_name  
ON table_name ( column_name COLLATE NOCASE );
```

**SQLite CREATE UNIQUE INDEX语句的语法：**

```sql
CREATE UNIQUE INDEX index_name  
ON table_name ( column1, column2,...columnN);
```

**SQLite CREATE TABLE语句的语法：**

```sql
CREATE TABLE table_name(  
   column1 datatype,  
   column2 datatype,  
   column3 datatype,  
   .....  
   columnN datatype,  
   PRIMARY KEY( one or more columns ));
```

**SQLite CREATE TRIGGER语句的语法：**

```sql
CREATE TRIGGER database_name.trigger_name   
BEFORE INSERT ON table_name FOR EACH ROW  
BEGIN   
   stmt1;   
   stmt2;  
   ....  
END;
```

**SQLite CREATE VIEW语句的语法：**

```sql
CREATE VIEW database_name.view_name  AS  
SELECT statement....;
```

**SQLite CREATE VIRTUAL TABLE语句的语法：**

```sql
CREATE VIRTUAL TABLE database_name.table_name USING weblog( access.log );  
-- or  
CREATE VIRTUAL TABLE database_name.table_name USING fts3( );
```

**SQLite COMMIT TRANSACTION语句的语法：**

```sql
COMMIT;
```

**SQLite COUNT语句的语法：**

```sql
SELECT COUNT(column_name)  
FROM   table_name  
WHERE  CONDITION;
```

**SQLite DELETE语句的语法：**

```sql
DELETE FROM table_name  
WHERE  {CONDITION};
```

**SQLite DETACH DATABASE语句的语法：**

```sql
DETACH DATABASE 'Alias-Name';
```

**SQLite DISTINCT语句的语法：**

```sql
SELECT DISTINCT column1, column2....columnN  
FROM   table_name;
```

**SQLite DROP INDEX语句的语法：**

```sql
DROP INDEX database_name.index_name;
```

**SQLite DROP TABLE语句的语法：**

```sql
DROP TABLE database_name.table_name;
```

**SQLite DROP VIEW语句的语法：**

```sql
DROP INDEX database_name.view_name;
SQL
```

**SQLite DROP TRIGGER 语句的语法：**

```sql
DROP INDEX database_name.trigger_name;
```

**SQLite EXISTS语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  column_name EXISTS (SELECT * FROM   table_name );
```

**SQLite EXPLAIN语句的语法：**

```sql
EXPLAIN INSERT statement...;  
-- or   
EXPLAIN QUERY PLAN SELECT statement...;
SQL
```

**SQLite GLOB语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  column_name GLOB { PATTERN };
```

**SQLite GROUP BY语句的语法：**

```sql
SELECT SUM(column_name)  
FROM   table_name  
WHERE  CONDITION  
GROUP BY column_name;
```

**SQLite HAVING语句的语法：**

```sql
SELECT SUM(column_name)  
FROM   table_name  
WHERE  CONDITION  
GROUP BY column_name  
HAVING (arithematic function condition);
```

**SQLite INSERT INTO语句的语法：**

```sql
INSERT INTO table_name( column1, column2....columnN)  
VALUES ( value1, value2....valueN);
```

**SQLite IN语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  column_name IN (val-1, val-2,...val-N);
SQL
```

**SQLite Like语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  column_name LIKE { PATTERN };
```

**SQLite NOT IN语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  column_name NOT IN (val-1, val-2,...val-N);
```

**SQLite ORDER BY语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  CONDITION  
ORDER BY column_name {ASC|DESC};
```

**SQLite PRAGMA语句的语法：**

```sql
PRAGMA pragma_name;
```

有关`pragma`的几个示例：

```sql
PRAGMA page_size;  
PRAGMA cache_size = 1024;  
PRAGMA table_info(table_name);
```

**SQLite RELEASE SAVEPOINT语句的语法：**

```sql
RELEASE savepoint_name;
```

**SQLite REINDEX语句的语法：**

```sql
REINDEX collation_name;  
REINDEX database_name.index_name;  
REINDEX database_name.table_name;
```

**SQLite ROLLBACK语句的语法：**

```sql
ROLLBACK;  
-- or  
ROLLBACK TO SAVEPOINT savepoint_name;
```

**SQLite SAVEPOINT语句的语法：**

```sql
SAVEPOINT savepoint_name;
```

**SQLite SELECT语句的语法：**

```sql
SELECT column1, column2....columnN  
FROM   table_name;
```

**SQLite UPDATE语句的语法：**

```sql
UPDATE table_name  
SET column1 = value1, column2 = value2....columnN=valueN  
[ WHERE  CONDITION ];
```

**SQLite VACUUM语句的语法：**

```sql
VACUUM;  
SQLite WHERE Clause:  
SELECT column1, column2....columnN  
FROM   table_name  
WHERE  CONDITION;
```
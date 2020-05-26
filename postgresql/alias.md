# PostgreSQL 别名(alias)

PostgreSQL别名(Alias)用于为列或表提供临时名称。您可以使用PostgreSQL别名为列或表创建一个临时名称。

通常来说，当您执行自联接时，会创建一个临时表。

## PostgreSQL 列别名

**语法：**

```sql
SELECT column_name AS alias_name  
FROM table_name  
conditions...  ;
```

### 参数说明

- `column_name`: 它指定要进行别名的列的原始名称。
- `alias_name`: 它指定分配给列的临时名称。
- `table_name`：它指定表的名称。
- `AS`：这是可选的。大多数程序员将在对列名进行别名时指定`AS`关键字，但在别名表名时不指定。

**注意：**

- 如果`alias_name`包含空格，则必须将`alias_name`包含在引号中。
- 在别名列名时，可以使用空格。 但是使用表名时，使用空格通常不是一个好习惯。
- `alias_name`仅在SQL语句的范围内有效。

**示例**

准备数据

执行以下查询使用别名的语句：

```sql
SELECT NAME, MAX(SALARY) AS PACKAGE  
FROM EMPLOYEES  
GROUP BY NAME;
```

## PostgreSQL 表别名

**语法：**

```sql
SELECT column1, column2....  
FROM table_name AS alias_name  
conditions....  ;
```

### 参数说明：

- `table_name`：它指定要进行别名的表的原始名称。
- `alias_name`：它指定分配给表的临时名称。
- `AS`：这是可选的。大多数程序员将在对列名进行别名时指定`AS`关键字，但在别名表名时不指定。

**注意：**

- 如果`alias_name`包含空格，则必须将`alias_name`包含在引号中。
- 在别名列名时，可以使用空格。 但是，当您使用表名时，使用空格通常不是一个好习惯。
- `alias_name`仅在SQL语句的范围内有效。

**示例**

```sql
SELECT E.ID, E.NAME, E.AGE, D.DEPT  
FROM COMPANY AS E, DEPARTMENT AS D  
WHERE  E.ID = D.ID;
```

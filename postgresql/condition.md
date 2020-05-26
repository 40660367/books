# PostgreSQL 条件查询

PostgreSQL条件用于从数据库获取更具体的结果。 它们通常与WHERE子句一起使用。 具有子句的条件就像双层过滤器。

以下是PostgreSQL条件的列表：

- AND 条件
- OR 条件
- AND & OR 条件
- NOT 条件
- LIKE 条件
- IN 条件
- NOT IN 条件
- BETWEEN 条件

## 示例

[准备环境及数据](./setup.html)

## PostgreSQL AND条件 			

PostgreSQL AND条件与`WHERE`子句一起使用，以从表中的多个列中选择唯一的数据。

**语法：**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition]    
AND [search_condition];
```

**示例：**

下面来查询所有ID小于`4`并且薪水大于`120000`的员工数据信息，执行以下查询语句：

```sql
SELECT *  
FROM COMAPNY  
WHERE SALARY > 120000  
AND ID <= 4;
```

## PostgreSQL OR条件 			

PostgreSQL OR条件与`WHERE`子句一起使用，以从表中的一列或多列列中选择唯一数据。

**语法**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition]    
OR [search_condition];
SQL
```

**示例：**

查询名字是`Minsu`或者地址为`Noida`员工信息，执行以下查询：

```sql
SELECT *  
FROM  COMAPNY 
WHERE NAME = 'Minsu'  
OR ADDRESS = 'Noida';
```

## PostgreSQL AND & OR条件 			

PostgreSQL AND＆OR条件在仅一个查询中提供了`AND`和`OR`条件的优点。

**语法：**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition]  AND [search_condition]     
OR [search_condition];
```

**示例：**

查询名字的值为`Minsu`和地址的值为’`Delhi`‘，或者ID值大于等`8`的记录信息，执行以下查询：

```sql
SELECT *  
FROM COMAPNY  
WHERE (NAME = 'Minsu' AND ADDRESS = 'Delhi')  
OR (ID>= 8);
```

## PostgreSQL NOT条件 			

PostgreSQL NOT条件与WHERE子句一起使用以否定查询中的条件。

**语法：**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition] NOT [condition];
SQL
```

**示例1：**

查询那些地址不为`NULL`的记录信息，执行以下查询：

```sql
SELECT *  
FROM COMAPNY  
WHERE address IS NOT NULL ;
```

**示例2：**

再来看另外一个示例，查询那些年龄不是`21`和`24`的所有记录，执行以下查询：

```sql
SELECT *  
FROM COMAPNY  
WHERE age NOT IN(21,24) ;
```

## PostgreSQL LIKE条件 			

PostgreSQL LIKE条件与WHERE子句一起用于从指定条件满足`LIKE`条件的表中获取数据。

**语法**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition] LIKE [condition];
SQL
```

**示例1**
查询名字以`Ma`开头的数据记录，如下查询语句：

```sql
SELECT *   
FROM COMAPNY   
WHERE NAME LIKE 'Ma%';
```

**示例2**
查询名字以`su`结尾的数据记录，如下查询语句：

```sql
SELECT *   
FROM COMAPNY   
WHERE NAME LIKE '%su';
```

## PostgreSQL IN条件 			

PostgreSQL IN条件与WHERE子句一起使用，从指定条件满足`IN`条件的表中获取数据。

**语法：**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition] IN [condition];
```

查询`employee`表中那些年龄为`19`，`21`的员工信息，执行以下查询：

```sql
SELECT *  
FROM COMAPNY  
WHERE AGE IN (19, 21);
```

## PostgreSQL NOT IN条件 			

PostgreSQL NOT IN条件与WHERE子句一起使用，以从指定条件否定`IN`条件的表中获取数据。

**语法：**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition] NOT IN [condition];
SQL
```

**示例1:**

查询那些年龄不是`19`，`25`的数据，执行以下查询：

```sql
SELECT *  
FROM COMAPNY  
WHERE AGE NOT IN (19, 25);
```

**示例2:**

再来看看另外一个例子，查询那些名字不是`Minsu`，`Maxsu`的数据信息，执行以下查询：

```sql
SELECT *  
FROM COMAPNY  
WHERE name NOT IN ('Maxsu', 'Minsu');
```

## PostgreSQL BETWEEN条件 			
PostgreSQL BETWEEN条件与WHERE子句一起使用，以从两个指定条件之间的表中获取数据。

**语法：**

```sql
SELECT column1, column2, ..... columnN    
FROM table_name    
WHERE [search_condition] BETWEEN [condition];
```

**示例：**

查询`COMAPNY`表中年龄在`24`~`27`之间(含`24`，`27`)的数据信息，执行以下查询：

```sql
SELECT *   
FROM COMAPNY   
WHERE AGE BETWEEN 24 AND 27;
```

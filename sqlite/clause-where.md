# SQLite WHERE(指定过滤条件)子句 			

SQLite WHERE子句通常与`SELECT`，`UPDATE`和`DELETE`语句一起使用，以便作为指定条件从一个表或多个表中获取数据。

如果条件满足或正确，则返回表中的特定值。 可使用WHERE子句来过滤记录并仅获取满足指定条件的记录。

WHERE子句还用于过滤记录并仅获取特定数据。

**语法**

```sql
SELECT column1, column2, columnN   
FROM table_name  
WHERE [condition]
```

## 示例：

在这个例子中，将使用WHERE子句与几个比较和逻辑运算符。如：`>`，`<`，`=`，`like`，`NOT`等等

您可以使用[比较运算符或逻辑运算符](/sqlite/operators.htm)例如>，<，=，LIKE，NOT等）来指定条件。



[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

以下是显示SQLite逻辑运算符用法的简单示例。在SELECT语句之后列出了AGE大于或等于25 **并且**薪水大于或等于65000.00的所有记录。

```sql
SELECT * FROM COMPANY WHERE AGE >= 25 AND SALARY >= 65000;
```

康康

在SELECT语句之后列出了AGE大于或等于25 **或**薪金大于或等于65000.00的所有记录。

```sql
SELECT * FROM COMPANY WHERE AGE >= 25 OR SALARY >= 65000;
```

康康

紧接着SELECT语句列出了AGE不为NULL的所有记录，这意味着所有记录，因为没有记录的AGE等于NULL。

```sql
SELECT * FROM COMPANY WHERE AGE IS NOT NULL;
```

康康

以下SELECT语句列出了NAME以'Ki'开头的所有记录，与'Ki'之后的记录无关。

```sql
sqlite> SELECT * FROM COMPANY WHERE NAME LIKE 'Ki%';
```

康康

以下SELECT语句列出了NAME以'Ki'开头的所有记录，与'Ki'之后的记录无关。

```sql
sqlite> SELECT * FROM COMPANY WHERE NAME GLOB 'Ki*';
```

康康

在SELECT语句之后，列出了AGE值为25或27的所有记录。

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE IN ( 25, 27 );
```

以下SELECT语句列出了AGE值既不是25也不是27的所有记录。

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE NOT IN ( 25, 27 );
```

康康

在SELECT语句之后，列出了AGE值在25和27之间的所有记录。

```sql
sqlite> SELECT * FROM COMPANY WHERE AGE BETWEEN 25 AND 27;
```

以下SELECT语句使用SQL子查询，其中子查询查找AGE字段的SALARY> 65000的所有记录，随后WHERE子句与EXISTS运算符一起使用，以列出外部查询存在AGE的所有记录在子查询返回的结果中-

```sql
SELECT AGE FROM COMPANY 
   WHERE EXISTS (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
```

康康

以下SELECT语句使用SQL子查询，其中子查询查找AGE字段具有SALARY> 65000的所有记录，并且随后使用WHERE子句与>运算符一起列出了外部查询中AGE较大的所有记录子查询返回的结果中的年龄。

```sql
SELECT * FROM COMPANY 
   WHERE AGE > (SELECT AGE FROM COMPANY WHERE SALARY > 65000);
```

康康
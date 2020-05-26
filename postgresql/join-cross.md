# PostgreSQL 交叉连接(CROSS JOIN)	

PostgreSQL跨连接(`CROSS JOIN`)将第一个表的每一行与第二个表的每一行相匹配。 它也被称为笛卡尔积。 如果`table1`具有“`x`”行，而`table2`具有“`y`”行，则所得到的表将具有(`x * y`)行。

**语法：**

```sql
SELECT coloums   
FROM table1   
CROSS JOIN table2
```

**示例:**

[准备环境及数据](./setup.html)

**表**： `DEPARTMENT` 

执行以下跨连接查询：

```sql
SELECT NAME, DEPT 
FROM EMPLOYEES  
CROSS JOIN DEPARTMENT;
```


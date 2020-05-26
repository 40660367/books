# SQLite 插入查询(query INSERT)

SQLite **INSERT INTO**语句用于将新的数据行添加到数据库的表中。

### 句法

以下是INSERT INTO语句的两种基本语法。

```sql
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);
```

在这里，column1，column2，... columnN是要在其中插入数据的表中各列的名称。

如果要为表的所有列添加值，则可能不需要在SQLite查询中指定列名称。但是，请确保值的顺序与表中各列的顺序相同。SQLite INSERT INTO语法如下-

```sql
INSERT INTO TABLE_NAME VALUES (value1,value2,value3,...valueN);
```

### 例

参照，创建创建数据库，与创建数据表。

创建COMPANY表，结构如下所示-

```sql
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);
```

现在，以下语句将在COMPANY表中创建六个记录。

```sql
INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (1, 'Paul', 32, 'California', 20000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (2, 'Allen', 25, 'Texas', 15000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (3, 'Teddy', 23, 'Norway', 20000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (5, 'David', 27, 'Texas', 85000.00 );

INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)
VALUES (6, 'Kim', 22, 'South-Hall', 45000.00 );
```

您可以使用第二种语法在COMPANY表中创建记录，如下所示：

```sql
INSERT INTO COMPANY VALUES (7, 'James', 24, 'Houston', 10000.00 );
```

## 使用另一个表填充一个表

您可以通过select语句将数据填充到另一个表中，前提是另一个表具有一组字段，这些字段是填充第一个表所必需的。

语法:

```sql
INSERT INTO first_table_name [(column1, column2, ... columnN)] 
   SELECT column1, column2, ...columnN 
   FROM second_table_name
   [WHERE condition];
```

以上所有语句将在COMPANY表中创建以下记录。

使用SELECT语句，查看刚刚插入的数据

```sql
SELECT * FROM COMPANY;
```

康康
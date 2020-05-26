# PostgreSQL创建表 			

在PostgreSQL中，`CREATE TABLE`语句用于在任何给定的数据库中创建一个新表。

## 示例：

[准备环境及数据](./setup.html)

**语法：**

```sql
CREATE TABLE table_name(  
   column1 datatype,  
   column2 datatype,  
   column3 datatype,  
   .....  
   columnN datatype,  
   PRIMARY KEY( one or more columns )  
);
```

**示例:**

```sql
CREATE TABLE public.student
(
  id integer NOT NULL,
  name character(100),
  subjects character(1),
  CONSTRAINT student2_pkey PRIMARY KEY (id)
)
WITH (
  OIDS=FALSE
);


ALTER TABLE public.student
  OWNER TO postgres;
COMMENT ON TABLE public.student
  IS 'This is a Student Table';
```

## 使用SQL语句来删除表

```sql
drop table student;
```


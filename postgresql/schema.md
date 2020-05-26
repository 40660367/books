# PostgreSQL 模式(schema) 

模式(也叫架构)是指定的表集合。 它还可以包含视图，索引，序列，数据类型，运算符和函数。

## 创建模式

在PostgreSQL中，`CREATE SCHEMA`语句用于创建模式。 模式不能嵌套。

**语法：**

```sql
CREATE SCHEMA schema_name;
SQL
```

通过SQL命令行直接创建 - 

```sql
CREATE SCHEMA myschema;
```

可以通过单击**列**并**添加**按钮添加列。

```sql
-- Table: myschema.tb_test

-- DROP TABLE myschema.tb_test;

CREATE TABLE myschema.tb_test
(
  id integer,
  name character(254)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE myschema.tb_test
  OWNER TO postgres;
```

## 删除PostgreSQL模式

## 使用架构的优点：

- 模式有助于多用户使用一个数据库，而不会互相干扰。
- 它将数据库对象组织成逻辑组，使其更易于管理。
- 可以将第三方模式放入单独的模式中，以避免与其他对象的名称相冲突。
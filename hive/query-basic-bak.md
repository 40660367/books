# Hive 基本查询

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

## select语句

先通过`desc tablename`查看表列信息。

```hql
desc employee;
```

### 查询所有列

```hql
select * from employees;
```

### 查询指定列并指定列别名

```hql
select name, salary as employees_salary from employees; 
```

### 查询集合数据类型列

#### 查询Array元素

subordinates为一个string类型的数组，数组下标从0开始。如果要看每条数据subordinates列的第一个元素，则用subordinates[0]的形式表示。

```hql
select name, subordinates[0] as first_subordinates from employees;
```

#### 查询Map元素

deductions列数据类型为map

```hql
select name, deductions["Insurance"] as Insutance_deduction from employees;
```

#### 查询Struct元素

```hql
select name, address.city as city from employees;
```

### 查询计算列

```hql
select upper(name) as name, salary, deductions["Federal Taxes"] as Federal_Taxes,
round(salary * (1 - deductions["Federal Taxes"])) as real_wages from employees;
```

### 嵌套select 语句

```hql
from (
select upper(name) as name, salary, deductions["Federal Taxes"] as Federal_Taxes,
round(salary * (1 - deductions["Federal Taxes"])) as real_wages from employees
) e
select e.name, e.real_wages;
```

### case语句

```hql
select name, salary, 
case
  when salary < 5000.0 then 'low'
  when salary >= 5000.0 and salary < 7000.0 then 'middle'
  when salary >= 7000.0 and salary < 10000.0 then 'high'
else 'very high'
end as bracket from employees;
```

## where子句

where语句用于过滤条件。

```hql
select upper(name) as name, salary, deductions["Federal Taxes"] as Federal_Taxes,round(salary * (1 - deductions["Federal Taxes"])) as real_wages from employee where round(salary * (1 - deductions["Federal Taxes"])) as real_wages >600;
```

##  模糊匹配 

###  like

like严格来说是匹配通配符。比如%匹配任意多的字符串。

```hql
select address from employee where address.street like '%Ave.';
```

### rlike
rlike匹配正则表达式。如下匹配的是`'.*(Chicago|Ontario).*'`，`.`表示任意字符串，`*`表示将左边的字符串重复任意次，`(Chicago|Ontario)`表示Chicago或Ontario。

```hql
select address from employees
where address.street rlike '.*(Chicago|Ontario).*';
```

## 返回限定:limit

限定查询的行数。

```hql
select name, salary from employees limit 2;
```

## 分组 group by

按一个列或者多个列对数据进行分组，然后对每组的数据进行聚合操作。如下，按address.city进行分组，然后通过avg(salary)求每组的salary的均值。group by之后的可以有一个或多个列。下面的例子只使用了struct类型的address列的一个city字段

```hql
select address.city, avg(salary) from employee
group by address.city;
```

## 分组过滤 having

如果要对聚合操作后的结果进行过滤，可以使用having。

```hql
select address.city, avg(salary) from employees
```

如果给avg(salary)起了别名，having是可以引用这个别名的。

```hql
select address.city, avg(salary) as avg from employees
group by address.city
having avg 8000;
```
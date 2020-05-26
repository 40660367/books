# Hive 基本查询

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

## select语句

先通过`desc tablename`查看表列信息。

```hql
desc employees;
```

### 查询所有列

```hql
select * from employees;
```

### 查询指定列并指定列别名

```hql
select name, salary as employeess_salary from employees; 
```

### 查询计算列

```hql
select upper(name) as name, salary, round(salary * (1 - 0.1)) as real_wages from employees;
```

### 嵌套select 语句

```hql
from (
select upper(name) as name, salary, round(salary * (1 - 0.1)) as real_wages from employees
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

## where过滤条件子句

```hql
select upper(name) as name, salary from employees where salary > 40000;
```

##  模糊匹配 like

like严格来说是匹配通配符。比如%匹配任意多的字符串。

```hql
select name,salary from employees where name like 'M%';
```

## 返回限定:limit

限定查询的行数。

```hql
select name, salary from employees limit 2;
```

## 分组 group by

按一个列或者多个列对数据进行分组，然后对每组的数据进行聚合操作。如下，按address.city进行分组，然后通过avg(salary)求每组的salary的均值。group by之后的可以有一个或多个列。下面的例子只使用了struct类型的address列的一个city字段

```hql
select destination, avg(salary) as avg from employees
group by destination;
```

## 分组过滤 having

如果要对聚合操作后的结果进行过滤，可以使用having。

如果给avg(salary)起了别名，having是可以引用这个别名的。

```hql
select destination, avg(salary) as avg from employees
group by destination
having avg > 40000;
```
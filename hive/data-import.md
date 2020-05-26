# Hive 示例数据准备


## 导入方法

进入hive

```bash
hive
```

执行导入脚本

```
source /share/lesson/hive/data-import.hql;
```


## 导入过程及说明

### 数据文件

**music表数据**

文件名:music.dat

```txt
M-0001,Valder Fields,S-0001,L-0001
M-0002,A Step You Can't Take Back,S-0002,L-0002
M-0003,For You,S-0003,L-0003
M-0004,Life is like a Boat,S-0003,L-0003
M-0005,Fake Song,<unknow>,<unknow>
```

**singer表数据**

文件名:singer.dat

```txt
S-0001,Tamas Wells
S-0002,Keira Knightley
S-0003,Rie fu
S-0004,YUI
```

**language表数据**

文件名:language.dat

```txt
L-0001,Chinese
L-0002,English
L-0003,Japanese
```

**employe表数据**

文件名:employee.dat

```txt
1201,Gopal,45000,Technical manager
1202,Manisha,45000,Proof reader
1203,Masthanvali 40000,Technical writer
1204,Kiran,40000,Hr Admin
1205,Kranthi,30000,Op Admin
```

**products表数据**

文件名:products.dat

```txt
F-000212,Dali milk,2.0,food,China
F-002839,Ice cream,12.0,food,China
F-000233,Banana milk,5.0,food,China
E-001283,Water watch,399,electronics,China
E-230004,S007 Phone,1999,electronic,China
```

### 创建表结构

进入Hive shell创建表结构

```hql
drop table if exists musics;
drop table if exists singers;
drop table if exists languages;
drop table if exists employees;
drop table if exists products;



create table if not exists musics(
  id string,
  name string,
  singerid string,
  languageid string)
row format delimited
fields terminated by ',';

create table if not exists singers(
  id string,
  name string)
row format delimited
fields terminated by ',';

create table if not exists languages(
  id string,
  type string)
row format delimited
fields terminated by ',';

create table if not exists employees ( 
eid int, name String,salary String, destination String)
ROW FORMAT DELIMITED
fields terminated by ',';

create table if not exists products(
id string, name string, price int, type string, locality string)
row format delimited
fields terminated by ',';
```

### 加载表数据

从外部文件加载数据到到表格中

```hql
load data local inpath '/share/lesson/hive/music.dat' into table musics;
load data local inpath '/share/lesson/hive/language.dat' into table languages;
load data local inpath '/share/lesson/hive/singer.dat' into table singers;
load data local inpath '/share/lesson/hive/employee.dat' overwrite into table employees;
load data local inpath '/share/lesson/hive/products.dat' overwrite into table products;
```

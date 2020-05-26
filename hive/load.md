# Hive 数据的装载(load)与导出(export)

一般来说，在SQL创建表后，我们就可以使用INSERT语句插入数据。但在Hive中可以使用LOAD DATA语句插入数据。

同时将数据插入到Hive，最好是使用LOAD DATA来存储大量记录。

有两种方法用来加载数据：一种是从本地文件系统，第二种是从Hadoop文件系统。

### 语法

加载数据的语法如下：

```
LOAD DATA [LOCAL] INPATH 'filepath' [OVERWRITE] INTO TABLE tablename 
[PARTITION (partcol1=val1, partcol2=val2 ...)]
```

- 	LOCAL是标识符指定本地路径。它是可选的。
- 	OVERWRITE 是可选的，覆盖表中的数据。
- 	PARTITION 这是可选的

## 导入数据示例

### 非分区表导入数据示例示例1

文件名:employee.dat

```
1201  Gopal       45000    Technical manager
1202  Manisha     45000    Proof reader
1203  Masthanvali 40000    Technical writer
1204  Kiran       40000    Hr Admin
1205  Kranthi     30000    Op Admin
```

进入Hive Shell,并创建对应数据的非分区表products

```hql
CREATE TABLE IF NOT EXISTS employee ( eid int, name String,
> salary String, destination String)
> COMMENT ‘Employee details’
> ROW FORMAT DELIMITED
> FIELDS TERMINATED BY ‘\t’
> LINES TERMINATED BY ‘\n’
> STORED AS TEXTFILE
```
然后通过`load`将employee.dat导入表中
```
LOAD DATA LOCAL INPATH '/share/lesson/hive/employee.dat' OVERWRITE INTO TABLE employee;
```

### 非分区表导入数据示例示例2

文件名:products.dat

```
F-000212,Dali milk,2.0,food,China
F-002839,Ice cream,12.0,food,China
F-000233,Banana milk,5.0,food,China
E-001283,Water watch,399,electronics,China
E-230004,S007 Phone,1999,electronic,China
```
进入Hive Shell,并创建对应数据的非分区表products

```hql
create table products(id string, name string, price int, type string, locality string)
> row format delimited
> fields terminated by ',';
```

然后通过`load`将products.dat导入表中

```
load data local inpath '/share/lesson/hive/products.dat' overwrite into table products;
```

`local`表示数据在本地。如果数据保存在hdfs上，则无需local关键字。（可选）
`overwrite`表示覆盖重写。如果表目录下存在文件，则会被删除。如果不使用overwrite，则只会将新文件据添加至原目录下。（可选）

`/share/lesson/hive/products.dat`数据文件的路径。通常这里的路径为一个目录，如/path，而不是指向具体的单个文件。如果这里是本地路径，那么数据被上传到到HDFS上来。而如果这是HDFS路径，则数据只是被转移到新的路径下。

### 非分区表导入数据示例

观察products.dat数据，如果经常需要查询来自某个国家的某种类型的产品，则可以将后面的两个字段（`type`，`locality`）作为分区字段。创建一张分区表part_products如下。

```hql
> create table part_products(id string, name string, price int)
           > partitioned by (type string, locality string)
           > row format delimited
           > fields terminated by ',';
```

倘若现在要向（type=food,locality=China）的分区加载数据。我们有一份products-china-food.dat文件，符合分区字段的要求。

文件名:products-china-food.dat

```
F-000212,Dali milk,2.0,food,China
F-002839,Ice cream,12.0,food,China
F-000233,Banana milk,5.0,food,China
```

通过load data加载products-china-food.dat到part_products表的分区目录下。

```hql
load data local inpath '/share/lesson/hive/products-china-food.dat'
> overwrite into table part_products
> partition (locality='China',type='food');
```

# Hive 外部表(external table)

Hive 中的表分为内部表、外部表、分区表和 Bucket 表

## 内部表和外部表的区别

删除内部表，删除表元数据和数据

删除外部表，删除元数据，不删除数据**

## 内部表和外部表的使用选择

大多数情况，他们的区别不明显，如果数据的所有处理都在 Hive 中进行，那么倾向于 选择内部表，但是如果 Hive 和其他工具要针对相同的数据集进行处理，外部表更合适。

使用外部表访问存储在 HDFS 上的初始数据，然后通过 Hive 转换数据并存到内部表中

使用外部表的场景是针对一个数据集有多个不同的 Schema

通过外部表和内部表的区别和使用选择的对比可以看出来，hive 其实仅仅只是对存储在 HDFS 上的数据提供了一种新的抽象。而不是管理存储在 HDFS 上的数据。所以不管创建内部 表还是外部表，都可以对 hive 表的数据存储目录中的数据进行增删操作。

## 外部表Load导入数据

外部表也可以像内部表一样通过load实现数据导入，但这里使用另一种方式，无需load即可实现数据导入。
假设在HDFS上存在数据文件/user/hive/external/etlemployees/data.dat。我们想使用Hive表操纵这个数据，但是表删除时，原数据文件依然保存。那么，应该选择建立外部表。
外部表的创建方式如下所示。其与内部表类似，但略有不同。
1.在table前多了external关键字，表明该表类型为外部表。
2.location的路径为数据存在的路径。注意，此路径只能指向数据存在的文件夹目录，而不能指向文件。否则，执行时会报“路径不是文件夹或者路径无法被创建”的错误。



```hive
create external table if not exists mydb.etlemployees(
  name string comment 'Employee name',
  salary float comment 'Employee salay',
  subordinates array<string> comment 'Names of subordiantes',
  deductions map<string, float> comment '<deductions name, percentages>',
  address struct<street:string, city:string, state:string, zip:int> comment 'Home address')
comment 'Description of the table'
location '/share/lesson/hive/etlemployees.dat'
tblproperties ('creator'='me', 'created_at'='2018-05-16');
```

创建后，可以直接显示表中数据。

```hive
select * from etlemployees;
```

删除该表后，show tables的结果不在存在etlemployees表，但是/user/hive/external/etlemployees/data.dat依然存在。
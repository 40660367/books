# Hive 分区表

表的分区实际上就是在表目录下创建多个子目录，将数据分成多份存在不同的子目录下。而这些数据按照设定的某些字段进行划分。

[环境安装](./setup.html)

### 数据文件准备与说明

例如，存在如下类型的学生数据文件。数据有6个字段，分别为id号、名字、性别、学校和年级。这些数据按学校和年级分为四个文件。

文件名:student-MingShengSchool-Grade1.dat

```
S0001,WangXiaoming,male,MingSheng School,Grade 1
S0003,ZhangSan,male,MingSheng School,Grade 1
```

文件名:student-MingShengSchool-Grade2.dat

```
S0002,ZhangBobo,male,MingSheng School,Grade 2
S0016,XiaoBaiBai,male,MingSheng School,Grade 2
```

文件名:student-DaHuaSchool-Grade1.dat

```
S0002,LiLeilei,male,DaHua School,Grade 1
S0007,LiDahua,male,DaHua School,Grade 1
```

文件名:student-DaHuaSchool-Grade2.dat

```
S0003,LuoDafu,male,DaHua School,Grade 2
S0012,ZhouXiaoJuan,male,DaHua School,Grade 2
```

如果经常需要查询某个学校某个年级的学生，则可以将这些文件按学校和年级进行逐级分区。如下：

```
1级目录              2级目录      
school=MingSheng    School/grade=Grade 1
school=MingSheng    School/grade=Grade 2
school=DaHua        School/grade=Grade 1
school=DaHua        School/grade=Grade 2
```

### 创建分区表

创建相应分区表时，通过`partitioned by`设定学校和年级为分区字段。具体语句如下所示，`create()`中定义的字段和`partitioned by()`的字段是分开的。两者组成了完整的字段。将下述写入create_part_tbl.hql文件中。

```bash
cat > create_part_tbl.hql << EOF
create table student (
id string,
name string,
sex string
)
partitioned by (school string, grade string)
row format delimited
fields terminated by ','
EOF
```

进入hive,使用`source`执行create_part_tbl.hql

```hive
source ./create_part_tbl.hql;
```

### 分区数据导入

创建表后，导入分区的数据。首先导入文件1：student-MingShengSchool-Grade1.dat

```sql
load data local inpath '/share/lesson/hive/student-MingShengSchool-Grade1.dat'
into table student
partition (school = 'MingSheng School', grade='Grade 1');
```

这一步完成后，在hive shell中使用如下命令，查看HDFS文件系统中的这个路径会发现：

```hql
dfs -ls /user/hive/warehouse/student;
```

出现了了`school=MingSheng School`。

请接着按如上方法依次导入剩下的3种文件。

### 查看分区

显示分区目录。

```
show partitions student;
```

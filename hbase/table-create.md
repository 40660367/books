# HBase 创建表(table create)

可以使用命令创建一个表，在这里必须指定表名和列族名。在HBase shell中创建表的语法如下所示。

```
create '<table name>','<column family>'
```

### 示例

下面给出的是一个表名为emp的样本模式。它有两个列族：“personal data”和“professional data”。

| Row key | personal data | professional data |
| ------- | ------------- | ----------------- |
|         |               |                   |

在HBase shell创建该表如下所示。

```hbase
create 'emp', 'personal data', ’professional data’
```

## 	验证创建

可以验证是否已经创建，使用 **list** 命令如下所示。在这里，可以看到创建的emp表。

```hbase
list
```

## 创建学生信息表

rowkey要求是学号，一个列簇，包含姓名、性别、年龄、地址。

```hbase
create 'student' 'info'
put 'student','2016211883','info:name','stu1'
```




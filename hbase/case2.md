# HBase Shell操作案例2

[环境准备](./setup.html)

**使用exists命令查看table_name表是否存在**

```
exists 'mytable'  
```

**使用desc命令来查看一下table_name表结构**

```
desc 'mytable'  
```

**修改table_name的表结构**

将TTL（生存周期）改为30天，这里要注意，修改表结构前必须先disable使表失效，修改完成后再使用enable命令，使表重新生效（可用is_enabled 'table_name'或is_disabled 'table_name'判断表的状态）

```
disable 'mytable'  
alter 'table_name',{NAME=>'f1',TTL=>'2592000'} 
enable 'mytable'  
```

**使用desc命令来验证一下修改后的table_name表结构**

```hbase
desc table_name
```

**现在我们使用put命令向table_name表中插入一行数据**

```
put 'table_name','rowkey001','f1:col1','value1' 
put 'table_name','rowkey001','f1:col2','value2' 
put 'table_name','rowkey002','f1:col1','value1' 
```

这其中，'table_name'为表名，'rowkey001'为rowkey，'f1:col1' f1为列族，col1为列，'value1'为值，同一个列族下可以有多个列，同一个rowkey视为同一行。

**使用get命令来查询一下table_name表，rowkey001中的f1下的col1的值**

```
get 'table_name','rowkey001', 'f1:col1' 
```

由于我们的数据只有2行，所以查询结果为2

**查询表table_name，rowkey001中的f1下的所有列值**

```
get 'table_name','rowkey001' 
```

**使用scan命令扫描全表**

```
scan 'mytable'  
```

也可以限定扫描表的前几行数据，我们扫描前1行数据

```
scan 'table_name',{LIMIT=>1} 
```

由此也可以看出，rowkey相同的数据视为一行数据

**使用count命令，查看table_name表中的数据行数**

INTERVAL设置多少行显示一次及对应的rowkey，默认1000；CACHE每次去取的缓存区大小，默认是10，调整该参数可提高查询速度

查询表table_name中的数据行数，每10条显示一次，缓存区为200

```
count 'table_name', {INTERVAL => 10, CACHE => 200} 
```

由于我们的数据只有2行，所以查询结果为2

**使用deleteall命令，删除table_name表中rowkey002这行数据**

```
deleteall 'table_name','rowkey002'
```

**使用truncate命令，删除table_name表中的所有数据**

（语法： truncate <table> 其具体过程是：disable table -> drop table -> create table）

```
truncate 'mytable'  
```


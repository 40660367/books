# MySQL 主从复制 验证

## 在主机`{host0.hostname}`上进行如下操作

在右侧实验区`root@{host0.hostname}:~#`提示符后进行如下操作

```bash
#密码为上一节设置的abcabc
mysql -u root -p
```

执行以下语句用于在主机`{host0.hostname}`上的建立一个新的数据库test1,并在此数据库下建立表格t11后，并退出。
```sql
create database test1;
use test1;
create table t11(id int);
```
使用`show processlist`命令，查看复制进程的提示中State是否为`Master has sent all binlog to slave; waiting for more updates`
```sql
show processlist\G
exit;
```



## 在从机`{host1.hostname}`上进行如下操作

连接到从机`{host1.hostname}`，验证是否同步了主机的操作。从右侧实验区的终端界面使用ssh命令进入从机`{host1.hostname} `

```bash
ssh root@{host1.ip}
```

密码为:`{host1.token}`

进入从机后`{host1.hostname}`后，命令行提示符应变为`root@{host1.hostname}:~#`

进入从机的mysql,密码为abcabc

```bash
mysql -uroot -p
```

使用`show processlist`命令，查看复制进程的提示中State是否为` Waiting for master to send event`和`Slave has read all relay log; waiting for more updates`,该种状态标明复制进程工作正常。
```sql
show processlist\G
```

查看是否同步了主机的test1数据库
```sql
show databases;
```
查看是否同步了主机的test1数据库中的数据表t11
```sql
use test1;
show tables;
```

如果显示与`{host0.hostname}`相同，恭喜您，则证明MySQL主从复制架构搭建完完成并工作正常。
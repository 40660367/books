# MySQL 主从复制 从机配置

## 在从机`{host1.hostname}`上进行如下操作

从右侧实验区的终端界面使用ssh命令进行从机`{host1.hostname} `

```bash
ssh root@{host1.ip}
```

密码为:`{host1.token}`

进入从机后`{host1.hostname}`后，命令行提示符应变为`root@{host1.hostname}:~# `

在从机上进行如下操作：

```bash
cd /usr/local/
cp /share/tar/mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz .
tar xvf mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz
rm mysql-5.7.19-linux-glibc2.12-x86_64.tar.gz
mv mysql-5.7.19-linux-glibc2.12-x86_64 /usr/local/mysql
```

配置MySQL用户

```bash
groupadd mysql
useradd -r -g mysql mysql
```

配置相关目录及权限

```bash
chown -R mysql  /usr/local/mysql
chgrp -R mysql /usr/local/mysql

#准备数据目录
mkdir -p /data/mysql
chown -R mysql:mysql /data/mysql
chmod -R 755 /data/mysql

mkdir -p /usr/local/mysql/mysqld
chown -R mysql:mysql /usr/local/mysql/mysqld
chmod -R 755 /usr/local/mysql/mysqld
```

配置相关环境变量

```bash
ln -fs /usr/local/mysql/bin/mysql /usr/local/bin/mysql
cp /usr/local/mysql/support-files/mysql.server /etc/init.d/mysqld
MYSQL_HOME=/usr/local/mysql/bin
PATH=$MYSQL_HOME/bin:$PATH
export MYSQL_HOME
```

安装必要的支持

```bash
apt update && apt install libaio1 numactl -y
```

生成从机上的MySQL配置文件

```bash
cat >/etc/my.cnf << EOF
[mysqld]
server_id=12
log-bin=mysql-bin
#binlog-do-db=test
sql_mode=NO_ENGINE_SUBSTITUTION,STRICT_TRANS_TABLES
explicit_defaults_for_timestamp=true
basedir = /usr/local/mysql/
datadir = /data/mysql
port = 3306
socket = /usr/local/mysql/mysqld/mysql.sock
pid-file = /usr/local/mysql/mysql.pid
character-set-server=utf8
back_log = 300
max_connections = 3000
max_connect_errors = 50
table_open_cache = 4096
max_allowed_packet = 32M
max_heap_table_size = 128M
read_rnd_buffer_size = 16M
sort_buffer_size = 16M
join_buffer_size = 16M
thread_cache_size = 16
query_cache_size = 128M
query_cache_limit = 4M
ft_min_word_len = 8
thread_stack = 512K
transaction_isolation = REPEATABLE-READ
tmp_table_size = 128M
long_query_time = 6
innodb_buffer_pool_size = 1G
innodb_thread_concurrency = 16
innodb_log_buffer_size = 16M
innodb_log_file_size = 512M
innodb_log_files_in_group = 3
innodb_max_dirty_pages_pct = 90
innodb_lock_wait_timeout = 120
innodb_file_per_table = on
[mysqldump]
quick
max_allowed_packet = 32M
[mysql]
no-auto-rehash
default-character-set=utf8
safe-updates
[myisamchk]
key_buffer = 16M
sort_buffer_size = 16M
read_buffer = 8M
write_buffer = 8M
[mysqlhotcopy]
interactive-timeout
[mysqld_safe]
open-files-limit = 8192
[client]
port = 3306
socket = /usr/local/mysql/mysqld/mysql.sock
default-character-set = utf8
EOF
```

开始初始化MYSQL配置文件

```bash
/usr/local/mysql/bin/mysqld --user=mysql --basedir=/usr/local/mysql --datadir=/data/mysql --initialize
```

注意：

一定要**记住临时密码，出现在初始化过程中的[Note] A temporary password is generated for root@localhost**后边。

启动MySQL服务

```bash
/etc/init.d/mysqld start
```

登陆MySQL，使用上边初始化时产生的临时密码

```bash
mysql -uroot -p
```

重新设置密码

```mysql
set password=password('abcabc')
```

设置主机信息

```mysql
CHANGE MASTER TO MASTER_HOST='{host0.ip}',MASTER_PORT=3306,MASTER_USER='replicationtester',MASTER_PASSWORD='123456',MASTER_LOG_FILE='mysql-bin.000002',MASTER_LOG_POS=154;
```

启动复制

```mysql
start slave;
```

查看从机复制状态
```mysql
show slave status\G
```

会出现以下类似信息：

```txt
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 172.165.46.11
                  Master_User: mstest
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000002
          Read_Master_Log_Pos: 701
               Relay_Log_File: node1-relay-bin.000002
                Relay_Log_Pos: 867
        Relay_Master_Log_File: mysql-bin.000002
             Slave_IO_Running: Yes
            Slave_SQL_Running: Yes
              Replicate_Do_DB: 
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0
                   Last_Error: 
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 701
              Relay_Log_Space: 1074
              Until_Condition: None
               Until_Log_File: 
                Until_Log_Pos: 0
           Master_SSL_Allowed: No
           Master_SSL_CA_File: 
           Master_SSL_CA_Path: 
              Master_SSL_Cert: 
            Master_SSL_Cipher: 
               Master_SSL_Key: 
        Seconds_Behind_Master: 0
Master_SSL_Verify_Server_Cert: No
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
  Replicate_Ignore_Server_Ids: 
             Master_Server_Id: 11
                  Master_UUID: a0542e1c-9b6a-11ea-a548-00000045a233
             Master_Info_File: /data/mysql/master.info
                    SQL_Delay: 0
          SQL_Remaining_Delay: NULL
      Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
           Master_Retry_Count: 86400
                  Master_Bind: 
      Last_IO_Error_Timestamp: 
     Last_SQL_Error_Timestamp: 
               Master_SSL_Crl: 
           Master_SSL_Crlpath: 
           Retrieved_Gtid_Set: 
            Executed_Gtid_Set: 
                Auto_Position: 0
         Replicate_Rewrite_DB: 
                 Channel_Name: 
           Master_TLS_Version:
```

**注意其中这两部分：**

```txt
Slave_SQL_Running_State: Slave has read all relay log; waiting for more updates
```

```txt
Slave_IO_State: Waiting for master to send event
```

当出现该提示，即证明主从已经搭建完成。
# MySQL 主从复制 Master主机配置

## 在主机`{host0.hostname}`上进行如下操作

在右侧实验区`root@{host0.hostname}:~#`提示符后进行如下操作

复制MySQL安装文件并解压到合适的目录

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

生成`{host0.hostname}`上的MySQL配置文件

```bash
cat >/etc/my.cnf << EOF
[mysqld]
server_id=11
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

一定要**记住临时密码，出现在初始化过程中的[Note] A temporary password is generated for root@localhost**后边12位长度的随机数字字母串。

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
set password=password('abcabc');
```
创建复制用户`replicationtester`并授权

```mysql
GRANT REPLICATION SLAVE,FILE ON *.* TO 'replicationtester'@'{host1.ip}' IDENTIFIED BY '123456';
```
查看binlog信息，记住当前binlog日志文件名及位置信息，用于在从机上进行配置。
```mysql
show master status;
```

**MySQL binlog扩展**

> 只查看第一个binlog文件的内容
> show binlog events;
>
> 查看指定binlog文件的内容
> show binlog events in 'mysql-bin.000002';
>
> 获取binlog文件列表
> show binary logs;
>
> show variables like 'log%';
>
> 清空所有binlog日志
> reset master;
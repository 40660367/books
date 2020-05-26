# SQLite 安装及导入示例数据库

## 在线上环境安装配置SQLite3

使用以下命令安装SQLite3：

```shell
apt update && apt install sqlite3 -y
```

安装完成后在命令行键入查看sqlite3版本信息

```shell
sqlite3 -version
```

直接键入sqlite3命令，进行sqlite环境

```shell
sqlite3
```

进入sqlite3环境后，提示符位置将会显示`sqlite> `，与操作系统做区别。

在sqlite3环境中键.quit，退出sqlite3环境

```sql
.quit
```

## 导入示例数据库			

先在linux系统下查看示例数据库的内容

```shell
cat /share/lesson/sqlite/sample.sql
```

再从Linux终端键入sqlite3，进入

```shell
sqlite3
```

如果该步报错，则说明系统还没有安装好sqlite。

导入示例数据库

```sql
.read /share/lesson/sqlite/sample.sql
.tables
```

查看其中有哪些表

```sql
.tables
```

看看`COMPANY`表中有哪些内容

```sql
SELECT * FROM COMPANY;
```

现在环境已经配置完成，可以进入课程各章节进行学习了。
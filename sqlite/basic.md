# SQLite 概念和命令

SQLite命令与SQL命令类似。 有三种类型的SQLite命令：

- **DDL**：数据定义语言
- **DML**：数据操作语言
- **DQL**：数据查询语言

## 数据定义语言

数据定义语言中主要有三个命令：

- **CREATE**：此命令用于创建表，数据库中的表或其他对象的视图。
- **ALTER**：此命令用于修改现有的数据库对象，如表。
- **DROP**：`DROP`命令用于删除整个表，数据库中的表或其他对象的视图。

## 数据操作语言

数据操作语言中主要有三个命令：

- **INSERT**：此命令用于创建记录。
- **UPDATE**：用于修改记录。
- **DELETE**：用于删除记录。

## 数据查询语言

- **SELECT**：此命令用于从一个或多个表中检索某些记录。

## SQLite的点命令

以下是SQLite点(`.`)命令的列表。 这些命令不会以分号(`;`)终止。

**.help**

可在任何时候使用“`.help`”检查点命令列表。

```shell
.help
```

以上是各种SQLite的点(`.`)命令的列表。 命令及其描述如下表所示：

| 命令                    | 描述说明                                                     |
| ----------------------- | ------------------------------------------------------------ |
| `.backup ?db? file`     | 备份数据库(默认“`main`”)到文件中                             |
| `.bail on/off`          | 遇到错误后停止,默认为`off`                                   |
| `.databases`            | 附件数据库的列表名称和文件                                   |
| `.dump ?table?`         | 以sql文本格式转储数据库。如果指定表，则只转储表匹配像模式表。 |
| `.echo on/off`          | 打开或关闭`echo`命令                                         |
| `.exit`                 | 退出`sqlite`提示符                                           |
| `.explain on/off`       | 转向输出模式适合说明`on/off`。如没有参参数，则它为`on`。     |
| `.header(s) on/off`     | 打开或关闭标题的显示                                         |
| `.help`                 | 显示指定帮助消息                                             |
| `.import file table`    | 将数据从文件导入表                                           |
| `.indices ?table?`      | 显示所有索引的名称。如果指定表，则只显示匹配的表的索引，如模式表。 |
| `.load file ?entry?`    | 加载扩展库                                                   |
| `.log file/off`         | 打开或关闭日志记录。文件可以是`stderr/stdout`                |
| `.mode mode`            | 设置输出模式                                                 |
| `.nullvalue string`     | 打印字符串代替空值                                           |
| `.output filename`      | 发送输出到文件名                                             |
| `.output stdout`        | 发送输出到屏幕                                               |
| `.print string...`      | 打印文字字符串                                               |
| `.prompt main continue` | 替换标准提示                                                 |
| `.quit`                 | 退出`sqlite`提示符                                           |
| `.read filename`        | 在文件名中执行sql                                            |
| `.schema ?table?`       | 显示创建语句。如果指定表，则只显示与模式表匹配的表。         |
| `.separator string`     | 更改分隔符由输出模式和`.import`使用                          |
| `.show`                 | 显示各种设置的当前值                                         |
| `.stats on/off`         | 打开或关闭统计信息                                           |
| `.tables ?pattern?`     | 列出匹配类似模式的表的名称                                   |
| `.timeout ms`           | 尝试打开锁定的表毫秒                                         |
| `.width num num`        | 设置“列”模式的列宽                                           |
| `.timer on/off`         | 打开或关闭cpu定时器测量                                      |

**.show命令**

可以使用`.show`命令查看SQLite命令提示符的默认设置。

> **注意**：不要在`sqlite>`提示符和`.`命令之间放置空格，否则将不起作用。

**其它特殊点命令**

有一些点(`.`)命令用于格式化输出。这些命令是：

```shell
.header on

.mode column

.timer on
```
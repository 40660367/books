# mongoDB 环境安装及配置 			

## 本课程在线环境的安装

### 安装

```bash
#更新源及安装
apt update && apt install mongodb -y
```

```bash
#验证安装是否成功
mongo -version
```

### 启动mongodb服务

首先，我们需要通过以下命令来检查mongodb服务器是否启动：

```bash
service mongodb status
```

如果mongodb已经启动，以上命令将输出mongodb服务的状态。

如果mongodb未启动，你可以使用以下命令来启动MySQL服务器:

```bash
service mongodb start
```

该服务使用/etc/mongodb.conf这个文件作为配置文件

```bash
mongo
```

当出现如下提示时，证明您已经连接上了mongdb，在 `>` 命令提示窗口，

```
MongoDB shell version v3.6.3
connecting to: mongodb://127.0.0.1:27017
MongoDB server version: 3.6.3
```

我们可以使用mongodb命令，进行操作，例如使用**"show dbs"** 命令可以显示所有数据的列表。

```sql
show dbs
```

退出命令提示窗口可以使用 `exit` 命令，返回到Linux系统中。如下所示：

```sql
exit
```

### 环境安装完成

到此本课程环境安装并验证完成。您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**
# MongoDB 分片

在Mongodb里面存在另一种集群，就是分片技术,可以满足MongoDB数据量大量增长的需求。

当MongoDB存储海量的数据时，一台机器可能不足以存储数据，也可能不足以提供可接受的读写吞吐量。这时，我们就可以通过在多台机器上分割数据，使得数据库系统能存储和处理更多的数据。

## 为什么使用分片

- 复制所有的写入操作到主节点
- 延迟的敏感数据会在主节点查询
- 单个副本集限制在12个节点
- 当请求量巨大时会出现内存不足。
- 本地磁盘不足
- 垂直扩展价格昂贵

## MongoDB分片

下图展示了在MongoDB中使用分片集群结构分布：

![img](./images/sharding.png)

上图中主要有如下所述三个主要组件：

- Shard:

  用于存储实际的数据块，实际生产环境中一个shard server角色可由几台机器组个一个replica set承担，防止主机单点故障

- Config Server:

  mongod实例，存储了整个 ClusterMetadata，其中包括 chunk信息。

- Query Routers:

  前端路由，客户端由此接入，且让整个集群看上去像单一数据库，前端应用可以透明使用。

## 分片实例

分片结构端口分布设计如下：

```
Shard Server 1：27021
Shard Server 2：27022
Shard Server 3：27023
Shard Server 4：27024
Config Server ：27100
Route Process：40000
```

#### 步骤一：启动Shard Server

```
mkdir -p /mongoDB/shard/s1
mkdir -p /mongoDB/shard/s2
mkdir -p /mongoDB/shard/s3
mkdir -p /mongoDB/shard/s4
mkdir -p /mongoDB/shard/log
```

```bash
kill `pidof mongod`
mongod --port 27021 --dbpath=/mongoDB/shard/s1 --logpath=/mongoDB/shard/log/s1.log --logappend --fork
mongod --port 27022 --dbpath=/mongoDB/shard/s2 --logpath=/mongoDB/shard/log/s2.log --logappend --fork
mongod --port 27023 --dbpath=/mongoDB/shard/s3 --logpath=/mongoDB/shard/log/s3.log --logappend --fork
mongod --port 27024 --dbpath=/mongoDB/shard/s4 --logpath=/mongoDB/shard/log/s4.log --logappend --fork
```

#### 步骤二： 启动Config Server

```bash
mkdir -p /mongoDB/shard/config
mongod --port 27100 --dbpath=/mongoDB/shard/config --logpath=/mongoDB/shard/log/config.log --logappend --fork
```

```bash
ps -ef | grep mongod #查看已经启动的进程
```

**注意：**这里我们完全可以像启动普通mongodb服务一样启动，不需要添加—shardsvr和configsvr参数。因为这两个参数的作用就是改变启动端口的，所以我们自行指定了端口就可以。

#### 步骤三： 启动Route Process(未成功)

```bash
mongos --port 40000 --configdb cf1/localhost:27100 --fork --logpath=/mongoDB/shard/log/route.log &
```

#### 步骤四： 配置Sharding

接下来，我们使用MongoDB Shell登录到mongos，添加Shard节点

```bash
mongo admin --port 40000
```

```sql
db.runCommand({ addshard:"localhost:27021" })
db.runCommand({ addshard:"localhost:27022" })
db.runCommand({ addshard:"localhost:27023" })
db.runCommand({ addshard:"localhost:27024" })
```
设置分片存储的数据库
```
db.runCommand({ enablesharding:"test" }) 
db.runCommand({ shardcollection: "test.log", key: { id:1,time:1}})
```

### 步骤五： 

程序代码内无需太大更改，直接按照连接普通的mongo数据库那样，将数据库连接接入接口40000


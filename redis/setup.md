# Redis 环境安装配置

## 本课程在线环境的安装

要在Ubuntu上安装Redis，打开终端并键入以下命令 -

```shell
apt-get update && apt-get install redis-server -y
```

**启动redis**

```shell
#加&是让redis-server运行在后台，按enter按后，即可不阻塞当前终端。
redis-server &
```

**使用redis自带客户自带客户端连接Redis-server**

```shell
redis-cli
```

这将打开一个**redis**提示，如下所示 - 

```
127.0.0.1:6379>
```

在上面的提示中，`127.0.0.1`是计算机的IP地址，`6379`是运行**Redis**服务器的默认端口。 键入`PING`命令。

```shell
ping
```

如返回为`PONG`

即表明**Redis**已在当前学习环境成功安装运行，并返回了客户端的请求。即证明您已经在您当前的云环境中安装成功，您就可以开始进行本课程下一步的学习了。

注：当云环境的生命周期失效后，需要重新进行安装。

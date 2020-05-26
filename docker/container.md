# Docker 容器操作(container)

## Docker 客户端

docker 客户端非常简单 ,我们可以直接输入 docker 命令来查看到 Docker 客户端的所有命令选项。

```bash
docker
```

可以通过命令 **docker command --help** 更深入的了解指定的 Docker 命令使用方法。

例如我们要查看 **docker stats** 指令的具体使用方法：

```bash
docker stats --help
```

## 容器使用

### 获取镜像

如果我们本地没有ubuntu:20.04镜像，我们可以使用 docker pull 命令来载入 ubuntu 镜像：

```bash
docker pull ubuntu:20.04
```

### 启动容器

以下命令使用 ubuntu 镜像启动一个容器，参数为以命令行模式进入该容器：

```bash
docker run -it --name c20 ubuntu:20.04 /bin/bash
```

参数说明：

- **-i**: 交互式操作。
- **-t**: 终端。
- **ubuntu:16.04**: ubuntu 镜像，版本为16.04
- **/bin/bash**：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 /bin/bash。

要退出终端，直接输入 **exit**:

```bash
exit
```

### 停止运行的容器

停止容器的命令如下：

```bash
docker stop c20 #c20为容器名或容器ID都可以
```

停止的容器可以通过 docker restart 重启：

```bash
docker restart c20 #c20为容器名或容器ID都可以
```

### 启动已停止运行的容器

查看所有的容器命令如下：

```bash
docker ps -a
```

使用 docker start 启动一个已停止的容器：

```bash
docker start c20
```

在使用 **-d** 参数时，容器启动后会进入后台。此时想要进入容器，可以通过以下指令进入：

- **docker attach**
- **docker exec**：推荐大家使用 docker exec 命令，因为此退出容器终端，不会导致容器的停止。

**attach 命令**

下面演示了使用 docker attach 命令。

```bash
docker attach c20
```

**注意：** 如果从这个容器退出，会导致容器的停止。

**exec 命令**

下面演示了使用 docker exec 命令。

```bash
docker exec -it c20 /bin/bash
```

**注意：** 如果从这个容器退出，不会导致容器的停止，这就是为什么推荐大家使用 **docker exec** 的原因。

更多参数说明请使用 **docker exec --help** 命令查看。

### 导出和导入容器

**导出容器**

如果要导出本地某个容器，可以使用 **docker export** 命令。

```bash
docker export c20 > ~/c20.tar
```

导出容器 c20快照到本地文件 c20.tar。这样将导出容器快照到本地文件。

**导入容器快照**

可以使用 docker import 从容器快照文件中再导入为镜像，以下实例将快照文件 redis.tar 导入到镜像 redis:latest:

```bash
docker import /share/images/redis.tar redis:latest
docker images #验证
```

### 删除容器

删除容器使用 **docker rm** 命令：

```bash
docker rm -f c20
#要删除一个容器，其必须在停止的状态
#参数 -f 代表为强制删除
```

下面的命令可以清理掉所有处于终止状态的容器。

```bash
docker container prune
```

```response
WARNING! This will remove all stopped containers.
Are you sure you want to continue? [y/N]
```


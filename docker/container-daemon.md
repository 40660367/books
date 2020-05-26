# Docker 容器以后台方式运行

## 以后台方式运行容器

在大部分的场景下，我们希望 docker 的服务是在后台运行的，我们可以过 **-d** 指定容器的运行模式。

**注：**加了 **-d** 参数默认不会进入容器，想要进入容器需要使用指令 **docker exec**（下面会介绍到）。

使用以下命令创建一个以进程方式运行的容器

```bash
docker run -d --name c30 ubuntu:20.04 /bin/sh -c "while true; do echo hello world！; sleep 3; done"
```

在输出中，我们没有看到期望的 "hello world"，而是一串长字符

这个长字符串叫做容器 ID，对每个容器来说都是唯一的，我们可以通过容器 ID 来查看对应的容器发生了什么。

首先，我们需要确认容器有在运行，可以通过 **docker ps** 来查看：

```bash
docker ps
```

输出详情介绍：

**CONTAINER ID:** 容器 ID。

**IMAGE:** 使用的镜像。

**COMMAND:** 启动容器时运行的命令。

**CREATED:** 容器的创建时间。

**STATUS:** 容器状态。

状态有7种：

- created（已创建）
- restarting（重启中）
- running（运行中）
- removing（迁移中）
- paused（暂停）
- exited（停止）
- dead（死亡）

**PORTS:** 容器的端口信息和使用的连接类型（tcp\udp）。

**NAMES:** 自动分配的容器名称。

在宿主主机内使用 多次使用**docker logs** 命令，查看容器内的标准输出：

```bash
docker logs c30
```

## 进入后台运行中的容器

```bash
docker exec -it c30 bash
```

这样我们就可以进入到已经在后台中运行的容器，执行各类操作了。
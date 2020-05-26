# Docker Web应用实例

我们尝试使用 docker 构建一个 web 应用程序。

我们将在docker容器中运行一个 Python Flask 应用来运行一个web应用。

```bash
docker load < /share/images/training.webapp.tar  # 载入镜像
docker run -d -p 5000:5000 --name casewebapp training/webapp python app.py
```

参数说明:

- **-d:**让容器在后台运行。
- **-p:**将容器内部使用的网络端口映射到我们使用的主机上。
- **--name**:创建容器名为`casewebapp`

## 查看 WEB 应用容器

使用 docker ps 来查看我们正在运行的容器：

```bash
docker ps
```

注意，这里多了端口信息。

```
PORTS
0.0.0.0:5000->5000/tcp
```

Docker 开放了 5000 端口（默认 Python Flask 端口）映射到主机端口 5000上。

这时，我们就可以通过访问本地主机的 5000 端口，从而访问到容器`casewebapp`的5000端口。

验证

```
curl localhost:5000
```

**docker ps**查看正在运行的容器

```bash
docker ps
```

## 网络端口的快捷方式

通过 **docker ps** 命令可以查看到容器的端口映射，**docker** 还提供了另一个快捷方式 **docker port**，使用 **docker port** 可以查看指定 （ID 或者名字）容器的某个确定端口映射到宿主机的端口号。

上面我们创建的 web 应用容器名字为 **casewebapp**。

我可以使用**docker port casewebapp** 来查看容器端口的映射情况。

```bash
docker port casewebapp
```

## 查看 WEB 应用程序日志

`docker logs`  可以查看容器内部的标准输出。

```bash
docker logs -f casewebapp
```

**-f:** 让 **docker logs** 像使用 **tail -f** 一样来输出容器内部的标准输出。

从上面，我们可以看到应用程序使用的是 5000 端口并且能够查看到应用程序的访问日志。

## 查看WEB应用程序容器的进程

我们还可以使用 docker top 来查看容器内部运行的进程

```bash
docker top casewebapp
```

## 检查 WEB 应用程序

使用 **docker inspect** 来查看 Docker 的底层信息。它会返回一个 JSON 文件记录着 Docker 容器的配置和状态信息。

```bash
docker inspect casewebapp
```

## 停止 WEB 应用容器

```bash
docker stop casewebapp
```

## 重启WEB应用容器

已经停止的容器，我们可以使用命令`docker start`来启动。

```bash
docker start casewebapp
```

查询最后一次创建的容器：

```bash
docker ps -l
```

正在运行的容器，我们可以使用 **docker restart** 命令来重启。

## 移除WEB应用容器

我们可以使用 docker rm 命令来删除不需要的容器

```bash
docker rm casewebapp  
```

删除容器时，容器必须是停止状态，否则会报如下类似错误

```response
Error response from daemon: You cannot remove a running container 
```
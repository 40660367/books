# Docker 仓库操作(Repository)

仓库（Repository）是集中存放镜像的地方。以下介绍一下 [Docker Hub](https://hub.docker.com/)。

## Docker Hub

目前 Docker 官方维护了一个公共仓库 [Docker Hub](https://hub.docker.com/)。

大部分需求都可以通过在 Docker Hub 中直接下载镜像来实现。

### 注册

在 [https://hub.docker.com](https://hub.docker.com/) 免费注册一个 Docker 账号。

### 登录和退出

登录需要输入用户名和密码，登录成功后，我们就可以从 docker hub 上拉取自己账号下的全部镜像。

```bash
docker login
```

**退出**

退出 docker hub 可以使用以下命令：

```bash
docker logout
```

**拉取镜像**

你可以通过 docker search 命令来查找官方仓库中的镜像，并利用 docker pull 命令来将它下载到本地。

以 ubuntu 为关键词进行搜索：

```bash
docker search ubuntu
```

使用 docker pull 将官方 ubuntu 镜像下载到本地：

```bash
docker pull ubuntu 
```

### 推送镜像

用户登录后，可以通过 docker push 命令将自己的镜像推送到 Docker Hub。

以下命令中的 username 请替换为你的 Docker 账号用户名。

```bash
docker tag ubuntu:18.04 yourusername/ubuntu:18.04
docker push yourusername/ubuntu:18.04
```

push提示成功后，登陆docker hub便可以看到刚刚推上去的镜像。
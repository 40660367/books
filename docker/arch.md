# Docker 架构

Docker遵循客户端 - 服务器架构。 其架构主要分为三个部分。

1. **客户端(Client)**：Docker提供命令行界面(CLI)工具，客户端与Docker守护进程交互。客户端可以构建，运行和停止应用程序。客户端还可以远程与`Docker_Host`进行交互。Docker客户端是许多Docker用户与Docker进行交互的主要方式。当使用`docker run`这样的命令时，客户端将这些命令发送到Docker守护进程。docker命令使用**Docker API**。

2. **Docker_Host**：它包含容器，映像和Docker守护程序。它提供完整的环境来执行和运行应用程序。

   其中**Docker守护进程**是一个用于监听Docker API请求的进程。 它还管理Docker对象，如：映像，容器，网络等。守护进程还可以与其他守护进程通信以管理Docker服务。
   
3. **注册表(Registry)**：它是全局映像库。可以访问并使用这些映像在Docker环境中运行应用程序。

   Docker注册表用于存储Docker映像。Docker提供**Docker Hub**和**Docker Cloud**，这是任何人都可以使用的公共注册表。Docker配置为默认在**Docker Hub**上查找映像。当我们使用`docker pull`或`docker run`命令时，从配置的注册表中提取所需的映像。 当使用`docker push`命令时，映像被推送到配置的注册表中。


![img](./images/arch.png)
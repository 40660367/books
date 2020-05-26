# kubectl 的基本使用

kubectl 是与 kubernetes 集群交互的一个命令行工具。我们可以用它来查看和管理 kubernetes 集群。

kubectl 是一个相对独立的工具。它可以配置用来访问本地的集群，也可以用来访问远端的集群。这些都可以保存在配置文件里并通过 context 进行切换。

kubernetes 对外通过 http 端口暴露服务，kubectl 正是通过与 kubernets api server 的 http 端口交互来操作集群。

### 使用kubectl查看k8s集群的版本和基本信息

```bash
kubectl cluster-info
```

可以看到， kubernetes 监听了本地的 32768 端口， kubectl 正是通过此端口与 kubernetes api server （master）交互。

版本信息里面显示了 client (kubectl) 以及 server( api server) 组件的版本等详细信息。

### 使用kubectl查看k8s集群结构

`pods`是类似于 docker 中 container 的概念，是 kubernetes 最基本的单元之一。可以看到， kubernetes 本身的组件也是通过容器化的方式运行在集群中，并且都存在于 kube-system 这个 namespace 下。

这些组件有：

- `etcd`： kubernetes 的存储组件。kubernetes 中的数据主要都存在于其中，比如我们之前提到的 ConfigMap,、Namespace 等各种 Resource。
- `apiserver`: kubernetes 对外提供 API 服务的组件，它也主要负责与 etcd 交互。
- `scheduler`: 负责调度 pod 的组件。当我们想在一堆机器中运行 pod 时，它负责决定将 pod 运行在哪个机器上。
- `controller-manager`: 当 pod 调度到机器上之后，其它服务将 pod 运行起来。controller manager 相当于一个具体执行任务的组件。V
- `proxy`: 负责 pod / 服务 访问的组件，每个机器上都会有一个，所以上面会有三个（三个节点）
- `dns`: 负责集群内的 dns 功能。
- `dashboard`: 提供了一个 UI 管理界面，是可选组件。本次实验中用不到，可忽略其错误。

可以将上面的 Pods 列表与 Kubernetes 集群的架构图对比观察：

![此处输入图片的描述](./images/cluster-arch.png)

其中 kubelet 是每个节点上都会有的 agent，负责本机器上的一些任务执行。



kubernetes 自身的组件也是通过上面所说的 Resource 结构来呈现的。之前说过，集群有一个已经创建的 namespace 叫 kube-system, 我们可以通过研究下它里面的内容来查看下集群结构：

```bash
kubectl get pods -n kube-system
```

### 查看 kubernetes 集群配置文件

在当前用户的目录下,我们可以看到 kubectl 的配置文件的内容：

```bash
cat ~/.kube/config
```

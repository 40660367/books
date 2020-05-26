# Kubernetes Pod启动阶段(phase)

Pod 创建完之后，一直到持久运行起来，中间有很多步骤，也就有很多出错的可能，因此会有很多不同的状态。一般来说，pod 这个过程包含以下几个步骤：

1. 调度到某台机器上。kubernetes 根据一定的优先级算法选择一台机器将其作为 pod 运行的机器
2. 拉取镜像
3. 挂载存储配置等
4. 运行起来。如果有健康检查，会根据检查的结果来设置其状态。

我们看下刚才的 pod 的状态结果：

分别包含了 pod 级别的信息以及各个 container 的信息。pod 部分的信息如下：

- `hostIP`: pod 所在主机的 ip

- phase

  : pod 的状态，目前是 Running。其它的可能状态有

  - `Pending`: 一般表示还没有开始调度到某台机器上。如果没有符合条件的主机，就会一直处于 Pending 状态
  - `Running`: 运行中
  - `Succeeded`：有些 pod 不是长久运行的，比如 cronjob,一段时间就结束了。需要反馈任务执行的结果
  - `Failed`：pod 的 container 异常退出，比如 command 写的有问题
  - `Unknown`：未知。比如 pod 所在的机器无法连接

- `podIP`: pod 所分配到的 ip, 这个 ip 是全集群唯一的

- `qosClass`: 资源分配相关，在后面小节介绍

- `startTime`: 启动时间

conditions 部分的信息比较多,包含了每个 container 的运行信息。比较重要的有：

- probe 信息

  : 是一列状态检查信息，表明 pod 是否到达某个状态。注意 type 字段，它有一些固定的值，大体代表了部署的一个过程。而 status 字段就具体表明是否达到这个状态。我们将所有的 type 列出如下：

  - `PodScheduled / Unschedulable`： 已经调度到某台机器了 / 无法调度到某台机器
  - `Initialized`：所有的 init containers 都成功启动（后续小节会详细介绍）
  - `ContainersReady`：所有的 containers 都已经 ready
  - `Ready`: pod 完全可以对外提供服务

至于 containerStatuses 部分，则提供了 pod 下各个容器的基本信息。比较重要的信息有：

- `restartCount`: 重启次数。因为 kubernetes 对于资源的处理不是一次性的，比如这一次部署出错了，它会一直重试，直到达到目标状态。比如 command 写的不对，启动后容器退出，kubernetes 会一直重启。restartCount 会记录这个次数
- `state`: pod 下每个 container 的状态。这个状态比 pod.phase 更加准时和精确。最终 pod 的 phase 也是根据此计算出来的。

一般来说，这些信息并不需要特别关注，pod 的 phase 字段大部分时间都能比较明确地提供大致的状态信息。但出错的时候，我们就需要综合各种信息来判断问题出在哪里。kubectl 在展示状态的时候，就做了一个特殊处理，将 pod 的 phase 字段以及 container 的状态信息结合起来计算出一个状态展示出来。我们可以通过创建一个有问题的 pod 来看下。

文件名:pod-phase.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-phase # 换了名字，避免与之前的pod名字冲突
spec:
  containers:
  - name: pod-phase
    image: busybox:nonexist # 加了一个不存在的tag
    command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 3600']
```

在命令行中执行如下命令：

```bash
kubectl create -f /share/lesson/kubernetes/pod-phase.yaml   # 创建 bad-pod
kubectl get po pod-phase -w   #观察pod phase的变化 
```

可以看到，一开始该pod的phase是`ContainerCreating`,但过了一小会之后，kubernetes 发现镜像拉取失败， phase变为`ErrImagePull`，经过一定次数尝试后，最终状态应是 `ImagePullBackOff`。然后k8s会尝试重新启动该pod，phase的状态会再进行如上一遍的过程。

```txt
NAME        READY   STATUS              RESTARTS   AGE
pod-phase   0/1     ContainerCreating   0          1s
pod-phase   0/1     ErrImagePull        0          41s
pod-phase   0/1     ImagePullBackOff    0          52s
pod-phase   0/1     ErrImagePull        0          97s
pod-phase   0/1     ImagePullBackOff    0          110s
pod-phase   0/1     ErrImagePull        0          2m42s
pod-phase   0/1     ImagePullBackOff    0          2m54s
```

这个状态不在 pod 的 yaml 中，是 kubectl 根据 pod 以及 containers 的状态综合计算出来的。kubectl 作为一个使用频率非常高的交互工具，用这样的状态能极大地增强易用性。
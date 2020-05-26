# Kubernetes Pod

熟悉Docker的同学都知道container的概念。在K8S中，简单来讲，Pod 是一组(可以为一个) container 的集合。这些 containers 一起调度，视为一个基本单元。为什么要有 Pod 这个概念。

Kubernetes 为了提供服务，需要有这么一个基本的计算单元，但它对这个“基本单元”的定位，现存的 container 并不十分适合。kubernetes 的需求是(下面以 unit 代指 “基本单元”这个概念):

- 这个 unit 需要有一个唯一的 ip ，并且可以跨机器、在集群内能互相访问
- 最好不能太依赖于 docker (也有商业上的考量)，而要支持多种 container runtime
- 用户最终使用 kubernetes 都是将其应用部署于集群内。这个 unit 最好贴近于应用的概念，也就是说更抽象一点,贴近于业务，而不是底层系统
- 在使用 container 时我们经常会发现有一个两难的处境，就是我们希望在容器里运行多个程序，但 container 对此支持不太好，放多个容器又太麻烦了。Pod 的概念就完美地支持了这种场景，在 Pod 中的多个容器虽然各自独立，但是默认共享网络和存储，并且还可以定制其它的共享资源

结合以上的考量，Kubernetes 将 Pod 作为其最基本的运算单元。

本实验中，也会大量地使用 应用/服务 的概念。这是一个业务上的概念，泛指用户想要在容器平台（kubernetes) 运行的程序，比如 mysql、nginx...等等。最终这些 应用/服务 都会以容器(Pod)的形式存在。

文件名:pod-sample.yaml

```bash
apiVersion: v1
kind: Pod
metadata:
  name: pod-sample
  labels:
    app: pod-sample
spec:
  containers:
  - name: pod-sample-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 3600']
```

这是一个非常简单的 Pod 样例。它的主要字段解释如下:

- apiVersion/kind  

  : 这是所有资源共有的基本字段，表示 api 版本号以及类型

  - `apiVersion`: 表示资源所属于的 group 以及 version。结构一般为 ``，其中 v1 是特例，其 group 为 "", 省去了中间的 `/`。一般核心的资源都是 v1,比如 Namespace / Pod / ConfigMap 等。其它的资源各有各自的 group 以及 version
  - `kind`: 资源类型，开头大写

- metadata

  - `name`: 这个 pod 的名字
  - `labels`: pod 的标签
  - `namespace`: 可选字段。Kubernetes 中的资源分为两类，一类属于 namespace, 一类不属于。Pod 属于 namespace, 如果 yaml 里没有写 namespace，表示属于 default namespace

- spec:**pod 的主要信息部分**

  - containers

    : 一个列表，因为可以有包含多个 container

    - `name`: 这个 container 的名字，一个 pod 下面的多个 container 名字不能冲突
  - `image`: 这个 container 的镜像信息
    
    - `command`: 启动命令。是可选项，因为一般镜像都有默认值

```bash
ctr -n k8s.io i import /share/images/busybox.latest.tar
kubectl create -f /share/lesson/kubernetes/pod-sample.yaml
```

我们可以看到创建的结果：`pod/pod-sample created`

接下来我们看一下新创建的 pod-sample 的详细信息

```bash
kubectl get po pod-sample -o yaml
```

可以看到，我们使用的 yaml 在创建之后包含了更多的字段。这些都是 kubernetes 帮助填写的默认值。metadata 的字段前面实验已经介绍过了。下面主要说下 pod 的 spec 和 status 字段。一般来说，很多资源都有这两个字段，而且含义类似。 spec 是具体的属性描述， status 是状态信息，会在创建后不断变化。Pod 的 spec 字段是一个 containers 列表，因为它支持多容器。每个 container 内部的信息与 docker 和 docker compose 包含的信息是类似的, 只是字段不同。因为最终目的都是要配置应用、运行应用，在这方面二者的目的是一致的。所以表现的主要差别只体现在语法上。

container 里主要包含的基本信息有：

- `启动命令`：主要是 command。很好理解。下面也会详细介绍。

- 镜像信息
  - `image`: 镜像地址
  - `imagePullPolicy`: 镜像拉取策略。因为有时候机器上已经有了 image，我们就可以不用去远端拉取。这时候可以在 pod yaml 里设置这个值为 IfNotPresent。Always 表示不管机器上存不存在都会重新 pull 镜像。适用于镜像 tag 不变但是内容会变化的场景。

- `名称`：容器的名称，kubernetes 中的所有资源的查找和使用主要都是靠名称，容器也是。比如我们用 kubectl 去 exec 到一个容器中时，就会用到这个名称。

- `resources`: 因为我们使用的 yaml 里没有这部分信息，所以创建出来的 yaml 里默认值为 {}。它具体描述了这个 Pod 对于计算资源的需求信息。下面也会详细介绍。

- `terminationMessagePath`: 用于记录容器退出时的最后信息（成功退出或者异常退出），这些信息可以用于监控展示或者 kubernetes 计算 container 以及 pod 的状态

- terminationMessagePolicy
  : 从哪些地方取容器最终的状态信息。

  - `File`: 默认值，表示只从上面 `terminationMessagePath` 所在的位置取状态信息
  - `FallbackToLogsOnError`： 如果上面的文件里没有内容，那么就从容器的日志里取一部分数据作为状态信息（一般是 stdout 的输出）



查看该Pod的日志
```bash
kubectl logs pod-sample
```

进入该Pod的内部（即进入容器pod-sample-container），因为该pod仅包含一个容器，所以不用指定容器名。

```bash
kubectl exec -it pod-sample sh
```




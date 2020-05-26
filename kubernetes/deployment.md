# Kuberntes Deployment

介绍和练习 Kubernetes 通过 Deployment这种 Workload 对多个 Pod 的管理模式。

,Pod 是 kubernetes 中最核心和基本的概念。我们可以通过它来了解 kubernetes 如何管理和调度用户服务的。但是在实际的使用中，直接用 Pod 是不适合的，因为必然会产生单点故障。我们需要有一种方法来方便地创建、管理同一个服务的多个实例（Pod)。Kubernetes 中引入了 Workload 的概念，它可以理解为 Pod 的父资源，主要的作用就是来管理多个 Pod 的生命周期。

Workload 主要分为三类：

- Deployment: 最常见的类型。广泛适用于多种业务场景。
- DaemonSet: 在集群的每个节点上部署一个 Pod ，适用于各种 agent 业务的场景。
- StatefulSet: 适用于各种有状态服务的场景。

StatefulSet 因为涉及到很多存储相关的内容，会放到后面的存储部分单独介绍。本节主要介绍 Deployment 以及 DaemonSet 类型的 Workload 。



Deployment 也是一种 Resource, 前面说过各个 Resource 都会有一个 group / version 信息。对于三种 Workload 而言，它们的 apiVersion 是一致的，都属于 apps/v1 。

我们直接看一个 yaml 样例，在 `/home/shiyanlou` 目录下新建 `deploy.yaml` 文件并向其中写入如下代码：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.15.4
        ports:
        - containerPort: 80
```

重点关注的是 spec 部分：

- replicas: Pod 的数量，也就是创建这个 Deployment 之后它会创建几个 Pod
- selector: Deployment 管理 Pod,可以理解为 Pod 的一个父资源。那么这个关联是如何体现的呢？一个 namespace 下有很多个 Pod，Deployment 是如何知道哪个是属于它管理的呢？这就需要 selector 字段，它设定了二者的关联。这个例子中使用了最常见的标签关联，也就是说任何有 `app:nginx` 标签的 Pod，Deployment 都会认为是属于它管理的。这是标签的一个重要作用：用来关联资源。
- template: Deployment 的定义其实就是 Pod 的定义加上一些其它的属性。这个 template 就是 Deployment 启动的 Pod 应该长什么样子的定义，它跟单独的一个 Pod 的定义是非常像的
  - labels: labels 定义了每个 Pod 应该有什么样的标签，这个是和 selector 一起使用的。
  - spec：spec 里面的内容就和 Pod 的 spec 部分是完全相同的，主要内容也是 containers 的列表。

在终端执行如下命令进行创建（先使用命令 `./dind-cluster-v1.10.sh up` 启动集群）：

```bash
kubectl create -f deploy.yaml
```

继续用 watch 来观测 deployment 的状态变化

```bash
kubectl get deploy nginx-deployment -w
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547286235818.png/wm)

各个字段的涵义如下：

- NAME: deployment 的名字
- DESIRED: 就是期望有多少个 Pod，也就是上面 yaml 中 `replicas` 的值
- CURRENT: 当前有多少个 Pod 处于运行中
- UP-TO-DATE: 达到最新状态的 Pod 的数量。当 Deployment 在进行更新时，会有新老版本的 Pod 同时存在，这时候这个字段会比较有用
- AVAILABLE: 可用的 Pod。上个实验我们讲了健康检查的相关配置，Pod 运行中和可以提供服务是不同的概念
- AGE: deployment 运行的时间

## 结构

从之前练习过的 Resource 资源我们可以知道， 一般我们使用的 yaml 会比 kubernetes 创建完之后的 yaml 少很多信息。因为有好多默认值的存在，kubernetes 会帮我们填好。这些默认值有助于我们理解很多 kubernetes resource 的行为和结构。 Deployment 也不例外。我们查看下刚才创建的 Deployment 的结构:

```bash
kubectl get deployment nginx-deployment -o yaml
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547286380731.png/wm)

首先我们查看下 metadata 部分以及 deployment 自身相关的部分：

- `apiVersion`: 注意这里的 apiVersion 与我们填写的不一样。这是因为除了属于 core group 的 resource (Pod, ConfigMap...), 其他很多 Resource 的定义都是不断变化的。大致都有一个 alpha - beta - stable 的阶段。在这个过程中， group 和 version 都有可能发生变化。在每一个 kubernetes 版本中，每个 resource 都会有一个推荐的默认版本，所有的资源不管以什么版本创建，都会被修改成这个默认版本。目前 deployment / statefulset / daemonset 等最新的 apiVersion 是 apps/v1, 但 kubernetes 1.10 版本时的默认版本是 extensions/v1beta1。deployment 等 workload 的版本变化比较多，好在具体的 yaml 结构变化并不大

- `progressDeadlineSeconds`: 过了多久时间 Deployment 会被认为失败。这时候 controller-manager 会停止继续部署 deployment

- `revisionHistoryLimit`: 历史版本，用于更新及回滚

- ```
  strategy
  ```

  : 更新策略。默认为 RollingUpdate，滚动更新

  - `maxSurge`: 就是最多会多部署多少个 Pod 。 假设一个 Deployment 有 10 个 Pod，当更新时，可以最多先启动 4 个新版本的 Pod，然后等它们成功后，再去 kill 旧版本的 Pod。
  - `maxUnavailable`: 最多有几个 Pod 不可用。假设一个 Deployment 有 10 个 Pod。 当更新时，最多可以先 kill 掉四个旧的 Pod, 然后启动新的 Pod。
  - `type`: RollingUpdate。更新策略，RollingUpdate 是默认选项且是目前最优选项，其他的选项都是一些老版本的策略，并不适用了。RollingUpdate 的设置能够适用于多种集群资源的状态，富余时可以先启动新的 Pod，资源紧张时可以先 kill 老的 Pod。这些配置能够最大限度地保证 Deployment 更新成功。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547286563758.png/wm)

Deployment 的 status 部分与 Pod 的也有些类似。基本状态 + conditions 的结构. 其中 readyReplicas 等几个字段与上述 get deployment list 时输出的几个 READY / UPDATE-TO-DATE 字段是一一对应的。

我们已经成功地创建了 Deployment ，现在看下具体的 Pods 状况：

```bash
kubectl get pods --show-labels
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547286872801.png/wm)

这里加了一个参数 `--show-labels`，可以看到这些 pod 的一些规律：

- NAME: 格式为: ` -  - ` 的结构。每次更新了 deployment 里面的 pod template 部分， `` 值也会对应更新。
- labels: 我们在 deployment 的 yaml 里指定的标签，也有一个自动添加的用于标记其版本的 pod-template-hash, 同一个 pod template 生成的 pod 的 hash 都是一样的值。



## 更新

除了创建，Deployment 提供的另一个重要的功能就是更新应用。这是一个比创建复杂很多的活动，想象在平时的应用中，在线升级是一个很常见的需求，不能因为升级中断服务。这就要求我们必须有一定的策略来决定何时创建新的 Pod,何时删除老的 Pod。如果前面有负载均衡，还需要动态的删除老的实例并把新的实例加上。Deployment 对这种场景提供了非常好的支持（负载均衡相关的由后续介绍的 Service 资源支持）

上面说到 Deployment 的 yaml 包含了两部分。一部分是属于 Deployment 自己的，比如它自己的基本信息：metadata、spec、标签之类的；一类是属于 pod 的 template 里面的内容。更新前面的部分，只是更新了 Deployment 本身，Pod 的信息并未变化，已经运行的 Pod 也就不需要更新。如果是更新了后面部分，比如镜像的版本，这是最常见的更新内容，那么所有的 Pod 都需要删掉并重新建立新的。

接下来我们就着重看下 PodTemplate 部分的更新。

下面是一个更新 pod 镜像的命令：

```bash
kubectl set image deployment.v1.apps/nginx-deployment nginx=nginx:1.9.1 --record
```

注：

- --record 命令将这条命令记录到了 deployment 的 yaml 的 annotations 里。它可以告诉我们这次更新的方式是什么，在回滚的时候也很有用。
- 我们仍然可以用 apps/v1 的版本来对 nginx-deployment 这个 deployment 操作，kubernetes 会自动处理版本信息。

这条命令更新了 podTemplate 里面的镜像。跟之前介绍的一些封装命令类似，底层仍然是调用的更新 api，只是因为常用所以 kubectl 封装了一下。有兴趣的同学可以加 -v 参数看它具体调用的 api 命令。

除了这种方式，我们也可以用如下的 edit 命令来更新镜像：

```bash
kubectl edit deployment.v1.apps/nginx-deployment
```

这个命令会打开一个编辑窗口，然后编辑 image 相关的部分保存即可。可以同样打开 -v 命令看它调用的 api 接口，跟上面的 set 命令是一样的结果。

更新完之后，我们可以立马用 watch 的方式来观察 deployment 的实例变更情况

```bash
kubectl get deploy nginx-deployment -w
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547290643954.png/wm)

可以从这 4 个值中推断出其更新步骤：

1. 创建一个新版本的 Pod ( CURRENT=4, UP-TO-DATE=1)。因为 maxSurge 为 25%, 向上取整可以多创建一个
2. 删除一个旧的 Pod (CURRENT=3, UP-TO-DATE=1)
3. 创建一个新的 Pod (CURRENT=4, UP-TO-DATE=2)
4. 删除一个旧的 Pod (CURRENT=3, UP-TO-DATE=2)
5. 创建一个新的 Pod (CURRENT=4, UP-TO-DATE=3)
6. 删除一个旧的 Pod (CURRENT=3, UP-TO-DATE=3)

上面说了 record 的作用，我们可以通过 get yaml 看到:

```bash
kubectl get deploy nginx-deployment -o yaml
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547290929078.png/wm)

而此时查看 pod 的 labels 信息，我们也可以看到其 template hash 已经发生了变化:

```bash
kubectl get pods --show-labels
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547290989169.png/wm)

## 回滚

有更新就有回滚。比如新的镜像版本有问题，或者配置不对等等，这是生产环境经常发生的事情。相对于更新，回滚镜像一般都是有问题了，所以需要更快地进行处理。Deployment 的回滚机制正是为此而生。

Deployment 本身保存了很多历史版本的信息（具体多少条可以配置,参考前面结构的`revisionHistoryLimit`）。我们可以查看下：

```bash
kubectl rollout history deployment.v1.apps/nginx-deployment
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547291231567.png/wm)

history 里面就保存了我们之前用 `—record` 记录的更新原因，`CHANGE-CAUSE` 字段。

回滚到上个版本:

```bash
kubectl rollout undo deployment.v1.apps/nginx-deployment
```

回滚到特定版本：

```bash
kubectl rollout undo deployment.v1.apps/nginx-deployment --to-revision=2
```


Deployment 的 replicas 指定了目标实例数。但在实际运行过程中，我们经常会有调整实例数的需求。比如业务的高峰期和低峰期，临时性的 debug 等等。我们可以通过前面提到的 edit 命令来编辑这个字段的值来提交，也可以直接用 kubectl 提供的 scale 命令来更方便地调整:

```bash
 kubectl scale deployment.v1.apps/nginx-deployment --replicas=10
```

--replicas 指定了目标实例数。可以通过 watch 观测到结果：

```bash
kubectl get pods -w
```



类似地，将其 scale 到一个更小的数值：

```bash
kubectl scale deployment.v1.apps/nginx-deployment --replicas=1
kubectl get pods -w
```


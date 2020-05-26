# Kuberntes daemonset

与 Deployment 一样，DaemonSet 也是一种 Workload，用来管理多个 Pod，只是使用的场景不同。相对来说，DaemonSet 的作用更为特殊化一些。首先，我们看它的主要特点：

- 每个 node 上都有一个实例，且只有一个。如果有新加的机器进来，DaemonSet 也会在新的机器上起一个新的 Pod
- 不能扩缩容，因为它的实例个数是随 node 数量的

由这些特点可以看出，它主要的使用场景是：

- 各类需要在每个机器部署的 agent 组件。比如负责监控的、日志的(fluentd/logstash)、存储的(glusterd/ceph)。这些组件一般都是每个机器都需要有，本身自己也不需要保存持久状态，一般都是向外部汇报数据。

其他方面，DaemonSet 与 Deployment 并无太大差别。

在 `/home/shiyanlou` 目录下新建 `ds.yaml` 并向其中写入如下代码：

```yaml
apiVersion: extensions/v1beta1
kind: DaemonSet
metadata:
  name: logging
spec:
  template:
    metadata:
      labels:
        app: logging-app
    spec:
      nodeSelector:
        app: logging-node
      containers:
        - name: webserver
          image: nginx
          ports:
          - containerPort: 80
```

大体来说，结构与 Deployment 是类似的。需要注意的点：

- 没有 replicas 字段
- spec.nodeSelector: Pod 与 主机标签的匹配。在 kubernetes 中，标签广泛应用于各种 resource 中，所有的 resource 都可以有标签，某些 resource 在 binding 的过程中，可以通过标签来进行匹配。匹配的概念就是说目标 resource 的标签必须包含 selector 中的全部标签。

在终端中执行如下命令：

```bash
kubectl create -f ds.yaml
```

我们可以观察或者 watch ds 的变化，会发现并没有 Pod 生成:

```bash
kubectl get ds
```

因为我们选的 selector 没有符合条件的 Node。 所以没有 Pod 可以部署成功。下面我们将其中的 node-1 打上这个标签：

```bash
kubectl get no
kubectl label node kube-node-1 app=logging-node --overwrite
```

label 命令可以用于给任何一个 resource 打标签， 其命令结构为：`kubectl label   =` , 其中 `--overwrite` 表示已存在的话会强制覆盖。

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547291942372.png/wm)

现在我们可以看到 ds 的变化：

```bash
kubectl  get ds
kubectl get pods -o wide
```

![此处输入图片的描述](https://doc.shiyanlou.com/document-uid600404labid9476timestamp1547292008153.png/wm)

新生成的 ds 的 pod 正是运行在 kube-node-1 上。
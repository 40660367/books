# Kubernetes 服务类别(type)

服务选择(selector)着重于 Service 与 backend pods 关联方式的不同。

在对外提供服务上，也有区分。本实验会介绍一下最常见的几种，分别是：

- `ClusterIP`：默认类型，提供一个虚拟 ip 来提供服务。这个已经在上面介绍过。
- `NodePort`：在主机上开一些随机端口来转发服务。
- `Headless`：也属于 ClusterIP 中的一类，但是不设置 ClusterIP，所以一般单独列出来算作一类。

## NodePort

Service 作为负载均衡组件，主要的职责在于集群内部访问。它的虚拟 ip 只能从集群内部访问，比较适合于集群内部组件之间的互相调用。集群外部的访问由其它的 Resource (Ingress) 负责，也相对更为重量级一些。Service 为了方便实用，也提供了集群外部的调用功能，方式就是类似于 docker 的主机端口绑定方式。我们来看一个例子:

先创建一个可以充当 backend pods

文件名:service-pod-helloagain.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: helloagain
  labels:
    app: helloagain
spec:
  containers:
  - name: servicetype
    image: nginx
    imagePullPolicy: IfNotPresent
    resources:
      requests:
        cpu: 100m
        memory: 100Mi
    ports:
    - containerPort: 80
```

```bash
kubectl create -f /share/lesson/kubernetes/service-pod-helloagain.yaml
```

我们可以看到生成的 yaml 里会记录下来刚才输入的端口信息：

```bash
kubectl get po helloagain
```



创建 service，根据pod信息，kubectl 也提供了便捷的方式：

```bash
kubectl expose po helloagain --type=NodePort
```

expose 就是创建出可以对外提供服务的 Service。唯一需要注意的参数就是 --type 这里，可以指定具体的 Service 类型。这里我们使用 NodePort 类型。

看下结果：

```bash
kubectl get svc helloagain
```

大体上跟 ClusterIP 差不多。需要注意的信息有：

- `type`: 已经是 NodePort 类型了
- `nodePort`: 对每一个端口来说，都自动选了一个随机端口。这个端口范围是可配的。

nodePort 这个端口是会在每一个 Node 上面开启，这样我们访问每一个 Node 的此端口都可以访问到这个服务。

```bash
helloagainnodeport=$(kubectl get svc helloagain -o go-template='{{(index .spec.ports 0).nodePort}}')
echo $helloagainnodeport
curl localhost:$helloagainnodeport
```

$helloagainnodeport的值 就是刚才节点开放的端口，该端口可访问到后端Pod。

我们看到已经K8S节点已经监听了此端口并且可以访问。

**注意：** node 上的 port 属于稀缺资源，所以一般 NodePort 比较适用于少量的需要对外提供访问的服务。同时, NodePort 和 ClusterIP, 也自动分配了 ClusterIP, 所以 ClusterIP 具有的内部访问功能它也有。


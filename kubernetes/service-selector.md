# Kubernetes 服务选择(selector)

K8S中的Service是一个抽象概念，它定义了一个服务的多个pod逻辑合集和访问pod的策略，一般把service称为微服务

**举个例子：**一个a服务运行3个pod，b服务怎么访问a服务的pod，pod的ip都不是持久化的重启之后就会有变化。
这时候b服务可以访问跟a服务绑定的service，service信息是固定的提前告诉b就行了，service通过Label Selector跟a服务的pod绑定,无论a的pod如何变化对b来说都是透明的。

## 创建服务对应的后端

先创建一个可以充当 backend pods 的 deployment

文件名:service-deployment-hello.yaml

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello
  labels:
    app: hello
spec:
  selector:
    matchLabels:
      app: hello
  replicas: 5
  template:
    metadata:
      labels:
        app: hello
    spec:
      containers:
      - name: hello
        image: nginx
        imagePullPolicy: IfNotPresent
        resources:
          requests:
            cpu: 100m
            memory: 100Mi
        ports:
        - containerPort: 80
```

这个普通的 Deployment。唯一需要注意的是 ports 信息，它显示了这个 Pod 暴露了哪些端口，类似于 docker 中 expose 的意义。但是一般来讲，这个信息是没必要的。因为 Pod 具有唯一的集群内可访问的 ip, 不会跟其他 Pod 产生冲突，任何监听了 0.0.0.0 这样地址的服务都可以通过 `:`的方式访问。这里写上的作用主要是提供一些更明确的信息，也方便一些工具比如 kubectl 的使用而已。

在终端执行如下命令创建 deployment:

```bash
ctr -n k8s.io i import /share/images/nginx.tar
kubectl create -f /share/lesson/kubernetes/service-deployment-hello.yaml
```

看下最终我们创建出来的 pods 结果

```bash
kubectl get po
```



然后我们来创建对应的 Service

文件名:service-svc-hello.yaml

```yaml
apiVersion: v1
kind: Service
metadata:
  name: hello
  labels:
    app: hello
spec:
  ports:
  - port: 80
    targetPort: 80
  selector:
    app: hello
```

Service 的 spec 部分就是它的主要信息，主要包含以下内容：

- `ports`: 是一个端口信息列表，也就是说一个 Service 可以管理多个端口的访问。本身 Pod 可以对外暴露多个端口
  - `port`: service 绑定的端口，也就是这个 Service 所对应的 ip 监听的端口
  - `targetPort`: backend 的端口，也就是 Pod 所暴露的端口
- `selector`: 标签选择，符合这个标签的 Pod 会作为这个 Service 的 backend。

在终端执行如下命令创建并查看：

```bash
kubectl create -f /share/lesson/kubernetes/service-svc-hello.yaml
kubectl get svc 
```

这条命令用来查看 default namespace 下的 Service 信息列表。因为 default namespace 是默认值，可不写。 `-o wide` 会增加一些额外的信息展示，看下结果：

除了 yaml 中我们填写的信息之外，kubernetes 帮我们补充了其他的默认信息:

- `Type`: 类型，决定着 Service 如何对外提供服务。因为我们在 yaml 里未设置，所以这里用的默认值: `ClusterIP`, 具体有哪些可选的会在下面讲解。
- `Cluster IP`: 系统帮我们自动生成的 ip 地址。这个 ip 地址的范围是可配置的，并且只能在集群内部访问。

看下完整的 yaml：

```bash
kubectl get svc hello -o yaml
```

这里又比刚才的列表页显示了更多的信息，需要注意的如下：

- `sessionAffinity`: 这是负载均衡里面比较常见的一个概念，就是让来自于同一个 client 的请求落到同一个 backend 上。默认为 None。
- `ports[0].protocol`: 端口协议，默认为 TCP ,目前只支持 TCP/UDP。

容器的轻量级特性，让作为 backend 的 Pod 可以比传统方式更加随意地起停。Service 只记录了 labelSelector，但具体的映射关系仍然需要有个地方记录下来。当然这个工作是由 kubernetes 来完成，而不是用户。记录这个映射关系的资源就是 Endpoints，同一个 namespace 下与 Service 同名的 Endpoints Resource 即是这个映射关系的管理者。刚才我们创建好了 Service 之后，Kubernetes 已经帮我们创建好了相应的 Endpoints 资源：

```bash
kubectl get ep hello -o yaml
```

注：ep 是 endpoints 的简称。

主要信息在 subsets 里面，addresses 列表记录了每个 backend 的信息，这里面的两个 Pod 信息就是我们刚才创建的两个 Pod 。addresses 里面记录了 Pod 的 ip、所在的主机名称、以及具体的 Resource Object 的引用。

下面我们可以通过访问这个 service 的 ip（即CLUSTERIP） 来访问这个服务了。

```bash
helloclusterip=$(kubectl get svc hello -o go-template --template='{{.spec.clusterIP}}')
echo $helloclusterip
curl $helloclusterip
```

其中`$helloclusterip`即上面的 service 生成之后所分配的 ip ,每次创建的 ip 都是不一样的。

注意：

- 我们的hello程序运行了一个页面，其中显示了运行其的 host 的 hostname, 在这个场景中就是 pod 的 hostname, 而 pod 的 hostname 一般就是其名字。
- 这里我们可以观察出来， **Service 做了负载均衡，将流量转发到了不同的pod实例上。**

## DNS

上面的使用 ip 的使用有一个很致命的问题，就是它不好记，而且不方便使用。如果你让系统自动分配，那很难知道生成的结果是什么，无法提前配置。如果是自己选好固定的 ip ,服务多了又不好管理。而服务发现就解决了这个问题。我们仍然拿刚才的实验继续验证下。

首先要注意的是，service 的 ip 是可以在 kubernetes 的 node 上和 pod 里面直接访问的。但 dns 只能在 pod 里面访问，因为它需要配置 kubernetes 的 dns 服务为解析服务器，而且还要配置其他参数。 kubernetes 在启动每个 pod 时都会将这些配置好。

准备busybox pod

```bash
ctr -n k8s.io i import /share/images/busybox.latest.tar
kubectl create -f /share/lesson/kubernetes/busybox.yaml
```
进入busybox pod
```bash
kubectl exec -it busybox sh
```
使用域名访问服务，而不是IP
```bash
wget -O- hello
```

可以看到，运行结果与上面通过 curl 是一样的。那么它是怎么实现的呢?

我们用 nslookup 命令来探究下：

```bash
nslookup hello
```

nslookup 命令用于解析某一个域名，会得到如下类似的结果

```txt
Server:         10.96.0.10
Address:        10.96.0.10:53

Name:   hello.default.svc.cluster.local
Address: 10.96.177.43
```

这里我们需要注意的是：

（1）server 的地址，这里显示的 server 就是 dns server, 它就是 kubernetes 中 dns 服务的地址。

```bash
kubectl get svc -n kube-system
```

在部署完集群后，这个 svc 就自动创建了。

（2）解析到的名字

dns server 帮我们解析到了正确的 ip ,但是后面显示的域名比较长。这里涉及到了一个 dns search-path 的概念。我们看下 dns resolve 的配置文件。

```bash
cat /etc/resolv.conf
```

简单来讲，当我们查询 hello 这个域名时，dns server 会帮我们查询下面的几个名字：

- hello
- hello.default.svc.cluster.local
- hello.svc.cluster.local
- hello.cluster.local

其中 `hello.default.svc.cluster.local` 是正确的域名，它的格式为`..svc.`。其中 suffix 是集群配置，而 namespace 则视具体的情况而定。有了 search path, kubernetes 的服务不仅实现了通过域名访问，而且实现了最简单的仅通过名字即可访问的模式。在实际的业务场景中，这是非常便利的一个条件。想象一个常见的场景, 有一个 namespace 叫 http，里面有服务 a 、 b, 有一个 namespace 叫 storage, 里面有 redis、db 两个服务，那么 a、b 之间的互相访问只需要知道对方的名字即可，不需要知道它们所处的 namespace（可以方便地一起迁移）。而 a b 想要访问 redis 或者 db, 那么也仅仅需要用 `redis.storage` 或者 `db.storage` 这两个名字即可。

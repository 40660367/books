# Kubernetes Pod 健康检查(healthy check)


docker 在较高的版本中也加入了健康检查的配置，可见它也意识到了其重要性。而 pod 在一开始就有了对健康检查的支持。因为我们一般使用容器来运行长时间运行的服务，比如 http 服务、cache 等。如果没有健康检查，很有可能容器仍在运行，但是服务已经不能正常工作了。因为最终说来，容器并不等于应用/服务。所以我们需要健康检查来统一两者的状态，这样我们就知道当服务异常时，容器也会退出。

在基础的健康检查的概念之上，kubernetes 提供了更加精细的概念。分别是存活性检查和可用性检查，分别介绍如下：

- `存活性检查`（liveness probe): 用于判断容器是否需要重启
- `可用性检查` （readiness probe): 用于判定容器是否可以正常提供服务。因为在一般的应用场景下，都会用负载均衡后面挂上多个实例来达到分担流量以及稳定性保障的目的。可用性检查就是用来保证这个 Pod 是否可以提供服务，并被挂载在负载均衡后面

一般的应用不会有这么精细的区分，这时候存活性检查和可用性检查用同样的配置即可。

通常来讲，应用对外提供服务都是通过 tcp 端口或者 http 端口，比如 nginx 提供 http 服务，redis 通过 6379 端口提供服务。对于这样的服务，我们可以通过检查其端口是否开启，http endpoint 是否可以访问来判断其健康状态。有的服务不暴露这样的网络端口，这时候可以通过 exec 进去之后执行相应的命令来检查。比如有的文件会写一个 pid 文件。kuberentes 提供了对这几种方式的支持，方式就是通过 pod 所在机器的 kubelet 来执行这些检查。我们可以逐一看下。

### EXEC

exec 就是指通过 exec 到容器中执行命令来进行健康检查。我们看一个示例。

文件名:pod-liveness-exec.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-liveness-exec
spec:
  containers:
  - name: liveness
    image: busybox
    imagePullPolicy: IfNotPresent
    args:
    - /bin/sh
    - -c
    - touch /tmp/healthy; sleep 30; rm -rf /tmp/healthy; sleep 600
    livenessProbe:
      exec:
        command:
        - cat
        - /tmp/healthy
      initialDelaySeconds: 5
      periodSeconds: 5
```

注意：

1. 例子中为了演示，让 command 不断地创建删除文件，健康检查去检查这个文件
2. 这个例子中只配置了 livenessProbe
3. command: 就是健康检查执行的命令。如果执行结果状态码为 0，就认为通过，其它的认为失败
4. periodSecounds: command 执行的间隔，健康检查是一个持续性的过程，需要反复执行。
5. initialDelaySeconds：因为好多程序启动时有初始化时间。比如 java 程序，初始化一般就比较慢。这时候如果立马做健康检查就不太合适，initialDelaySeconds 就是设置了一个合理的时间，等过了这个时间再做检查。

上面的例子中。容器启动后，前三十秒，有这个文件。健康检查是 ok 的，之后文件被删，健康检查就有问题了。我们可以看看它的事件：

在命令行中执行如下命令进行创建：

```bash
ctr -n k8s.io i import /share/images/busybox.latest.tar
kubectl create -f /share/lesson/kubernetes/pod-liveness-exec.yaml
```

然后执行：

```bash
watch kubectl get po pod-liveness-exec
```

可以看到，刚开始的 event 都是 Normal 的，在 36s 之后， 变成 Warning, 因为 Livenss probe 失败了。失败之后，Pod 也会被重启，我们可以看下:

```bash
kubectl get po | grep pod-liveness-exec
```

这个是过了一段时间之后看到的，已经重启了 3 次了。等的时间越久，重启的次数也就越多。

### HTTP

http 检查即是通过调用 http 服务的某个路径，然后根据错误码来判定。 http status code 的 200-400 代表成功，其它代表失败。

文件名: pod-liveness-http.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-liveness-http
spec:
  containers:
  - name: liveness
    image: kubernetes/liveness
    imagePullPolicy: IfNotPresent
    args:
    - /server
    livenessProbe:
      httpGet:
        path: /healthz
        port: 8080
        httpHeaders:
        - name: X-Custom-Header
          value: Awesome
      initialDelaySeconds: 3
      periodSeconds: 3
```

依然是 livenessProbe:

- httpGet: 表示这是一个 http 类型的健康检查
- path: http 的路径
- httpHeaders: 发送请求所带的 headers 字段，不同的场景可能有不能的需求。

这个镜像里，我们依然动态修改了返回结果，用来演示 healtcheck 的不同效果。其实现代码如下图所示：

```golang
http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
    duration := time.Now().Sub(started)
    if duration.Seconds() > 10 {
        w.WriteHeader(500)
        w.Write([]byte(fmt.Sprintf("error: %v", duration.Seconds())))
    } else {
        w.WriteHeader(200)
        w.Write([]byte("ok"))
    }
})
```

前 10s 返回 200， 之后返回 500。

在命令行中执行如下命令进行创建：

```bash
ctr -n k8s.io i import /share/images/kubernetes.liveness.tar
kubectl create -f /share/lesson/kubernetes/pod-liveness-http.yaml
watch kubectl get po pod-liveness-http
```

看下 pod 的 event:

event 中显示，10s 后通过事件就可以看到健康检查已经失败了，kubelet 在重启 pod。


### TCP

对于监听 tcp 端口的服务，我们可以尝试与这个端口建立连接。如果成功，则认为服务正常。

文件名: pod-liveness-tcp.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-liveness-tcp
spec:
  containers:
  - name: goproxy
    image: googlecontainer/goproxy:0.1
    imagePullPolicy: IfNotPresent
    ports:
    - containerPort: 8080
    readinessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 5
      periodSeconds: 10
    livenessProbe:
      tcpSocket:
        port: 8080
      initialDelaySeconds: 15
      periodSeconds: 20
```

这个实例中配置了 livenessProbe 和 readinessProbe,从具体的配置上来看，与 http 的配置是很像的。只是其配置中需要指明的是端口。

在命令行中执行如下命令进行创建查看:

```bash
ctr -n k8s.io i import /share/images/googlecontainer.goproxy.0.1.tar
kubectl create -f /share/lesson/kubernetes/pod-liveness-tcp.yaml
watch kubectl get po pod-liveness-tcp
```

这个地方因为镜像配置的是一直运行，所以结果 healthcheck 会一直过的。这里着重看下 liveness 和 readiness 的一些其他默认值：

- timeout: 超时时间，如果超时了就认为失败了
- success/failure: 图中的配置是如果成功一次了就认为正常，如果失败了三次才认为失败。这样可以有效地避免因为偶然的偏差导致容器被标记为异常。

# Kubernetes Pod 资源申请request与限制limit 

我们知道使用容器的一个优点是可以控制每个容器使用资源的大小，docker 提供了参数来控制 cpu 和内存的使用，pod 也同样，但仍然是容器级别的，需要对 pod 的每个容器做设置。在之前的例子中，我们没有设置这个字段，表示默认是不限制的。但是在一般的使用中，还是要限制的。



Pod 中的资源限制也主要是针对 cpu 和 内存。与 docker 不同的是，它提供了 requests 和 limits 两个设置。具体的含义为：

- `requests`：pod 运行所需要的最少资源。例如 kubernetes 在调度 pod 时，就是以这个设置来挑选 node
- `limits`: pod 运行的资源上限。也就说，超过这个 limits, pod 会被 kill 掉。

文件名:pod-request-limit.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-request-limit
spec:
  containers:
  - name: busybox
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 3600']
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

注： cpu 仅支持 1 或者 500m 这样的写法。500m = 0.5(核)。内存有很多单位，都是我们常用的。具体有哪些可用在使用时查看官方文档即可。

在命令行中执行如下命令用 kubectl 创建：

```bash
kubectl create -f /share/lesson/kubernetes/pod-request-limit.yaml
```

这个 pod 明确设置了 requests 和 limits, 并且 requests <= limits。我们看下运行结果(等到运行中）：

```bash
kubectl describe po pod-request-limit
```

这里我们要介绍一个 kubectl 的命令，叫 describe。 它与 get 类似，都是查看某个资源的信息，但是包含的信息更多。它重新排版了资源的 yaml, 凸显了重要信息，并且将这个资源创建以来的事件信息也展示出来了，在排查问题时很有用。

我们可以在这里以更直观的方式看到 pod 的信息以及 events。
# Kubernetes Pod QoS(服务等级)

刚才我们创建的 Pod 在 describe 的信息里有一个字段叫 `Qos Class` ,它的值是 `Burstable`。这是由 Pod 的 requests 和 limits 设计所决定的一个字段。Qos 全称是 `Quality of Service`, 表示了 Kubernetes 对不同的 Pod 因其 requests/limits 设置而对其运行情况的保障，具体分为以下几类：

- `Guaranteed`: requests = limits ，二者是一样的值。高优先级，Kubernetes 保证只要资源使用不超过 limits 就不会被 kill
- `Burstable`: requests < limits，Pod 可以使用 requests 到 limits 之间数量的资源，中优先级， 但是当机器资源紧张的时候，如果这些 Pod 对资源的使用超过了 requests ,就很有可能会被 kill 掉 (没有 BestEffort 的 pod 的情况下)
- `BestEffort`: 没有设置具体的 requests 和 limits。低优先级， 如果机器资源紧张，这些 Pod 会优先被 kill 掉

由此可见，它其实是类似于 linux 中进程 priority 的一个概念，通过 requests 值和 limits 值的设置，让用户自己选择去将其应用划分为不同的优先级。我们上面使用的例子就是一个 `Burstable` 的 pod。下面我们看看其他的例子。

## Guaranteed

文件名:pod-qos-guaranteed.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-qos-guaranteed
spec:
  containers:
  - name: busybox
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 3600']
    resources:
      limits:
        memory: "200Mi"
        cpu: "700m"
      requests:
        memory: "200Mi"
        cpu: "700m"
```

这个示例中, requests = limits, 在命令行中执行如下命令进行创建：

```bash
kubectl create -f /share/lesson/kubernetes/pod-qos-guaranteed.yaml
kubectl describe po pod-qos-guaranteed | grep QoS
```

可以看到其 QoS Class 是 Guaranteed

## BestEffort

文件名:pod-qos-besteffort.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-qos-besteffort
spec:
  containers:
  - name: busybox
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ['sh', '-c', 'echo Hello Kubernetes! && sleep 3600']
```

在命令行中执行如下命令进行创建：

```bash
kubectl create -f /share/lesson/kubernetes/pod-qos-besteffort.yaml
kubectl describe po pod-qos-besteffort | grep QoS
```

可以看到其 QosClass 为 BestEffort

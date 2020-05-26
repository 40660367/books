# Kubernetes Pod多容器

在某些情况下，多容器的 Pod 更能适应需求。这样的模式通常是一个容器用来主要提供服务，另一个做一些其他的零碎工作。比如：

1. 收集日志。这样不用修改原来的服务，可以用另外的容器来适配各种日志收集系统。
2. 做 Proxy。比如我们的程序需要访问外部服务（ db 等），可以固定配置为 localhost, 由其他的容器来决定如何转发请求，相当于将动态配置的需求交由其他的容器来做。

综合来讲，这样做的好处就是让主要的服务容器不做修改，就能更好地适配各种系统。另外，也能较好地做到职责分离，不需要由一个容器来处理过多的任务。

文件名:pod-multipod.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-multipod
spec:
  restartPolicy: Never
  volumes:
  - name: shared-data
    emptyDir: {}
  containers:
  - name: nginx-container
    image: nginx:latest
    imagePullPolicy: IfNotPresent
    volumeMounts:
    - name: shared-data
      mountPath: /usr/share/nginx/html
  - name: ubuntu-container
    image: ubuntu:20.04
    imagePullPolicy: IfNotPresent
    volumeMounts:
    - name: shared-data
      mountPath: /pod-data
    command: ["/bin/bash"]
    args: ["-c", "echo Hello from the ubuntu container > /pod-data/index.html && sleep 3600"]
```

这个例子中我们使用了 volume, docker 中也有这个概念，二者是类似的。 Pod 中的 volume 是各个容器共享的，我们可以用它来让各个容器交互。

在这个例子中，ubuntu-container 往 /pod-data/ 里面写入了一个文件，而这个目录是两个 container 共享的 volume, nginx 将其挂载到其配置的目录。

在命令行中执行如下命令:

```bash
ctr -n k8s.io i import /share/images/nginx.tar
ctr -n k8s.io i import /share/images/ubuntu.20.04.tar

kubectl create -f /share/lesson/kubernetes/pod-multipod.yaml
```

`-w` 的意思是 watch, 就是监听的意思。加了这个参数后， kubectl 不会退出，会一直监听 pods 的变化。这样 pods 的状态变化我们都能看到。

需要注意到 READY 下面的 0/2 ，这个 2 就是表示两个容器的意思。一般情况下，需要等到 2 个容器都是 ready 之后 Pod 才会处于运行中。这时候我们可以 exec 进去看看能否读取到 ubuntu-container 写入的文件:

```bash
kubectl exec pod-multipod -c nginx-container cat /usr/share/nginx/html/index.html
```

我们会看到`Hello from the ubuntu container`的输出，证明从nginx-container容器中成功读取到了由来自ubuntu-container容器写入的文件。



kubectl 的 exec 命令非常类似于 docker 的 exec ,区别之处在于其 exec 的目标是 Pod 。

当 Pod 是单个容器时，其结构与 docker exec 是一致的。当 Pod 有多个容器时，就需要指明具体的目标 container 是哪个。默认值是 yaml 里的第一个容器，这里为了演示，加上了明确的参数。

我们可以指定pod中的容器ubuntu-container，执行交互模式的bash

```bash
kubectl exec -it pod-multipod -c ubuntu-container bash
```


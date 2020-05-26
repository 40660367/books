# Kubernetes Pod 启动命令

我们在使用 docker run 的时候可以指定启动命令，在 Dockerfile 里也可以设置 ENETRYPOINT 和 RUN 指令。在 pod 中，kubernetes 使用了更加简单的 command /args 参数来设置，它与 docker 使用的参数对应如下：

| 镜像 Entrypoint | 镜像 Cmd    | 容器 command | 容器 args   | 命令执行         |
| :-------------- | :---------- | :----------- | :---------- | :--------------- |
| `[/ep-1]`       | `[foo bar]` | <not set>    | <not set>   | `[ep-1 foo bar]` |
| `[/ep-1]`       | `[foo bar]` | `[/ep-2]`    | <not set>   | `[ep-2]`         |
| `[/ep-1]`       | `[foo bar]` | <not set>    | `[zoo boo]` | `[ep-1 zoo boo]` |
| `[/ep-1]`       | `[foo bar]` | `[/ep-2]`    | `[zoo boo]` | `[ep-2 zoo boo]` |

之所以要介绍这部分，是因为本身镜像层面的 entrypoint 和 cmd 就容易混淆。再加上 pod 又抽象出了新的参数，很容易误用出 bug。上面的几条规则大概意思如下：

- pod 不设置任何参数，直接用镜像里面自带的参数
- pod 的 command 和 args 都设置，使用设置的命令和参数
- pod 只设置 command ，完全忽略镜像里的参数
- pod 只设置 args，镜像中的命令与新参数一起使用

一般来说，我们最好将启动命令在镜像里设置好，这样就不用在 pod 里设置。如果要在 pod 里面设置，最好填上 command, 这样就完全以 pod 的参数为准，方便理解。下面看个例子：

文件名：pod-command.yaml

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pod-command
spec:
  restartPolicy: Never
  containers:
  - name: pod-command-container
    image: busybox
    imagePullPolicy: IfNotPresent
    command: ["printenv"]
    args: ["HOSTNAME","PATH","KUBERNETES_PORT"]
```

在命令行中执行如下命令：

```bash
kubectl create -f /share/lesson/kubernetes/pod-command.yaml
kubectl get pods -w   # 查看 command-demo 是否是 Running 或 Completed 状态，如果不是就等待一会
```

查看该pod的日志输出

```bash
kubectl logs pod-command
```

这个例子中我们就是将 command 和 args 都设置了，默认的 debian 的启动命令是 bash,在 pod 里面没有什么实际的用途。这里我们使用了 printenv 命令来打印出来 HOSTNAME 和 KUBERNETES_PORT 两个环境变量的值。
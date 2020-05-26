# Kubernetes 环境安装及配置 			

## 本课程在线环境的安装-单机模式

```bash
#关闭磁盘swap提升性能
swapoff -a

#进行相应的网络配置
modprobe br_netfilter
echo 1 > /proc/sys/net/ipv4/ip_forward
```

```bash
#使用Kubernetes官方提供的kubeadm工具快速地部署kubernetes集群
kubeadm init  --cri-socket /run/containerd/containerd.sock --pod-network-cidr=10.244.0.0/16 --node-name=master --image-repository registry.cn-hangzhou.aliyuncs.com/google_containers --kubernetes-version v1.18.2
```

```bash
#设置配置文件
rm -rf $HOME/.kube
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config
```

```bash
#将主节点标记为可供pod调度
kubectl taint nodes master node-role.kubernetes.io/master-
```

```bash
#安装Flannel网络插件
kubectl create -f /share/images/kube-flannel.yml
```


```bash
#验证集群内pod工作情况
kubectl get po  -A 
```
会出现如下类似的提示,当STATUS为Runing，代表Pod运行正常。
```txt
NAMESPACE     NAME                             READY   STATUS    RESTARTS   AGE
kube-system   coredns-546565776c-4k6cn         1/1     Running   0          6m16s
kube-system   coredns-546565776c-sdd4n         1/1     Running   1          6m16s
kube-system   etcd-master                      1/1     Running   0          6m25s
kube-system   kube-apiserver-master            1/1     Running   0          6m25s
kube-system   kube-controller-manager-master   1/1     Running   0          6m25s
kube-system   kube-flannel-ds-amd64-glzlx      1/1     Running   0          54s
kube-system   kube-proxy-gzkbf                 1/1     Running   0          6m17s
kube-system   kube-scheduler-master            1/1     Running   0          6m25s
```

```bash
#验证节点
kubectl get node
```
当节点STATUS为Ready，代表节点上的k8s集群已经准备好了。
```txt
NAME     STATUS   ROLES    AGE     VERSION
master   Ready    master   6m40s   v1.18.2
```

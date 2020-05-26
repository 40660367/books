# Linux 性能监控

## CPU监控相关命令

### `top`
Linux下常用的性能分析工具，能够实时显示系统中各个进程的资源占用状况及总体状况。实时显示系统中各个进程的资源占用状况及总体状况。

### `mpstat`
实时系统监控工具，它会报告与多核心CPU相关的统计信息。
```bash
apt install sysstat -y
mpstat 1 #每隔一秒输出CPU占用情况
```

## 内存监控相关命令
### `free`命令
可以用来快速查看主机的内存使用情况，包括了物理内存和虚拟内存。后面可以加上参数：-h和-m，否则默认会以kb为单位显示。
```bash
free -h
```
相关参数说明:
> total：物理内存大小，就是机器实际的内存  
> used：已使用的内存大小，这个值包括了 cached 和 应用程序实际使用的内存  
> free：未被使用的内存大小  
> shared：共享内存大小，是进程间通信的一种方式  
> buffers：被缓冲区占用的内存大小  
> cached：被缓存占用的内存大小  

### `vmstat`
vmstat（Virtual Meomory Statistics，虚拟内存统计）是对系统的整体情况进行统计，包括内核进程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息。命令格式：vmstat 2 100，其中2表示刷新间隔，100表示输出次数。
```bash
vmstat 2 100
```

## 网络监控
### sar
`sar`是一个在Unix和Linux操作系统中用来收集、报告和保存CPU、内存、输入输出端口使用情况的命令。SAR命令可以动态产生报告，也可以把报告保存在日志文件中。
```bash
sar -n DEV 3 100
```

### netstat
`netstat`命令一般用于检验本机各端口的网络连接情况，用于显示与IP、TCP、UDP和ICMP协议相关的统计数据。

```bash
netstat -aup # 输出所有UDP连接状况
netstat -atp # 输出所有TCP连接状况
netstat -s # 显示各个协议的网络统计信息
netstat -i # 显示网卡列表
netstat -r # 显示路由表信息
```

### tcpdump
`tcpdump`是最广泛使用的网络包分析器或者包监控程序之一，它用于捕捉或者过滤网络上指定接口上接收或者传输的TCP/IP包。格式：

```bash
apt install tcpdump -y
tcpdump -i eth0 -c 3
```
该命令不是系统自带的，可能需要自己搬运安装。命令执行效果如下：

## 磁盘监控
### `iostat`
`iostat`是一个用于收集显示系统存储设备输入和输出状态统计的简单工具。这个工具常常用来追踪存储设备的性能问题，其中存储设备包括设备、本地磁盘，以及诸如使用NFS等的远端磁盘。常用格式：

```bash
iostat -x -k 2 100 # 2表示刷新间隔，100表示刷新次数
```

### `iotop`
`iotop`命令是一个用来监视磁盘I/O使用状况的top类工具。iotop具有与top相似的UI，其中包括PID、用户、I/O、进程等相关信息。Linux下的IO统计工具如iostat，nmon等大多数是只能统计到per设备的读写情况，如果你想知道每个进程是如何使用IO的就比较麻烦，使用iotop命令可以很方便的查看。


## 全系统监控
上面分享的都是单个查看Linux系统磁盘、CPU、内存等指标的工具，如果我们想要迅速找出来主机的性能瓶颈所在，我们可以采用以下全能工具：

### glances
Glances是一个用来监视 GNU/Linux 和 FreeBSD 操作系统的 GPL 授权的免费软件，通过 Glances，我们可以监视 CPU，平均负载，内存，网络流量，磁盘 I/O，其他处理器 和 文件系统 空间的利用情况。

Glances 会用一下几种颜色来代表状态：
绿色：OK（一切正常） 
蓝色：CAREFUL（需要注意）
紫色：WARNING（警告）
红色：CRITICAL（严重）。

阀值可以在配置文件中设置，一般阀值被默认设置为（careful=50、warning=70、critical=90）。

```bash
apt install glances -y
glances
```


### dstat工具
dstat命令是一个用来替换vmstat、iostat、netstat、nfsstat和ifstat这些命令的工具，是一个全能系统信息统计工具。与sysstat相比，dstat拥有一个彩色的界面，在手动观察性能状况时，数据比较显眼容易观察；而且dstat支持即时刷新，譬如输入dstat 3即每三秒收集一次，但最新的数据都会每秒刷新显示。

直接使用dstat，默认使用的是-cdngy参数，分别显示cpu、disk、net、page、system信息，默认是1s显示一条信息。可以在最后指定显示一条信息的时间间隔，如`dstat 5`是每5s显示一条，`dstat 5 10`表示没5s显示一条，一共显示10条。
```bash
apt install dstat -y
dstat 5 10
```


#### 练习

## 本节作业
### 1. 创建文件，结果检查：
### 2. 对文件进行操作

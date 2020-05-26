# Linux 远程登录SSH

Linux一般作为服务器使用，这时我们就需要远程登录到Linux服务器来管理维护系统。

Linux系统中是通过ssh服务实现的远程登录功能，默认ssh服务端口号为 22。

## 从Linux终端利用登录远程服务器

安装ssh并启动ssh服务：

```bash
#apt install openssh-server && service sshd start
#右侧实验区系统已经安装
```

终端下使用ssh登录远程服务器：

```bash
#在右侧实验区，尝试从本地登陆本地
ssh -p 22 root@127.0.0.1
```

-p** 后面是端口,默认不指定的话是22

**username** 是服务器用户名,**127.0.0.1** 是本地服务器 ip，也可以是远程服务器的IP.

回国后会出现如下类似提示：

```reponse
The authenticity of host '127.0.0.1 (127.0.0.1)' can't be established.
ECDSA key fingerprint is SHA256:8c69pPPyheuR4qjFit+ZSz47G8mfgKYXRrPFex6Vcj4.
Are you sure you want to continue connecting (yes/no)? 
```

回车输入yes后，输入实验区提示的密码`{host0.token}`即可重复登录云环境本身。

## 实验

### 1、查看SSH客户端版本

有的时候需要确认一下SSH客户端及其相应的版本号。使用ssh -V命令可以得到版本号。需要注意的是，Linux一般自带的是OpenSSH:

```bash
ssh -V
```

### 2、连接到远程主机：

```bash
ssh name@remoteserver
```


说明：remoteserver代表远程主机，name为登录远程主机的用户名。

### 3、连接到远程主机指定的端口：

```bash
ssh name@remoteserver -p 2222
```


说明：p 参数指定端口号，通常在路由里做端口映射时，我们不会把22端口直接映射出去，而是转换成其他端口号，这时就需要使用-p端口号命令格式。

### 4、通过远程主机1跳到远程主机2：

```bash
ssh -t remoteserver1 ssh remoteserver2
```


说明：当远程主机remoteserver2无法直接到达时，可以使用-t参数，然后由remoteserver1跳转到remoteserver2。在此过程中要先输入remoteserver1的密码，然后再输入remoteserver2的密码，然后就可以操作remoteserver2了。

### 5、通过SSH运行远程shell命令：

```bash
ssh -l name remoteserver 'linux-command'
```

说明：连接到远程主机，并执行远程主机的linux命令。

例如：查看远程主机的内存使用情况。

```bash
ssh root@localhost free -G
```

### 6、修改SSH监听端口：

默认情况下，SSH监听连接端口22，攻击者使用端口扫描软件就可以看到主机是否运行有SSH服务，将SSH端口修改为大于1024的端口是一个明智的选择，因为大多数端口扫描软件（包括nmap）默认情况都不扫描高位端口。

```bash
cat /etc/ssh/sshd_config
```

并查找下面这样的行：`Port 22`
去掉该行前面的# 号，然后修改端口号并重新启动SSH服务：

```bash
service ssh restart
```

### 7、仅允许SSH协议版本2：

有两个SSH协议版本，仅使用SSH协议版本2会更安全，SSH协议版本1有安全问题，包括中间人攻击（man-in-the-middle）和注入（insertion）攻击。编辑

```bash
cat /etc/ssh/sshd_config
```

文件并查找下面这样的行：
\# Protocol 2，1
修改为
Protocol 2

```bash
service ssh restart
```

### 8、禁止root用户登录：

通常情况下，不采用直接用root用户登录到远程主机，由于root用户拥有超级权限，这样会带来安全隐患，所以，一般我们用普通用户登录，当需要管理远程主机时，再切换到root用户下。打开/etc/ssh/sshd_config文件并查找下面这样的行：

\#PermitRootLogin yes
将#号去掉，然后将yes修改成no，重启ssh服务，这样就可以禁止root用户登录。

```bash
cat /etc/ssh/sshd_config
```

```bash
service ssh restart
```

### 9、进行端口映射：

假如公司内网有台web服务器，但是只对内不对外，这样，外网就无法访问，可以用ssh进行端口映射来实现外网访问内网的web服务器。假如web服务器名为webserver，webserver可以用ssh访问到远端主机remoteserver，登录到webserver，然后用下面命令进行映射
命令格式：

```shell
ssh -R 3000:localhost:80 remoteserver
```

执行完成后，在remoteserver机器上，执行netstat -an | grep 3000，查看有没有开通3000端口。并执行以下命令观察是否可以打开webserver上的网页

```bash
wget http://127.0.0.1:3000
```

如果能打开界面，说明映射成功.但是，这只限于本机访问web服务器，即只能remoteserver机器访问webserver。因为3000端口绑定的是remoteserver机器的127.0.0.1端口。可以编辑remoteserver机器上的/etc/ssh/sshd_config文件并添加如下内容：
添加 GatewayPorts yes 内容，把监听端口3000绑定到 0.0.0.0 地址上，这样外部的所有机器都能访问到这个监听端口，然后保存退出。并重启ssh服务。完成后其它机器就可以在浏览器中输入 http://remoteserver:3000来访问webserver了。

### 10、设置登录时提示信息

首先编辑一个文件，如bannertest.txt，文件内容自行定义。

```bash
echo 'my welcome info' > /welcome.text
vim /etc/ssh/sshd_config
```

然后打开文件并查找下面这样的行：
\#Banner /some/path

将#号去掉，然后将bannertest.txt文件的全路径替换/welcome.text，然后保存，

```bash
service ssh restart
```

```bash
ssh root@localhost
```

重启ssh服务。当客户端登录时，就会看到bannertest.txt文件中的提示信息。
# Go语言 环境安装及配置 			

在学习Go语言编程之前，我们需要安装和配置好Go语言的开发环境。可以选择在右侧的在线环境进行配置安装使用，也可以在您自己的计算机上安装开发编译环境。

## 本课程在线环境的安装

```shell
#1.下载Go安装包到当前目录
#wget https://dl.google.com/go/go1.12.9.linux-amd64.tar.gz
cp /share/tar/go1.12.9.linux-amd64.tar.gz .

#2.解压到安装包/usr/local目录
#说明：解压成功后，会在/usr/local目录下生成go目录，亦即go的安装路径是/usr/local/go
tar -C /usr/local -xzvf go1.12.9.linux-amd64.tar.gz

#3.添加/usr/local/go/bin这个安装路径到系统PATH环境变量(需要root权限)
echo export PATH=$PATH:/usr/local/go/bin >> /etc/profile

#4.使对环境变量的变更立刻生效
source /etc/profile

#5.验证安装
go version
```

当有提示时，即证明您已经在您当前的云环境中安装成功，您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**
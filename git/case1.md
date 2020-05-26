# Git 开发示例

## 注册GitHub
本练习以 Github 为例作为远程仓库，如果你没有 Github 可以在官网 https://github.com/ 注册。

以注册名为`giter`，邮箱为`giter@qq.com`为例 。

新建一个repo,名为test。

## 配置本地连接加密
首先在本地创建ssh key；
```shell
ssh-keygen -t rsa -C "giter@qq.com"
```
注意将`giter@qq.com`改为你在github上注册的邮箱，之后会要求确认路径和输入密码，我们这使用默认的一路回车就行。

成功的话会在~/下生成.ssh文件夹，进去，打开id_rsa.pub，复制里面的key。

```shell
cat ~/id_rsa.pub
```
## 将本地信息添加至Github用户设置中
登陆github，进入 Account Settings（账户配置），左边选择`SSH and GPG keys`，选择绿色的`New SSH Key`后,title部分填写主机名，key部分粘贴`cat ~/id_rsa.pub`的结果。

为了验证是否成功，在git bash下输入：
```shell
ssh -T git@github.com
```
如果是第一次的会提示是否continue，输入yes就会看到：

> Hi giter! You've successfully authenticated, but GitHub does not provide shell access.

这就表示已成功连上github。

## 设置姓名和邮箱地址
接下来我们要做的就是把本地仓库传到github上去，在此之前还需要设置username和email，因为github每次commit都会记录他们。

```shell
git config --global user.name "giter"
git config --global user.email "giter@qq.com"
```
这个命令，会在“ ~/.gitconfig ”中以如下形式输出设置文件
```shell
cat ~/.gitconfig
```

## 配置远程仓库
远程(remote)服务器端包含多个repository，每个repository可以理解为一个仓库或项目。而每个repository下有多个branch。

### 远程branch指针:master

服务器端的"master"（强调服务器端是因为本地端也有master）就是指向某个repository的一个branch的指针。

### 远程repo指针
"origin"是指向远程某个repository的指针。

### branch指针:head，`*`号表示
```shell
git remote #查看当前已经配置了哪些远程仓库

git remote add origin https://github.com/giter/test #添加一个远程仓库
git remote show origin #查看origin指向远程仓库的信息

git remote -v #查看远程仓库的版本变动记录

git ls-remote #查看远程仓库的分支
```
## 推送到远程仓库

命令格式：

`git push [alias] [branch]`


将本地仓库 [branch] 分支推送成为 [alias] 远程仓库上的 [branch] 分支


`git push <远程git库完整库名> <本地分支>:<远程分支>`

指定本地分支推送至远程分支

```shell
echo local >> local.txt
git add local.txt
git commit -m 'add a local file'
#此时改动已经提交到了 HEAD，但是还没到远端仓库。

git push -u origin master
#origin是指向某个远程仓库，master指向某个仓库下某个branch
#-u 第一次提交时将本地的master与远程的master关联起来
```
返回GitHub上查看，可以在master分支上看到刚刚从本地push上来的local.txt这个文件


## 删除远程仓库
我们需要将远程仓库与本地解除绑定。
```shell
git remote rm origin #查看origin指标指向远程仓库的信息
git remote -v
```
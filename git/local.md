# Git 本地仓库(local)

## 创建仓库
本章节我们将为大家介绍如何创建一个Git仓库。

Git使用`git init`命令来初始化一个 Git 仓库，Git 的很多命令都需要在 Git 的仓库中运行，所以 git init 是使用 Git 的第一个命令。

在执行完成`git init`命令后，Git 仓库会生成一个.git目录，该目录包含了资源的所有元数据，其他的项目目录保持不变

```shell
cd ~
git init #使用当前目录作为Git仓库
mkdir repotest
git init repotest #或者可以使用指定已存在的目录作为Git仓库
```

现在你可以看到在你的项目中生成了 .git 这个子目录。 这就是你的 Git 仓库了，所有有关你的此项目的快照数据都存放在这里。

## 加入跟踪
初始化后，会在`repotest`目录下会出现一个名为`.git`的目录，所有 Git 需要的数据和资源都存放在这个目录中。

如果当前目录下有几个文件想要纳入版本控制，需要先用`git add`命令告诉Git开始对哪些文件进行跟踪。
```shell
touch aaa 
git add aaa
```
## 查看当前仓库状态
`git status`命令用于查看仓库已被追踪的文件和未被追踪的文件
```shell
echo '# README' >> README
git add README 
git status 
```
### 查看跟踪文件的不同版本
`git diff`命令来查看执行`git status`的结果的详细信息。在这里可以看到对README文件的变化的记录。
```shell
#修改README后使用git diff查看README这个文件日哟微信
echo '## Title 1' >> README
git diff
```

## 提交
使用`git add`命令将想要快照的内容写入缓存区， 而执行`git commit`将缓存区内容添加到仓库中。
```shell
git add README #将已经发生更新的README加入追踪
git commit -m 'add file: aaa and README'
```
现在我们已经将快照写入仓库。如果我们再执行`git status`会显示清空的状态。
```shell
git status
```
以上输出说明我们在最近一次提交之后，没有做任何改动，是一个"working directory clean：干净的工作目录"。

## 提交历史
`git log`显示所有的提交历史记录
```shell
git log
git log --oneline #简要版
```
## 复制一个现在有仓库
使用`git clone`拷贝一个Git仓库到本地，让自己能够查看该项目，或者进行修改。

克隆仓库的命令格式为：`git clone <reponame>`
```shell
git clone https://github.com/tensorflow/tensorflow.git
#将Github上tensorflow这个Repo克隆至当前目录下的tensorflow目录
ll tensorflow #查看clone下来的东西
```
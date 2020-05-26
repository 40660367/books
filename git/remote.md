
# Git 远程仓库(remote)

## 克隆远程仓库
`git clone 远程git仓库地址`从远程仓库完全克隆下来


## 提取远程仓库
### `git fetch`
`git fetch`从远程仓库下载新分支与数据
```shell
git fetch origin
```
### `git merge`
`git merge`从远端仓库提取数据并尝试合并到当前分支,该命令就是在执行 git fetch 之后紧接着执行`git merge`远程分支到你所在的任意分支。
`git pull`

### `git pull `
可以这样简单理解`git pull = git fetch + git merge`

每次工作之前，先把远程库的最新的内容pull下来，可以立刻看到别人的改动，然后在前人的工作基础上开始一天的工作，这是一个好习惯！！！

另外所有的push操作，只有在pull之后才能进行,换句话来说就是你本地的分支必须先拥有远程分支所有的东西之后，才允许你提交新的修改内容。

#### `git pull`命令格式
`git pull <远程主机> <远程分支>:<本地分支>`  //将远程分支拉取到本地，并与本地分支合并

`git pull <远程主机> <远程分支>`  //将远程分支拉取到本地，并与当前分支合并,可省略本地分支

`git pull <远程主机> ` //本地的当前分支自动与对应的origin主机追踪分支(remote-tracking branch)进行合并。

Git也允许手动建立追踪关系。

`git branch --set-upstream master origin/next`将本地master分支与远程的next分支建立tracking关系

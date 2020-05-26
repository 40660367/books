# Git 分支(branch)

几乎每一种版本控制系统都以某种形式支持分支。使用分支意味着你可以从开发主线上分离开来，然后在不影响主线的同时继续工作。

查看分支命令：`git branch`
创建分支命令：`git branch (branchname)`
切换分支命令: `git checkout (branchname)`


## 在gitbranch目录下创建仓库
```shell
mkdir ~/gitbranch && cd ~/gitbranch
git
```
## 对master分支进行操作
```shell
cd ~/gitbranch
touch master-test
git add master-test
git commit -m 'add file master-test'
```

## 列出gitbranch仓库下所有分支,并创建一个新的分支dev
```shell
git branch #查看当前所处分支
git branch dev #创建新分支dev
git checkout dev #切换分支至dev
git branch# #查看当前所处分支
```

## 在该分支下创建文件并加入仓库
```shell
touch dev-test
git add dev-test
git commit -m 'add file dev-test'
ll
```

## 切换分支至master
```shell
git checkout master
ls
```

## 合并
当你切换分支的时候，Git 会用该分支的最后提交的快照替换你的工作目录的内容， 所以多个分支不需要多个目录。

一旦某分支有了独立内容，你终究会希望将它合并回到你的主分支。 你可以使用以下命令将任何分支合并到当前分支中去：
`git merge`命令可以多次合并到统一分支，也可以选择在合并之后直接删除被并入的分支。

```shell
git checkout master #切回主分支master
git merge dev #将dev分支合并至master
```

## 合并冲突
合并并不仅仅是简单的文件添加、移除的操作，Git 也会合并修改。

例如，我们可以将在master上的一个文件，在另一个分支dev下进行修改并提交。切换回master分支也进行修改后。对两个分去进行合并，这时git就会提醒会有合并冲突，需要我们手工来解决
```shell
git branch checkout master
touch merge
git commit -m 'add merge empty file!'

git branch checkout dev
git add merge
echo merge in dev >> merge
git commit -m 'modify merge in dev'

git branch checkout master
git add merge
echo merge in master >> merge
git commit -m 'modify merge in master'


git merge dev
```

## 删除分支
```shell
git branch -d dev #删除分支
ll #查看分支合并后的文件
```
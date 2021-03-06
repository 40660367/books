# Linux 简介
Linux 内核最初只是由芬兰人林纳斯·托瓦兹（Linus Torvalds）在赫尔辛基大学上学时出于个人爱好而编写的。

Linux 是一套免费使用和自由传播的类 Unix 操作系统，是一个基于 POSIX 和 UNIX 的多用户、多任务、支持多线程和多 CPU 的操作系统。Linux 能运行主要的 UNIX 工具软件、应用程序和网络协议。它支持 32 位和 64 位硬件。Linux 继承了 Unix 以网络为核心的设计思想，是一个性能稳定的多用户网络操作系统。

### Linux与UNIX的渊源

Linux 和 UNIX 之间的关系是一个很有意思的话题。在目前主流的服务器端操作系统中，UNIX 诞生于 20 世纪 60 年代末，Windows 诞生于 20 世纪 80 年代中期，Linux 诞生于 20 世纪 90 年代初，可以说 UNIX 是操作系统中的"老大哥"，后来的 Windows 和 Linux 都参考了 UNIX。

## Linux 应用领域
今天各种场合都有使用各种 Linux 发行版，从嵌入式设备到超级计算机，并且在服务器领域确定了地位。
- IT服务器Linux系统应用领域
- 嵌入式Linux系统应用领域
- 个人桌面Linux应用领域

## 为什么要用Linux系统

- 长期运行的稳定性
- 多数软件只有Linux版本
- 强大的Bash命令简化繁琐的操作，尤其是大大简化重复性工作

## 如何上手Linux？
对于初学者来说，接触和理解Linux操作系统需要一些时间和摸索。陡然从可视化点选操作的Windows进入到只有命令行界面的Linux，最大的陌生感是不知道做什么，不知道文件在哪？本课程通过在线练习帮助大家适应Linux系统。

打开Windows，首先看到的是桌面；不爱整理文件的我，桌面的东西已经多到需要2个屏幕才能显示的完。另外一个常用的就是我的电脑，然后打开D盘，依次点开对应的文件夹，然后点开文件。

Linux的文件系统组织方式与Windows略有不同，登录进去就是家目录，可视为Windows下的桌面。在这个目录下，我们可以新建文件、新建文件夹，就像在桌面上的操作一样。

### 初识Linux系统
登录Linux系统后，呈现在眼前的是这样一个界面:

> `root@FreeAIHub:~#`

首先解释下出现的这几个字母和符号:
- `root`: 用户名
- `FreeAIHub`：登陆计算机的主机名
- `@`：用户名与主机名的分隔符
- `~`: 代表root用户的家目录, 在我们其它路径后，这处会跟着改变
- `#`: 用来指示根用户输入命令的地方；对普通用户来说一般是`$`

我们与Linux的交互是通过命令进行的，命令就在后边输入即可。

## Linux命令
### Linux命令语法格式
Linux命令由命令选择和参数三部分组成

命令格式： 命令 选项 参数  
例子：`ls -la /etc`  

> 说明：  
> 1.个别命令使用不遵循此格式，选择和参数这种符号表示可以省略  
> 2.当有多个选项时，可以写在一起  
> 3.简化选项(一般用一个-)与完整选项（一般用两个--）比如`ls  -a`等于`ls  --all`

如果想查看当前目录下都有什么内容，输入命令`ls`，回车即可 (ls可以理解为单词list的缩写)。
#### 练习
```bash
ls
ls -l
ls --all
```

### Linux命令报错
如果错把l看成了i，输入了is，则会出现下面的提示`-bash: is: command not found
`未找到命令。
如果输入的是Linux基本命令，出现这个提示，基本可以判定是命令输入错了，瞪大眼睛仔细看就是了。在敲完命令回车后，注意查看终端的输出，以判断是否有问题。

另外，Linux大小写敏感的，is与IS,iS是`不一样`的。

### Linux命令的参数
前面使用的命令，有几个用到了参数如`ls -l`, `head -n 6`等，需要注意的是命令跟参数之间要有空格。

#### 练习:使用带参数的命令
```bash
ls -l
head /etc/passwd -n 5
```

### Linux命令帮助
终端运行man ls可以查看ls所有可用的参数，上下箭头翻页，按q退出查看。(man: manual, 手册),或者在命令后使用 --help 阅读其帮助信息。

#### 练习：两种方式查看ls命令的帮助
```bash
man ls
ls --help
```

## Linux 的发行版
Linux 的发行版说简单点就是将 Linux 内核与应用软件做一个打包。

Linux发行版主要有三个分支：Debian、Redhat、Slackware。

目前市面上较知名的发行版有：Ubuntu、RedHat、CentOS、Debian、Fedora、SuSE、OpenSUSE、Arch Linux、SolusOS 等。


#### 练习: 查看当前Linux系统的发行版本
```bash
cat /etc/issue
```
#### 练习: 查看当前计算机及操作系统的相关信息

```bash
uname -a
```
#### 练习: 查看当前系统启动了多久

```bash
uptime
```

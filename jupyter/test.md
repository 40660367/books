# Jupyter 测试

下面我们将通过完成几个简单的测试来达到熟悉平台的目标.

## 环境配置

[环境安装](./setup.html)

## 任务1：新建个人目录/程序/终端环境

点击右上角 'new' 按钮,在弹出菜单中:
- new-> python : 创建一个python的程序文档
- new-> folder  : 创建一个目录

点击右上角 'upload' 按钮, 可以“上传”个人的文件

## 任务2：熟悉工具栏操作

上图所示区域就是工具栏。鼠标悬停可以显示各按钮含义。

请通过工具栏操作完成下面的练习:

（注意：在Python中#号开头，代表注释开始，注释可以执行，但不会有任何反馈）


```python
#操作练习1: 把我这行复制一份...
```


```python
#操作练习2: 把我移动到上面去...
#事实上同一个notebook中各种代码框，不管是否已执行，都是可以自由移动的。
```

## 任务3：熟悉快捷键操作

除了点击工具栏,大部分操作都可以通过键盘快捷键来完成的, 这会大大提高操作的效率。

详细的键盘快捷操作信息可以点击工具栏的如下按钮查看到:


最最常用的键盘快捷键:
- ↑和↓ ： 切换代码框（cell） 
- shift + enter : 运行当前cell并挪动到下一个cell
- ctrl + enter ：运行当前cell，保持在当前cell
- b : 在当前cell下面插入新cell
- a : 在当前cell上面插入新cell
- dd (敲击d键两下): 删除当前cell
- m : 将当前cell由code模式转换成markdown模式
- y : 将当前cell由markdown模式转换成code模式

下面,你需要通过键盘操作的方式完成下面的练习:


```python
#操作练习: 敲击 b 键,在我下面增加一行...
```


```python
##### 操作练习: 敲击 m 键,把我转成markdown并运行
```

操作练习: 敲击 y 键,把下列转成code并运行

print("Hello, world!")


### 关于markdown

Markdown 是一种「电子邮件」风格的「标记语言」，作为对比，我们经常看到的用于写网页的html语言也是一门标记语言。关于md具体的介绍我不做展开，可以参阅[Markdown 新手指南](/markdown.html)。作为简单了解，大家可以双击本Notebook中的任意一个文本形式的cell，即可看到源代码，不出几分钟就可以弄清我是怎么利用Markdown实现设置各级标题、插入图片、列举等功能的。Markdown cell

事实上，内嵌Markdown也是Jupyter Notebook的一大亮点。Markdown与Python code结合，这感觉就像在写文章的过程中穿插代码，用户体验非常好。

## 任务4：自由操作

关于菜单栏，我重点说一下Kernel菜单。当我们遇到程序出故障时，可以在kernel菜单进行Interrupt。如果界面右上方显示not connected提示，表明和Python的连接丢失了，可以在Kernel菜单进行reconnect。破罐子破摔的时候，我们可以选择restart，但这会丢失所有之前已经存储在内存中内容。当然有时候我们想从头到尾跑一遍这个notebook中的所有代码，这时可以restart & run all。如果我们单纯只是想清空所有输出，也可以用restart & clear output。

请大家自由尝试。

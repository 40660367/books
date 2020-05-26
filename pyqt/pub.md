# PyQt 发布

将.py 文件打包成.exe可执行程序

这里我用到的Pyinstaller这个模块，首先，需要安装pyinstaller; 安装方法推荐 使用 pip install pyinstaller(由于这个功能的实现还需要依赖一些其他的库，pip比较省事)

安装完成后，我们可以在如下路径找到Pyinstaller应用程序：C:\Python27\Scripts\

参考链接：http://jingyan.baidu.com/article/a378c960b47034b3282830bb.html

比较直接的方法就是使用Pyinstaller应用程序调用待发布脚本

　即执行：pyinstaller.exe  -w -F xx\xx\xxx.py

-w: 直接发布的exe应用带命令行调试窗口，在指令内加入-w命令可以屏蔽掉命令框（调试阶段可不加-w, 最终发布时加入-w参数）

-F: 这里是大写。使用-F指令可以把应用打包成一个独立的exe文件，否则是一个带各种dll和依赖文件的文件夹

-p :这个指令后面可以增加pyinstaller搜索模块的路径。因为应用打包涉及的模块很多。这里可以自己添加路径。不过经过笔者测试，site-packages目录下都是可以被识别的，一般不需要再手动添加

```shell
pip3 install pyinstaller==3.6 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

打包这个软件

```shell
pyinstaller -w -F /share/lesson/pyqt5/qprinter.py
```

看看在当前目录的dist路径下，产生了新的，可以在右侧的实验区进行执行

```
./dist/qprinter
```


# PyQt 多文档界面(mdi)

典型的GUI应用程序可能具有多个窗口。选项卡式和堆叠式小部件允许一次激活一个这样的窗口。但是，由于隐藏了其他窗口的视图，很多时候这种方法可能没有用。

同时显示多个窗口的一种方法是将它们创建为独立的窗口。这称为SDI（单个文档接口）。这需要更多的内存资源，因为每个窗口可能都有其自己的菜单系统，工具栏等。

MDI（多文档界面）应用程序消耗较少的内存资源。子窗口相对于彼此放置在主容器内。容器小部件称为**QMdiArea**。

QMdiArea小部件通常占据QMainWondow对象的中央小部件。此区域中的子窗口是QMdiSubWindow类的实例。可以将任何QWidget设置为subWindow对象的内部小部件。MDI区域中的子窗口可以级联或平铺方式排列。

下表列出了QMdiArea类和QMdiSubWindow类的重要方法-

| 序号 |                          方法与说明                          |
| :--: | :----------------------------------------------------------: |
| 1个  |    **addSubWindow（）**将小部件添加为MDI区域中的新子窗口     |
|  2   | **removeSubWindow（）**删除作为子窗口内部窗口小部件的窗口小部件 |
|  3   |           **setActiveSubWindow（）**激活一个子窗口           |
|  4   |   **CascadeSubWindows（）**以级联方式在MDiArea中排列子窗口   |
|  5   |    **tileSubWindows（）**以平铺方式在MDiArea中排列子窗口     |
|  6   |          **closeActiveSubWindow（）**关闭活动子窗口          |
|  7   |        **subWindowList（）**返回MDI区域中的子窗口列表        |
|  8   | **setWidget（）**将QWidget设置为QMdiSubwindow实例的内部窗口小部件 |

QMdiArea对象发出subWindowActivated（）信号，而windowStateChanged（）信号由QMdisubWindow对象发出。

## 例

在下面的示例中，由QMainWindow组成的顶级窗口具有一个菜单和MdiArea。

```python
self.mdi = QMdiArea()
self.setCentralWidget(self.mdi)
bar = self.menuBar()
file = bar.addMenu("File")

file.addAction("New")
file.addAction("cascade")
file.addAction("Tiled")
```

菜单的Triggered（）信号连接到windowaction（）函数。

```python
file.triggered[QAction].connect(self.windowaction)
```

菜单的新操作在MDI区域中添加了一个带有递增编号的标题的子窗口。

```python
MainWindow.count = MainWindow.count+1
sub = QMdiSubWindow()
sub.setWidget(QTextEdit())
sub.setWindowTitle("subwindow"+str(MainWindow.count))
self.mdi.addSubWindow(sub)
sub.show()
```

菜单的级联和平铺按钮分别以级联和平铺方式排列当前显示的子窗口。

## 示例

完整的代码如下-

文件名：mdi.py

```python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class MainWindow(QMainWindow):
    count = 0

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()

        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered[QAction].connect(self.windowaction)
        self.setWindowTitle("MDI demo")
        
    def windowaction(self, q):
        print("triggered")
        
        if q.text() == "New":
            MainWindow.count = MainWindow.count+1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("subwindow"+str(MainWindow.count))
            self.mdi.addSubWindow(sub)
            sub.show()
            
        if q.text() == "cascade":
            self.mdi.cascadeSubWindows()
                
        if q.text() == "Tiled":
            self.mdi.tileSubWindows()
            
def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
```

```shell
python3 /share/lesson/pyqt5/mdi.py
```

康康
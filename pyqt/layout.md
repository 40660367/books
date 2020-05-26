# PyQt 布局(layout)

通过指定以像素为单位的绝对坐标，可以将GUI小部件放置在容器窗口内。坐标相对于由setGeometry（）方法定义的窗口的尺寸。

## setGeometry()语法

```
QWidget.setGeometry(xpos, ypos, width, height)
```

在以下代码段中，监视器上位置（10、10）上显示了300 x 200像素尺寸的顶级窗口。

```python3
import sys
from PyQt4 import QtGui

def window():
   app = QtGui.QApplication(sys.argv)
   w = QtGui.QWidget()
	
   b = QtGui.QPushButton(w)
   b.setText("Hello World!")
   b.move(50,20)
	
   w.setGeometry(10,10,300,200)
   w.setWindowTitle(“PyQt”)
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()
```

在窗口中添加了一个**PushWidget**小部件，并将其放置在窗口右50像素和窗口左上20像素以下的位置。

但是，由于以下原因，此**绝对定位**不适合-

- 即使调整窗口大小，小部件的位置也不会改变。
- 在具有不同分辨率的不同显示设备上，外观可能不一致。
- 布局修改很困难，因为可能需要重新设计整个表单。

![原始和调整大小的窗口](https://www.tutorialspoint.com/pyqt/images/original_resized_window.jpg)

PyQt API提供了布局类，用于更优雅地管理容器内小部件的位置。布局管理器相对于绝对定位的优势是-

- 窗口内的小部件会自动调整大小。
- 确保具有不同分辨率的显示设备上的外观均匀。
- 无需重新设计，就可以动态添加或删除小部件。

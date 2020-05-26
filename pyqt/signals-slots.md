# PyQt-信号和插槽

与以顺序方式执行的控制台模式应用程序不同，基于GUI的应用程序是事件驱动的。函数或方法是根据用户的操作执行的，例如单击按钮，从集合中选择项目或单击鼠标等，称为**事件**。

用于构建GUI界面的小部件充当此类事件的来源。每个派生自QObject类的PyQt小部件都旨在响应一个或多个事件而发出“ **信号** ”。信号本身不执行任何操作。而是将其“连接”到“ **插槽** ”。该插槽可以是任何**可调用的Python函数**。

在PyQt中，可以通过不同的方式来实现信号和插槽之间的连接。以下是最常用的技术-

```python
QtCore.QObject.connect(widget, QtCore.SIGNAL(‘signalname’), slot_function)
```

当小部件发出信号时，调用slot_function的更方便的方法如下-

```python
widget.signal.connect(slot_function)
```

假设单击按钮时是否要调用一个函数。在此，点击信号将连接至可调用的功能。它可以通过以下两种技术中的任何一种来实现-

```python
QtCore.QObject.connect(button, QtCore.SIGNAL(“clicked()”), slot_function)
```

要么

```python
button.clicked.connect(slot_function)
```

## 例

在下面的示例中，在QDialog窗口中添加了两个QPushButton对象（b1和b2）。我们要在分别单击b1和b2时调用函数b1_clicked（）和b2_clicked（）。

单击b1时，将clicked（）信号连接到b1_clicked（）函数

```python
b1.clicked.connect(b1_clicked())
```

单击b2时，将clicked（）信号连接到b2_clicked（）函数

```python
QObject.connect(b2, SIGNAL("clicked()"), b2_clicked)
```

## 案例完整代码

文件名:signals-slots.py

```python
import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

def window():
   app = QApplication(sys.argv)
   win = QDialog()
   b1 = QPushButton(win)
   b1.setText("Button1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)

   b2 = QPushButton(win)
   b2.setText("Button2")
   b2.move(50,50)
   QObject.connect(b2,SIGNAL("clicked()"),b2_clicked)

   win.setGeometry(100,100,200,100)
   win.setWindowTitle("PyQt")
   win.show()
   sys.exit(app.exec_())

def b1_clicked():
   print "Button 1 clicked"

def b2_clicked():
   print "Button 2 clicked"

if __name__ == '__main__':
   window()
```

```shell
python3 /share/lesson/pyqt5/signals-slots.py
```
康康
# PyQt 对话框(QDialog)

**QDialog**小部件提供了一个顶级窗口，主要用于收集用户的响应。 它可以配置为**Modal** （它阻止其父窗口）或**Modeless** （可以绕过对话框窗口）。

PyQt API有许多预配置的Dialog小部件，如InputDialog，FileDialog，FontDialog等。

## 例子 (Example)

在以下示例中，Dialog窗口的WindowModality属性决定它是模态还是无模式。 对话框上的任何一个按钮都可以设置为默认值。 当用户按下Escape键时，QDialog.reject（）方法将丢弃该对话框。

顶级QWidget窗口上的PushButton，单击时会生成一个Dialog窗口。 对话框在其标题栏上没有最小化和最大化控件。

用户无法在后台下载此对话框，因为其WindowModality设置为ApplicationModal。

```python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("Hello World!")
   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())
def showdialog():
   d = QDialog()
   b1 = QPushButton("ok",d)
   b1.move(50,50)
   d.setWindowTitle("Dialog")
   d.setWindowModality(Qt.ApplicationModal)
   d.exec_()
if __name__ == '__main__':
   window()
```

```shell
python3 /share/lesson/pyqt5/qdialog.py
```

康康
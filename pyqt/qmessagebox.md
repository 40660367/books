# PyQt 消息框(qmessagebox)

**QMessageBox**是一个常用的模式对话框，用于显示一些参考消息，并有选择地要求用户通过单击其上的任一标准按钮来进行响应。每个标准按钮都有一个预定义的标题，一个角色并返回预定义的十六进制数字。

## 例

在以下示例中，在顶级窗口上单击按钮的信号，所连接的功能将显示消息框对话框。

```
msg = QMessageBox()
msg.setIcon(QMessageBox.Information)
msg.setText("This is a message box")
msg.setInformativeText("This is additional information")
msg.setWindowTitle("MessageBox demo")
msg.setDetailedText("The details are as follows:")
```

setStandardButton（）函数显示所需的按钮。

```
msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
```

buttonClicked（）信号连接到插槽功能，该功能标识信号源的标题。

```
msg.buttonClicked.connect(msgbtn)
```

该示例的完整代码如下

文件名:qmessage.py

```python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

def window():
   app = QApplication(sys.argv)
   w = QWidget()
   b = QPushButton(w)
   b.setText("Show message!")

   b.move(50,50)
   b.clicked.connect(showdialog)
   w.setWindowTitle("PyQt Dialog demo")
   w.show()
   sys.exit(app.exec_())
	
def showdialog():
   msg = QMessageBox()
   msg.setIcon(QMessageBox.Information)

   msg.setText("This is a message box")
   msg.setInformativeText("This is additional information")
   msg.setWindowTitle("MessageBox demo")
   msg.setDetailedText("The details are as follows:")
   msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   msg.buttonClicked.connect(msgbtn)
	
   retval = msg.exec_()
   print "value of pressed message box button:", retval
	
def msgbtn(i):
   print "Button pressed is:",i.text()
	
if __name__ == '__main__': 
   window()
```

```
python3 /share/lesson/pyqt5/qmessage.py
```

康康
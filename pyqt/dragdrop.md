# PyQt 拖放(dragdrop)

PyQt提供**拖放**对用户非常直观。在许多桌面应用程序中都可以找到它，用户可以在其中将对象从一个窗口复制或移动到另一个窗口。

基于MIME的拖放数据传输基于QDrag类。**QMimeData**对象将数据与其对应的MIME类型相关联。它存储在剪贴板上，然后在拖放过程中使用。

以下QMimeData类函数允许方便地检测和使用MIME类型。

|    测试仪    |    吸气剂     |      塞特犬      |   MIME类型    |
| :----------: | :-----------: | :--------------: | :-----------: |
| hasText（）  |   文本（）    |   setText（）    |  文字/纯文字  |
| hasHtml（）  |   html（）    |   setHtml（）    |  文字/ HTML   |
| hasUrls（）  |   urls（）    |   setUrls（）    | 文字/ uri列表 |
| hasImage（） | imageData（） | setImageData（） |    图片/ *    |
| hasColor（） | colorData（） | setColorData（） |   应用/ x色   |

许多QWidget对象都支持拖放活动。那些允许其数据被拖动的对象具有setDragEnabled（），必须将其设置为true。另一方面，小部件应响应拖放事件，以存储拖动到其中的数据。

- **DragEnterEvent**提供一个事件，当拖动动作进入该事件时，该事件将发送到目标窗口小部件。
- **DragMoveEvent**在进行拖放操作时使用。
- **DragLeaveEvent**是在拖放动作离开小部件时生成的。
- 另一方面，**DropEvent**在放置完成时发生。可以有条件地接受或拒绝事件的建议操作。

## 例

在下面的代码中，DragEnterEvent验证事件的MIME数据是否包含文本。如果是，则接受事件的建议操作，并将文本作为新项添加到ComboBox中。

文件名:dragdrop.py

```python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class combo(QComboBox):

   def __init__(self, title, parent):
      super(combo, self).__init__( parent)
	
      self.setAcceptDrops(True)
		
   def dragEnterEvent(self, e):
      print e
		
      if e.mimeData().hasText():
         e.accept()
      else:
         e.ignore()
			
   def dropEvent(self, e):
      self.addItem(e.mimeData().text())
		
class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()
		
      self.initUI()
		
   def initUI(self):
      lo = QFormLayout()
      lo.addRow(QLabel("Type some text in textbox and drag it into combo box"))
		
      edit = QLineEdit()
      edit.setDragEnabled(True)
      com = combo("Button", self)
      lo.addRow(edit,com)
      self.setLayout(lo)
      self.setWindowTitle('Simple drag & drop')
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   ex.show()
   app.exec_()
	
if __name__ == '__main__':
   main()
```

```shell
python3 /share/lesson/pyqt5/dragdrop.py
```


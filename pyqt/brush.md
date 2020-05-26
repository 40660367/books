# PyQt 画笔Brush

## 示例

```python
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

class Example(QWidget):

   def __init__(self):
      super(Example, self).__init__()
      self.initUI()
		
   def initUI(self):
      self.text = "hello world"
      self.setGeometry(100,100, 400,300)
      self.setWindowTitle('Draw Demo')
      self.show()
		
   def paintEvent(self, event):
      qp = QPainter()
      qp.begin(self)
      qp.setPen(QColor(Qt.red))
      qp.setFont(QFont('Arial', 20))
		
      qp.drawText(10,50, "hello Pyth
		on")
      qp.setPen(QColor(Qt.blue))
      qp.drawLine(10,100,100,100)
      qp.drawRect(10,150,150,100)
		
      qp.setPen(QColor(Qt.yellow))
      qp.drawEllipse(100,50,100,50)
      qp.drawPixmap(220,10,QPixmap("python.jpg"))
      qp.fillRect(200,175,150,100,QBrush(Qt.SolidPattern))
      qp.end()
		
def main():
   app = QApplication(sys.argv)
   ex = Example()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
```

```shell
python3 /share/lesson/pyqt5/brush.py
```

## 预定义的QColor样式

| Qt.NoBrush          | 无刷纹             |
| ------------------- | ------------------ |
| Qt.SolidPattern     | 颜色均匀           |
| Qt.Dense1Pattern    | 极密的画笔图案     |
| Qt.HorPattern       | 水平线             |
| Qt.VerPattern       | 垂直线             |
| Qt.CrossPattern     | 交叉水平线和垂直线 |
| Qt.BDiagPattern     | 向后斜线           |
| Qt.FDiagPattern     | 前斜线             |
| Qt.DiagCrossPattern | 交叉对角线         |

可以通过指定RGB或CMYK或HSV值来选择自定义颜色。

# PyQt 基础部件(BasicWidget)

## 示例

文件名:collection.py
```python
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 设置窗口标题
        self.setWindowTitle('My First App')

        # 定义布局
        layout = QVBoxLayout()

        # 展示的部件列表
        widgets = [QCheckBox,
                QComboBox,
                QDateEdit,
                QDateTimeEdit,
                QDial,
                QDoubleSpinBox,
                QFontComboBox,
                QLCDNumber,
                QLineEdit,
                QProgressBar,
                QPushButton,
                QRadioButton,
                QSlider,
                QSpinBox,
                QTimeEdit]

        # 将部件添加到列表中
        for item in widgets:
            layout.addWidget(item())

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
```

```shell
python3 /share/lesson/pyqt5/collection.py
```



| Sr.No |                         小部件和描述                         |
| :---: | :----------------------------------------------------------: |
|   1   | **QLabel** QLabel对象充当占位符以显示不可编辑的文本或图像，或充当动画GIF的影片。 它还可以用作其他小部件的助记键。 |
|   2   | **QLineEdit** QLineEdit对象是最常用的输入字段。 它提供了一个框，其中可以输入一行文本。 要输入多行文本，需要QTextEdit对象。 |
|   3   | **QPushButton** 在PyQt API中，QPushButton类对象提供了一个按钮，单击该按钮可以编程以调用某个功能。 |
|   4   | **QRadioButton** QRadioButton类对象提供带有文本标签的可选按钮。 用户可以选择表单上显示的众多选项之一。 此类派生自QAbstractButton类。 |
|   5   | **QCheckBox** 将QCheckBox对象添加到父窗口时，会出现文本标签前的矩形框。 就像QRadioButton一样，它也是一个可选择的按钮。 |
|   6   | **QComboBox** QComboBox对象显示可供选择的项目的下拉列表。 只需要显示当前所选项目所需的表单上的最小屏幕空间。 |
|   7   | **QSpinBox** QSpinBox对象向用户显示一个文本框，该文本框右侧显示带有向上/向下按钮的整数。 |
|   8   | **QSlider** QSlider类对象为用户提供了一个可以滑动槽。 它是一个控制数值的经典小部件。 |
|   9   | **小工具和信号QMenuBar，QMenu和QAction** QMainWindow对象标题栏正下方的水平QMenuBar保留用于显示QMenu对象。 |
|  10   | **QToolBar** QToolBar小部件是一个可移动的面板，由文本按钮，带图标的按钮或其他小部件组成。 |
|  11   | **QInputDialog**这是一个预先配置的对话框，带有文本字段和两个按钮，确定和取消。 用户单击“确定”按钮或按Enter后，父窗口将在文本框中收集输入。 |
|  12   | **QFontDialog** 另一个常用的对话框，字体选择器小部件是QDialog类的视觉外观。 此对话框的结果是Qfont对象，可以由父窗口使用。 |
|  13   | **QFileDialog**此小部件是文件选择器对话框。 它使用户能够浏览文件系统并选择要打开或保存的文件。 通过静态函数或通过调用对话框对象上的exec_（）函数来调用该对话框。 |
|  14   | **QTab**如果表单有太多字段无法同时显示，则可以将它们排列在选项卡式窗口小部件的每个选项卡下的不同页面中。 QTabWidget提供标签栏和页面区域。 |
|  15   | **QStacked**QStackedWidget的功能类似于QTabWidget。 它还有助于有效使用窗口的客户区域。 |
|  16   | **QSplitter**如果表单有太多字段无法同时显示，则可以将它们排列在选项卡式窗口小部件的每个选项卡下的不同页面中。 QTabWidget提供标签栏和页面区域。 |
|  17   | **QDock**可停靠窗口是一个子窗口，可以保持浮动状态，也可以在指定位置附加到主窗口。 QMainWindow类的主窗口对象具有为可停靠窗口保留的区域。 |
|  18   | **QStatusBar**QMainWindow对象在底部保留一个水平条作为状态栏。 它用于显示永久或上下文状态信息。 |
|  19   | **QList**QListWidget类是一个基于项的界面，用于在列表中添加或删除项。 列表中的每个项目都是QListWidgetItem对象。 ListWidget可以设置为多选。 |
|  20   | **QScrollBar**滚动条控件使用户能够访问可视区域外的文档部分。 它为当前位置提供视觉指示。 |
|  21   | **QCalendar**QCalendar小部件是一个有用的日期选择器控件。 它提供了基于月份的视图。 用户可以通过使用鼠标或键盘选择日期，默认为今天的日期。 |

# PyQt 主要类

PyQt API是大量的类和方法的集合。这些类在20多个模块中定义。以下是一些常用模块-

| 序号 |              模块与说明              |
| :--: | :----------------------------------: |
| 1个  | **QtCore**其他模块使用的核心非GUI类  |
|  2   |      **QtGui**图形用户界面组件       |
|  3   |    **Qt多媒体**低级多媒体编程的类    |
|  4   |       **QtNetwork**网络编程类        |
|  5   |       **QtOpenGL**OpenGL支持类       |
|  6   |       **Qt脚本**评估Qt脚本的类       |
|  7   | **QtSql的**使用SQL进行数据库集成的类 |
|  8   |   **QtSvg**用于显示SVG文件内容的类   |
|  9   |  **QtWebKit**用于渲染和编辑HTML的类  |
|  10  |         **QtXml**处理XML的类         |
|  11  |        **Qt助手**支持在线帮助        |
|  12  |  **QtDesigner**扩展Qt Designer的类   |

PyQt API包含400多个类。该**QObject的**类是类层次结构的顶部。它是所有Qt对象的基类。此外，**QPaintDevice**类是所有可以绘制的对象的基类。

**QApplication**类管理GUI应用程序的主要设置和控制流。它包含主事件循环，在其中处理和调度由窗口元素和其他源生成的事件。它还处理系统范围和应用程序范围的设置。

从QObject和QPaintDevice类派生的**QWidget**类是所有用户界面对象的基类。**QDialog**和**QFrame**类也从QWidget类派生。他们有自己的子类系统。

下图描述了层次结构中的一些重要类。

![层次结构](https://www.tutorialspoint.com/pyqt/images/hierarchy.jpg)![QWidget](https://www.tutorialspoint.com/pyqt/images/qwidget.jpg)![Q对话框](https://www.tutorialspoint.com/pyqt/images/qdialog.jpg)![QIO设备](https://www.tutorialspoint.com/pyqt/images/qiodevice.jpg)![QPaintDevice](https://www.tutorialspoint.com/pyqt/images/qpaintdevice.jpg)

这是常用小部件的选择列表-

以下是常用的小部件。

| 序号 |                         小部件和说明                         |
| :--: | :----------------------------------------------------------: |
| 1个  |                 **QLabel**用于显示文字或图像                 |
|  2   |              **QLineEdit**允许用户输入一行文字               |
|  3   |              **QTextEdit**允许用户输入多行文字               |
|  4   |               **Q按钮**一个命令按钮来调用动作                |
|  5   |           **QRadioButton**可以从多个选项中选择一个           |
|  6   |                **QCheckBox**可以选择多个选项                 |
|  7   |               **QSpinBox**允许增加/减少整数值                |
|  8   |     **QScrollBar**允许访问超出显示范围的窗口小部件的内容     |
|  9   |                **Q滑子**允许线性更改边界值。                 |
|  10  |            **QComboBox**提供项目下拉列表供您选择             |
|  11  |                **QMenuBar**单杠持有QMenu对象                 |
|  12  |    **QStatusBar**通常在QMainWindow的底部，提供状态信息。     |
|  13  |    **QToolBar**通常在QMainWindow顶部或浮动。包含动作按钮     |
|  14  |    **QListView**提供ListMode或IconMode中的项目的可选列表     |
|  15  | **QPixmap**屏幕外图像表示，用于显示在QLabel或QPushButton对象上 |
|  16  |      **Q对话框**模态或非模态窗口可以将信息返回到父窗口       |

一个典型的基于GUI的应用程序的顶层窗口是由**QMainWindow**小部件对象创建的。上面列出的某些小部件在此主窗口中占据指定的位置，而其他小部件则使用各种布局管理器放置在中央小部件区域中。

下图显示了QMainWindow框架-

![QMainWindow](https://www.tutorialspoint.com/pyqt/images/qmainwindow.jpg)
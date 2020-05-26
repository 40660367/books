# PyQt5 简介

## 关于PyQt5

PyQt5是Digia的一组Qt5应用程序框架的Python绑定。它适用于Python 2.x和3.x。本教程使用Python3。Qt库是功能最强大的GUI库之一。PyQt5的官方主页是 [www.riverbankcomputing.co.uk/news](http://www.riverbankcomputing.co.uk/news)。PyQt5由Riverbank Computing开发。

PyQt5被实现为一组Python模块。它具有620多个类和6000种功能和方法。它是一个多平台工具包，可在所有主要操作系统（包括Unix，Windows和Mac OS）上运行。PyQt5是双重许可的。开发人员可以在GPL和商业许可之间进行选择。

## PyQt5模块

PyQt5的类分为几个模块，包括以下模块：

- QtCore
- QtGui
- Qt小部件
- Qt多媒体
- Qt蓝牙
- QtNetwork
- Qt定位
- 恩吉尼奥
- QtWebSockets
- QtWebKit
- QtWebKitWidgets
- QtXml
- QtSvg
- QtSql的
- QtTest

该`QtCore`模块包含核心的非GUI功能。该模块用于处理时间，文件和目录，各种数据类型，流，URL，mime类型，线程或进程。在`QtGui`包含窗口系统集成，事件处理，2D图形，基本图像，字体和文本类。该`QtWidgets`模块包含提供一组UI元素的类，以创建经典的桌面样式用户界面。该`QtMultimedia`含有类来处理多媒体内容和API来访问照相机和收音机功能。

该`QtBluetooth`模块包含用于扫描设备以及与它们连接和交互的类。该`QtNetwork`模块包含用于网络编程的类。这些类通过使网络编程更加容易和可移植性，来简化TCP / IP和UDP客户端和服务器的编码。该`QtPositioning`包含的类通过使用各种可能的源，包括卫星，无线网络，或一个文本文件以确定位置。该`Enginio`模块实现了用于访问Qt Cloud Services托管应用程序运行时的客户端库。该`QtWebSockets`模块包含实现WebSocket协议的类。该`QtWebKit`包含基于该WebKit2库中的Web浏览器实现类。的`QtWebKitWidgets`包含用于基于WebKit的Web浏览器实现的类，以用于基于`QtWidgets`基础的应用程序。

该`QtXml`包含用于处理XML文件中的类。该模块提供了SAX和DOM API的实现。该`QtSvg`模块提供了用于显示SVG文件内容的类。可缩放矢量图形（SVG）是一种用于描述XML中的二维图形和图形应用程序的语言。该`QtSql`模块提供用于处理数据库的类。该`QtTest`包含的功能，使的PyQt5应用单元测试。

## PyQt4和PyQt5的区别

PyQt5与PyQt4向后不兼容。PyQt5有一些重大变化。但是，将旧代码调整为新库并不是很困难。除其他外，差异如下：

- Python模块已重新组织。有些模块已被丢弃（`QtScript`），其他人被分成子模块（`QtGui`，`QtWebKit`）。
- 新的模块已经出台，包括`QtBluetooth`，`QtPositioning`或`Enginio`。
- PyQt5仅支持新型信号和插槽handlig。`SIGNAL()` 或`SLOT()`不再支持该呼叫。
- PyQt5不支持Qt v5.0中标记为已弃用或过时的Qt API的任何部分。

## Python

![python徽标](D:\freeaihub\books\pyqt5\images\pythonlogo.png)

Python是一种通用的，动态的，面向对象的编程语言。Python语言的设计目的强调程序员的生产力和代码可读性。Python最初是由*Guido van Rossum*开发的。它于1991年首次发布。Python受到ABC，Haskell，Java，Lisp，Icon和Perl编程语言的启发。Python是一种高级通用通用解释型语言。Python是一种简约语言。它最明显的功能之一是它不使用分号或方括号。它改用缩进。目前，Python有两个主要分支：Python 2.x和Python3.x。Python 3.x破坏了与早期版本Python的向后兼容性。它的创建是为了纠正该语言的某些设计缺陷并使该语言更简洁。Python由世界各地的一大批志愿者维护。Python是开源软件。对于那些想学习编程的人来说，Python是一个理想的起点。

本教程使用Python 3.x版本。

Python编程语言支持多种编程样式。它不会强迫程序员采用特定的范例。Python支持面向对象和过程编程。对功能编程的支持也很有限。

Python编程语言的官方网站是 [python.org](http://python.org/)

Perl，Python和Ruby是广泛使用的脚本语言。它们具有许多相似之处，并且是紧密的竞争对手。
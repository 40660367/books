# PyQt 数据库处理

PyQt API包含精心设计的类系统，可与许多基于SQL的数据库进行通信。它的QSqlDatabase通过Connection对象提供访问。以下是当前可用的SQL驱动程序的列表-

| 序号 |                驱动程序类型和说明                 |
| :--: | :-----------------------------------------------: |
| 1个  |                  **QDB2**IBM DB2                  |
|  2   |        **QIBASE**Borland InterBase驱动程序        |
|  3   |                **QMYSQL**MySQL驱动                |
|  4   |      **生活质量指数**Oracle呼叫接口驱动程序       |
|  5   | **QODBC**ODBC驱动程序（包括Microsoft SQL Server） |
|  6   |              **QPSQL**PostgreSQL驱动              |
|  7   |         **QSQLITE**SQLite版本3或更高版本          |
|  8   |              **QSQLITE2**SQLite版本2              |

## 例

使用静态方法建立与SQLite数据库的连接-

```
db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('sports.db')
```

QSqlDatabase类的其他方法如下-

| 序号 |                      方法与说明                       |
| :--: | :---------------------------------------------------: |
| 1个  | **setDatabaseName（）**设置与之建立连接的数据库的名称 |
|  2   |     **setHostName（）**设置安装数据库的主机的名称     |
|  3   |        **setUserName（）**指定用于连接的用户名        |
|  4   |     **设置密码（）**设置连接对象的密码（如果有）      |
|  5   |      **承诺（）**提交事务，如果成功，则返回true       |
|  6   |            **rollback（）**回滚数据库事务             |
|  7   |                  **关（）**关闭连接                   |



QSqlQuery类具有执行和操纵SQL命令的功能。可以执行DDL和DML类型的SQL查询。

该类中最重要的方法是exec_（），该方法将包含要执行的SQL语句的字符串作为参数。

```python
query = QtSql.QSqlQuery()
query.exec_("create table sportsmen(id int primary key, 
   " "firstname varchar(20), lastname varchar(20))")
```



下面的脚本创建一个SQLite数据库sports.db，其中有一个填充了五个记录的Sportsperson表。

文件名:db-create.py

```python
from PyQt4 import QtSql, QtGui

def createDB():
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sports.db')
	
   if not db.open():
      QtGui.QMessageBox.critical(None, QtGui.qApp.tr("Cannot open database"),
         QtGui.qApp.tr("Unable to establish a database connection.\n"
            "This example needs SQLite support. Please read "
            "the Qt SQL driver documentation for information "
            "how to build it.\n\n" "Click Cancel to exit."),
         QtGui.QMessageBox.Cancel)
			
      return False
		
   query = QtSql.QSqlQuery()
	
   query.exec_("create table sportsmen(id int primary key, "
      "firstname varchar(20), lastname varchar(20))")
		
   query.exec_("insert into sportsmen values(101, 'Roger', 'Federer')")
   query.exec_("insert into sportsmen values(102, 'Christiano', 'Ronaldo')")
   query.exec_("insert into sportsmen values(103, 'Ussain', 'Bolt')")
   query.exec_("insert into sportsmen values(104, 'Sachin', 'Tendulkar')")
   query.exec_("insert into sportsmen values(105, 'Saina', 'Nehwal')")
   return True
	
if __name__ == '__main__':
   import sys
	
   app = QtGui.QApplication(sys.argv)
   createDB()
```

PyQt中的QSqlTableModel类是一个高级接口，提供可编辑的数据模型以在单个表中读取和写入记录。该模型用于填充QTableView对象。它向用户提供了可滚动和可编辑的视图，可以将其放在任何顶级窗口中。

QTableModel对象以以下方式声明-

```python
model = QtSql.QSqlTableModel()
```

可以将其编辑策略设置为以下任意一种：

| QSqlTableModel.OnFieldChange  | 所有更改将立即应用                                         |
| ----------------------------- | ---------------------------------------------------------- |
| QSqlTableModel.OnRowChange    | 当用户选择其他行时，将应用更改                             |
| QSqlTableModel.OnManualSubmit | 所有更改将被缓存，直到调用SubmitAll（）或revertAll（）为止 |

## 例

在以下示例中，运动员表被用作模型，策略被设置为

```python
model.setTable('sportsmen') 
model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
model.select()
```

QTableView类是PyQt中Model / View框架的一部分。QTableView对象创建如下-

```python
view = QtGui.QTableView()
view.setModel(model)
view.setWindowTitle(title)
return view
```

这个QTableView对象和两个QPushButton小部件被添加到顶级QDialog窗口中。添加按钮的clicked（）信号连接到addrow（），后者在模型表上执行insertRow（）。

```python
button.clicked.connect(addrow)
def addrow():
   print model.rowCount()
   ret = model.insertRows(model.rowCount(), 1)
   print(ret)
```

与删除按钮关联的Slot执行lambda函数，该函数删除用户选择的行。

```python
btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
```

完整的代码如下:

文件名：db.py

```python
import sys
from PyQt4 import QtCore, QtGui, QtSql
import sportsconnection

def initializeModel(model):
   model.setTable('sportsmen')
   model.setEditStrategy(QtSql.QSqlTableModel.OnFieldChange)
   model.select()
   model.setHeaderData(0, QtCore.Qt.Horizontal, "ID")
   model.setHeaderData(1, QtCore.Qt.Horizontal, "First name")
   model.setHeaderData(2, QtCore.Qt.Horizontal, "Last name")
	
def createView(title, model):
   view = QtGui.QTableView()
   view.setModel(model)
   view.setWindowTitle(title)
   return view
	
def addrow():
   print model.rowCount()
   ret = model.insertRows(model.rowCount(), 1)
   print(ret)
	
def findrow(i):
   delrow = i.row()
	
if __name__ == '__main__':
   app = QtGui.QApplication(sys.argv)
   db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
   db.setDatabaseName('sports.db')
   model = QtSql.QSqlTableModel()
   delrow = -1
   initializeModel(model)
	
   view1 = createView("Table Model (View 1)", model)
   view1.clicked.connect(findrow)
	
   dlg = QtGui.QDialog()
   layout = QtGui.QVBoxLayout()
   layout.addWidget(view1)
	
   button = QtGui.QPushButton("Add a row")
   button.clicked.connect(addrow)
   layout.addWidget(button)
	
   btn1 = QtGui.QPushButton("del a row")
   btn1.clicked.connect(lambda: model.removeRow(view1.currentIndex().row()))
   layout.addWidget(btn1)
	
   dlg.setLayout(layout)
   dlg.setWindowTitle("Database Demo")
   dlg.show()
   sys.exit(app.exec_())
```

康康

```
python3 /share/lesson/pyqt5/db-create.py
python3 /share/lesson/pyqt5/db.py
```


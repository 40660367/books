# Tornado 第一章：引言

在过去的五年里，Web开发人员的可用工具实现了跨越式地增长。当技术专家不断推动极限，使Web应用无处不在时，我们也不得不升级我们的工具、创建框架以保证构建更好的应用。我们希望能够使用新的工具，方便我们写出更加整洁、可维护的代码，使部署到世界各地的用户时拥有高效的可扩展性。

这就让我们谈论到Tornado，一个编写易创建、扩展和部署的强力Web应用的梦幻选择。我们三个都因为Tornado的速度、简单和可扩展性而深深地爱上了它，在一些个人项目中尝试之后，我们将其运用到日常工作中。我们已经看到，Tornado在很多大型或小型的项目中提升了开发者的速度（和乐趣！），同时，其鲁棒性和轻量级也给开发者一次又一次留下了深刻的印象。

本书的目的是对Tornado Web服务器进行一个概述，通过框架基础、一些示例应用和真实世界使用的最佳实践来引导读者。我们将使用示例来详细讲解Tornado如何工作，你可以用它做什么，以及在构建自己第一个应用时要避免什么。

在本书中，我们假定你对Python已经有了粗略的了解，知道Web服务如何运作，对数据库有一定的熟悉。有一些不错的书籍可以为你深入了解这些提供参考（比如Learning Python，Restful Web Service和MongoDB: The Definitive Guide）。

你可以在[Github](https://github.com/Introduction-to-Tornado)上获得本书中示例的代码。如果你有关于这些示例或其他方面的任何思想，欢迎在那里告诉我们。

所以，事不宜迟，让我们开始深入了解吧！

## 简单的Web服务

既然我们已经知道了Tornado是什么了，现在让我们看看它能做什么吧。我们首先从使用Tornado编写一个简单的Web应用开始。

### 1.2.1 Hello Tornado

Tornado是一个编写对HTTP请求响应的框架。作为程序员，你的工作是编写响应特定条件HTTP请求的响应的handler。下面是一个全功能的Tornado应用的基础示例：

文件名:hello.py

```python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

编写一个Tornado应用中最多的工作是定义类继承Tornado的RequestHandler类。在这个例子中，我们创建了一个简单的应用，在给定的端口监听请求，并在根目录（"/"）响应请求。

你可以在命令行里尝试运行这个程序以测试输出：

```bash
python /share/lesson/tornado/hello.py &
```

现在你可以在浏览器中打开`{host0.http_url}`，`{host0.http_url}?greeting=Salutations`,或者打开另一个终端窗口使用curl测试我们的应用：

```bash
curl {host0.http_url} && curl {host0.http_url}?greeting=Salutations
```

**注意：**

该样例学习完成后,输入`fg`命令，把在后台运行的torando web服务提到前台，然后按<kbd>Ctrl</kbd>+<kbd>c</kbd>结束 ，以免阻塞后面示例的学习

```bash
fg
```



### 分步解析

让我们把这个例子分成小块，逐步分析它们：

```python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
```

在程序的最顶部，我们导入了一些Tornado模块。虽然Tornado还有另外一些有用的模块，但在这个例子中我们必须至少包含这四个模块。

```python
from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)
```

Tornado包括了一个有用的模块（tornado.options）来从命令行中读取设置。我们在这里使用这个模块指定我们的应用监听HTTP请求的端口。它的工作流程如下：如果一个与define语句中同名的设置在命令行中被给出，那么它将成为全局options的一个属性。如果用户运行程序时使用了`--help`选项，程序将打印出所有你定义的选项以及你在define函数的help参数中指定的文本。如果用户没有为这个选项指定值，则使用default的值进行代替。Tornado使用type参数进行基本的参数类型验证，当不合适的类型被给出时抛出一个异常。因此，我们允许一个整数的port参数作为options.port来访问程序。如果用户没有指定值，则默认为80。

```python
class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')
```

这是Tornado的请求处理函数类。当处理一个请求时，Tornado将这个类实例化，并调用与HTTP请求方法所对应的方法。在这个例子中，我们只定义了一个get方法，也就是说这个处理函数将对HTTP的GET请求作出响应。我们稍后将看到实现不止一个HTTP方法的处理函数。

```python
greeting = self.get_argument('greeting', 'Hello')
```

Tornado的RequestHandler类有一系列有用的内建方法，包括get_argument，我们在这里从一个查询字符串中取得参数greeting的值。（如果这个参数没有出现在查询字符串中，Tornado将使用get_argument的第二个参数作为默认值。）

```python
self.write(greeting + ', friendly user!')
```

RequestHandler的另一个有用的方法是write，它以一个字符串作为函数的参数，并将其写入到HTTP响应中。在这里，我们使用请求中greeting参数提供的值插入到greeting中，并写回到响应中。

```python
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
```

这是真正使得Tornado运转起来的语句。首先，我们使用Tornado的options模块来解析命令行。然后我们创建了一个Tornado的Application类的实例。传递给Application类**init**方法的最重要的参数是handlers。它告诉Tornado应该用哪个类来响应请求。马上我们讲解更多相关知识。

```python
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(options.port)
tornado.ioloop.IOLoop.instance().start()
```

从这里开始的代码将会被反复使用：一旦Application对象被创建，我们可以将其传递给Tornado的HTTPServer对象，然后使用我们在命令行指定的端口进行监听（通过options对象取出。）最后，在程序准备好接收HTTP请求后，我们创建一个Tornado的IOLoop的实例。

#### 1.2.1.1 参数handlers

让我们再看一眼hello.py示例中的这一行：

```python
app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
```

这里的参数handlers非常重要，值得我们更加深入的研究。它应该是一个元组组成的列表，其中每个元组的第一个元素是一个用于匹配的正则表达式，第二个元素是一个RequestHanlder类。在hello.py中，我们只指定了一个正则表达式-RequestHanlder对，但你可以按你的需要指定任意多个。

#### 1.2.1.2 使用正则表达式指定路径

Tornado在元组中使用正则表达式来匹配HTTP请求的路径。（这个路径是URL中主机名后面的部分，不包括查询字符串和碎片。）Tornado把这些正则表达式看作已经包含了行开始和结束锚点（即，字符串"/"被看作为"^/$"）。

如果一个正则表达式包含一个捕获分组（即，正则表达式中的部分被括号括起来），匹配的内容将作为相应HTTP请求的参数传到RequestHandler对象中。我们将在下个例子中看到它的用法。

### 1.2.2 字符串服务

例1-2是一个我们目前为止看到的更复杂的例子，它将介绍更多Tornado的基本概念。

文件名:string_service.py

```python
import textwrap

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])

class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/reverse/(\w+)", ReverseHandler),
            (r"/wrap", WrapHandler)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

如同运行第一个例子，你可以在命令行中运行这个例子使用如下的命令：

```bash
python /share/lesson/tornado/string_service.py &
```

这个程序是一个通用的字符串操作的Web服务端基本框架。到目前为止，你可以用它做两件事情。其一，到`/reverse/string`的GET请求将会返回URL路径中指定字符串的反转形式。

访问：`{host0.http_url}reverse/stressed`，和`{host0.http_url}reverse/slipup`，比较区别。



其二，到`/wrap`的POST请求将从参数text中取得指定的文本，并返回按照参数width指定宽度装饰的文本。下面的请求指定一个没有宽度的字符串，所以它的输出宽度被指定为程序中的get_argument的默认值40个字符。

```bash
curl {host0.http_ur}wrap -d text=Lorem+ipsum+dolor+sit+amet,+consectetuer+adipiscing+elit.
```

字符串服务示例和上一节示例代码中大部分是一样的。让我们关注那些新的代码。首先，让我们看看传递给Application构造函数的handlers参数的值：

```python
app = tornado.web.Application(handlers=[
    (r"/reverse/(\w+)", ReverseHandler),
    (r"/wrap", WrapHandler)
])
```

在上面的代码中，Application类在"handlers"参数中实例化了两个RequestHandler类对象。第一个引导Tornado传递路径匹配下面的正则表达式的请求：

```python
/reverse/(\w+)
```

正则表达式告诉Tornado匹配任何以字符串/reverse/开始并紧跟着一个或多个字母的路径。括号的含义是让Tornado保存匹配括号里面表达式的字符串，并将其作为请求方法的一个参数传递给RequestHandler类。让我们检查ReverseHandler的定义来看看它是如何工作的：

```python
class ReverseHandler(tornado.web.RequestHandler):
    def get(self, input):
        self.write(input[::-1])
```

你可以看到这里的get方法有一个额外的参数input。这个参数将包含匹配处理函数正则表达式第一个括号里的字符串。（如果正则表达式中有一系列额外的括号，匹配的字符串将被按照在正则表达式中出现的顺序作为额外的参数传递进来。）

现在，让我们看一下WrapHandler的定义：

```python
class WrapHandler(tornado.web.RequestHandler):
    def post(self):
        text = self.get_argument('text')
        width = self.get_argument('width', 40)
        self.write(textwrap.fill(text, int(width)))
```

WrapHandler类处理匹配路径为`/wrap`的请求。这个处理函数定义了一个post方法，也就是说它接收HTTP的POST方法的请求。

我们之前使用RequestHandler对象的get_argument方法来捕获请求查询字符串的的参数。同样，我们也可以使用相同的方法来获得POST请求传递的参数。（Tornado可以解析URLencoded和multipart结构的POST请求）。一旦我们从POST中获得了文本和宽度的参数，我们使用Python内建的textwrap模块来以指定的宽度装饰文本，并将结果字符串写回到HTTP响应中。

### 1.2.3 关于RequestHandler的更多知识

到目前为止，我们已经了解了RequestHandler对象的基础：如何从一个传入的HTTP请求中获得信息（使用get_argument和传入到get和post的参数）以及写HTTP响应（使用write方法）。除此之外，还有很多需要学习的，我们将在接下来的章节中进行讲解。同时，还有一些关于RequestHandler和Tornado如何使用它的只是需要记住。

#### 1.2.3.1 HTTP方法

截止到目前讨论的例子，每个RequestHandler类都只定义了一个HTTP方法的行为。但是，在同一个处理函数中定义多个方法是可能的，并且是有用的。把概念相关的功能绑定到同一个类是一个很好的方法。比如，你可能会编写一个处理函数来处理数据库中某个特定ID的对象，既使用GET方法，也使用POST方法。想象GET方法来返回这个部件的信息，而POST方法在数据库中对这个ID的部件进行改变：

```python
# matched with (r"/widget/(\d+)", WidgetHandler)
class WidgetHandler(tornado.web.RequestHandler):
    def get(self, widget_id):
        widget = retrieve_from_db(widget_id)
        self.write(widget.serialize())

    def post(self, widget_id):
        widget = retrieve_from_db(widget_id)
        widget['foo'] = self.get_argument('foo')
        save_to_db(widget)
```

我们到目前为止只是用了GET和POST方法，但Tornado支持任何合法的HTTP请求（GET、POST、PUT、DELETE、HEAD、OPTIONS）。你可以非常容易地定义上述任一种方法的行为，只需要在RequestHandler类中使用同名的方法。下面是另一个想象的例子，在这个例子中针对特定frob ID的HEAD请求只根据frob是否存在给出信息，而GET方法返回整个对象：

```python
# matched with (r"/frob/(\d+)", FrobHandler)
class FrobHandler(tornado.web.RequestHandler):
    def head(self, frob_id):
        frob = retrieve_from_db(frob_id)
        if frob is not None:
            self.set_status(200)
        else:
            self.set_status(404)
    def get(self, frob_id):
        frob = retrieve_from_db(frob_id)
        self.write(frob.serialize())
```

#### 1.2.3.2 HTTP状态码

从上面的代码可以看出，你可以使用RequestHandler类的ser_status()方法显式地设置HTTP状态码。然而，你需要记住在某些情况下，Tornado会自动地设置HTTP状态码。下面是一个常用情况的纲要：

##### 404 Not Found

Tornado会在HTTP请求的路径无法匹配任何RequestHandler类相对应的模式时返回404（Not Found）响应码。

##### 400 Bad Request

如果你调用了一个没有默认值的get_argument函数，并且没有发现给定名称的参数，Tornado将自动返回一个400（Bad Request）响应码。

##### 405 Method Not Allowed

如果传入的请求使用了RequestHandler中没有定义的HTTP方法（比如，一个POST请求，但是处理函数中只有定义了get方法），Tornado将返回一个405（Methos Not Allowed）响应码。

##### 500 Internal Server Error

当程序遇到任何不能让其退出的错误时，Tornado将返回500（Internal Server Error）响应码。你代码中任何没有捕获的异常也会导致500响应码。

##### 200 OK

如果响应成功，并且没有其他返回码被设置，Tornado将默认返回一个200（OK）响应码。

当上述任何一种错误发生时，Tornado将默认向客户端发送一个包含状态码和错误信息的简短片段。如果你想使用自己的方法代替默认的错误响应，你可以重写write_error方法在你的RequestHandler类中。比如，代码清单1-3是hello.py示例添加了常规的错误消息的版本。

文件名:hello-errors.py

```python
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=80, help="run on the given port", type=int)

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        greeting = self.get_argument('greeting', 'Hello')
        self.write(greeting + ', friendly user!')
    def write_error(self, status_code, **kwargs):
        self.write("Gosh darnit, user! You caused a %d error." % status_code)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
```

```bash
python /share/lesson/tornado/hello-errors.py &
```

当我们尝试一个POST请求时，会得到下面的响应。一般来说，我们应该得到Tornado默认的错误响应，但因为我们覆写了write_error，我们会得到不一样的东西：

```bash
curl -d foo=bar {host0.http_url}
```

### 1.2.4 下一步

现在你已经明白了最基本的东西，我们渴望你想了解更多。在接下来的章节，我们将向你展示能够帮助你使用Tornado创建成熟的Web服务和应用的功能和技术。首先是：Tornado的模板系统。
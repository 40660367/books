# Tornado 简介

![img](./images/logo.png)

[Tornado](http://www.tornadoweb.org/) 是一个基于Python的Web服务框架和 异步网络库, 最早开发与 [FriendFeed](http://friendfeed.com/) 公司. 通过利用非阻塞网络 I/O, Tornado 可以承载成千上万的活动连接, 完美的实现了 [长连接](http://en.wikipedia.org/wiki/Push_technology#Long_polling), [WebSockets](http://en.wikipedia.org/wiki/WebSocket), 和其他对于每一位用户来说需要长连接的程序.

Tornado 可以被分为以下四个主要部分:

- Web 框架 (包括用来创建 Web 应用程序的 [`RequestHandler`](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/web.html#tornado.web.RequestHandler) 类, 还有很多其它支持的类).
- HTTP 客户端和服务器的实现 ([`HTTPServer`](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/httpserver.html#tornado.httpserver.HTTPServer) 和 [`AsyncHTTPClient`](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/httpclient.html#tornado.httpclient.AsyncHTTPClient)).
- 异步网络库 ([`IOLoop`](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/ioloop.html#tornado.ioloop.IOLoop) 和 [`IOStream`](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/iostream.html#tornado.iostream.IOStream)), 对 HTTP 的实现提供构建模块, 还可以用来实现其他协议.
- 协程库 ([`tornado.gen`](https://tornado-zh-cn.readthedocs.io/zh_CN/latest/gen.html#module-tornado.gen)) 让用户通过更直接的方法来实现异步编程, 而不是通过回调的方式.

Tornado是 FriendFeed 使用的可扩展的非阻塞式 web 服务器及其相关工具的开源版本。这个 Web 框架看起来有些像 web.py 或者 Google 的 webapp，不过为了能有效利用非阻塞式服务器环境，这个 Web 框架还包含了一些相关的有用工具和优化。

Tornado 和现在的主流 Web 服务器框架（包括大多数 Python 的框架）有着明显的区别：它是非阻塞式服务器，而且速度相当快。得利于其非阻塞的方式和对 epoll 的运用，Tornado 每秒可以处理数以千计的连接，这意味着对于实时 Web 服务来说，Tornado 是一个理想的 Web 框架。

> 我们开发这个 Web 服务器的主要目的就是为了处理 FriendFeed 的实时功能 ——在 FriendFeed 的应用里每一个活动用户都会保持着一个服务器连接。

#### 模块

Tornado 是个轻量级框架，它的模块不多，最重要的一个模块是[web](http://github.com/facebook/tornado/blob/master/tornado/web.py)， 它就是包含了 Tornado 的大部分主要功能的 Web 框架。其它的模块都是工具性质的， 以便让 web 模块更加有用 后面的 Tornado 攻略 详细讲解了 web 模块的使用方法。

#### 主要模块

- [web](http://github.com/facebook/tornado/blob/master/tornado/web.py) - FriendFeed 使用的基础 Web 框架，包含了 Tornado 的大多数重要的功能
- [escape](http://github.com/facebook/tornado/blob/master/tornado/escape.py) - XHTML, JSON, URL 的编码/解码方法
- [database](http://github.com/facebook/tornado/blob/master/tornado/database.py) - 对 MySQLdb 的简单封装，使其更容易使用
- [template](http://github.com/facebook/tornado/blob/master/tornado/template.py) - 基于 Python 的 web 模板系统
- [httpclient](http://github.com/facebook/tornado/blob/master/tornado/httpclient.py) - 非阻塞式 HTTP 客户端，它被设计用来和 web 及 httpserver 协同工作
- [auth](http://github.com/facebook/tornado/blob/master/tornado/auth.py) - 第三方认证的实现（包括 Google OpenID/OAuth、Facebook Platform、Yahoo BBAuth、FriendFeed OpenID/OAuth、Twitter OAuth）
- [locale](http://github.com/facebook/tornado/blob/master/tornado/locale.py) - 针对本地化和翻译的支持
- [options](http://github.com/facebook/tornado/blob/master/tornado/options.py) - 命令行和配置文件解析工具，针对服务器环境做了优化

#### 底层模块

- [httpserver](http://github.com/facebook/tornado/blob/master/tornado/httpserver.py) - 服务于 web 模块的一个非常简单的 HTTP 服务器的实现
- [iostream](http://github.com/facebook/tornado/blob/master/tornado/iostream.py) - 对非阻塞式的 socket 的简单封装，以方便常用读写操作
- [ioloop](http://github.com/facebook/tornado/blob/master/tornado/ioloop.py) - 核心的 I/O 循环
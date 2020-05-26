# node.js HelloWorld!

如果我们使用PHP来编写后端的代码时，需要Apache或者Nginx的HTTP服务器，并配上mod_php5模块和php-cgi。

从这个角度看，整个"接收HTTP请求并提供Web页面"的需求根本不需要PHP来处理。

不过对Node.js来说，概念完全不一样了。使用Node.js时，我们不仅仅在实现一个应用，同时还实现了整个HTTP服务器。事实上，我们的Web应用以及对应的Web服务器基本上是一样的。

在我们创建Node.js第一个"Hello, World!"应用前，让我们先了解下Node.js应用是由哪几部分组成的：

1. **引入required模块：**我们可以使用**require**指令来载入Node.js模块。
2. **创建服务器：**服务器可以监听客户端的请求，类似于Apache 、Nginx等HTTP服务器。
3. **接收请求与响应请求**：服务器很容易创建，客户端可以使用浏览器或终端发送HTTP请求，服务器接收请求后返回响应数据。

## 创建 Node.js 应用

### 引入required模块

我们使用**require**指令来载入http模块，并将实例化的HTTP赋值给变量http

```js
var http = require("http");
```

### 创建服务器

接下来我们使用http.createServer()方法创建服务器，并使用listen方法绑定8888端口。 函数通过request, response参数来接收和响应数据。

文件名:simpleserver.js

```js
var http = require('http');

http.createServer(function (request, response) {
	// 发送 HTTP 头部 
	// HTTP 状态值: 200 : OK
	// 内容类型: text/plain
	response.writeHead(200, {'Content-Type': 'text/plain'});
	// 发送响应数据 "Hello World"
	response.end('Hello World\nThis is From Node.js Server');
}).listen(80);

// 终端打印如下信息
console.log('Server running at port 80!');
```
以上代码我们完成了一个可以工作的HTTP服务器。

**分析Node.js的HTTP服务器：**

- 第一行请求（require）Node.js自带的 http 模块，并且把它赋值给http变量。
- 接下来我们调用http模块提供的函数：createServer 。这个函数会返回 一个对象，这个对象有一个叫做listen的方法，这个方法有一个数值参数，指定这个HTTP服务器监听的端口号。

### 使用node执行以上的代码就可以访问了：

```shell
node /share/lesson/node.js/simpleserver.js
```
接下来点击右侧实验区伪终端的加号，再点击`{host0.http_url}`访问，这个地址就可以看到我们刚刚运行的node.js服务。

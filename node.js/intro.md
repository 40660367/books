# Node.js 简介

![nodejs](./images/nodejs.jpg)

Node.js 是运行在服务端的 JavaScript。等于运行环境+ JavaScript库

Node.js 是一个基于Chrome JavaScript 运行时建立的一个平台。

Node.js是一个事件驱动I/O服务端JavaScript环境，基于Google的V8引擎，V8引擎执行Javascript的速度非常快，性能非常好。

Node.js在[官方网站](https://nodejs.org/)的定义文件内容如下：

> Node.js® is a platform built on [Chrome's JavaScript runtime](http://code.google.com/p/v8/) for easily building fast, scalable network applications. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time applications that run across distributed devices.

Node.js自带运行时环境可在Javascript脚本的基础上可以解释和执行(这类似于JVM的Java字节码)。这个运行时允许在浏览器以外的任何机器上执行JavaScript代码。由于这种运行时在Node.js上，所以JavaScript现在可以在服务器上并执行。

Node.js还提供了各种丰富的JavaScript模块库，它极大简化了使用Node.js来扩展Web应用程序的研究与开发。

## 	Node.js特性

- Node.js库的异步和事件驱动的API全部都是异步就是非阻塞。它主要是指基于Node.js的服务器不会等待API返回的数据。服务器移动到下一个API调用，Node.js发生的事件通知机制后有助于服务器获得从之前的API调用的响应。
- 非常快的内置谷歌Chrome的V8 JavaScript引擎，Node.js库代码执行是非常快的。
- 单线程但高度可扩展 - Node.js使用具有循环事件单线程模型。事件机制有助于服务器在一个非阻塞的方式响应并使得服务器高度可扩展，而不是创建线程限制来处理请求的传统服务器。Node.js使用单线程的程序，但可以提供比传统的服务器(比如Apache HTTP服务器)的请求服务数量要大得多。
- 没有缓冲 - Node.js的应用从来不使用缓冲任何数据。这些应用只是输出数据在块中。
- 许可证协议 - Node.js 在 [MIT 协议](https://raw.githubusercontent.com/joyent/node/v0.12.0/LICENSE) 下发布

## 	都有谁在使用Node.js?

​	以下是包含正在使用node.js的项目，应用和公司，一个详尽的清单请点击 github维基链接查看，这些清单里包括：eBay, General Electric, GoDaddy, Microsoft, PayPal, Uber, Wikipins, Yahoo!, Yammer 并越来越多加入继续扩大这个列表：[使用NodeJS的项目, 应用和公司](https://github.com/joyent/node/wiki/projects,-applications,-and-companies-using-node)

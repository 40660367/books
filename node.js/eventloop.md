# node.js 事件循环(event loop)	

node.js单线程应用程序，但它通过事件和回调概念，支持并发。 由于node.js每一个API是异步的，作为一个单独的线程，它使用异步函数调用，以保持并发性。node.js使用观察者模式。node线程保持一个事件循环，每当任何任务得到完成，它触发这标志着该事件侦听器函数执行相应的事件。

## 事件驱动编程

node.js大量使用事件，这也是为何node.js是相当快相对于其他类似的技术。当node.js启动其服务器，它可以简单地启动它的变量，声明的函数，然后简单地等待发生的事件。

![img](./images/event_loop.jpg)

在事件驱动的应用中，通常主循环监听事件，然后触发回调函数时被检测到这些事件之一。

尽管事件似乎类似于回调。不同之处在于如下事实，当异步函数返回其结果的回调函数被调用的地方作为对观察者模式的事件处理。 监听事件的功能作为观察员。每当一个事件被触发，它的监听函数就开始执行。node.js具有多个内置通过事件模块和用于将事件绑定和事件侦听，如下EventEmitter类可用事件：

```js
// Import events module
var events = require('events');
// Create an eventEmitter object
var eventEmitter = new events.EventEmitter();
```

以下为事件处理程序绑定使用事件的语法：

```js
// Bind event and even handler as follows
eventEmitter.on('eventName', eventHandler);
```

我们可以通过编程触发一个事件，如下所示：

```js
// Fire an event 
eventEmitter.emit('eventName');
```

## 	例子

文件名:eventloop.js

```js
// Import events module
var events = require('events');
// Create an eventEmitter object
var eventEmitter = new events.EventEmitter();

// Create an event handler as follows
var connectHandler = function connected() {
   console.log('connection succesful.');
  
   // Fire the data_received event 
   eventEmitter.emit('data_received');
}

// Bind the connection event with the handler
eventEmitter.on('connection', connectHandler);
 
// Bind the data_received event with the anonymous function
eventEmitter.on('data_received', function(){
   console.log('data received succesfully.');
});

// Fire the connection event 
eventEmitter.emit('connection');

console.log("Program Ended.");
```

康康

```bash
node /share/lesson/node.js/eventloop.js
```

## 	Node应用程序是如何工作的？

在Node应用程序，任何异步函数接受回调作为最后的参数和回调函数接受错误的第一个参数。我们再看一下前面的例子了。

### 示例

在当前目录准备实验用文本文件，文件名:input.txt

```bash
echo To go in is giving yourself learning content to teach the world in simple and easy way!!!!! > input.txt
```

文件名:nodeworks.js

```js
var fs = require("fs");

fs.readFile('input.txt', function (err, data) {
   if (err){
      console.log(err.stack);
      return;
   }
   console.log(data.toString());
});
console.log("Program Ended");
```

康康

```bash
node /share/lesson/node.js/nodeworks.js
```

这里fs.readFile()是一个异步函数，其目的是要读取文件。如果在文件的读出发生了错误，则er对象将包含相应的错误，否则数据将包含该文件的内容。readFile传递err和数据，回调函数后，文件读取操作完成，并最终打印的内容。
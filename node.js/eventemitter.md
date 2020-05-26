# node.js 事件发射器(evente mitter)

在Node很多对象发出事件，例如net.Server每个同级连接到它，一个fs.readStream发出打开文件事件时，每次都发出一个事件。 它发出事件的所有对象都是events.EventEmitter的实例。

## 	例子

文件名:eventemitter.js

```js
var events = require('events');
var eventEmitter = new events.EventEmitter();

// listener #1
var listner1 = function listner1() {
   console.log('listner1 executed.');
}

// listener #2
var listner2 = function listner2() {
  console.log('listner2 executed.');
}

// Bind the connection event with the listner1 function
eventEmitter.addListener('connection', listner1);

// Bind the connection event with the listner2 function
eventEmitter.on('connection', listner2);

var eventListeners = require('events').EventEmitter.listenerCount(eventEmitter,'connection');
console.log(eventListeners + " Listner(s) listening to connection event");

// Fire the connection event 
eventEmitter.emit('connection');

// Remove the binding of listner1 function
eventEmitter.removeListener('connection', listner1);
console.log("Listner1 will not listen now.");

// Fire the connection event 
eventEmitter.emit('connection');

eventListeners = require('events').EventEmitter.listenerCount(eventEmitter,'connection');
console.log(eventListeners + " Listner(s) listening to connection event");

console.log("Program Ended.");
```

康康

```
node /share/lesson/node.js/eventemitter.js
```

## EventEmitter 类

正如我们已经看到在上一节，EventEmitter类在于事件的模块。它是通过通俗易懂的语法如下：

```js
// Import events module
var events = require('events');
// Create an eventEmitter object
var eventEmitter = new events.EventEmitter();
```

EventEmitter实例对任何错误，它会发出一个“error”事件。当新的侦听器被添加，“newListener'事件被触发，当一个侦听器被删除，'removeListener”事件被触发。

EventEmitter提供多种性能如在发射。On属性用于绑定事件函数，发射用于触发一个事件。

## 	方法

| S.N. | 方法 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | **addListener(event, listener)**  			添加一个监听器监听器数组指定事件的结束。没有进行检查，以查看是否侦听器已经添加。多次调用传递事件和监听器的相同组合，将导致在侦听器被添加多次。返回发射器，所以调用可以链接。 |
| 2    | **on(event, listener)**  			添加一个监听器监听器数组在未尾指定事件. 没有进行检查，以查看是否侦听器已经添加。多次调用传递事件和监听器的相同组合，将导致在侦听器被添加多次。返回发射器，所以调用可以链接。 |
| 3    | **once(event, listener)**  			增加一次监听事件。 监听器调用仅在下一次事件被触发，之后被删除。返回发射器，所以调用可以链接。 |
| 4    | **removeListener(event, listener)**  			从侦听器数组指定事件删除监听器。注意：改变数组索引侦听器后面监听器数组中。removeListener将从监听数组中删除至多侦听器一个实例。如果任何一个监听器已经被多次添加到侦听数组指定事件，然后removeListener必须多次删除每个实例。返回发射器，所以调用可以链接。 |
| 5    | **removeAllListeners([event])**  			删除所有监听器，或者那些指定的事件。这不是一个好主意，删除在其他地方添加代码，特别是当它在还没有创建（如套接字或文件流）发射器监听器。 返回发射器，所以调用可以链接。 |
| 6    | **setMaxListeners(n)**  			默认情况下EventEmitters将打印一个警告，如果超过10个监听器添加特定事件。这是一个有用的默认这有助于发现内存泄漏。显然，并非所有的发射器应限制在10个，此功能允许增加。设置为零无限制。 |
| 7    | **listeners(event)**  			返回监听器为指定事件的数组。 |
| 8    | **emit(event, [arg1], [arg2], [...])**  			为了与提供的参数执行每一个监听器。如果事件有监听器返回true，否则为false。 |

## 	类方法

| S.N. | 方法 & 描述                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | **listenerCount(emitter, event)**  返回对于一个给定的事件监听器的数量。 |

## 	事件

| S.No. | 事件 & 描述                                                  |
| ----- | ------------------------------------------------------------ |
| 1     | **newListener**  		event - 事件字符串名称 		listener - 函数的事件处理函数 		此事件发出的侦听器在任何时间添加。当该事件被触发，监听器可能还没有被添加到监听的数组，用于该事件。 |
| 2     | **removeListener**  	event - 字符串事件名称 				 				 					 						listener - 函数的事件处理函数 	此事件发出任何时当要删除一个侦听器。当该事件被触发，监听器可能还没有被从监听的阵列删除，而用于在事件中删除。 |

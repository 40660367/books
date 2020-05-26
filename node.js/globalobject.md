# Node.js全局对象 			

Node.js的全局对象是具有全局性的，它们可在所有的模块中应用。我们并不需要包括这些对象在应用中，而可以直接使用它们。这些对象的模块，函数，字符串和对象本身，如下所述。

## 	__filename

__filename 表示正在执行的代码的文件名。这是此代码文件的解析绝对路径。 为一个主程序这不一定是在命令行中使用相同的文件名。 模块内的路径模块文件的值。

### 示例

文件名:global1.js

```javascript
// Let's try to print the value of __filename

console.log( __filename );
```

康康

```bash
node /share/lesson/node.js/global1.js
```

## 	__dirname

__dirname表示当前正在执行的脚本所在目录的名称。

### 	示例

文件名:global2.js

```javascript
// Let's try to print the value of __dirname

console.log( __dirname );
```

康康

```bash
node /share/lesson/node.js/global2.js
```

## 	setTimeout(cb, ms)

setTimeout(cb, ms) 全局函数用于至少毫秒毫秒后运行回调cb。实际延迟取决于外部因素，如OS计时器粒度和系统负载。计时器不能跨越超过24.8天。

该函数返回一个表示可用于清除定时器，定时器的不透明值。

### 	示例

文件名:global3.js

```javascript
function printHello(){
   console.log( "Hello, World!");
}
// Now call above function after 2 seconds
setTimeout(printHello, 2000);
```

康康

```bash
node /share/lesson/node.js/global3.js
```

## 	clearTimeout(t)

clearTimeout（t）的全局函数用来停止以前用的setTimeout()创建一个定时器。这里t是由setTimeout()函数返回的计时器。

### 	示例

文件名:global4.js

```javascript
function printHello(){
   console.log( "Hello, World!");
}
// Now call above function after 2 seconds
var t = setTimeout(printHello, 2000);

// Now clear the timer
clearTimeout(t);
```

康康

```
node /share/lesson/node.js/global4.js
```

## 	setInterval(cb, ms)

setInterval(cb, ms) 全局函数是用来至少毫秒后重复运行回调cb。实际延迟取决于外部因素，如OS计时器粒度和系统负载。计时器不能跨越超过24.8天。

函数返回一个表示可用于清除定时器使用功能的计时器的不透明值 clearInterval(t).

### 	示例

文件名:global5.js

```javascript
function printHello(){
   console.log( "Hello, World!");
}
// Now call above function after 2 seconds
setInterval(printHello, 2000);
```

现在运行main.js看到的结果：

```
node /share/lesson/node.js/global5.js
```

上述程序将每2秒之后执行函数printHello()。由于系统的限制，此方案不能执行选项，所以可以在本地检查你的机器。

## 	全局对象

下表列出了一些我们经常使用在我们的应用中另一个对象的细节。对于进一步的细节，可以参考官方文档。

| S.N. | 模块名称 & 描述                                              |
| ---- | ------------------------------------------------------------ |
| 1    | **Console**用于打印输出和错误信息                            |
| 2    | **Process**用于获取当前进程的信息。提供处理活动有关的多个事件 |
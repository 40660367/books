# Node.js 流(Stream)

## 什么是流Stream?

流是可以从一个源读取或写入数据到连续的目标对象。在Node.js，有四种类型的数据流。

- **Readable** - 其是用于读操作。
- **Writable** - 用在写操作。
- **Duplex** - 其可以用于读取和写入操作。
- **Transform** - 输出基于输入的地方进行计算的一种双相流。

​	每种类型的流是一个EventEmitter实例，并抛出的时代不同的实例几个事件。例如，一些常用的事件是：

- **data** - 当有数据可读取此事件。
- **end** - 当没有更多的数据读取此事件被触发。
- **error** - 当有任何错误或接收数据写入此事件。
- **finish** - 当所有数据已刷新到底层系统触发此事件

​	本教程将让您了解关于数据流的常用操作。

## 	从流中读取

文件名:input2.txt

```
To go in is giving yourself learning content to teach the world in simple and easy way!!!!!
```

文件名:streamread.js

```js
var fs = require("fs");
var data = '';

// Create a readable stream
var readerStream = fs.createReadStream('input2.txt');

// Set the encoding to be utf8. 
readerStream.setEncoding('UTF8');

// Handle stream events --> data, end, and error
readerStream.on('data', function(chunk) {
   data += chunk;
});

readerStream.on('end',function(){
   console.log(data);
});

readerStream.on('error', function(err){
   console.log(err.stack);
});

console.log("Program Ended");
```
康康
```bash
node /share/lesson/node.js/stream.js
```

## 	写入流

文件名:streamwrite.js

```
var fs = require("fs");
var data = 'Simply Easy Learning';

// Create a writable stream
var writerStream = fs.createWriteStream('output.txt');

// Write the data to stream with encoding to be utf8
writerStream.write(data,'UTF8');

// Mark the end of file
writerStream.end();

// Handle stream events --> finish, and error
writerStream.on('finish', function() {
    console.log("Write completed.");
});

writerStream.on('error', function(err){
   console.log(err.stack);
});

console.log("Program Ended");
```

康康

```bash
node /share/lesson/node.js/stream.js
```

验证输出,现在打开在当前目录中创建output.txt文件，验证output.txt文件中有以下内容。

```
!cat output.txt
```

## 	管道流

管道是我们提供一个流的输出作为输入到另一个流的机制。它通常被用于从一个流中获取数据，并通过该流输出到另一个流。没有对管道的操作没有限制。现在，我们将展示一个管道从一个文件中读取和写入到另一个文件的例子。

创建一个js文件名为main.js里面有如下代码：

文件名:streampipe.js

```js
var fs = require("fs");

// Create a readable stream
var readerStream = fs.createReadStream('input.txt');

// Create a writable stream
var writerStream = fs.createWriteStream('output.txt');

// Pipe the read and write operations
// read input.txt and write data to output.txt
readerStream.pipe(writerStream);

console.log("Program Ended");
```

康康

```bash
node /share/lesson/node.js/streampipe.js
```

在当前目录打开所创建的output.txt文件，并验证output.txt文件中有以下内容。

```bash
!cat output.txt
```

## 	链式流

链式是一个机制，一个流的输出连接到另一个流，并创建一个链多流操作。它通常用于管道的操作。现在，我们将使用管道和链接先压缩文件，然后解压缩。

**示例**

文件名:streamgzip.js

```js
var fs = require("fs");
var zlib = require('zlib');

// Compress the file input.txt to input.txt.gz
fs.createReadStream('input.txt')
  .pipe(zlib.createGzip())
  .pipe(fs.createWriteStream('input.txt.gz'));
  
console.log("File Compressed.");
```

康康

```bash
node /share/lesson/node.js/streamgzip.js
```

你会发现，input.txt文件已经被压缩，并在当前目录下创建的文件input.txt.gz。

**示例**

现在，让我们尝试使用下面的代码进行解压缩同一个文件。

文件名:streamgzip1.js

```js
var fs = require("fs");
var zlib = require('zlib');

// Decompress the file input.txt.gz to input.txt
fs.createReadStream('input.txt.gz')
  .pipe(zlib.createGunzip())
  .pipe(fs.createWriteStream('input.txt'));
  
console.log("File Decompressed.");
```

康康

```bash
node /share/lesson/node.js/streamgzip.js
```


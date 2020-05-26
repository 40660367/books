# Node.js文件系统 			

Node实现文件I/O使用标准的POSIX函数的简单包装。Node文件系统(FS)模块可以使用以下语法输入：

```js
var fs = require("fs")
```

## 	同步和异步

在fs模块的每一个方法都有同步和异步形式。异步方法需要最后一个参数为完成回调函数和回调函数的第一个参数是错误的。它优选使用异步方法来代替同步方法，前者从来不阻止程序的执行，作为第二使用。



## 示例文件准备：

在当前路径下生成名为input.txt的文本文件

```bash 
echo To go in is giving yourself learning content to teach the world in simple and easy way!!!!! > input.txt
```

### 示例

文件名:fs-readfile.js

```js
var fs = require("fs");

// Asynchronous read
fs.readFile('input.txt', function (err, data) {
   if (err) {
       return console.error(err);
   }
   console.log("Asynchronous read: " + data.toString());
});

// Synchronous read
var data = fs.readFileSync('input.txt');
console.log("Synchronous read: " + data.toString());

console.log("Program Ended");
```

康康

```bash
node /share/lesson/node.js/fs-readfile.js
```

## 	打开一个文件

以下部分将提供有关主要文件I/ O方法很好的例子。

### 	语法

以下是在异步模式下打开文件的方法的语法：

```js
fs.open(path, flags[, mode], callback)
```

### 	参数

下面是使用的参数的说明：

- 		**path** - 这是文件名，包括路径字符串。
- 		**flags** - 标志告知要打开的文件的行为。所有可能的值已经提及以下。
- 		**mode** - 这将设置文件模式(许可和粘性位)，但前提是在创建该文件。它默认为0666，读取和写入。
- 		**callback** - 这是回调函数得到两个参数(err, fd)。

## 	Flags

标志进行读/写操作是：

| Flag | 描述                                                         |
| ---- | ------------------------------------------------------------ |
| r    | 打开文件进行读取。如果该文件不存在发生异常。                 |
| r+   | 打开文件进行读取和写入。如果该文件不存在发生异常。           |
| rs   | 打开文件，用于读取在同步方式。                               |
| rs+  | 打开文件进行读取和写入，告诉OS同步地打开它。对于'rs'有关使用此慎用见注解。 |
| w    | 打开文件进行写入。该文件被创建（如果它不存在）或截断（如果它存在）。 |
| wx   | 类似'w'，如果路径存在则失败。                                |
| w+   | 打开文件进行读取和写入。该文件被创建（如果它不存在）或截断（如果它存在）。 |
| wx+  | 类似“w+”，但如果路径存在则失败。                             |
| a    | 打开文件进行追加。如果它不存在，则创建该文件。               |
| ax   | 类似“a”，但如果路径存在则失败。                              |
| a+   | 打开文件进行读取和附加。如果它不存在，则创建该文件。         |
| ax+  | 类似'a+'，但如果路径存在则失败。                             |

### 	示例

文件名fs-open.js

```js
var fs = require("fs");

// Asynchronous - Opening File
console.log("Going to open file!");
fs.open('input.txt', 'r+', function(err, fd) {
   if (err) {
       return console.error(err);
   }
  console.log("File opened successfully!");     
});
```

康康

```bash
node /share/lesson/node.js/fs-open.js
```

## 	获取文件信息

### 	语法

下面是获取一个文件有关的信息的方法的语法：

```js
fs.stat(path, callback)
```

### 	语法

下面是使用的参数的说明：

- 		**path** - 这是有文件名，包括路径字符串。
- 		**callback** - 这是回调函数得到两个参数(err, stats) ，其中统计数据是这是印在下面的例子中的fs.Stats类型的对象。

除了这些在下面的例子中打印的重要属性， 还有可以用于检查文件类型的fs.Stats类可用的有用的方法。这些方法列于下表中。

| 方法                      | 描述                                   |
| ------------------------- | -------------------------------------- |
| stats.isFile()            | 返回true，如果文件类型是一个简单的文件 |
| stats.isDirectory()       | 返回true，如果文件类型是目录           |
| stats.isBlockDevice()     | 返回true，如果文件类型是块设备         |
| stats.isCharacterDevice() | 返回true，如果文件类型是字符设备       |
| stats.isSymbolicLink()    | 返回true，如果文件类型是符号连接       |
| stats.isFIFO()            | 返回true，如果文件类型是FIFO           |
| stats.isSocket()          | 返回true，如果文件类型是套接字         |

### 	示例

文件名:file-stats.js

```
var fs = require("fs");

console.log("Going to get file info!");
fs.stat('input.txt', function (err, stats) {
   if (err) {
       return console.error(err);
   }
   console.log(stats);
   console.log("Got file info successfully!");
   
   // Check file type
   console.log("isFile ? " + stats.isFile());
   console.log("isDirectory ? " + stats.isDirectory());    
});
```

康康

```bash
node /share/lesson/node.js/file-stats.js
```

## 	写入文件

### 	语法

下面是写入到一个文件中的方法之一的语法：

```js
fs.writeFile(filename, data[, options], callback)
```

这种方法如果文件已经存在将会覆盖文件。如果想写入到现有的文件，那么你应该使用其他的方法。

### 	参数

下面是使用的参数的说明：

- 		**path** - 这是有文件名，包括路径字符串
- 		**data** - 这是字符串或缓冲将被写入到文件中
- 		**options** - 第三个参数是一个对象，它将于{编码，模式，标志}。默认编码是UTF8，模式是八进制值0666和标志 'w'
- 		**callback** - 这是回调函数获取一个参数err，并用于在发生任何写入错误返回错误。

### 	示例

文件名:file-write.js

```js
var fs = require("fs");

console.log("Going to write into existing file");
fs.writeFile('input.txt', 'Simply Easy Learning!',  function(err) {
   if (err) {
       return console.error(err);
   }
   console.log("Data written successfully!");
   console.log("Let's read newly written data");
   fs.readFile('input.txt', function (err, data) {
      if (err) {
         return console.error(err);
      }
      console.log("Asynchronous read: " + data.toString());
   });
});
```

康康

```bash
node /share/lesson/node.js/file-stats.js
```

## 	读取文件

### 	语法

以下是从文件读取的方法之一的语法：

```
fs.read(fd, buffer, offset, length, position, callback)
```

此方法将使用文件描述符来读取文件，如果你想直接使用文件名，那么应该使用其他可用的方法来读取文件。

### 	参数

下面是使用的参数的说明：

- 		**fd** - 这是通过文件fs.open()方法返回的文件描述符
- 		**buffer** - 这是该数据将被写入到缓冲器
- 		**offset** - 这是偏移量在缓冲器开始写入处
- 		**length** - 这是一个整数，指定要读取的字节的数目
- 		**position** - 这是一个整数，指定从文件中开始读取。如果位置为null，数据将从当前文件位置读取。
- 		**callback** - 这是回调函数获取三个参数，(err, bytesRead, buffer).

### 	示例

文件名:file-read.js

```js
var fs = require("fs");
var buf = new Buffer(1024);

console.log("Going to open an existing file");
fs.open('input.txt', 'r+', function(err, fd) {
   if (err) {
       return console.error(err);
   }
   console.log("File opened successfully!");
   console.log("Going to read the file");
   fs.read(fd, buf, 0, buf.length, 0, function(err, bytes){
      if (err){
         console.log(err);
      }
      console.log(bytes + " bytes read");
      
      // Print only read bytes to avoid junk.
      if(bytes > 0){
         console.log(buf.slice(0, bytes).toString());
      }
   });
});
```

康康

```bash
node /share/lesson/node.js/file-read.js
```

## 	关闭文件

### 	语法

以下是关闭一个打开的文件的方法之一的语法：

```js
fs.close(fd, callback)
```

### 	参数

下面是使用的参数的说明：

- 		**fd** - 这是通过文件fs.open()方法返回的文件描述符。
- 		**callback** - 这是回调函数

### 	示例

文件名:fs-close.js

```js
var fs = require("fs");
var buf = new Buffer(1024);

console.log("Going to open an existing file");
fs.open('input.txt', 'r+', function(err, fd) {
   if (err) {
       return console.error(err);
   }
   console.log("File opened successfully!");
   console.log("Going to read the file");
   fs.read(fd, buf, 0, buf.length, 0, function(err, bytes){
      if (err){
         console.log(err);
      }

      // Print only read bytes to avoid junk.
      if(bytes > 0){
         console.log(buf.slice(0, bytes).toString());
      }

      // Close the opened file.
      fs.close(fd, function(err){
         if (err){
            console.log(err);
         } 
         console.log("File closed successfully.");
      });
   });
});
```

康康

```bash
node /share/lesson/node.js/fs-close.js
```

## 	截断文件

### 	语法

下面是要截断的打开文件的方法的语法：

```
fs.ftruncate(fd, len, callback)
```

### 	参数

下面是使用的参数的说明：

- 		fd - 这是通过文件fs.open()方法返回的文件描述符。
- 		len - 这是后的文件将被截断文件的长度。
- 		callback - 这是回调函数

### 	示例

文件名:fs-ftruncate.js

```js
var fs = require("fs");
var buf = new Buffer(1024);

console.log("Going to open an existing file");
fs.open('input.txt', 'r+', function(err, fd) {
   if (err) {
       return console.error(err);
   }
   console.log("File opened successfully!");
   console.log("Going to truncate the file after 10 bytes");
   
   // Truncate the opened file.
   fs.ftruncate(fd, 10, function(err){
      if (err){
         console.log(err);
      } 
      console.log("File truncated successfully.");
      console.log("Going to read the same file"); 
      fs.read(fd, buf, 0, buf.length, 0, function(err, bytes){
         if (err){
            console.log(err);
         }

         // Print only read bytes to avoid junk.
         if(bytes > 0){
            console.log(buf.slice(0, bytes).toString());
         }

         // Close the opened file.
         fs.close(fd, function(err){
            if (err){
               console.log(err);
            } 
            console.log("File closed successfully.");
         });
      });
   });
});
```

康康

```bash
node /share/lesson/node.js/fs-ftruncate.js
```

## 	删除文件

### 	语法

以下是删除文件的方法的语法：

```js
fs.unlink(path, callback)
```

### 	参数

下面是使用的参数的说明：

- 		path - 这是文件名，包括路径
- 		callback - 这是回调函数

### 	示例

文件名:fs-unlink.js

```js
var fs = require("fs");

console.log("Going to delete an existing file");
fs.unlink('input.txt', function(err) {
   if (err) {
       return console.error(err);
   }
   console.log("File deleted successfully!");
});
```

康康

```bash
node /share/lesson/node.js/fs-unlink.js
```

## 	创建目录

### 	语法

下面是创建一个目录的方法的语法：

```js
fs.mkdir(path[, mode], callback)
```

### 	参数

下面是使用的参数的说明：

- 		path - 这是包括路径的目录名。
- 		mode - 这是要设置的目录权限。默认为0777。
- 		callback - 这是回调函数

### 	示例

文件名:fs-mkdir.js

```js
var fs = require("fs");

console.log("Going to create directory /tmp/test");
fs.mkdir('/tmp/test',function(err){
   if (err) {
       return console.error(err);
   }
   console.log("Directory created successfully!");
});
```

康康

```bash
node /share/lesson/node.js/fs-mkdir.js
```

验证:

```bash
ls /tmp
```

## 	读取目录

### 	语法

下面是读取一个目录的方法的语法：

```js
fs.readdir(path, callback)
```

### 	参数

下面是使用的参数的说明：

- 		path - 这是包括路径的目录名。
- 		callback - 这是回调函数得到两个参数（err, files），其中文件的文件名的目录中的数组排除 '.' 和  '..'.

### 	示例

文件名:fs-readdir.js

```js
var fs = require("fs");

console.log("Going to read directory /tmp");
fs.readdir("/tmp/",function(err, files){
   if (err) {
       return console.error(err);
   }
   files.forEach( function (file){
       console.log( file );
   });
});
```

康康

```bash
node /share/lesson/node.js/fs-readdir.js
```

## 	删除目录

### 	语法

下面是该方法删除目录的语法：

```js
fs.rmdir(path, callback)
```

### 	参数

下面是使用的参数的说明：

- 		path - 这是包括路径的目录名。
- 		callback - 这是回调函数

### 	示例

文件名:fs-rmdir.js

```js
var fs = require("fs");

console.log("Going to delete directory /tmp/test");
fs.rmdir("/tmp/test",function(err){
   if (err) {
       return console.error(err);
   }
   console.log("Going to read directory /tmp");
   fs.readdir("/tmp/",function(err, files){
      if (err) {
          return console.error(err);
      }
      files.forEach( function (file){
          console.log( file );
      });
   });
});
```

康康

```bash
node /share/lesson/node.js/fs-rmdir.js
```

验证

```bash
ls /tmp
```


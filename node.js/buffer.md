# node.js 缓冲器(buffer) 			

纯JavaScript是Unicode友好的，但对二进制数据不是很好。当与TCP流或文件系统打交道时，有必要处理字节流。 Node提供缓冲器类，它提供实例来存储原始数据相似的一个整数数组，但对应于在V8堆外的原始存储器的分配。

Buffer类是一个全局类，可以在应用程序，导入缓冲模块进行访问。

## 	创建缓冲区

 Node缓冲器可以以各种方式来构造。

### 方法 1

 以下是创建10个字节的汉缓冲的语法：

```js
var buf = new Buffer(10);
```

###  方法 2

 下面是用来从给定数组创建一个缓冲区的语法：

```js
var buf = new Buffer([10, 20, 30, 40, 50]);
```

### 方法 3

 下面是用来从给定的字符串和可选的编码类型创建缓冲区的语法：

```js
var buf = new Buffer("Simply Easy Learning", "utf-8");
```

 虽然“UTF8”是默认的编码，但你可以使用其它的编码： "ascii", "utf8", "utf16le", "ucs2", "base64" 或 "hex".

## 	写到缓冲器

### 	语法

 以下被写入到一个节点缓冲器的方法的语法：

```js
buf.write(string[, offset][, length][, encoding])
```

### 	参数

 下面是使用的参数的说明：

-  		**string** - 这是要被写入的数据串缓冲区。
-  		**offset** - 这是缓冲区开始的索引。默认值为0。
-  		**length** - 这是要写入的字节的数目。默认是 buffer.length
-  		**encoding** - 编码使用。 “UTF8”是默认的编码

### 	返回值

 这个方法返回写入的字节数。如果没有足够的空间在缓冲，以适应整个字符串，它将写该字符串的一部分。

### 	示例

文件名:bufferwrite.js

```js
buf = new Buffer(256);
len = buf.write("Simply Easy Learning");

console.log("Octets written : "+  len);
```

康康

```bash
node /share/lesson/node.js/bufferwrite.js
```

## 	从缓冲器读取

### 	语法

 下面是从节点缓冲器的数据的方法读取的语法：

```js
buf.toString([encoding][, start][, end])
```

### 	参数

 下面是使用的参数的说明：

-  		**encoding** - 编码使用。 “UTF8”是默认的编码
-  		**start** - 开始读取的索引，默认为0。
-  		**end** - 最终读数结束的索引，默认值是整个缓冲区。

### 	返回值

 此方法解码并返回来自使用指定的字符集编码的编码缓冲器的数据的字符串。

### 	示例

文件名:buffertostring.js

```js
buf = new Buffer(256);
len = buf.write("Simply Easy Learning");

console.log("Octets written : "+  len);
buf = new Buffer(26);
for (var i = 0 ; i < 26 ; i++) {
  buf[i] = i + 97;
}

console.log( buf.toString('ascii'));       // outputs: abcdefghijklmnopqrstuvwxyz
console.log( buf.toString('ascii',0,5));   // outputs: abcde
console.log( buf.toString('utf8',0,5));    // outputs: abcde
console.log( buf.toString(undefined,0,5)); // encoding defaults to 'utf8', outputs abcde
```

康康

```bash
node /share/lesson/node.js/buffertostring.js
```

## 	转换缓冲到JSON

### 	语法

 以下是转换节点缓存到JSON对象方法的语法：

```js
buf.toJSON()
```

### 	返回值

 此方法返回缓冲区JSON-表示。

### 	示例

文件名:buffertojson.js

```js
var buf = new Buffer('Simply Easy Learning');
var json = buf.toJSON(buf);

console.log(json);
```

康康

```bash
node /share/lesson/node.js/buffertojson.js
```

## 	接续缓冲器

### 	语法

 以下是连接Node缓存到单个节点缓存方法的语法：

```js
Buffer.concat(list[, totalLength])
```

### 	参数

 下面是使用的参数的说明：

-  		**list** -要连接缓冲区的数组对象列表
-  		**totalLength** - 这是缓冲器连接在一起时的总长度

### 	返回值

 该方法返回一个缓冲区实例。

### 	示例

文件名:buffercontact.js

```js
var buffer1 = new Buffer('To Go In Is ');
var buffer2 = new Buffer('Simply Easy Learning');
var buffer3 = Buffer.concat([buffer1,buffer2]);
console.log("buffer3 content: " + buffer3.toString());
```

康康

```bash
node /share/lesson/node.js/buffercontact.js
```

## 	比较缓冲器

### 	语法

 下面是比较两个Node缓冲器的方法的语法：

```js
buf.compare(otherBuffer);
```

### 	参数

 下面是使用参数的说明：

-  		**otherBuffer** - 这是将与被比较的其它缓冲 buf

### 	返回值

 返回一个数字，表示否到来之前或之后或和otherBuffer排序顺序一样。

### 	示例

文件名:buffercompare.js

```js
var buffer1 = new Buffer('ABC');
var buffer2 = new Buffer('ABCD');
var result = buffer1.compare(buffer2);

if(result < 0) {
   console.log(buffer1 +" comes before " + buffer2);
}else if(result == 0){
   console.log(buffer1 +" is same as " + buffer2);
}else {
   console.log(buffer1 +" comes after " + buffer2);
}
```

康康

```bash
node /share/lesson/node.js/buffercompare.js
```

## 	复制缓冲区

### 	语法

 以下是复制节点缓冲器的方法的语法：

```js
buf.copy(targetBuffer[, targetStart][, sourceStart][, sourceEnd])
```

### 	参数

 下面是使用的参数的说明：

-  		**targetBuffer** - 缓冲区对象的缓冲区将被复制。
-  		**targetStart** - 数量，可选，默认：0
-  		**sourceStart** - 数量，可选，默认：0
-  		**sourceEnd** - 数量，可选，默认：buffer.length

### 	返回值

 没有返回值。拷贝数据从该缓冲器的一区域中，即使在目标内存区域与源重叠的目标缓冲器的区域。如果不确定targetStart，那么sourceStart参数默认为0，sourceEnd默认为buffer.length。

### 	示例

文件名:buffercopy.js

```js
var buffer1 = new Buffer('ABC');
//copy a buffer
var buffer2 = new Buffer(3);
buffer1.copy(buffer2);
console.log("buffer2 content: " + buffer2.toString());
```

康康

```bash
node /share/lesson/node.js/buffercopy.js
```

## 	切片式缓冲器

### 	语法

 以下是获得一个节点缓冲器的子缓冲器的方法的语法：

```js
buf.slice([start][, end])
```

### 	参数

 下面是使用的参数的说明：

-  		start - 数量，可选，默认：0
-  		end - 数量可选，默认：buffer.length

### 	返回值

 返回一个新的缓冲区，它引用相同的内存如old，并 start 切片（默认为0）和 end（默认为buffer.length）索引。负索引则从缓冲区末尾开始。

### 	示例

文件名:bufferslice.js

```js
var buffer1 = new Buffer('node.js');
//slicing a buffer
var buffer2 = buffer1.slice(0,7);
console.log("buffer2 content: " + buffer2.toString());
```

康康

```bash
node /share/lesson/node.js/bufferslice.js
```

## 	缓冲区长度

### 	语法

 以下是得到以字节为单位的节点缓冲器的大小的方法的语法：

```js
buf.length;
```

### 	返回值

 返回缓冲器的字节的大小。

### 	示例

文件名:bufferlen.js

```js
var buffer = new Buffer('node.js');
//length of the buffer
console.log("buffer length: " + buffer.length);
```

康康

```bash
node /share/lesson/node.js/bufferlen.js
```

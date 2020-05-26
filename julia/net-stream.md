# Julia 网络和流

## 网络和流

Julia 提供了一个丰富的接口处理终端、管道、tcp套接字等等I/O流对象。

接口在系统层的实现是异步的，开发者以同步的方式调用该接口、一般无需关注底层异步实现。 接口实现主要基于Julia支持的协程(coroutine)功能。

## 基本流 I/O

所有 Julia 流都至少提供一个 `read` 和一个 `write` 方法，且第一个参数都是流对象，例如:

```julia
write(STDOUT,"Hello World")

read(STDIN,Char)
```

注意我又输入了一次回车，这样 Julia 会读入换行符。现在，由例子可见，`write` 方法的第二个参数是将要写入的数据，`read` 方法的第二个参数是即将读入的数据类型。例如，要读入一个简单的字节数组，我们可以:

```julia
x = zeros(Uint8,4)

read(STDIN,x)
```

不过像上面这么写有点麻烦，还提供了一些简化的方法。例如，我们可以将上例重写成:

```julia
readbytes(STDIN,4)
    abcd 
```

或者直接读入整行数据:

```julia
readline(STDIN)
    abcd
```

注意这取决于你的终端配置，你的 TTY 可能是行缓冲、需要多输入一个回车才会把数据传给 julia。

如果你想要通过 STDIN 去读每一行，你可以使用 eachline 方法：

```julia
for line in eachline(STDIN)
    print("Found $line")
end
```

或者如果你想要以字符为单位去读，则如下：

```julia
while !eof(STDIN)
    x = read(STDIN, Char)
    println("Found: $x")
end
```

## 文本 I/O

注意上面提到的写方法是对二进制流进行操作的。特别是，值不会被转换成任何规范的文本表示，而是会被写成如下：

```julia
write(STDOUT,0x61)
```

对于文本 I/O，可以使用 print 或 show 方法，这取决你的需求（可以查看标准库中对于两者不同之处的细节描述）：

```julia
print(STDOUT,0x61)
```

## 使用文件

像其他的环境一样，Julia 有一个开放的函数，它以一个文件名作为参数并且返回一个 IO 流对象，通过这个 IO 流，你可以从文件中读或者写其中的内容。举个例子来说，如果我们有一个文件，hello.txt，它的内容为 “Hello, World!”:

```julia
f = open("hello.txt")

readlines(f)
```

如果你想要写入某些内容到文件当中，你可以用写标志 (“w”) 打开它：

```julia
f = open("hello.txt","w")

write(f,"Hello again.")
```

如果你用这种方式检查 hello.txt 的内容，你将会注意到它是空的；其实没有任何东西被写入磁盘。这是因为 IO 流在数据真正写到磁盘之前必须被关掉：

```julia
close(f)
```

再次检查 hello.txt 将会显示它的内容已经被改变了。

打开一个文件，对它的内容做一些改变，然后关闭它是一个常见的模式。为了让这个过程更简单，这里存在另一个 open 的调用，用一个方法作为其第一个参数，用文件名作为他的第二个参数，打开文件，调用该文件的方法作为一个参数，然后再次关闭它。举一个例子，给出一个方法：

```julia
function read_and_capitalize(f::IOStream)
    return uppercase(readall(f))
end
```

你可以调用：

```julia
open(read_and_capitalize, "hello.txt")
    "HELLO AGAIN."
```

为了打开 *hello.txt*，调用它的 *read_and_capitalize* 方法，关闭 *hello.txt* 然后返回大写的内容。

为了避免去定义一个已经命名的函数，你可以使用 *do* 语法，动态的去创建一个匿名函数：

```julia
open("hello.txt") do f
  uppercase(readall(f))
end
```

## 简单的 TCP 例子

让我们直接用一个简单的 Tcp Sockets 的示例来说明。我们首先需要创建一个简单地服务器：

```julia
@async begin
     server = listen(2000)
     while true
       sock = accept(server)
       println("Hello World\n")
     end
    end
Task
```

那些熟悉 Unix socket API 的人，会觉得方法名和 Unix socket 很相似，尽管他们的用法比原生 Unix socket API 要简单。第一次调用 *listen* 将会创建一个服务器来等待即将到来的连接，在这个案例中监听的端口为 2000。相同的方法可能会用来去创建不同的其他种类的服务器：

```julia
listen(2000) # Listens on localhost:2000 (IPv4)

listen(ip"127.0.0.1",2000) # Equivalent to the first

listen(ip"::1",2000) # Listens on localhost:2000 (IPv6)

listen(IPv4(0),2001) # Listens on port 2001 on all IPv4 interfaces

listen(IPv6(0),2001) # Listens on port 2001 on all IPv6 interfaces

listen("testsocket") # Listens on a domain socket/named pipe
```

注意最后一次调用的返回值类型是不同的。这是因为这个服务器没有监听 TCP，而是在一个命名管道（Windows 术语）- 同样也称为域套接字（UNIX 的术语）。他们的不同之处非常微小，并且与他们的接收和连接方法有关系。接受方法会检索一个到客户端的连接，连接到我们刚刚创建的服务器端，而连接到服务器的函数使用的是特定的方法。连接方法和监听方法的参数是一样的，所以使用的环境（比如主机，cwd 等等）能够传递和监听方法相同的参数来建立一个连接。所以让我们来尝试一下（前提是已经创建好上面的服务器）：

```julia
connect(2000)
    TcpSocket(open, 0 bytes waiting)

Hello World
```

正如我们预期的那样，我们会看到 “Hello World” 被打印出来了。所以我让我们分析一下在后台发生了什么。当我们调用连接函数时，我们连接到了我们刚刚创建的服务器。同时，接收方法返回一个服务器端的连接到最新创建的套接字上，然后打印 “Hello World” 来表明连接成功了。

Julia 的一个强大功能是尽管 I/O 实际上是异步发生的，但 API 仍然是同步的，我们甚至不必担心回调或服务器是否继续正常运行。当我们调用连接时，当前任务会等待连接建立，并且在连接建立之后，当前任务才会继续执行。在暂停期间，服务器任务会恢复执行（因为现在一个连接请求可用），接受这个连接，打印出信息并且等待下一个客户端。读和写的工作是相同的。为了更好地理解，请看以下一个简单的 echo 服务器：

```julia
@async begin
     server = listen(2001)
     while true
       sock = accept(server)
       @async while true
         write(sock,readline(sock))
       end
     end
   end
Task

clientside=connect(2001)
    TcpSocket(open, 0 bytes waiting)

@async while true
  write(STDOUT,readline(clientside))
end

println(clientside,"Hello World from the Echo Server")
```

## 解析 IP 地址

一种不伴随监听方法的 *connect* 函数为 *connect(host::ASCIIString,port)*,它会尝试去连接到主机端口参数给出的端口提供的主机参数给出的主机。它允许你如下操作：

```julia
connect("google.com",80)
    TcpSocket(open, 0 bytes waiting)
```

这个功能的基础是 getaddrinfo 方法，将提供适当的地址解析:

```julia
getaddrinfo("google.com")
    IPv4(74.125.226.225)
```


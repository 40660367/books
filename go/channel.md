# Go语言 通道(channel)

通道是连接并发`goroutine`的管道。可以从一个`goroutine`向通道发送值，并在另一个`goroutine`中接收到这些值。


使用`make(chan val-type)`创建一个新通道，通道由输入的值传入。使用通道 `<-` 语法将值发送到通道。 这里从一个新的`goroutine`发送“`ping`”到在上面的消息通道。

`<-channel`语法从通道接收值。在这里，将收到上面发送的“`ping`”消息并打印出来。当运行程序时，“`ping`”消息通过通道成功地从一个`goroutine`传递到另一个`goroutine`。默认情况下发送和接收块，直到发送方和接收方都准备好。此属性允许在程序结束时等待“`ping`”消息，而不必使用任何其他同步。

文件名:`channels.go`

```go
package main

import "fmt"

func main() {

    // Create a new channel with `make(chan val-type)`.
    // Channels are typed by the values they convey.
    messages := make(chan string)

    // _Send_ a value into a channel using the `channel <-`
    // syntax. Here we send `"ping"`  to the `messages`
    // channel we made above, from a new goroutine.
    go func() { messages <- "ping" }()

    // The `<-channel` syntax _receives_ a value from the
    // channel. Here we'll receive the `"ping"` message
    // we sent above and print it out.
    msg := <-messages
    fmt.Println(msg)
}
```

```bash
go run /share/lesson/go/channels.go
```

康康
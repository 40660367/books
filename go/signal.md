# Go语言 信号(signal)	

有时我们希望Go程序能够智能地处理Unix信号。 例如，可能希望服务器在接收到`SIGTERM`时正常关闭，或者在收到`SIGINT`时使用命令行工具停止处理输入。下面介绍如何使用Go语言处理信号。

Go信号通知通过在通道上发送`os.Signal`值来工作。创建一个通道来接收这些通知(还会在程序退出时通知我们)。

文件：`signal.go`

```go
package main

import "fmt"
import "os"
import "os/signal"
import "syscall"

func main() {

    // Go signal notification works by sending `os.Signal`
    // values on a channel. We'll create a channel to
    // receive these notifications (we'll also make one to
    // notify us when the program can exit).
    sigs := make(chan os.Signal, 1)
    done := make(chan bool, 1)

    // `signal.Notify` registers the given channel to
    // receive notifications of the specified signals.
    signal.Notify(sigs, syscall.SIGINT, syscall.SIGTERM)

    // This goroutine executes a blocking receive for
    // signals. When it gets one it'll print it out
    // and then notify the program that it can finish.
    go func() {
        sig := <-sigs
        fmt.Println()
        fmt.Println(sig)
        done <- true
    }()

    // The program will wait here until it gets the
    // expected signal (as indicated by the goroutine
    // above sending a value on `done`) and then exit.
    fmt.Println("awaiting signal")
    <-done
    fmt.Println("exiting")
}
```

```bash
go run /share/lesson/go/signal.go
```

康康
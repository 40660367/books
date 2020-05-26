# Go HelloWorld

在学习Go编程语言的基本构建块之前，我们先来看看一个最小的Go程序结构，以便我们可在未来的章节将它作为参考。

<iframe src="//player.bilibili.com/player.html?aid=18523501&bvid=BV1cW411i7jg&cid=30224079&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true" width="100%"  height="460"> </iframe>
## Go Hello World示例

Go程序基本上由以下部分组成：

- 软件包声明
- 导入包
- 函数(功能)
- 变量
- 语句和表达式
- 注释

现在来看看一个简单的代码，打印一段话：“`Hello World`”：

文件名:helloworld.go

```go
package main

import "fmt"

func main() {
   /* This is Go Hello World program! */
   fmt.Println("Hello, World!")
}
```

让我们来看看以上程序的各个部分：

- 程序 `package main` 的第一行定义了程序应该包含的包名。它是一个必须的语句，因为Go程序在包中运行。`main`包是运行程序的起点(入口点)。每个包都有一个与之相关的路径和名称。
- 下一行`import "fmt"`是一个预处理器命令，它告诉Go编译器包含位于包`fmt`中的文件。
- 下一行`func main()`是程序执行开始的主函数。
- 下一行`/*...*/`将被编译器忽略，并且已经在程序中添加了额外的注释。 所以这样的行称为程序中的注释。注释也使用`//`表示，类似于`Java`或`C++`注释。
- 下一行`fmt.Println(...)`是Go中的另一个函数，它会产生消息“`Hello，World！`”。 以显示在屏幕上。这里`fmt`包已经导出`Println`方法，用于在屏幕上打印消息。
- 注意`Println`方法的大写`P`。在Go语言中，如果以大写字母开头，则是导出的名称。导出意味着相应包装的输入者可以访问函数或变量/常数。

## 执行Go程序

让我们看一下如何保存的源代码在一个文件中，以及如何编译并运行它。以下是简单的步骤：

- 打开文本编辑器并添加上述代码
- 将文件另存为`hello.go`
- 打开命令提示符，转到保存文件的目录
- 键入`go run hello.go`，然后按Enter键运行代码
- 如果代码中没有错误，那么将能够看到屏幕上打印的`“Hello World`”

```bash
go run /share/lesson/go/helloworld.go
```

康康
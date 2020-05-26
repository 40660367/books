# Go语言 字符串(string)

在Go编程中广泛使用的字符串是只读字节。在Go编程语言中，字符串是切片。 Go平台提供了各种库来操作字符串。

- unicode
- 正则表达式
- 字符串


## 创建字符串

创建字符串的最直接的方法如下：

```go
var greeting = "Hello world!"
```

每当遇到代码中的字符串时，编译器将创建一个字符串对象，其值为“`Hello world！`”。字符串文字持有有效的UTF-8序列称为符文。字符串可保存任意字节。参考如下代码 - 

文件名:string.go

```go
package main
import "fmt"
func main() {
   var greeting =  "Hello world!"

   fmt.Printf("normal string: ")
   fmt.Printf("%s", greeting)
   fmt.Printf("\n")
   fmt.Printf("hex bytes: ")
   for i := 0; i < len(greeting); i++ {
       fmt.Printf("%x ", greeting[i])
   }
   fmt.Printf("\n")

   const sampleText = "\xbd\xb2\x3d\xbc\x20\xe2\x8c\x98" 
   /*q flag escapes unprintable characters, with + flag it escapses non-ascii characters as well 
     to make output unambigous  */
   fmt.Printf("quoted string: ")
   fmt.Printf("%+q", sampleText)
   fmt.Printf("\n")  
}
```

```shell
go run /share/lesson/go/string.go
```
康康

> 注意：字符串文字是不可变的，因此一旦创建后，字符串文字就不能更改了。

## 字符串长度

`len(str)`方法返回包含在字符串文字中的字节数。请参考以下代码示例 - 

文件名:string-len.go

```go
package main
import "fmt"
func main() {
   var greeting =  "Hello world!"

   fmt.Printf("String Length is: ")
   fmt.Println(len(greeting))  
}
```

```shell
go run /share/lesson/go/string-len.go
```

康康

## 连接字符串

`strings`包包含一个用于连接多个字符串的`join()`方法，其语法如下：

```go
strings.Join(sample, " ")
```

`Join`连接数组的元素以创建单个字符串。第二个参数是分隔符，放置在数组的元素之间。
现在来看看下面的例子：

文件名:string-join.go

```go
package main
import (
 "fmt"
 "strings"
)
func main() {
   greetings :=  []string{"Hello","world!"}   
   fmt.Println(strings.Join(greetings, " "))
}
```

```shell
go run /share/lesson/go/string-join.go
```

康康
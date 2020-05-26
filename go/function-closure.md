# Go语言 函数闭包(function closure)

Go编程语言支持可以充当函数闭包的匿名函数。 当想要定义一个函数内联而不传递任何名称时，使用匿名函数。 在这个示例中，我们创建了一个函数`getSequence()`，它将返回另一个函数。该函数的目的是关闭上函数的变量`i`以形成闭包。 

<iframe src="//player.bilibili.com/player.html?aid=92510911&bvid=BV16E411H7og&cid=157940804&page=39" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
**示例：**

文件名:function-closure.go

```go
package main

import "fmt"

func getSequence() func() int {
   i:=0
   return func() int {
      i+=1
      return i  
   }
}

func main(){
   /* nextNumber is now a function with i as 0 */
   nextNumber := getSequence()  

   /* invoke nextNumber to increase i by 1 and return the same */
   fmt.Println(nextNumber())
   fmt.Println(nextNumber())
   fmt.Println(nextNumber())

   /* create a new sequence and see the result, i is 0 again*/
   nextNumber1 := getSequence()  
   fmt.Println(nextNumber1())
   fmt.Println(nextNumber1())
}
```

```shell
go run /share/lesson/go/function-closure.go
```

康康


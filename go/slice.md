# Go语言 切片(slice)

Go切片(Slice)是Go数组的一个抽象。 由于Go数组允许定义类型的变量，可以容纳相同数据类型的几个数据项，但它不提供任何内置的方法来动态增加其大小或获取自己的子数组。切片就没有这样的限制。 它提供了数组所需的许多实用功能，并广泛用于Go编程。


## 定义切片

要定义切片，可以将其声明为数组，而不指定大小或使用`make`函数创建一个。

```go
var numbers []int /* a slice of unspecified size */
/* numbers == []int{0,0,0,0,0}*/
numbers = make([]int,5,5) /* a slice of length 5 and capacity 5*/
```

### len() 和 cap()函数

因为切片(Slice)是数组上的抽象。 它实际上使用数组作为底层结构体`.len()`函数返回切片中存在的元素数量，其中`cap()`函数返回切片(Slice)的容量(大小)，即可容纳多少个元素。 以下是解释切片(Slice)的用法的示例：

文件名:slice-len-cap.go

```go
package main

import "fmt"

func main() {
   var numbers = make([]int,3,5)

   printSlice(numbers)
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```

```shell
go run /share/lesson/go/slice-len-cap.go
```

康康

### Nil切片

如果缺省情况下声明没有输入切片，则将其初始化为`nil`。 其长度和容量为零。 以下是一个示例：

文件名:slice-nil.go

```go
package main

import "fmt"

func main() {
   var numbers []int

   printSlice(numbers)

   if(numbers == nil){
      fmt.Printf("slice is nil")
   }
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```

```shell
go run /share/lesson/go/slice-nil.go
```

康康

### 子切片

切片(Slice)允许指定下界和上界，以使用`[lower-bound：upper-bound]`获取它的子切片。 以下是示例：

文件名：slice-bound.go

```go
package main

import "fmt"

func main() {
   /* create a slice */
   numbers := []int{0,1,2,3,4,5,6,7,8}   
   printSlice(numbers)

   /* print the original slice */
   fmt.Println("numbers ==", numbers)

   /* print the sub slice starting from index 1(included) to index 4(excluded)*/
   fmt.Println("numbers[1:4] ==", numbers[1:4])

   /* missing lower bound implies 0*/
   fmt.Println("numbers[:3] ==", numbers[:3])

   /* missing upper bound implies len(s)*/
   fmt.Println("numbers[4:] ==", numbers[4:])

   numbers1 := make([]int,0,5)
   printSlice(numbers1)

   /* print the sub slice starting from index 0(included) to index 2(excluded) */
   number2 := numbers[:2]
   printSlice(number2)

   /* print the sub slice starting from index 2(included) to index 5(excluded) */
   number3 := numbers[2:5]
   printSlice(number3)

}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```

当上述代码编译和执行时，它产生以下结果：

```shell
go run /share/lesson/go/slice-bound.go
```

康康

### append()和copy()函数

切片(Slice)允许使用`append()`函数增加切片的容量(大小)。使用`copy()`函数，将源切片的内容复制到目标切片。以下是示例：

文件名：slice-append.go

```go
package main

import "fmt"

func main() {
   var numbers []int
   printSlice(numbers)

   /* append allows nil slice */
   numbers = append(numbers, 0)
   printSlice(numbers)

   /* add one element to slice*/
   numbers = append(numbers, 1)
   printSlice(numbers)

   /* add more than one element at a time*/
   numbers = append(numbers, 2,3,4)
   printSlice(numbers)

   /* create a slice numbers1 with double the capacity of earlier slice*/
   numbers1 := make([]int, len(numbers), (cap(numbers))*2)

   /* copy content of numbers to numbers1 */
   copy(numbers1,numbers)
   printSlice(numbers1)   
}

func printSlice(x []int){
   fmt.Printf("len=%d cap=%d slice=%v\n",len(x),cap(x),x)
}
```

```shell
go run /share/lesson/go/slice-append.go
```

康康
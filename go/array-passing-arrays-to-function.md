# Go语言 将数组传递给函数

如果想传递一个一维数组作为参数到一个函数中，必须声明函数形式参数以下面两种方式的其中一种，两个声明方法都产生类似的结果，因为每个方式都告诉编译器要接收一个整数数组。类似的方式，可以传递多维数组作为形式参数。

### 方法-1

形式参数作为一个已知大小数组如下：

```go
void myFunction(param [10]int)
{
.
.
.
}
```

### 方法-2

形式参数作为一个未知道大小的数组如下：

```go
void myFunction(param []int)
{
.
.
.
}
```

现在，考虑下面的函数，它将数组作为参数和另一个指定数组大小的参数，并基于传递的参数，计算数组传递的数组中每个元素的平均值返回，如下：

```go
func getAverage(arr []int, int size) float32
{
   var i int
   var avg, sum float32  

   for i = 0; i < size; ++i {
      sum += arr[i]
   }

   avg = sum / size

   return avg;
}
```

### 示例

文件名:array-passing-arrays-to-function.go

```go
package main

import "fmt"

func main() {
   /* an int array with 5 elements */
   var  balance = []int {1000, 2, 3, 17, 50}
   var avg float32

   /* pass array as an argument */
   avg = getAverage( balance, 5 ) ;

   /* output the returned value */
   fmt.Printf( "Average value is: %f ", avg );
}
func getAverage(arr []int, size int) float32 {
   var i,sum int
   var avg float32  

   for i = 0; i < size;i++ {
      sum += arr[i]
   }

   avg = float32(sum / size)

   return avg;
}
```

```bash
go run /share/lesson/go/array-passing-arrays-to-function.go
```

康康

正如上面所看到的，数组的长度与函数无关，因为Go对形式参数不执行边界检查。
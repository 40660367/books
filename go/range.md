# Go语言 范围(range)

`range`关键字在`for`循环中用于遍历数组，切片，通道或映射的项目。 使用数组和切片，它返回项的索引为整数。 使用映射则它返回下一个键值对的键。 范围返回一个或两个值。如果在范围表达式的左侧仅使用一个值，则它是下表中的第一个值。

| 范围表达式       | 第1个值     | 第2个值(可选) |
| ---------------- | ----------- | ------------- |
| 数组或切片a[n]E  | 索引 i 整数 | a[i]E         |
| Strubg s字符串   | 索引 i 整数 | 符文整数      |
| map m map[K]V    | key k K     | value m[k] V  |
| channel c chan E | element e E | none          |

## 示例

文件名:range.go

```go
package main

import "fmt"

func main() {
   /* create a slice */
   numbers := []int{0,1,2,3,4,5,6,7,8} 

   /* print the numbers */
   for i:= range numbers {
      fmt.Println("Slice item",i,"is",numbers[i])
   }

   /* create a map*/
   countryCapitalMap := map[string] string {"France":"Paris","Italy":"Rome","Japan":"Tokyo"}

   /* print map using keys*/
   for country := range countryCapitalMap {
      fmt.Println("Capital of",country,"is",countryCapitalMap[country])
   }

   /* print map using key-value*/
   for country,capital := range countryCapitalMap {
      fmt.Println("Capital of",country,"is",capital)
   }
}
```

```bash
go run /share/lesson/go/range.go
```

康康


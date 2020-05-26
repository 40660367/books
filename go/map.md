# Go语言 映射(map)

Go提供了另一个重要的数据类型：**映射**(`Map`)，它将唯一键映射到值。 键是用于在检索值的对象。 给定一个键和一个值就可以在`Map`对象中设置值。设置存储值后，就可以使用其键检索它对应的值了。

<iframe src="//player.bilibili.com/player.html?aid=92510911&bvid=BV16E411H7og&cid=157939338&page=27" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>
### 定义映射

必须要使用`make`函数来创建映射。

```go
/* declare a variable, by default map will be nil*/
var map_variable map[key_data_type]value_data_type

/* define the map as nil map can not be assigned any value*/
map_variable = make(map[key_data_type]value_data_type)
```

### 示例

以下示例说明了映射的创建和使用。

文件名:map.go

```go
package main

import "fmt"

func main() {
   var countryCapitalMap map[string]string
   /* create a map*/
   countryCapitalMap = make(map[string]string)

   /* insert key-value pairs in the map*/
   countryCapitalMap["France"] = "Paris"
   countryCapitalMap["Italy"] = "Rome"
   countryCapitalMap["Japan"] = "Tokyo"
   countryCapitalMap["India"] = "New Delhi"

   /* print map using keys*/
   for country := range countryCapitalMap {
      fmt.Println("Capital of",country,"is",countryCapitalMap[country])
   }

   /* test if entry is present in the map or not*/
   capital, ok := countryCapitalMap["United States"]
   /* if ok is true, entry is present otherwise entry is absent*/
   if(ok){
      fmt.Println("Capital of United States is", capital)  
   }else {
      fmt.Println("Capital of United States is not present") 
   }
}
```

```bash
go run /share/lesson/go/map.go
```

康康

### delete()函数

`delete()`函数用于从映射中删除项目。它需要映射以及指定要删除的相应键。 以下是示例：

文件名:map-delete.go

```go
package main

import "fmt"

func main() {   
   /* create a map*/
   countryCapitalMap := map[string] string {"France":"Paris","Italy":"Rome","Japan":"Tokyo","India":"New Delhi"}

   fmt.Println("Original map")   

   /* print map */
   for country := range countryCapitalMap {
      fmt.Println("Capital of",country,"is",countryCapitalMap[country])
   }

   /* delete an entry */
   delete(countryCapitalMap,"France");
   fmt.Println("Entry for France is deleted")  

   fmt.Println("Updated map")   

   /* print map */
   for country := range countryCapitalMap {
      fmt.Println("Capital of",country,"is",countryCapitalMap[country])
   }
}
```

```bash
go run /share/lesson/go/map-delete.go
```

康康
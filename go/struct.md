# Go语言 结构体(struct)

Go数组允许定义一种可以保存多个相同类型的数据项的变量类型，但结构体是Go编程中可用的另一个用户定义的数据类型，它允许组合不同类型的数据项。

结构体用于表示记录，假设想在图书馆中跟踪图书。可能希望跟踪每本图书的以下属性：

- 标题(Title)
- 作者(Author)
- 科目(Subject)
- 图书编号(Book ID)

### 定义结构体

要定义结构，必须使用`type`和`struct`语句。`struct`语句定义了一个新的数据类型，在程序中有多个成员。`type`语句在例子中绑定一个类型为`struct`的名字。 `struct`语句的格式如下：

```go
type struct_variable_type struct {
   member definition;
   member definition;
   ...
   member definition;
}
```

当定义了结构体类型，它可以用于使用以下语法声明该类型的变量。

```go
variable_name := structure_variable_type {value1, value2...valuen}
```

### 访问结构体成员

要访问结构的任何成员，可使用成员访问运算符(`.`)。成员访问运算符被编码为结构变量名称和希望访问的结构成员的名称。使用`struct`关键字定义结构类型的变量。以下是解释结构用法的示例：


文件名:structure.go

```go
package main

import "fmt"

type Books struct {
   title string
   author string
   subject string
   book_id int
}

func main() {
   var Book1 Books        /* Declare Book1 of type Book */
   var Book2 Books        /* Declare Book2 of type Book */

   /* book 1 specification */
   Book1.title = "Go Programming"
   Book1.author = "Mahesh Kumar"
   Book1.subject = "Go Programming Tutorial"
   Book1.book_id = 6495407

   /* book 2 specification */
   Book2.title = "Telecom Billing"
   Book2.author = "Zara Ali"
   Book2.subject = "Telecom Billing Tutorial"
   Book2.book_id = 6495700

   /* print Book1 info */
   fmt.Printf( "Book 1 title : %s\n", Book1.title)
   fmt.Printf( "Book 1 author : %s\n", Book1.author)
   fmt.Printf( "Book 1 subject : %s\n", Book1.subject)
   fmt.Printf( "Book 1 book_id : %d\n", Book1.book_id)

   /* print Book2 info */
   fmt.Printf( "Book 2 title : %s\n", Book2.title)
   fmt.Printf( "Book 2 author : %s\n", Book2.author)
   fmt.Printf( "Book 2 subject : %s\n", Book2.subject)
   fmt.Printf( "Book 2 book_id : %d\n", Book2.book_id)
}
```

```shell
go run /share/lesson/go/structure.go
```

康康

### 结构体作为函数参数

可以传递一个结构体作为一个函数参数，与传递其他变量或指针的方式非常相似。可以使用类似于上面示例中访问的方式来访问结构变量：

文件名:structure-parm.go

```go
package main

import "fmt"

type Books struct {
   title string
   author string
   subject string
   book_id int
}

func main() {
   var Book1 Books        /* Declare Book1 of type Book */
   var Book2 Books        /* Declare Book2 of type Book */

   /* book 1 specification */
   Book1.title = "Go Programming"
   Book1.author = "Mahesh Kumar"
   Book1.subject = "Go Programming Tutorial"
   Book1.book_id = 6495407

   /* book 2 specification */
   Book2.title = "Telecom Billing"
   Book2.author = "Zara Ali"
   Book2.subject = "Telecom Billing Tutorial"
   Book2.book_id = 6495700

   /* print Book1 info */
   printBook(Book1)

   /* print Book2 info */
   printBook(Book2)
}
func printBook( book Books ) {
   fmt.Printf( "Book title : %s\n", book.title);
   fmt.Printf( "Book author : %s\n", book.author);
   fmt.Printf( "Book subject : %s\n", book.subject);
   fmt.Printf( "Book book_id : %d\n", book.book_id);
}
```

```shell
go run /share/lesson/go/structure-parm.go
```

康康

### 指针指向结构

可以以非常类似于定义指向其他变量的指针的方式来定义结构的指针，如下所示：

```go
var struct_pointer *Books
```

现在，可以在上面定义的指针变量中存储结构体变量的地址。要查找结构体变量的地址，将`&`操作符放在结构体名称之前，如下：

```go
struct_pointer = &Book1;
```

要使用指向该结构体的指针来访问结构的成员，必须使用“`.`”。 运算符如下：

```go
struct_pointer.title;
```

现在，重写上面的例子使用结构指针，希望这能让您更容易地理解这个概念，代码如下：

文件名:struct-pointer.go

```go
package main

import "fmt"

type Books struct {
   title string
   author string
   subject string
   book_id int
}

func main() {
   var Book1 Books        /* Declare Book1 of type Book */
   var Book2 Books        /* Declare Book2 of type Book */

   /* book 1 specification */
   Book1.title = "Go Programming"
   Book1.author = "Mahesh Kumar"
   Book1.subject = "Go Programming Tutorial"
   Book1.book_id = 6495407

   /* book 2 specification */
   Book2.title = "Telecom Billing"
   Book2.author = "Zara Ali"
   Book2.subject = "Telecom Billing Tutorial"
   Book2.book_id = 6495700

   /* print Book1 info */
   printBook(&Book1)

   /* print Book2 info */
   printBook(&Book2)
}
func printBook( book *Books ) {
   fmt.Printf( "Book title : %s\n", book.title);
   fmt.Printf( "Book author : %s\n", book.author);
   fmt.Printf( "Book subject : %s\n", book.subject);
   fmt.Printf( "Book book_id : %d\n", book.book_id);
}
```

```shell
go run /share/lesson/go/struct-pointer.go
```

康康
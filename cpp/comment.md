# C++ 注释(comment)

C++注释是不会被编译器执行的语句(或语句块)。 C++编程中的注释可用于提供对代码，变量，方法或类的解释。 借助于注释，您还可以隐藏程序代码。

在C++中有两种类型的注释。

- 单行注释
- 多行(跨行)注释

## C++单行注释

单行注释以`//`(双斜杠)开头。 下面来看看一个在C++中单行注释的例子。

文件名:

```cpp
#include <iostream>  
using namespace std;  
int main()  
{  
    int x = 11; // x is a variable      
    cout<<x<<"\n";         
}
```
```bash
g++ /share/lesson/cpp/comment1.cpp && ./a.out
```

康康

## C++多行注释

C++多行注释用于注释多行代码。 它被斜线和星号(`/ * ..... * /`)包围。 下面来看看一个C++多行注释的例子。

文件名:comment2.cpp

```cpp
#include <iostream>  
using namespace std;  
int main()  
{
    /* declare and
    print variable in C++. */  
    int x = 11; // x is a variable      
    cout<<x<<"\n";        
}
```

```bash
g++ /share/lesson/cpp/comment2.cpp && ./a.out
```

康康
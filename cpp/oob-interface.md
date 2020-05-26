# C++ 接口 (interface)

抽象类是在C++中实现抽象的方式。 C++中的抽象是隐藏内部细节和仅显示功能的过程。 抽象可以通过两种方式实现：

- 抽象类
- 接口

抽象类和接口都可以有抽象所需的抽象方法。

## C++抽象类

在C++类中，通过将其函数中的至少一个声明为纯虚函数，使其变得抽象。 通过在其声明中放置“`= 0`”来指定纯虚函数。 它的实现必须由派生类提供。

下面来看看一个C++中的抽象类的例子，它有一个抽象方法`draw()`。 它的实现由派生类：`Rectangle`和`Circle` 提供。 这两个类对抽象方法`draw()`有不同的实现。

文件名:oob-interface.cpp

```cpp
#include <iostream>  
using namespace std;  
 class Shape    
{    
    public:   
    virtual void draw()=0;    
};    
 class Rectangle : Shape    
{    
    public:  
     void draw()    
    {    
        cout <<"drawing rectangle..." <<endl;    
    }    
};    
class Circle : Shape    
{    
    public:  
     void draw()    
    {    
        cout <<"drawing circle..." <<endl;    
    }    
};    
int main( ) {  
    Rectangle rec;  
    Circle cir;  
    rec.draw();    
    cir.draw();   
   return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-interface.cpp && ./a.out
```


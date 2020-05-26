# C++ 结构体(struct)

在C++中，类和结构体(`struct`)是用于创建类的实例的蓝图(或叫模板)。结构体可用于轻量级对象，如矩形，颜色，点等。

与类不同，C++中的结构体(`struct`)是值类型而不是引用类型。 如果想在创建结构体之后不想修改的数据，结构体(`struct`)是很有用的。

## C++结构体示例

下面来看看一个简单的结构体`Rectangle`示例，它有两个数据成员：`width`和`height`。

文件名:oob-struct1.cpp

```cpp
#include <iostream>  
using namespace std;  
 struct Rectangle    
{    
   int width, height;    

 };    
int main(void) {  
    struct Rectangle rec;  
    rec.width=8;  
    rec.height=5;  
    cout<<"Area of Rectangle is: "<<(rec.width * rec.height)<<endl;  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-struct1.cpp && ./a.out
```

康康

**C++结构示例：使用构造函数和方法**

下面来看看另一个结构体的例子，使用构造函数初始化数据和方法来计算矩形的面积。

文件名:oob-struct2.cpp

```cpp
#include <iostream>  
using namespace std;  
 struct Rectangle    
{    
   int width, height;    
  Rectangle(int w, int h)    
    {    
        width = w;    
        height = h;    
    }    
  void areaOfRectangle() {     
    cout<<"Area of Rectangle is: "<<(width*height); }    
 };    
int main(void) {  
    struct Rectangle rec=Rectangle(4,6);  
    rec.areaOfRectangle();  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-struct2.cpp && ./a.out
```

康康
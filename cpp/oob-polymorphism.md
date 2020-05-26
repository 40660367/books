# C++ 多态(polymorphism)

术语“多态”(`Polymorphism`)是”`poly`“ + “`morphs`“的组合，其意味着多种形式。 这是一个希腊词。 在面向对象编程中，我们使用`3`个主要概念：继承，封装和多态。

C++中有两种类型的多态：

- **编译时多态性**：通过函数重载和操作符重载来实现，这也称为静态绑定或早期绑定。
- **运行时多态性**：它通过方法覆盖来实现，也称为动态绑定或后期绑定。

## C++运行时多态性示例

下面来看看一个简单的C++运行时多态的例子。

文件名:oob-polymorphism1.cpp

```cpp
#include <iostream>  
using namespace std;  
class Animal {  
    public:  
void eat(){    
cout<<"Eating...";    
    }      
};   
class Dog: public Animal    
{    
 public:  
 void eat()    
    {    
       cout<<"Eating bread...";    
    }    
};  
int main(void) {  
   Dog d = Dog();    
   d.eat();  
   return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-polymorphism1.cpp && ./a.out
```

康康

## C++运行时多态性示例：通过使用两个派生类

下面来看看看C++中的运行时多态性的另一个例子，下面有两个派生类。

文件名:oob-polymorphism2.cpp

```cpp
#include <iostream>  
using namespace std;  
class Shape {  
    public:  
virtual void draw(){    
cout<<"drawing..."<<endl;    
    }      
};   
class Rectangle: public Shape    
{    
 public:  
 void draw()    
    {    
       cout<<"drawing rectangle..."<<endl;    
    }    
};  
class Circle: public Shape    
{    
 public:  
 void draw()    
    {    
       cout<<"drawing circle..."<<endl;    
    }    
};  
int main(void) {  
   Shape *s;  
   Shape sh;  
   Rectangle rec;  
   Circle cir;  
   s=&sh;  
   s->draw();   
   s=&rec;  
   s->draw();    
   s->draw();   
}
```

```bash
g++ /share/lesson/cpp/oob-polymorphism2.cpp && ./a.out
```

康康

## 运行时多态性与数据成员

运行时多态性可以通过C++中的数据成员来实现。 下面来看看一个例子，通过引用变量访问字段，引用变量引用派生类的实例。

文件名:oob-polymorphism3.cpp

```cpp
#include <iostream>  
using namespace std;  
class Animal {  
    public:  
    string color = "Black";    
};   
class Dog: public Animal   
{    
 public:  
    string color = "Grey";    
};  
int main(void) {  
     Animal d= Dog();    
    cout<<d.color;   
}
```

```bash
g++ /share/lesson/cpp/oob-polymorphism3.cpp && ./a.out
```

康康
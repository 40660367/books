# C++ 虚函数(virtual function)	

C++虚函数是基类中的一个成员函数，您可以在派生类中重新定义它。 它声明使用`virtual`关键字。

它用于告诉编译器对函数执行动态链接或后期绑定。

 **后期绑定或动态链接**

在后期绑定函数调用在运行时被解决。 因此，编译器在运行时确定对象的类型，然后绑定函数调用。

**C++虚函数示例**

下面来看看看在程序中用来调用派生类的C++虚函数的简单例子。

文件名:oob-vf.cpp

```cpp
#include <iostream>  
using namespace std;  
class A  
{  
 public:  
     virtual void display()  
     {  
      cout << "Base class is invoked"<<endl;  
     }  
};  
class B:public A  
{  
 public:  
     void display()  
     {  
      cout << "Derived Class is invoked"<<endl;  
     }  
};  
int main()  
{  
    A* a;    //pointer of base class  
    B b;     //object of derived class  
    a = &b;  
    a->display();   //Late Binding occurs  
    return 0;
}
```

```bash
g++ /share/lesson/cpp/oob-vf.cpp && ./a.out
```

康康
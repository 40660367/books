# C++ 重载(overloading)

如果创建两个或多个成员(函数)具有相同的名称，但参数的数量或类型不同，则称为C++重载。 在C++中，我们可以重载：

- 方法
- 构造函数
- 索引属性

这是因为这些成员只有参数。

**C++中的重载类型有：**

- 函数重载
- 运算符重载

## C++函数重载

在C++中，具有两个或更多个具有相同名称但参数不同的函数称为**函数重载**。

函数重载的优点是它增加了程序的可读性，不需要为同一个函数操作功能使用不同的名称。

**C++函数重载示例**

下面来看看看函数重载的简单例子，修改了`add()`方法的参数数量。

文件名:oob-overloading1.cpp

```cpp
#include <iostream>  
using namespace std;  
class Cal {  
    public:  
static int add(int a,int b){    
        return a + b;    
    }    
static int add(int a, int b, int c)    
    {    
        return a + b + c;    
    }    
};   
int main(void) {  
    Cal C;  
    cout<<C.add(10, 20)<<endl;    
    cout<<C.add(12, 20, 23);   
   return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-overloading1.cpp && ./a.out
```

康康

## C++操作符重载

操作符重载用于重载或重新定义C++中可用的大多数操作符。 它用于对用户定义数据类型执行操作。

运算符重载的优点是对同一操作数执行不同的操作。

**C++操作符重载示例**

下面来看看看在C++中运算符重载的简单例子。 在本示例中，定义了`void operator ++ ()`运算符函数(在`Test`类内部)。

文件名:oob-overloading2.cpp

```cpp
#include <iostream>  
using namespace std;  
class Test  
{  
   private:  
      int num;  
   public:  
       Test(): num(8){}  
       void operator ++()   
       {   
          num = num+2;   
       }  
       void Print() {   
           cout<<"The Count is: "<<num;   
       }  
};  
int main()  
{  
    Test tt;  
    ++tt;  // calling of a function "void operator ++()"  
    tt.Print();  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/oob-overloading2.cpp && ./a.out
```

康康

## C++函数重写

在C++中，如果派生类定义了与其基类中定义的函数相同，则称函数重写。 它用于实现运行时多态性。 它使您能够提供已由其基类提供的函数有所区别的特定实现。

**C++函数重写/覆盖示例**

下面来看看一个简单的C++中函数重写/覆盖的例子。 在这个例子中，我们重写/覆盖了`eat()`函数。

文件名:oob-overloading3.cpp

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
g++ /share/lesson/cpp/oob-overloading3.cpp && ./a.out
```

康康


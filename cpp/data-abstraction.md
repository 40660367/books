# C++ 数据抽象(data abstraction)

下面来看看一个C++中的抽象类的例子，它有一个抽象方法`draw()`。 在C++程序中，如果实现类的私有和公共成员，那么它是一个数据抽象的例子。

下面来看看看数据抽象的简单例子。

文件名:data-abstraction.cpp

```cpp
#include <iostream>  
using namespace std;  
class Sum  
{  
    private: int x, y, z;  
    public:  
        void add()  
        {  
            cout<<"Enter two numbers: ";  
            cin>>x>>y;  
            z= x+y;  
            cout<<"Sum of two number is: "<<z<<endl;  
        }  
};  
int main()  
{  
    Sum sm;  
    sm.add();  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/data-abstraction.cpp && ./a.out
```

康康
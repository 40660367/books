# C++ 命名空间 (namespace)			

C++中的命名空间用于组织项目中的类，以方便处理应用程序结构。

对于访问命名空间的类，我们需要使用`namespacename::classname`。 可以使用 `using` 关键字，所以不必一直使用完整的名称。

在C++中，全局命名空间是根命名空间。 `global::std`总是引用C++ 框架的命名空间“`std`”。

## C++命名空间示例

下面来看看看包含变量和函数的命名空间的一个简单例子。

文件名:namespace1.cpp

```cpp
#include <iostream>  
using namespace std;  
namespace First {    
    void sayHello() {   
        cout<<"Hello First Namespace"<<endl;          
    }    
}    
namespace Second  {    
    void sayHello() {   
        cout<<"Hello Second Namespace"<<endl;   
    }    
}   
int main()  
{  
    First::sayHello();  
    Second::sayHello();  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/namespace1.cpp && ./a.out
```

康康

**C++命名空间示例：通过使用 using 关键字**

文件名:namespace2.cpp

下面来看看看另一个命名空间的例子，使用“`using`”关键字，这样就不必使用完整的名称来访问命名空间程序。

```cpp
#include <iostream>  
using namespace std;  
namespace First{  
   void sayHello(){  
      cout << "Hello First Namespace" << endl;  
   }  
}  
namespace Second{  
   void sayHello(){  
      cout << "Hello Second Namespace" << endl;  
   }  
}  
using namespace First;  
int main () {  
   sayHello();  
   return 0;  
}
```

```bash
g++ /share/lesson/cpp/namespace2.cpp && ./a.out
```

康康
# C++ goto语句

C++ **goto语句**也称为跳转语句。 它用于将控制转移到程序的其他部分。 它无条件跳转到指定的标签。

它可用于从深层嵌套循环或`switch case`标签传输控制。

**C++ Goto语句示例**

下面来看看看C++中goto语句的简单例子。

文件名:loopcontrol-goto.cpp

```cpp
#include <iostream>  
using namespace std;  
int main()  
{  
ineligible:    
    cout<<"You are not eligible to vote!\n";    
    cout<<"Enter your age:\n";    
    int age;  
    cin>>age;  
    if (age < 18){    
        goto ineligible;    
    }    
    else    
    {    
        cout<<"You are eligible to vote!";     
    }
    return 0;
}
```

```bash
g++ /share/lesson/cpp/loopcontrol-goto.cpp && ./a.out
```
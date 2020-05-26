# C++ Switch语句

C++ **switch语句**从多个条件执行一个语句。 它就类似于在C++中的`if-else-if`语句。

**switch语句**的基本语法如下所示 -

```cpp
switch(expression){      
    case value1:      
        //code to be executed;      
        break;    
    case value2:      
        //code to be executed;      
        break;    
    ......      

    default:       
        //code to be executed if all cases are not matched;      
        break;    
}
```

**C++ Switch示例**

文件名:logic-switch.cpp

```cpp
#include <iostream>  
using namespace std;  
int main () {  
    int num;  
    cout<<"Enter a number to check grade:";    
    cin>>num;  
    switch (num)    
    {    
        case 10: cout<<"It is 10"<<endl; break;    
        case 20: cout<<"It is 20"<<endl; break;    
        case 30: cout<<"It is 30"<<endl; break;    
        default: cout<<"Not 10, 20 or 30"<<endl; break;    
    }
    return 0;
}
```

```bash
g++ /share/lesson/cpp/logic-switch.cpp && ./a.out
```
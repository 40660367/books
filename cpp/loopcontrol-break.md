# C++ break语句

C++ break用于中断循环或switch语句。 它在给定条件下中断程序的当前执行流程。 在内循环的情况下，它仅中断内循环。

```cpp
statement;      
break;
```

**C++ Break语句示例**

下面来看看一个在循环中使用的C++ break语句的简单示例。

文件名:loopcontrol-break.cpp

```cpp
#include <iostream>  
using namespace std;  
int main() {  
    for (int i = 1; i <= 10; i++)    
    {    
        if (i == 5)    
        {    
            break;    
        }    
        cout<<i<<"\n";    
    }
    return 0;
}
```

```bash
g++ /share/lesson/cpp/loopcontrol-break.cpp && ./a.out
```

## C++ break语句与内循环

只有在内循环中使用break语句，C++ break语句才会中断内循环。

文件名:loopcontrol-breakinner.cpp

```cpp
#include <iostream>  
using namespace std;  
int main()  
{  
    for(int i=1;i<=3;i++){        
        for(int j=1;j<=3;j++){        
            if(i==2&&j==2){        
                break;        
            }        
            cout<<i<<" "<<j<<"\n";             
        }        
    }
    return 0;
}
```

```bash
g++ /share/lesson/cpp/loopcontrol-breakinner.cpp && ./a.out
```
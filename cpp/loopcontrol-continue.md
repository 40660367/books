# C++ continue语句

C++ `continue`语句用于继续循环。它继续程序的当前流程，并在指定条件下跳过剩余的代码。 在内循环的情况下，它仅继续内循环，即：跳过内循环，继续执行下一个内循环。

```cpp
statement;      
continue;
```

## C++ Continue语句示例

文件名:loopcontrol-continue.cpp

```cpp
#include <iostream>  
using namespace std;  
int main()  
{  
    for(int i=1;i<=10;i++){      
        if(i==5){      
            continue;      
        }      
        cout<<i<<"\n";      
    }
    return 0;
}
```

```bash
g++ /share/lesson/cpp/loopcontrol-continue.cpp && ./a.out
```

## C++使用内循环continue声明

C++ continue语句只有在内循环中使用，continue语句时继续内循环。

文件名:loopcontrol-continueinner.cpp

```cpp
#include <iostream>  
using namespace std;  
int main()  
{  
    for(int i=1;i<=3;i++){        
        for(int j=1;j<=3;j++){        
            if(i==2&&j==2){        
                continue;        
            }        
            cout<<i<<" "<<j<<"\n";                  
        }        
    }
    return 0;
}
```

```bash
g++ /share/lesson/cpp/loopcontrol-continueinner.cpp && ./a.out
```
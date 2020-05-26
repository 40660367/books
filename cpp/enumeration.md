# C++ 枚举(enumeration)

C++中的枚举是一种包含固定常量的数据类型。

枚举可以用于星期几(`SUNDAY`，`MONDAY`，`TUESDAY`，`WEDNESDAY`，`THURSDAY`，`FRIDAY`和`SATURDAY`)，方向(`NORTH`，`SOUTH`，`EAST`和`WEST`等)。C++枚举常量是静态和最终隐式。

C++枚举可以认为是具有固定的常量集合的类。

**C++中枚举注意事项**

- 枚举提高了类型安全性
- 枚举可以很容易地在`switch`语句块中使用
- 枚举可以遍历
- 枚举可以有字段，构造函数和方法
- 枚举可以实现许多接口，但不能扩展任何类，因为它在内部扩展`Enum`类

## C++枚举示例

下面来看看看在C++程序中使用的枚举数据类型的简单例子。

文件名:enumeration.cpp

```cpp
#include <iostream>  
using namespace std;  
enum week { Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday };  
int main()  
{  
    week day;  
    day = Friday;  
    cout << "Day: " << day+1<<endl;  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/enumeration.cpp && ./a.out
```

康康
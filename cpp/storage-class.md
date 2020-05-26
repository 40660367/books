# C++ 存储类(storage class)			

存储类用于定义C++程序中变量和/或函数的生命周期和可见性。

寿命是指变量保持活动的时间段，可见性是指可访问变量的程序的模块。

有五种类型的存储类，可以在C++程序中使用

- 自动(Automatic)
- 寄存器(Register)
- 静态(Static)
- 外部(External)
- 可变(Mutable)

| 存储类 | 关键字   | 生命周期 | 可见性 | 初始值 |
| ------ | -------- | -------- | ------ | ------ |
| 自动   | auto     | 函数块   | 局部   | 垃圾   |
| 寄存器 | register | 函数块   | 局部   | 垃圾   |
| 可变   | mutable  | 类       | 局部   | 垃圾   |
| 静态   | static   | 整个程序 | 全局   | 零     |
| 外部   | extern   | 整个程序 | 局部   | 零     |

## 自动存储类

它是所有局部变量的默认存储类。 `auto`关键字自动应用于所有局部变量。

```cpp
{   
    auto int y;  
    float y = 3.45;  
}
```

上面的例子定义了两个具有相同存储类的变量，`auto`只能在函数中使用。

## 注册存储类

寄存器变量在寄存器中分配存储器而不是`RAM`。 其大小与寄存器大小相同。 它比其他变量具有更快的访问速度。
建议仅使用寄存器变量进行快速访问，例如:在计数器中。

> **注意**：我们不能得到寄存器变量的地址。

```cpp
register int counter=0;
```

## 静态存储类

静态变量只初始化一次，直到程序结束。 它保留可在多个函数之间调用的值。
静态变量由编译器提供的一个默认值：`0`。

文件名：storage-classes.cpp

```cpp
#include <iostream>  
using namespace std;  
void func() {    
    static int i=0; //static variable    
    int j=0; //local variable    
    i++;    
    j++;    
    cout<<"i=" << i<<" and j=" <<j<<endl;    
}    
int main()  
{  
    func();    
    func();    
    func();    
}
```

```bash
g++ /share/lesson/cpp/storage-classes.cpp && ./a.out
```

康康

## 外部存储类

`extern`变量对所有程序都可见。 如果两个或多个文件共享相同的变量或函数，则使用它。

```cpp
extern int counter=0;
```
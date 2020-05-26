# C++函数 通过值调用和引用调用 			

有两种方法可以将值或数据传递给C++语言的函数：通过值调用和通过引用调用。 原始值在值调用中不会被修改，但通过引用调用中会被修改。

下面来理解在C++语言中的通过值调用和通过引用调用。

## 在C++中通过值调用

在值调用中，不修改原始值。
在值调用中，传递给函数的值由函数参数本地存储在堆栈存储器位置。 如果更改函数参数的值，则仅更改当前函数的值，函数内修改的参数值不会反映到函数的外部。 它不会改变调用方法中的变量的值，如：main()函数。

下面我们通过下面的例子来尝试理解C++语言中的按值调用的概念：

文件名:function-callbyvalue.cpp

```cpp
#include <iostream>  
using namespace std;  
void change(int data);  
int main()  
{  
    int data = 3;  
    change(data);  
    cout << "Value of the data is: " << data<< endl;  
    return 0;  
}  
void change(int data)  
{  
    data = 5;  
}
```

```bash
g++ /share/lesson/cpp/function-callbyvalue.cpp && ./a.out
```

康康

## 在C++中通过引用调用

在引用调用中，原始值会被修改，因为我们是通过引用(地址)来调用的。

这里，值的地址在函数中传递，因此实际和形式参数共享相同的地址空间。 因此，在函数内部改变的值会反映在函数内部以及外部。

> **注意**：要理解通过引用调用，您必须具有指针的基本知识。

通过下面的例子来尝试理解C++语言中的引用的概念：

文件名:function-callbyref.cpp

```cpp
#include<iostream>  
using namespace std;    
void swap(int *x, int *y)  
{  
    int swap;  
    swap=*x;  
    *x=*y;  
    *y=swap;  
}  
int main()   
{    
    int x=500, y=100;    
    swap(&x, &y);  // passing value to function  
    cout<<"Value of x is: "<<x<<endl;  
    cout<<"Value of y is: "<<y<<endl;  
    return 0;  
}
```

```bash
g++ /share/lesson/cpp/function-callbyref.cpp && ./a.out
```

康康

**在C++中通过值调用和通过引用调用的区别**

| 序号 | 通过值调用                             | 通过引用调用                         |
| ---- | -------------------------------------- | ------------------------------------ |
| 1    | 将值的副本传递给函数                   | 将值的地址传递给函数                 |
| 2    | 在函数内部进行的更改不会反映在函数外部 | 在函数内部进行的更改也反映在函数外部 |
| 3    | 实际和形式参数将在不同的内存位置创建   | 实际和形式参数将在同一内存位置创建   |
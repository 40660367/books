# C++ 函数递归(function recursion)

当函数在同一个函数内调用时，它被称为C++中的递归。 调用相同函数的函数(函数自已调用自已)称为递归函数。

在函数调用之后调用自身并且不执行任何任务的函数称为尾递归。 在尾递归中，我们通常使用`return`语句调用相同的函数。

下面来看看一个简单的递归示例。

```cpp
recursionfunction(){    
    recursionfunction(); //calling self function    
}
```

## C++递归示例

下面来看看一个例子，使用C++语言中的递归来打印一个数的阶乘。

文件名：recursion.cpp

```cpp
#include<iostream>  
using namespace std;    
int main()  
{  
    int factorial(int);  
    int fact,value;  
    cout<<"Enter any number: ";  
    cin>>value;  
    fact=factorial(value);  
    cout<<"Factorial of a number is: "<<fact<<endl;  
    return 0;  
}  

int factorial(int n)  
{  
    if(n<0)  
        return(-1); /*Wrong value*/    
    if(n==0)  
        return(1);  /*Terminating condition*/  
    else  
    {  
        return(n*factorial(n-1));      
    }  
}
```

```bash
g++ /share/lesson/cpp/recursion.cpp && ./a.out
```

康康
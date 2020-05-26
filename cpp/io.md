# C++ 输入输出(io)			

C++中的I/O操作使用流概念。 流是字节或数据流的序列。 它能使有效提高性能。如果字节从主存储器流向设备，如：打印机，显示屏或网络连接等，则称为**输出操作**。

如果字节从打印机，显示屏幕或网络连接等设备流向主存储器，则称为**输入操作**。

## I/O库头文件

下面来看看在C++编程中使用的公共头文件，它们分别是：

| 头文件       | 函数及描述                                                   |
| ------------ | ------------------------------------------------------------ |
| `<iostream>` | 它用于定义`cout`，`cin`和`cerr`对象，分别对应于标准输出流，标准输入流和标准错误流。 |
| `<iomanip>`           | 它用于声明对执行格式化 I/O 的服务，如：`setprecision` 和 `setw`。 |
| `<fstream>`           | 它用于声明用户控制文件处理的服务。                           |

## 标准输出流(cout)

`cout`是`ostream`类的预定义对象。 它与标准输出设备连接，通常是一个显示屏。 `cout`与流插入运算符(`<<`)结合使用，以在控制台上显示输出

下面来看看标准输出流(`cout`)的简单例子：

文件名:cout.cpp

```cpp
#include <iostream>  
using namespace std;  
int main( ) {  
   char ary[] = "Welcome to C++ tutorial";  
   cout << "Value of ary is: " << ary << endl;  
}
```

```cpp
g++ /share/lesson/cpp/cout.cpp && ./a.out
```

康康

## 标准输入流(cin)

`cin`是`istream`类的预定义对象。 它与标准输入设备连接，标准输入设备通常是键盘。 `cin`与流提取运算符(`>>`)结合使用，从控制台读取输入。

下面来看看标准输入流(`cin`)的简单例子：

文件名:cin.cpp

```cpp
#include <iostream>  
using namespace std;  
int main( ) {  
  int age;  
   cout << "Enter your age: ";  
   cin >> age;  
   cout << "Your age is: " << age s<< endl;  
}
```

```bash
g++ /share/lesson/cpp/cin.cpp && ./a.out
```

康康

## 结束行(endl)

`endl`是`ostream类`的预定义对象。 它用于插入新行字符并刷新流。

下面来看看标准结束行(`endl`)的简单例子：

```cpp
#include <iostream>  
using namespace std;  
int main( ) {  
    cout << "C++ Tutorial";     
    cout << "End of line"<<endl;   
}
```

执行上面的代码得到以下结果 -

```bash
g++ /share/lesson/cpp/endl.cpp && ./a.out
```

康康
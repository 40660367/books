# C++ HelloWorld

要编写第一个C++程序，依据以下三步即可

## 编写代码

在右侧实验区打开编辑器vim，并编写以下代码：

文件名:helloworld.cpp

```cpp
#include <iostream>
using namespace std;
 
int main()
{
   cout << "Hello World"; // 输出 Hello World
   return 0;
}
```

把上述代码保存在当前路径下的 `hw.cpp` 的文件中。

- `#include `包括标准输入输出库函数。它提供`cin`和`cout`方法分别从输入和写入到输出。
- `int main()` 这里的`main()`函数是C++语言中每个程序的入口点。 `int`关键字指定它返回一个`int`类型的值。
- `cout << "Hello World"`。 用于打印字符串“`Welcome to C++ Programming.`”在控制台上。

## 编译

```bash
g++ /share/lesson/cpp/helloworld.cpp
```

## 运行

```bash
./a.out
```


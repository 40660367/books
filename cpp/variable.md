# C++ 变量(variable)

数据类型指定变量可存储的数据类型，例如：整数，浮点，字符等。

C++语言中有`4`种类型的数据类型。

| 类型                             | 数据类型                           |
| -------------------------------- | ---------------------------------- |
| 基本数据类型(Basic)              | `int`, `char`, `float`, `double`等 |
| 派生数据类型(Derived)            | 数组, 指针等                       |
| 枚举数据类型(Enumeration)        | 枚举(`enum`)                       |
| 用户定义的数据类型(User Defined) | 结构体                             |

## 基本数据类型

基本数据类型是基于整数和浮点的。 C++语言支持有符号和无符号文字。基本数据类型的内存大小可能会根据`32`位或`64`位操作系统而改变。
下面为看看基本的数据类型。 它的大小根据`32`位操作系统给出的。

| 数据类型           | 内存大小 | 范围             |
| ------------------ | -------- | ---------------- |
| char               | 1 byte   | -128 ~ 127       |
| signed char        | 1 byte   | -128 ~ 127       |
| unsigned char      | 1 byte   | 0 ~ 127          |
| short              | 2 byte   | -32,768 ~ 32,767 |
| signed short       | 2 byte   | -32,768 ~ 32,767 |
| unsigned short     | 2 byte   | 0 ~ 32,767       |
| int                | 2 byte   | -32,768 ~ 32,767 |
| signed int         | 2 byte   | -32,768 ~ 32,767 |
| unsigned int       | 2 byte   | 0 ~ 32,767       |
| short int          | 2 byte   | -32,768 ~ 32,767 |
| signed short int   | 2 byte   | -32,768 ~ 32,767 |
| unsigned short int | 2 byte   | 0 ~ 32,767       |
| long int           | 4 byte   |                  |
| signed long int    | 4 byte   |                  |
| unsigned long int  | 4 byte   |                  |
| float              | 4 byte   |                  |
| double             | 8 byte   |                  |
| long double        | 10 byte  |                  |
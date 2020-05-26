# Python3 基础语法(syntax)

## 编码

默认情况下，Python 3 源码文件以 **UTF-8** 编码，所有字符串都是 unicode 字符串。 当然你也可以为源码文件指定不同的编码：`# -*- coding: cp-1252 -*-`

上述定义允许在源文件中使用 Windows-1252 字符集中的字符编码，对应适合语言为保加利亚语、白罗斯语、马其顿语、俄语、塞尔维亚语。

## 标识符

- 第一个字符必须是字母表中字母或下划线 `_` 。
- 标识符的其他的部分由字母、数字和下划线组成。
- 标识符对大小写敏感。

在 Python 3 中，可以用中文作为变量名，非 ASCII 标识符也是允许的了。

## python保留字

保留字即关键字，我们不能把它们用作任何标识符名称。Python 的标准库提供了一个`keyword`模块，可以输出当前版本的所有关键字。

#### 练习：列出Python保留的所有关键字

```Python
import keyword
keyword.kwlist
```

## 注释

Python中单行注释以`#`开头

#### 练习:Python简单注释
```Python
%%writefile a.py

# 第一个注释
print("Hello, Python!")# 第二个注释
```

执行以上代码，输出结果为：

```Python
!python a.py
```

#### 练习：Python多行注释

多行注释可以用多个 `#`号，还有 `'''` 和`"""`：

```Python
%%writefile b.py
# 第一个注释
# 第二个注释
 
'''
第三注释
第四注释
'''
 
"""
第五注释
第六注释
"""
print("Hello, Python!")
```

```Python
#执行并查看输出结果
!python b.py
```

## 行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号 `{}` 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

#### 练习：行与缩进

```Python
if True:
    print("True")
else:
    print("False")
```

#### 练习：错误的行与缩进

以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：

```Python
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
  print("False")    # 缩进不一致，会导致运行错误
```

以上程序由于缩进不一致，执行后会出现类似错误

## 多行语句

Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠`\`来实现多行语句

#### 练习：`\`实现的多行语句

```Python
total = 'a' + \
        'b' + \
        'c'
total
```

#### 练习：不需要`\`实现的多行语句

在 `[]`, `{}`, 或 `()` 等对象中出现的多行语句，不需要使用反斜杠`\`

```Python
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']
total
```

## 数字(Number)类型

python中数字有四种类型：整数、布尔型、浮点数和复数。

- **int** (整数), 如 1, 只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。
- **bool** (布尔), 如 True。
- **float** (浮点数), 如 1.23、3E-2
- **complex** (复数), 如 1 + 2j、 1.1 + 2.2j

## 字符串(String)

- python中单引号和双引号使用完全相同。
- 使用三引号(`'''`或`"""`)可以指定一个多行字符串。
- 转义符`\`
- 反斜杠可以用来转义，使用r可以让反斜杠不发生转义。。 如`r"this is a line with \n"` 则`\n`会显示，并不是换行。
- 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
- 字符串可以用 + 运算符连接在一起，用 * 运算符重复。
- Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
- Python中的字符串不能改变。
- Python 没有单独的字符类型，一个字符就是长度为 1 的字符串。
- 字符串的截取的语法格式如下：**变量[头下标:尾下标:步长]**

#### 练习：字符串初始化
```Python
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""
print(word)
print(sentence)
print(paragraph)
```

#### 练习：字符串截取与连接

```Python
str='Python3'
 
print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串
 
print('')
 
print('hello\nPythoner')      # 使用反斜杠(\)+n转义特殊字符

#这里的 r 指 raw，即 raw string。
print(r'hello\nPythoner')     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
```
## 空行

函数之间或类的方法之间用空行分隔，表示一段新的代码的开始。类和函数入口之间也用一行空行分隔，以突出函数入口的开始。

空行与代码缩进不同，空行并不是Python语法的一部分。书写时不插入空行，Python解释器运行也不会出错。但是空行的作用在于分隔两段不同功能或含义的代码，便于日后代码的维护或重构。

**记住：**空行也是程序代码的一部分。

## 等待用户输入

执行下面的程序在按回车键后就会等待用户输入：

#### 练习：输入

```Python
x=input("\n\n按下 enter 键后退出。")
print(x)
```
以上代码中 ，"\n\n"在结果输出前会输出两个新的空行。一旦用户按下 enter 键时，程序将退出。

## `;`一行写多条语句

Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

#### 练习:多个语句`;`分割

```Python
import sys; x = 'python3'; sys.stdout.write(x + '\n')
```

## 多个语句构成代码组

缩进相同的一组语句构成一个代码块，我们称之代码组。

像`if`、`while`、`def`和`class`这样的复合语句，首行以关键字开始，以冒号`: `结束，该行之后的一行或多行代码构成代码组。

我们将首行及后面的代码组称为一个子句(clause)。

#### 练习：代码组
```Python
a=int(input('please input a int number to a!'))

if a>10 : 
   print('a is bigger than 10')
elif a<10 : 
   print('a is smaller than 10') 
else : 
   print('a is equal 10') 
```


## `print()`打印对象

#### 练习:`print()`默认换行输出

```Python
x="a"
y="b"
# 换行输出
print( x )
print( y )
```
#### 练习:`print()`不换行输出

```Python
x="a"
y="b"
# 不换行输出
print( x, end=" " )
print( y, end=" " )
```

```Python
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
```

## 导入模块

### import 与 from...import的区别

在 python 用 **import** 或者 **from...import** 来导入相应的模块。

将整个模块(somemodule)导入，格式为： **import somemodule**

从某个模块中导入某个函数,格式为： **from somemodule import somefunction**

从某个模块中导入多个函数,格式为： **from somemodule import firstfunc, secondfunc, thirdfunc**

将某个模块中的全部函数导入，格式为： **from somemodule import \***

#### 练习：导入 sys 模块

```Python
import sys
print('================Python import mode==========================')
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为',sys.path)
```

#### 练习：导入 sys 模块的 argv,path 成员

```Python
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path
```

## Python脚本接收命令行参数

我们在使用脚本形式执行 Python 时，可以接收命令行输入的参数。

如果想对python脚本传参数，那么就需要命令行参数的支持了，这样可以省的每次去改脚步了。

#### 练习：Python脚本接收命令行参数

```Python
%%writefile argv.py

#写入argv.py这个Python脚本
from sys import argv
script,first,second = argv
print("the script is called:", script)
print("the first variable is:", first)
print("the second variable is:", second)
```

```Python
#调用Python解释器执行这个脚本
!python argv.py 人生苦短 我用Python
```


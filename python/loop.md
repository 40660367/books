# Python3 循环

本章节将为大家介绍 Python 循环语句的使用。

Python 中的循环语句有`for`和`while`

## while 循环

Python 中`while`语句的一般形式：

```
while 判断条件(condition)：
    执行语句(statements)……
```

同样需要注意冒号和缩进。另外，在 Python 中没有do..while 循环。

#### 练习:使用`while`来计算 1 到 100 的总和
```Python
n = 100
 
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1
 
print("1 到 %d 之和为: %d" % (n,sum))
```


### 无限循环

无限循环也常被叫做死循环，我们可以通过设置条件表达式永远不为 false 来实现无限循环

#### 练习：无限循环

```Python
var = 1
while var == 1 :  # 表达式永远为 true
   num = int(input("输入一个数字  :"))
   print("你输入的数字是: ", num)
   if num == 99:#输入99跳出无限循环
      break
 
print("Good bye!")
```


你可以使用 **CTRL+C** 来退出当前的无限循环。

无限循环在服务器上客户端的实时请求非常有用。

### while 循环使用 else 语句

在`while … else`在条件语句为 false 时执行 else 的语句块。

语法格式如下：
```
while <expr>:
    <statement(s)>
else:
    <additional_statement(s)>
```
#### 练习:循环输出数字，并判断大小
```Python
count = 0
while count < 5:
   print(count, " 小于 5")
   count = count + 1
else:
   print(count, " 大于或等于 5")
```

### 简单语句组

类似`if`语句的语法，如果你的`while`循环体中只有一条语句，你可以将该语句与`while`写在同一行中

#### 练习：简单while语句循环

```Python
flag = 1
 
while (flag): print('I Love Python!')
 
print("Good bye!")
```
**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。


## for 循环

Python`for`循环可以遍历任何序列的项目，如一个列表或者一个字符串。

for循环的一般格式如下：

```
if 表达式1:
    语句
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
```

#### 练习:for 实例

```Python
languages = ["C", "C++", "Perl", "Python"] 
for x in languages: 
    print(x)
```

#### 练习:使用了 break 语句，break 语句用于跳出当前循环体：

```Python
sites = ["Baidu", "Google","Python","Taobao"]
for site in sites:
    if site == "Python":
        print("Python教程!")
        break
    print("循环数据 " + site)
else:
    print("没有循环数据!")
print("完成循环!")
```


## `break` 和 `continue` 语句及循环中的 `else `子句

`break` 语句可以跳出 for 和 while 的循环体。如果你从 for 或 while 循环中终止，任何对应的循环 else 块将不执行。

`continue`语句被用来告诉 Python 跳过当前循环块中的剩余语句，然后继续进行下一轮循环。

#### 练习:`while `中使用 `break`：
```Python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        break
    print(n)
print('循环结束。')
```


#### 练习:`while` 中使用`continue`

```Python
n = 5
while n > 0:
    n -= 1
    if n == 2:
        continue
    print(n)
print('循环结束。')
```


#### 练习:循环中使用`break`

```Python
for letter in 'Python':     # 第一个实例
   if letter == 'o':
      break
   print('当前字母为 :', letter)
  
var = 10                    # 第二个实例
while var > 0:              
   print('当期变量值为 :', var)
   var = var -1
   if var == 5:
      break
 
print("Good bye!")
```

#### 练习:以下实例循环字符串Python，碰到字母 o 跳过输出

```Python
for letter in 'Python':     # 第一个实例
   if letter == 'o':        # 字母为 o 时跳过输出
      continue
   print('当前字母 :', letter)
 
var = 10                    # 第二个实例
while var > 0:              
   var = var -1
   if var == 5:             # 变量为 5 时跳过输出
      continue
   print('当前变量值 :', var)
print("Good bye!")
```

循环语句可以有`else`子句，它在穷尽列表(以`for`循环)或条件变为 false (以`while`循环)导致循环终止时被执行，但循环被 `break `终止时不执行。


#### 练习:查询质数的循环

```Python
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, '等于', x, '*', n//x)
            break
    else:
        # 循环中没有找到元素
        print(n, ' 是质数')
```

## `pass`语句

`pass`是空语句，是为了保持程序结构的完整性。`pass` 不做任何事情，一般用做占位语句

#### 练习：空循环

```
while True:
    pass  # 等待键盘中断 (Ctrl+C)
```

#### 练习:最小的类

```Python
class MyEmptyClass:
    pass
    
MyEmptyClass
```

#### 练习:以下实例在字母为 o 时 执行 pass 语句块:


```Python
for letter in 'Python': 
   if letter == 'o':
      pass
      print('执行 pass 块')
   print('当前字母 :', letter)
 
print("Good bye!")
```

#### 练习:斐波纳契数列

```Python
# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a+b
```

其中代码 **a, b = b, a+b** 的计算方式为先计算右边表达式，然后同时赋值给左边，等价于：`n=b;m=a+b;a=n;b=m`

这个例子介绍了几个新特征。

第一行包含了一个复合赋值：变量`a`和`b`同时得到新值 0 和 1。最后一行再次使用了同样的方法，可以看到，右边的表达式会在赋值变动之前执行。右边表达式的执行顺序是从左往右的。

## `range()`函数

如果你需要遍历数字序列，可以使用内置`range()`函数。它会生成数列，例如:

#### 练习:使用`range()`产生数列 

```Python
for i in range(5):
    print(i)
```

#### 练习:`range()`指定区间的值：

```Python
for i in range(5,9) :
    print(i)
```

#### 练习:也可以使range以指定数字开始并指定不同的步长

```
for i in range(0, 10, 3) :
    print(i)
```

甚至可以是负数

```Python
for i in range(-10, -100, -30) :
    print(i)
```

#### 练习:结合`range()`和`len()`函数以遍历一个序列的索引

```Python
a = ['Google', 'Baidu', 'Python', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])
```

#### 练习:可以使用range()函数来创建一个列表

```Python
list(range(50)) 
```


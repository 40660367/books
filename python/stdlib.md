# Python3 标准库(stdlib)概览

## 操作系统接口

`os`模块提供了不少与操作系统相关联的函数。

```Python
import os
print(os.getcwd())      # 返回当前的工作目录
os.chdir('/')   # 修改当前的工作目录
print(os.getcwd())
print(os.system('ls'))   # 执行系统命令 ls
```

建议使用`import os` 风格而非`from os import *`。这样可以保证随操作系统不同而有所变化的 `os.open() `不会覆盖内置函数`open()`。

在使用`os`这样的大型模块时内置的`dir() `和`help() `函数非常有用:

```Python
import os
dir(os)#<returns a list of all module functions>
help(os)#<returns an extensive manual page created from the module's docstrings>
```

针对日常的文件和目录管理任务，`shutil`模块提供了一个易于使用的高级接口:

```Python
!touch data.db

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/', 'installdir')
```

## 文件通配符

`glob`模块提供了一个函数`glob()`用于从目录通配符搜索中生成文件列表:

```Python
import glob
glob.glob('*.py')
```

## 命令行参数

通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于`sys`模块的`argv`变量。

```Python
%%write demo.py
import sys
print(sys.argv)
```

```Python
#在命令行中执行
!python demo.py one two three
```


## 错误输出重定向和程序终止

`sys` 还有 `stdin`，`stdout` 和 `stderr` 属性，即使在 `stdout` 被重定向时，后者也可以用于显示警告和错误信息。
`sys.stderr.write('Warning, log file not found starting a new one\n')Warning, log file not found starting a new one`

大多脚本的定向终止都使用`sys.exit()`。

## 字符串正则匹配

re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:

```Python
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
```

如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:

```Python
'tea for too'.replace('too', 'two')
```

## 数学

`math`模块为浮点运算提供了对底层C函数库的访问:

```Python
import math
math.cos(math.pi / 4)
math.log(1024, 2)
```

`random`提供了生成随机数的工具。

```Python
import random
list1=['apple','pear','banana','orange']
print(random.choice(list1))
print(random.choice(list1))
print(random.choice(list1))


print(random.sample(range(100), 10))   # sampling without replacement
print(random.sample(range(100), 10))   # sampling without replacement
print(random.sample(range(100), 10))   # sampling without replacement


print(random.random())    # random float
print(random.random())    # random float
print(random.random())    # random float

print(random.randrange(10))    # random integer chosen from range(6)
print(random.randrange(10))    # random integer chosen from range(6)
print(random.randrange(10))    # random integer chosen from range(6)
```

## 访问互联网

有几个模块用于访问互联网以及处理网络通信协议。其中最简单的两个是用于处理从 urls 接收的数据的 `urllib.request` 以及用于发送电子邮件的 smtplib:

```Python
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
     line = line.decode('utf-8')  # Decoding the binary data to text.
     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
         print(line)

            import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org',
 """To: jcaesar@example.org
 From: soothsayer@example.org

 Beware the Ides of March.
 """)
server.quit()
```

注意第二个例子需要本地有一个在运行的邮件服务器。

## 日期和时间

`datetime`模块为日期和时间处理同时提供了简单和复杂的方法。

支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。

该模块还支持时区处理:

```Python
# dates are easily constructed and formatted
from datetime import date
now = date.today()
now
datetime.date(2020, 2, 2)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

# dates support calendar arithmetic
birthday = date(1990, 7, 4)
age = now - birthday
age.days
```

## 数据压缩

以下模块直接支持通用的数据打包和压缩格式：zlib，gzip，bz2，zipfile，以及 tarfile。

```Python
import zlib
s = b'witch which has which witches wrist watch'
len(s)
t = zlib.compress(s)
len(t)
zlib.decompress(t)
zlib.crc32(s)
```

## 性能度量

有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。Python 提供了一个度量工具，为这些问题提供了直接答案。

例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,timeit 证明了现代的方法更快一些。

```Python
from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()
Timer('a,b = b,a', 'a=1; b=2').timeit()
```

相对于 timeit 的细粒度，:mod:profile 和 pstats 模块提供了针对更大代码块的时间度量工具。

## 测试模块

开发高质量软件的方法之一是为每一个函数开发测试代码，并且在开发过程中经常进行测试

doctest模块提供了一个工具，扫描模块并根据程序中内嵌的文档字符串执行测试。

测试构造如同简单的将它的输出结果剪切并粘贴到文档字符串中。

通过用户提供的例子，它强化了文档，允许 doctest 模块确认代码的结果是否与文档一致:

```Python
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试
```

`unittest`模块不像 `doctest`模块那么容易使用，不过它可以在一个独立的文件里提供一个更全面的测试集:

```Python
import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests
```
# turtle 示例:各类不同的树

### 绘制树

文件名:t1.py

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-
from turtle import *

speed(0) # 将绘制速度设置为0，这是最快的
pencolor('red') #  将笔/线的颜色设置为红色
bgcolor('black') # 将背景/画布的颜色设置为黑色

x = 0 # 创建一个值为0的变量x
up() # 抬起笔，所以没有画线

#nota fd()表示向前移动，bk()表示向后移动
# rt() 或 lt()表示向右倾斜一定角度

rt(45)
fd(90)
rt(135)

down() # 放下笔，以便乌龟可以画画
# 当x的值小于120时
while x < 120:
    print(x)
    x = x+1 # adds 1 to the value of x,
exitonclick() # 当您单击时，乌龟退出。
```

```bash
python3 /share/lesson/turtle/t1.py
```
### 绘制树

文件名:t2.py

```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

from turtle import *

speed(0) # 将绘制速度设置为0，这是最快的
pencolor('red') #  将笔/线的颜色设置为红色
bgcolor('black') # 将背景/画布的颜色设置为黑色

x = 0 # 创建一个值为0的变量x
up() # 抬起笔，所以没有画线

#nota fd()表示向前移动，bk()表示向后移动
# rt() 或 lt()表示向右倾斜一定角度

rt(45)
fd(90)
rt(135)

down() # 放下笔，以便乌龟可以画画
# 当x的值小于120时，
while x < 120:
  fd(200)
  rt(61)
  fd(200)
  rt(61)
  fd(200)
  rt(61)
  fd(200)
  rt(61)
  fd(200)
  rt(61)
  fd(200)
  rt(61)
  rt(11.1111)
  x = x+1 # adds 1 to the value of x,

exitonclick() # 当您单击时，乌龟退出。
```

```bash
python3 /share/lesson/turtle/t2.py
```

康康

## 樱花树1

文件名:tree1.py

```python
from turtle import *
from random import *
from math import *
 
def tree(n, l):
    pd() # 下笔
    # 阴影效果
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 3)
    forward(l) # 画树枝
 
 
    if n > 0:
        b = random() * 15 + 10 # 右分支偏转角度
        c = random() * 15 + 10 # 左分支偏转角度
        d = l * (random() * 0.25 + 0.7) # 下一个分支的长度
        # 右转一定角度，画右分支
        right(b)
        tree(n - 1, d)
        # 左转一定角度，画左分支
        left(b + c)
        tree(n - 1, d)
 
        # 转回来
        right(c)
    else:
        # 画叶子
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n*0.8, n*0.8)
        circle(3)
        left(90)
 
        # 添加0.3倍的飘落叶子
        if(random() > 0.7):
            pu()
            # 飘落
            t = heading()
            an = -40 + random()*40
            setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            forward(dis)
            setheading(t)
 
 
            # 画叶子
            pd()
            right(90)
            n = cos(radians(heading() - 45)) / 4 + 0.5
            pencolor(n*0.5+0.5, 0.4+n*0.4, 0.4+n*0.4)
            circle(2)
            left(90)
            pu()
 
            #返回
            t = heading()
            setheading(an)
            backward(dis)
            setheading(t)
 
    pu()
    backward(l)# 退回
 
bgcolor(0.5, 0.5, 0.5) # 背景色
ht() # 隐藏turtle
speed(0) # 速度，1-10渐进，0最快
tracer(0, 0)
pu() # 抬笔
backward(100)
left(90) # 左转90度
pu() # 抬笔
backward(300) # 后退300
tree(12, 100) # 递归7层
done()
```

康康


```bash
python3 /share/lesson/turtle/tree1.py
```
## 樱花树2

文件名:tree2.py

```python
from turtle import *
from random import *
from math import *
 
def tree(n, l):
    pd()
    t = cos(radians(heading() + 45)) / 8 + 0.25
    pencolor(t, t, t)
    pensize(n / 4)
    forward(l)
    if n > 0:
        b = random() * 15 + 10
        c = random() * 15 + 10
        d = l * (random() * 0.35 + 0.6)
        right(b)
        tree(n - 1, d)
        left(b + c)
        tree(n - 1, d)
        right(c)
    else:
        right(90)
        n = cos(radians(heading() - 45)) / 4 + 0.5
        pencolor(n, n, n)
        circle(2)
        left(90)
    pu()
    backward(l)
 
bgcolor(0.5, 0.5, 0.5)
ht()
speed(0)
tracer(0, 0)
left(90)
pu()
backward(300)
tree(13, 100)
done()
```

```bash
python3 /share/lesson/turtle/tree2.py
```
康康

## 樱花树3

文件名:tree3.py

```python
from turtle import *
 
# 设置色彩模式是RGB:
colormode(255)
 
lt(90)
 
lv = 14
l = 120
s = 45
 
width(lv)
 
# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)
 
penup()
bk(l)
pendown()
fd(l)
 
def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()
 
    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)
 
    l = 3.0 / 4.0 * l
 
    lt(s)
    fd(l)
 
    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)
 
    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)
 
    # restore the previous pen width
    width(w)
 
speed("fastest")
 
draw_tree(l, 4)
 
done()
```

```bash
python3 /share/lesson/turtle/tree3.py
```

康康
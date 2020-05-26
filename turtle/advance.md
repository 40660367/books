# turtle 高级篇

到目前为止我们通过**turtle**库了解了**Python**的基本语法，包括顺序与循环、函数的调用与方法的定义、列表与简单的数学运算等；也学习了用**turtle**库绘图的基本用法，包括坐标与角度、落笔抬笔、颜色与填充等。

但是我们所绘的所有内容仅限于直线，对于曲线的绘制，一直没有涉及。从现在开始，我们就来了角一下用**turtle**库怎么画曲线，首先我们来画一个圆，看代码：

文件名:circle1.py

```python
import turtle as t 
t.circle(100)        # 画一个半径为100的圆
t.mainloop()         # 等效于t.done()
```

```bash
python3 /share/lesson/turtle/circle1.py
```

康康

我们可以看到，**turtle**从坐标原点开始，按逆时针方向画出了一个圆。非常简单，一条语句就实现了。



第一个问题是，如果有希望**turtle**按顺时针方向画，应该怎样实现？嗯，将t.circle(100)中的参数100改为-100即可，也就是t.circle(-100)。也就是说明这个参数除了表示圆的半径面，其正负性还定义了画圆的方向。修改一下上面的代码：

文件名:circle2.py

```python
import turtle as t 
t.circle(100)        # 从原点开始按逆时针方向画圆，直径为100
t.circle(-100)       # 从鼠标所在点开始按顺时针方向画圆，直径为100
t.mainloop() 
```

```bash
python3 /share/lesson/turtle/circle2.py
```

康康

运行这段代码，可以看到**turtle**在界面上画出一个8字形，先逆时针方向画圆，再顺时针方向画圆。可以看到**turtle**画这两个圆中的第一个时，相当于从圆的下底开始画（也即圆的-90度位置）；画第二个圆相当于从上顶位置开始画（也即90度的位置）。





那么，第二个问题来了，如果我希望从圆的0度位置开始画，或者180度位置开始画，应该怎么操作？修改一下上面的实例代码：

文件名:circle3.py

```python
import turtle as t
t.setheading(90)    # 设置turtle的方向为正北（向上）方向
t.circle(100)       # 逆时针画
t.circle(-100)      # 顺时针画
t.mainloop()
```

```bash
python3 /share/lesson/turtle/circle3.py
```

康康

可以看到，第一个圆是从0度位置开始画的，而第二个圆是从180度位置开始画的。通过这个小改动，我们可以看到，**turtle**画圆时，没有明确的“圆心”概念，而是以“**初始方向+半径**”来决定一个圆的位置和大小。其核心原理等同于割圆术。



接下来，我们来看一下怎样画一段弧线，而不是完整的圆。t.circle()的第一个参数是半径，第二个参数就是圆弧的角度，默认是360度。修改一下上面的例子：

文件名:circle4.py

```python
import turtle as t
t.setheading(90)
t.circle(100, 120)   # 画一段120度的弧线
t.penup()            # 抬起笔来
t.goto(0, 0)         # 回到圆点位置
t.setheading(90)     # 向上画
t.pendown()          # 落笔，开始画
t.circle(-100, 120)  # 画一段120度的弧线
t.mainloop()
```

```bash
python3 /share/lesson/turtle/circle4.py
```

康康

可以看到**turtle**在界面上向左和向右各画了两段弧，即120度长度的弧线。中间增加的抬笔、回圆点、设置初始方向、落笔，主要是为了重新初始化绘图的前提条件，以便于跟前面的例子做对比。



由此可见，**turtle**画曲线的方法还是比较简陋的，需要配合其它的方向、坐标、位移等来一起实现。接下来，我们来画一个稍微复杂一点，但是非常有趣的小蛇，看代码：

文件

```python
import turtle as t
t.penup()
t.goto(-150, 0)        # 到起始点
t.pensize(25)          # 设置画笔粗细
t.pencolor('green')    # 设置画笔颜色
t.setheading(45)       # 向45度方向画
t.pendown()
t.circle(-50, 90)      # 顺时针方向画90度的弧线
t.circle(50, 90)       # 继续按逆时针方向画弧
t.circle(-50, 90)
t.circle(50, 45)
t.setheading(0)        # 继续向0度方向画
t.forward(50)
t.circle(10, 160)      # 继续画一个160度的小弧
t.setheading(160)      # 面向小弧的最后角度
t.forward(8)           # 再向前伸一点
t.mainloop()
```

```bash
python3 /share/lesson/turtle/snake.py
```

康康

可以看到，**turtle**在界面上画出了一条弯弯曲曲的小绿蛇。通过编程，可以清晰的展现出用**turtle**库画弧线，就是**要配合方向、坐标、位移**等来一起实现。



接下来，我们再配合上初级篇中的函数定义，来画一只小狮子

文件名:l

```python
import turtle as t

def hair():    # 画头发
    t.penup()
    t.goto(-50, 150)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    for j in range(10):                   # 重复执行10次
        t.setheading(60 - (j * 36))       # 每次调整初始角度
        t.circle(-50, 120)                # 画120度的弧
    t.end_fill()

def face():    # 画脸
    t.penup()
    t.goto(0, 100)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.setheading(180)
    t.circle(85)
    t.end_fill()
    #下巴
    t.circle(85, 120)
    t.fillcolor('white')
    t.begin_fill()
    t.circle(85, 120)
    t.setheading(135)
    t.circle(100, 95)
    t.end_fill()
    
def ears(dir):    # 画眼睛，dir用来设置方向，左右眼对称
    t.penup()
    t.goto((0-dir)*30, 90)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#f2ae20')
    t.begin_fill()
    t.circle(dir*30)
    t.end_fill()
    
    t.penup()
    t.goto((0-dir)*40, 85)
    t.setheading(90)
    t.pendown()
    t.fillcolor('white')
    t.begin_fill()
    t.circle(dir*17)
    t.end_fill()
    
def nose():    # 画鼻子
    t.penup()
    t.goto(20, 0)
    t.setheading(90)
    t.pendown()
    t.fillcolor('#a2774d')
    t.begin_fill()
    t.circle(20)
    t.end_fill()
    
def eye(dir):    # 画耳朵，dir用来设置方向，左右耳对称
    t.penup()
    t.goto((0-dir)*30, 20)
    t.setheading(0)
    t.pendown()
    t.fillcolor('black')
    t.begin_fill()
    t.circle(10)
    t.end_fill()

def mouth():    # 画嘴巴
    t.penup()
    t.goto(0, 0)
    t.setheading(-90)
    t.pendown()
    t.forward(50)
    t.setheading(0)
    t.circle(80, 30)
    t.penup()
    t.goto(0, -50)
    t.setheading(180)
    t.pendown()
    t.circle(-80, 30)   
    
hair()
ears(1)
ears(-1)
face()
eye(1)
eye(-1)
mouth()
nose()
t.done()
```

```bash
python3 /share/lesson/turtle/lion.py
```

康康

可以看到**turtle**在界面上画出一个小狮子的头像。综合运用方向、坐标、位移，加上一点耐心和对坐标位置的调试，用**turtle**的确可以画出任何你想像的图形。



入门篇中有个小彩蛋，也就是可以修改**Python**的**turtle**指针外形。默认的指针就是一个小箭头，我们可以通过t.shape('**turtle**')，将这个小箭头改成一只真正的小乌龟，增加编程的趣味性。

但是，我们还可以进一步，来设定自己的指针外形，将指针改成我们希望的任何样式，这一过程主要通过以下几个方法的组合来实现：

```python
t.begin_poly()                    # 开始绘制
# 绘制指针过程省略
t.end_poly()                      # 结束绘制      
poly = t.get_poly()               # 获取绘制
t.register_shape('name', ploy)    # 注册一个名为'name'的shape
newPoint = t.Pen()                # 初始化一只新turtle
newPoint.shape('name')            # 让这只turtle使用名为'name'的shape
```

可见，重点是**turtle**库中提供了一个t.register_shape()方法，以供我们注册自己的shape，有了这个方法，在特定的条件下，就可以极大的方便我们的程序设计。通过初始化出多只新**turtle**，可以同时在一个界面上以不同的shape绘图。下面给出一段绘制实时时钟的代码，重点部分我已给出注释。

文件名:clocks.py

```python
#-*- coding:utf-8 –*-
#以自定义shape的方式实现
#当然，使用多只turtle来完全重绘的方法实现，也没有问题。
#如果需要重绘方法的代码，请加公众号：see_goal 留言“turtle时钟”
import turtle as t
import datetime as d

def skip(step):            # 抬笔，跳到一个地方
    t.penup()
    t.forward(step)
    t.pendown()


def drawClock(radius):     # 画表盘
    t.speed(0)
    t.mode("logo")         # 以Logo坐标、角度方式
    t.hideturtle()
    t.pensize(7)
    t.home()               # 回到圆点
    for j in range(60):
        skip(radius)
        if (j % 5 == 0):
            t.forward(20)
            skip(-radius-20)
        else:
            t.dot(5)
            skip(-radius)
        t.right(6)
    
def makePoint(pointName, len):            # 钟的指针，时针、分针、秒针
    t.penup()
    t.home()
    t.begin_poly()
    t.back(0.1*len)
    t.forward(len*1.1)
    t.end_poly()
    poly = t.get_poly()
    t.register_shape(pointName, poly)    # 注册为一个shape

def drawPoint():                         # 画指针
    global hourPoint, minPoint, secPoint, fontWriter
    makePoint("hourPoint", 100)
    makePoint("minPoint", 120)
    makePoint("secPoint", 140)
    
    hourPoint = t.Pen()                  # 每个指针是一只新turtle
    hourPoint.shape("hourPoint")
    hourPoint.shapesize(1, 1, 6)
    
    minPoint = t.Pen()
    minPoint.shape("minPoint")
    minPoint.shapesize(1, 1, 4)
    
    secPoint = t.Pen()
    secPoint.shape("secPoint")
    secPoint.pencolor('red')
    
    fontWriter = t.Pen()
    fontWriter.pencolor('gray')
    fontWriter.hideturtle()

def getWeekName(weekday):
    weekName = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日']
    return weekName[weekday]

def getDate(year, month, day):
    return "%s-%s-%s" % (year, month, day)

def realTime():
    curr = d.datetime.now()
    curr_year = curr.year
    curr_month = curr.month
    curr_day = curr.day
    curr_hour = curr.hour
    curr_minute = curr.minute
    curr_second = curr.second
    curr_weekday = curr.weekday()
    
    t.tracer(False)
    secPoint.setheading(360/60*curr_second)
    minPoint.setheading(360/60*curr_minute)
    hourPoint.setheading(360/12*curr_hour + 30/60*curr_minute)
    
    fontWriter.clear()
    fontWriter.home()
    fontWriter.penup()
    fontWriter.forward(80)
    # 用turtle写文字
    fontWriter.write(getWeekName(curr_weekday), align="center", font=("Courier", 14, "bold"))
    fontWriter.forward(-160)
    fontWriter.write(getDate(curr_year, curr_month, curr_day), align="center", font=("Courier", 14, "bold"))
    
    t.tracer(True)
    print(curr_second)
    t.ontimer(realTime, 100)    # 每隔100毫秒调用一次realTime()

def main():  
    t.tracer(False)
    drawClock(160)
    drawPoint()
    realTime()
    t.tracer(True)
    t.mainloop()
    
if __name__ == '__main__':
    main()
```

```bash
python3 /share/lesson/turtle/clocks.py
```

康康

运行这个例子，可以看到**turtle**在界面上实时展示出一个时钟。我们重新编写过的这段代码还是比较简洁，之前没有介绍到的就是用**turtle**怎么输出文字，详细可以看例子中的write()方法。
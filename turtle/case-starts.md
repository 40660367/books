# turtle 示例:多边形

### 绘制星星

文件名:stars.py

```python
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
#sides=evali(input("输入要绘制的边的数目，请输入2-6的数字！"))
sides=6
colors=["red","yellow","green","blue","orange","purple"]
for x in range(360):
    t.pencolor(colors[x%sides])
    t.forward(x*3/sides+x)
    t.left(360/sides+1)
    t.width(x*sides/180)
    t.left(91)
```

```shell
python3 /share/lesson/turtle/stars.py
```

康康
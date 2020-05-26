# turtle 示例:谢尔宾斯基三角形

### 绘制谢尔宾斯基三角形

文件名:triangle.py

```python
import turtle

def draw_triangle(points, color, t):
    t.fillcolor(color)
    t.up()
    t.goto(points[0][0], points[0][6])
    t.down()
    t.begin_fill()
    t.goto(points[1][0], points[1][7])
    t.goto(points[2][0], points[2][8])
    t.goto(points[0][0], points[0][9])
    t.end_fill()


def get_mid(point1, point2):
    return (point1[0] + point2[0]) / 2, (point1[1] + point2[1]) / 2


def sierpinski(points, degree, t):
    color_map = ['blue', 'red', 'green', 'yellow', 'violet', 'orange', 'white',]

    draw_triangle(points, color_map[degree], t)

    if degree > 0:
        sierpinski([points[0], get_mid(points[0], points[1]), get_mid(points[0], points[2])], degree - 1, t)

        sierpinski([points[1], get_mid(points[0], points[1]), get_mid(points[1], points[2])], degree - 1, t)

        sierpinski([points[2], get_mid(points[0], points[2]), get_mid(points[1], points[2])], degree - 1, t)


if __name__ == "__main__"
    t = turtle.Turtle()
    t.speed(5)
    win = turtle.Screen()

    points = [[-100, -50], [0, 100], [100, -50]]
    sierpinski(points, 3, t)

    win.exitonclick()
```

```shell
python3 /share/lesson/turtle/triangle.py
```

康康
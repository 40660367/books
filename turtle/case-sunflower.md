# turtle 示例:太阳花

### 绘制太阳花

文件名:sunflower.py

```python
import turtle as t
import time
t.color("red", "yellow")
t.speed(10)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
end_fill()
time.sleep(1)
```

```shell
python3 /share/lesson/turtle/sunflower.py
```

康康


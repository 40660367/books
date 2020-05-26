```bash
#安装chord库
pip install chord -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install numpy -i https://pypi.tuna.tsinghua.edu.cn/simple/
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple/
```
```python
import numpy as np
import pandas as pd
import itertools
from chord import Chord

#
data=pd.read_csv('/share/datasets/chord-citysample.txt')
print(data)

data = list(itertools.chain.from_iterable((i, i[::-1]) for i in data.values))
matrix = pd.pivot_table(
    pd.DataFrame(data), index=0, columns=1, aggfunc="size", fill_value=0
).values.tolist()

print(pd.DataFrame(matrix))

#生成out.html
Chord(matrix, 'a', colors="d3.schemeSet2").to_html()
```

```bash
#
python /share/lesson/turtle/chord.py
ls
```


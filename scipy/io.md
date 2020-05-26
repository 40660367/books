# Scipy 输入和输出(io)

Scipy.io包提供了多种功能来解决不同格式的文件(输入和输出)。 其中一些格式

- Matlab
- IDL
- Matrix Market
- Wave
- Arff
- Netcdf等

这里讨论最常用的文件格式 -

**MATLAB**

以下是用于加载和保存`.mat`文件的函数。

| 编号 | 函数      | 描述                   |
| ---- | --------- | ---------------------- |
| 1    | `loadmat` | 加载一个MATLAB文件     |
| 2    | `savemat` | 保存为一个MATLAB文件   |
| 3    | `whosmat` | 列出MATLAB文件中的变量 |

让我们来看看下面的例子。

```python
import scipy.io as sio
import numpy as np

#Save a mat file
vect = np.arange(10)
sio.savemat('array.mat', {'vect':vect})

#Now Load the File
mat_file_content = sio.loadmat('array.mat')
print(mat_file_content)
```

可以看到数组以及元信息。 如果想在不读取数据到内存的情况下检查MATLAB文件的内容，请使用如下所示的`whosmat`命令。

```python
import scipy.io as sio
mat_file_content = sio.whosmat(‘array.mat’)
print(mat_file_content)
```


<code class=gatsby-kernelname data-language=python></code>

# Scipy 快速傅立叶变换(FFTpack)

对时域信号计算傅里叶变换以检查其在频域中的行为。 傅里叶变换可用于信号和噪声处理，图像处理，音频信号处理等领域。SciPy提供`fftpack`模块，可让用户计算快速傅立叶变换。

以下是一个正弦函数的例子，它将用于使用`fftpack`模块计算傅里叶变换。

## 快速傅立叶变换

下面来了解一下快速傅立叶变换的细节。

**一维离散傅立叶变换**

长度为`N`的序列`x [n]`的`FFT y [k]`由`fft()`计算，逆变换使用`ifft()`计算。 看看下面的例子

```python
import numpy as np

#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
print(y)
```

再看另一个示例 - 

```python
import numpy as np

#Importing the fft and inverse fft functions from fftpackage
from scipy.fftpack import fft
from scipy.fftpack import ifft

#create an array with random n numbers
x = np.array([1.0, 2.0, 1.0, -1.0, 1.5])

#Applying the fft function
y = fft(x)
#FFT is already in the workspace, using the same workspace to for inverse transform

yinv = ifft(y)

print(yinv)
```

`scipy.fftpack`模块允许计算快速傅立叶变换。 作为一个例子，一个(嘈杂的)输入信号可能看起来如下 ,我们正以`0.02`秒的时间步长创建一个信号。 最后一条语句显示信号`sig`的大小。 

```python
import numpy as np
time_step = 0.02
period = 5.
time_vec = np.arange(0, 20, time_step)
sig = np.sin(2 * np.pi / period * time_vec) + 0.5 *np.random.randn(time_vec.size)
print(sig.size)
```



我们不知道信号频率; 只知道信号`sig`的采样时间步长。 信号应该来自实际函数，所以傅里叶变换将是对称的。 `scipy.fftpack.fftfreq()`函数将生成采样频率，`scipy.fftpack.fft()`将计算快速傅里叶变换。

下面通过一个例子来理解这一点。

```python
from scipy import fftpack
sample_freq = fftpack.fftfreq(sig.size, d = time_step)
sig_fft = fftpack.fft(sig)
print(sig_fft)
```

## 离散余弦变换

离散余弦变换(DCT)根据以不同频率振荡的余弦函数的和表示有限数据点序列。 SciPy提供了一个带有函数`idct`的DCT和一个带有函数`idct`的相应IDCT。看看下面的一个例子。

```python
from scipy.fftpack import dct
mydict = dct(np.array([4., 3., 5., 10., 5., 3.]))
print(mydict)
```

逆离散余弦变换从其离散余弦变换(DCT)系数重建序列。 `idct`函数是`dct`函数的反函数。 可通过下面的例子来理解这一点。

```python
from scipy.fftpack import dct
from scipy.fftpack import idct
d = idct(np.array([4., 3., 5., 10., 5., 3.]))
print(d)
```
<code class=gatsby-kernelname data-language=python></code>

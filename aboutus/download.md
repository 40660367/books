# 常用软件下载

#### Anaconda

Anaconda官方站下载 ：https://www.anaconda.com/distribution/  
Anaconda国内镜像：[清华镜像站](<https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/>)    

#### PIP 国内镜像： [清华镜像](<https://mirrors.tuna.tsinghua.edu.cn/help/pypi/>)

- 临时使用

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
```

注意，`simple` 不能少, 是 `https` 而不是 `http`

- 设为默认
  升级 pip 到最新的版本 (>=10.0.0) 后进行配置：

```
pip install pip -U
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

如果您到 pip 默认源的网络连接较差，临时使用本镜像站来升级 pip：

```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -U
```

### 参考文档 

#### 小抄

- [Pandas1](res/Pandas-1.jpg) [Pandas2](res/Pandas-2.jpg) [Pandas3](res/Pandas-3.jpg)
- [Numpy](res/Numpy.png)
- [Matplotlib](res/Matplotlib.png)
- [ScikitLearn](res/ScikitLearn.png)
- [Scipy](res/Scipy.png)
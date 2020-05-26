# SciPy 简介

SciPy，发音为`Sigh Pi`，是一个科学的python开源代码，在BSD许可下分发的库，用于执行数学，科学和工程计算。

![logo](./images/logo.png)

SciPy库依赖于NumPy，它提供了便捷且快速的`N`维数组操作。 SciPy库的构建与NumPy数组一起工作，并提供了许多用户友好和高效的数字实践，例如:数值积分和优化的例程。 它们一起运行在所有流行的操作系统上，安装快速且免费。 NumPy和SciPy易于使用，但强大到足以依靠世界上一些顶尖的科学家和工程师。

## SciPy子包

SciPy被组织成覆盖不同科学计算领域的子包。 这些总结在下表中 -

| 子包                                                         |                    |
| ------------------------------------------------------------ | ------------------ |
| [scipy.cluster](https://docs.scipy.org/doc/scipy/reference/cluster.html#module-scipy.cluster) | 矢量量化/Kmeans    |
| [scipy.constants](https://docs.scipy.org/doc/scipy/reference/constants.html#module-scipy.constants) | 物理和数学常数     |
| [scipy.fftpack](https://docs.scipy.org/doc/scipy/reference/fftpack.html#module-scipy.fftpack) | 傅里叶变换         |
| [scipy.integrate](https://docs.scipy.org/doc/scipy/reference/integrate.html#module-scipy.integrate) | 集成例程           |
| [scipy.interpolate](https://docs.scipy.org/doc/scipy/reference/interpolate.html#module-scipy.interpolate) | 插值               |
| [scipy.io](https://docs.scipy.org/doc/scipy/reference/io.html#module-scipy.io) | 数据输入和输出     |
| [scipy.linalg](https://docs.scipy.org/doc/scipy/reference/linalg.html#module-scipy.linalg) | 线性代数例程       |
| [scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html#module-scipy.ndimage) | n维图像包          |
| [scipy.odr](https://docs.scipy.org/doc/scipy/reference/odr.html#module-scipy.odr) | 正交距离回归       |
| [scipy.optimize](https://docs.scipy.org/doc/scipy/reference/optimize.html#module-scipy.optimize) | 优化               |
| [scipy.signal](https://docs.scipy.org/doc/scipy/reference/signal.html#module-scipy.signal) | 信号处理           |
| [scipy.sparse](https://docs.scipy.org/doc/scipy/reference/sparse.html#module-scipy.sparse) | 稀疏矩阵           |
| [scipy.spatial](https://docs.scipy.org/doc/scipy/reference/spatial.html#module-scipy.spatial) | 空间数据结构和算法 |
| [scipy.special](https://docs.scipy.org/doc/scipy/reference/special.html#module-scipy.special) | 任何特殊的数学函数 |
| [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html#module-scipy.stats) | 统计               |

## 数据结构

SciPy使用的基本数据结构是由NumPy模块提供的多维数组。 NumPy为线性代数，傅立叶变换和随机数生成提供了一些功能，但与SciPy中等效函数的一般性不同。
<code class=gatsby-kernelname data-language=python></code>

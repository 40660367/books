# Scipy 空间(spatial)

`scipy.spatial`包可以通过利用Qhull库来计算一组点的三角剖分，Voronoi图和凸壳。 此外，它包含用于最近邻点查询的KDTree实现以及用于各种度量中的距离计算的实用程序。

## Delaunay三角

下面来了解Delaunay Triangulations是什么以及如何在SciPy中使用。

**什么是Delaunay三角？**

在数学和计算几何中，对于平面中离散点的给定集合P的Delaunay三角剖分是三角形DT(P)，使得P中的任何点都不在DT(P)中的任何三角形的外接圆内。

可以通过SciPy进行相同的计算。 参考下面的一个例子。

```python
%matplotlib inline
import numpy as np
from scipy.spatial import Delaunay
points = np.array([[0, 4], [2, 1.1], [1, 3], [1, 2]])
tri = Delaunay(points)
import matplotlib.pyplot as plt
plt.triplot(points[:,0], points[:,1], tri.simplices.copy())
plt.plot(points[:,0], points[:,1], 'o')
plt.show()
```

## 共面点

下面了解共面点是什么以及它们如何在SciPy中使用。

**什么是共面点？**

共平面点是三个或更多点位于同一平面上。 回想一下，一个平面是平坦的表面，其在所有方向端延伸没有终点。 它通常在数学教科书中显示为**四面体**。

下面来看看如何在SciPy中使用它，参考下面的例子。

```python
from scipy.spatial import Delaunay
points = np.array([[0, 0], [0, 1], [1, 0], [1, 1], [1, 1]])
tri = Delaunay(points)
print(tri.coplanar)
```

这意味着顶点`4`位于三角形顶点`0`和顶点`3`附近，但不包含在三角中。

## 凸壳

下面来了解什么是凸壳，以及它们如何在SciPy中使用。

**什么是凸壳？**

在数学中，欧几里德平面或欧几里德空间(或更一般地说，在实数上的仿射空间中)中的一组点`X`的凸包或凸包是包含`X`的最小凸集。

参考下面的例子来详细了解它 - 

```python
%matplotlib inline
from scipy.spatial import ConvexHull
points = np.random.rand(10, 2) # 30 random points in 2-D
hull = ConvexHull(points)
import matplotlib.pyplot as plt
plt.plot(points[:,0], points[:,1], 'o')
for simplex in hull.simplices:
   plt.plot(points[simplex,0], points[simplex,1], 'k-')
plt.show()
```

<code class=gatsby-kernelname data-language=python></code>
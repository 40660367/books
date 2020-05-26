# Scipy 常量

SciPy常量(`constant`)包提供了广泛的常量，用于一般科学领域。

## SciPy常量包

`scipy.constants`包提供了各种常量。必须导入所需的常量并根据需要来使用它们。下面看看这些常量变量是如何导入和使用的。

首先，通过下面的例子来比较`'pi'`值。

```python
#Import pi constant from both the packages
from scipy import constants
import math


print("scipy - pi = %.16f"%constants.pi)
print("math - pi = %.16f"%math.pi)
```

## 可用的常量列表

下表简要介绍了各种常数(常量)。

**数学常量**

| 编号 | 常量     | 描述     |
| ---- | -------- | -------- |
| 1    | `pi`     | PI值     |
| 2    | `golden` | 黄金比例 |

**物理常量**

下表列出了最常用的物理常量。

| 编号 | 常量                      | 描述           |
| ---- | ------------------------- | -------------- |
| 1    | `c`                       | 真空中的光速   |
| 2    | `speed_of_light`          | 真空中的光速   |
| 3    | `h`                       | 普朗克常数     |
| 4    | `Planck`                  | 普朗克常数`h`  |
| 5    | `G`                       | 牛顿的引力常数 |
| 6    | `e`                       | 基本电荷       |
| 7    | `R`                       | 摩尔气体常数   |
| 8    | `Avogadro`                | 阿伏加德罗常数 |
| 9    | `k`                       | 波尔兹曼常数   |
| 10   | `electron_mass`或者 `m_e` | 电子质量       |
| 11   | `proton_mass`或者`m_p`    | 质子质量       |
| 12   | `neutron_mass`或`m_n`     | 中子质量       |

**单位**

下表列出了SI单位。

| 编号 | 单位    | 值    |
| ---- | ------- | ----- |
| 1    | `milli` | 0.001 |
| 2    | `micro` | 1e-06 |
| 3    | `kilo`  | 1000  |

这些单位范围从`yotta`，`zetta`，`exa`，`peta`，`tera ...... kilo`，`hector`，`... nano`，`pico`，`...`到`zepto`。

**其他重要常量**

下表列出了SciPy中使用的其他重要常量。

| 编号 | 单位                | 值                        |
| ---- | ------------------- | ------------------------- |
| 1    | `gram`              | 0.001 kg                  |
| 2    | `atomic_mass`       | 原子质量常数              |
| 3    | `degree`            | 弧度                      |
| 4    | `minute`            | 一分钟秒数(60)            |
| 5    | `day`               | 一天的秒数                |
| 6    | `inch`              | 一米的英寸数              |
| 7    | `micron`            | 一米的微米数              |
| 8    | `light_year`        | 一光年的米数              |
| 9    | `atm`               | 帕斯卡标准大气压          |
| 10   | `acre`              | 一平方米的英亩数          |
| 11   | `liter`             | 一立方米的升数            |
| 12   | `gallon`            | 一立方米的加仑数          |
| 13   | `kmh`               | 公里每小时，以米/秒为单位 |
| 14   | `degree_fahrenheit` | 一凯尔文的华氏数          |
| 15   | `eV`                | 一焦耳的电子伏特数        |
| 16   | `hp`                | 一瓦特的马力数            |
| 17   | `dyn`               | 一牛顿的达因数            |
| 18   | `lambda2nu`         | 将波长转换为光频率        |

要记住所有这些都有点困难。可使用`scipy.constants.find()`方法获取指定键的简单方法。 看看下面的例子。

```python
import scipy.constants
res = scipy.constants.physical_constants["alpha particle mass"]
print(res)
```
<code class=gatsby-kernelname data-language=python></code>

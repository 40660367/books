# R语言 分布函数(distribution function)

## 正态分布

在来自独立源的数据的随机集合中，通常观察到数据的分布是正常的。 这意味着，在绘制水平轴上的变量值和垂直轴上的值的计数的图形时，我们得到钟形曲线。 曲线的中心表示数据集的平均值。 

在图中，50％的值位于平均值的左侧，另外50％位于图表的右侧。 这在统计学中被称为正态分布。

R语言有四个内置函数来产生正态分布。 它们描述如下。

`dnorm(x, mean, sd)`,`pnorm(x, mean, sd)`,`qnorm(p, mean, sd)`,`rnorm(n, mean, sd)`

以下是在上述功能中使用的参数的描述 - 

- **x**是数字的向量。
- **p**是概率的向量。
- **n**是观察的数量（样本大小）。
- **mean**是样本数据的平均值。 它的默认值为零。
- **sd**是标准偏差。 它的默认值为1。

### `dnorm()`

该函数给出给定平均值和标准偏差在每个点的概率分布的高度。

```R
# Create a sequence of numbers between -10 and 10 incrementing by 0.1.
x <- seq(-10, 10, by = .1)

# Choose the mean as 2.5 and standard deviation as 0.5.
y <- dnorm(x, mean = 2.5, sd = 0.5)

# Plot the graph.
plot(x,y)
```


### `pnorm()`

该函数给出正态分布随机数的概率小于给定数的值。 它也被称为“累积分布函数”。

```R
# Create a sequence of numbers between -10 and 10 incrementing by 0.2.
x <- seq(-10,10,by = .2)
 
# Choose the mean as 2.5 and standard deviation as 2. 
y <- pnorm(x, mean = 2.5, sd = 2)

# Plot the graph.
plot(x,y)
```

### `qnorm()`

该函数采用概率值，并给出累积值与概率值匹配的数字。

```R
# Create a sequence of probability values incrementing by 0.02.
x <- seq(0, 1, by = 0.02)

# Choose the mean as 2 and standard deviation as 3.
y <- qnorm(x, mean = 2, sd = 1)

# Plot the graph.
plot(x,y)
```

### `rnorm（）`

此函数用于生成分布正常的随机数。 它将样本大小作为输入，并生成许多随机数。 我们绘制一个直方图来显示生成的数字的分布。

```R
# Create a sample of 50 numbers which are normally distributed.
y <- rnorm(50)

# Plot the histogram for this sample.
hist(y, main = "Normal DIstribution")
```


## 二项分布

二项分布模型处理在一系列实验中仅发现两个可能结果的事件的成功概率。 例如，掷硬币总是给出头或尾。 在二项分布期间估计在10次重复抛掷硬币中精确找到3个头的概率。

R语言有四个内置函数来生成二项分布。 它们描述如下。

`dbinom(x, size, prob),pbinom(x, size, prob),qbinom(p, size, prob),rbinom(n, size, prob)
`

以下是所使用的参数的描述 - 

- **x**是数字的向量。
- **p**是概率向量。
- **n**是观察的数量。
- **size**是试验的数量。
- **prob**是每个试验成功的概率。

### `dbinom()`

该函数给出每个点的概率密度分布。

```R
# Create a sample of 50 numbers which are incremented by 1.
x <- seq(0,50,by = 1)

# Create the binomial distribution.
y <- dbinom(x,50,0.5)

# Plot the graph for this sample.
plot(x,y)
```

### `pbinom()`

此函数给出事件的累积概率。 它是表示概率的单个值。

```R
# Probability of getting 26 or less heads from a 51 tosses of a coin.
x <- pbinom(26,51,0.5)

print(x)
```


### `qbinom()`

该函数采用概率值，并给出累积值与概率值匹配的数字。

```R
# How many heads will have a probability of 0.25 will come out when a coin is tossed 51 times.
x <- qbinom(0.25,51,1/2)

print(x)
```


### `rbinom()`

该函数从给定样本产生给定概率的所需数量的随机值。

```R
# Find 8 random values from a sample of 150 with probability of 0.4.
x <- rbinom(8,150,.4)

print(x)
```
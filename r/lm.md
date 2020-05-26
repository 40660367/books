# R语言 线性回归模型(liner model)

回归分析是一种非常广泛使用的统计工具，用于建立两个变量之间的关系模型。 这些变量之一称为预测变量，其值通过实验收集。 另一个变量称为响应变量，其值从预测变量派生。

在线性回归中，这两个变量通过方程相关，其中这两个变量的指数（幂）为1.数学上，线性关系表示当绘制为曲线图时的直线。 任何变量的指数不等于1的非线性关系将创建一条曲线。

线性回归的一般数学方程为：
$$
y = ax + b
$$

以下是所使用的参数的描述 - 

- $y$是响应变量。
- $x$是预测变量。
- $a$和 $b$ 称为系数常数。

## 建立回归的步骤

回归的简单例子是当人的身高已知时预测人的体重。 为了做到这一点，我们需要有一个人的身高和体重之间的关系。

创建关系的步骤是:

- 进行收集高度和相应重量的观测值的样本的实验。
- 使用R语言中的`lm()`函数创建关系模型。
- 从创建的模型中找到系数，并使用这些创建数学方程
- 获得关系模型的摘要以了解预测中的平均误差。 也称为残差。
- 为了预测新人的体重，使用R中的`predict()`函数。

### 数据说明

```
# Values of height
151, 174, 138, 186, 128, 136, 179, 163, 152, 131

# Values of weight.
63, 81, 56, 91, 47, 57, 76, 72, 62, 48
```

## `lm()`函数

此函数创建预测变量和响应变量之间的关系模型。

### 语法

线性回归中`lm()`函数的基本语法是:`lm(formula,data)`

以下是所使用的参数的说明 -

- 公式是表示$x$和$y$之间的关系的符号。
- 数据是应用公式的向量。

#### 练习:线性回归

创建关系模型并获取系数

```R
x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

# Apply the lm() function.
relation <- lm(y~x)

print(relation)
```
获取相关的摘要

```R
x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

# Apply the lm() function.
relation <- lm(y~x)

print(summary(relation))
```

## `predict()`函数

### 语法

线性回归中的predict（）的基本语法: `predict(object, newdata)`

以下是所使用的参数的描述 - 

- **object**是已使用**lm()**函数创建的公式。
- **newdata**是包含预测变量的新值的向量。

### 预测新人的体重

```R
# The predictor vector.
x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)

# The resposne vector.
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)

# Apply the lm() function.
relation <- lm(y~x)

# Find weight of a person with height 170.
a <- data.frame(x = 170)
result <-  predict(relation,a)
print(result)
```
### 以图形方式可视化回归
```R
# Create the predictor and response variable.
x <- c(151, 174, 138, 186, 128, 136, 179, 163, 152, 131)
y <- c(63, 81, 56, 91, 47, 57, 76, 72, 62, 48)
relation <- lm(y~x)


# Plot the chart.
plot(y,x,col = "blue",main = "Height & Weight Regression",
abline(lm(x~y)),cex = 1.3,pch = 16,xlab = "Weight in Kg",ylab = "Height in cm")
```

## 多重回归

多元回归是线性回归到两个以上变量之间的关系的延伸。 在简单线性关系中，我们有一个预测变量和一个响应变量，但在多元回归中，我们有多个预测变量和一个响应变量。

多元回归的一般数学方程为 -

$$
y = a + b1x1 + b2x2 +...bnxn
$$

以下是所使用的参数的描述 - 

- $y$是响应变量。
- $a，b1，b2 ... bn$是系数。
- $x1，x2，... xn$是预测变量。

我们使用R语言中的`lm()`函数创建回归模型。模型使用输入数据确定系数的值。 接下来，我们可以使用这些系数来预测给定的一组预测变量的响应变量的值。

## `lm()`函数

此函数创建预测变量和响应变量之间的关系模型。

### 语法

`lm()`函数在多元回归中的基本语法是:`lm(y ~ x1+x2+x3...,data)`

以下是所使用的参数的描述 - 

- 公式是表示响应变量和预测变量之间的关系的符号。
- 数据是应用公式的向量。

#### 练习：
输入数据

考虑在R语言环境中可用的数据集`mtcars`。 它给出了每加仑里程`mpg`，气缸排量`disp`，马力`hp`，汽车重量`wt`和一些其他参数的不同汽车模型之间的比较。

模型的目标是建立`mpg`作为响应变量与`disp`，`hp`和`wt`作为预测变量之间的关系。 为此，我们从`mtcars`数据集中创建这些变量的子集。

```R
input <- mtcars[,c("mpg","disp","hp","wt")]
print(head(input))
```

创建关系模型并获取系数

```R
input <- mtcars[,c("mpg","disp","hp","wt")]

# Create the relationship model.
model <- lm(mpg~disp+hp+wt, data = input)

# Show the model.
print(model)

# Get the Intercept and coefficients as vector elements.
cat("# # # # The Coefficient Values # # # ","
")

a <- coef(model)[1]
print(a)

Xdisp <- coef(model)[2]
Xhp <- coef(model)[3]
Xwt <- coef(model)[4]

print(Xdisp)
print(Xhp)
print(Xwt)
```

创建回归模型的方程:

基于上述截距和系数值，我们创建了数学方程。

$$
Y = a+Xdisp.x1+Xhp.x2+Xwt.x3
$$

or

$$
Y = 37.15+(-0.000937)\times X1+(-0.0311)\times X2+(-3.8008)\times X3
$$

应用方程预测新值:

当提供一组新的位移，马力和重量值时，我们可以使用上面创建的回归方程来预测里程数。

对于`disp = 221`，`hp = 102`和`wt = 2.91`的汽车，预测里程为:

$$
Y = 37.15+(-0.000937)\times221+(-0.0311)\times102+(-3.8008)\times2.91 = 22.7104
$$

#  逻辑回归

逻辑回归是回归模型，其中响应变量（因变量）具有诸如True / False或0/1的分类值。 它实际上基于将其与预测变量相关的数学方程测量二元响应的概率作为响应变量的值。

逻辑回归的一般数学方程为 -

$$
y = 1/(1+e^-(a+b1x1+b2x2+b3x3+...))
$$

以下是所使用的参数的描述 - 

- $y$是响应变量。
- $x$是预测变量。
- $a$和$b$是作为数字常数的系数。

用于创建回归模型的函数是`glm()`函数。

## 语法

逻辑回归中glm()函数的基本语法是:`glm(formula,data,family)`

以下是所使用的参数的描述 - 

- **formula**是表示变量之间的关系的符号。
- **data**是给出这些变量的值的数据集。
- **family**是R语言对象来指定模型的细节。 它的值是二项逻辑回归。

#### 练习:实现逻辑回归

内置数据集`mtcars`描述具有各种发动机规格的汽车的不同型号。 在`mtcars`数据集中，传输模式（自动或手动）由`am`列描述，它是一个二进制值（0或1）。 我们可以在列`am`和其他3列`hp`，`wt`和`cyl`之间创建逻辑回归模型。

```R
# Select some columns form mtcars.
input <- mtcars[,c("am","cyl","hp","wt")]

print(head(input))
```

创建回归模型

我们使用`glm()`函数创建回归模型，并得到其摘要进行分析。

```R
input <- mtcars[,c("am","cyl","hp","wt")]

am.data = glm(formula = am ~ cyl + hp + wt, data = input, family = binomial)

print(summary(am.data))
```

结论:
在总结中，对于变量`cyl`和`hp`，最后一列中的$p$值大于$0.05$，我们认为它们对变量`am`的值有贡献是无关紧要的。 只有重量`wt`影响该回归模型中的`am`值。

# 泊松回归

泊松回归包括回归模型，其中响应变量是计数而不是分数的形式。 例如，足球比赛系列中的出生次数或胜利次数。 此外，响应变量的值遵循泊松分布。

泊松回归的一般数学方程为 :`log(y) = a + b1x1 + b2x2 + bnxn.....`

以下是所使用的参数的描述 - 

- **y**是响应变量。
- **a**和**b**是数字系数。
- **x**是预测变量。

用于创建泊松回归模型的函数是`glm()`函数。

## 语法

在泊松回归中`glm()`函数的基本语法是 -:`glm(formula,data,family)`

以下是在上述功能中使用的参数的描述 - 

- **formula**是表示变量之间的关系的符号。
- **data**是给出这些变量的值的数据集。
- **family**是R语言对象来指定模型的细节。 它的值是“泊松”的逻辑回归。

#### 练习：泊松回归

我们有内置的数据集`warpbreaks`，其描述了羊毛类型（A或B）和张力（低，中或高）对每个织机的经纱断裂数量的影响。 让我们考虑“休息”作为响应变量，它是休息次数的计数。 羊毛“类型”和“张力”作为预测变量。

输入数据

```R
input <- warpbreaks
print(head(input))
```

创建回归模型

```R
output <-glm(formula = breaks ~ wool+tension, 
                   data = warpbreaks, 
                 family = poisson)
print(summary(output))
```
在摘要中，我们查找最后一列中的$p$值小于$0.05$，以考虑预测变量对响应变量的影响。 如图所示，具有张力类型M和H的羊毛类型B对断裂计数有影响。

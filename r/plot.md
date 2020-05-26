# R语言 绘图(plot)
## 条形图

条形图表示矩形条中的数据，条的长度与变量的值成比例。 R语言使用函数**barplot()**创建条形图。 R语言可以在条形图中绘制垂直和水平条。 在条形图中，每个条可以给予不同的颜色。

### 语法

在R语言中创建条形图的基本语法是：`barplot(H, xlab, ylab, main, names.arg, col)`

以下是所使用的参数的描述 - 

- **H**是包含在条形图中使用的数值的向量或矩阵。
- **xlab**是x轴的标签。
- **ylab**是y轴的标签。
- **main**是条形图的标题。
- **names.arg**是在每个条下出现的名称的向量。
- **col**用于向图中的条形提供颜色。

#### 练习：R语言绘制条形图

使用输入向量和每个条的名称创建一个简单的条形图。

以下脚本将创建并保存当前R语言工作目录中的条形图。

```R
# Create the data for the chart.
H <- c(7,12,28,3,41)

# Plot the bar chart.
barplot(H)
```
### 条形图标签，标题和颜色

可以通过添加更多参数来扩展条形图的功能。 主要参数用于添加标题。 `col`参数用于向条形添加颜色。 `args.name`是具有与输入向量相同数量的值的向量，以描述每个条的含义。

#### 练习：自定义条形图标签，标题和颜色

以下脚本将在当前R语言工作目录中创建并保存条形图。

```R
# Create the data for the chart.
H <- c(7,12,28,3,41)
M <- c("Mar","Apr","May","Jun","Jul")

# Plot the bar chart.
barplot(H,names.arg = M,xlab = "Month",ylab = "Revenue",col = "blue",
main = "Revenue chart",border = "red")
```

### 组合条形图和堆积条形图

我们可以使用矩阵作为输入值，在每个条中创建条形图和堆叠组的条形图。
超过两个变量表示为用于创建组合条形图和堆叠条形图的矩阵。

#### 练习：创建组合条形图和堆叠条形图的矩阵
```R
# Create the input vectors.
colors <- c("green","orange","brown")
months <- c("Mar","Apr","May","Jun","Jul")
regions <- c("East","West","North")

# Create the matrix of the values.
Values <- matrix(c(2,9,3,11,9,4,8,7,3,12,5,2,8,10,11),nrow = 3,ncol = 5,byrow = TRUE)

# Create the bar chart.
barplot(Values,main = "total revenue",names.arg = months,xlab = "month",ylab = "revenue",
   col = colors)

# Add the legend to the chart.
legend("topleft", regions, cex = 1.3, fill = colors)
```
## 箱线图

箱线图是数据集中的数据分布良好的度量。 它将数据集分成三个四分位数。 此图表表示数据集中的最小值，最大值，中值，第一四分位数和第三四分位数。 它还可用于通过绘制每个数据集的箱线图来比较数据集之间的数据分布。

R语言中使用`boxplot()`函数来创建箱线图。

### 语法
在R语言中创建箱线图的基本语法是：`boxplot(x, data, notch, varwidth, names, main)`

以下是所使用的参数的描述 - 

- **x**是向量或公式。
- 数据是数据帧。
- **notch**是逻辑值。 设置为TRUE以绘制凹口。
- **varwidth**是一个逻辑值。 设置为true以绘制与样本大小成比例的框的宽度。
- **names**是将打印在每个箱线图下的组标签。
- **main**用于给图表标题。

#### 练习：创建基本箱线图

我们使用R语言环境中可用的数据集`mtcars`来创建基本箱线图。 让我们看看`mtcars`中的列`mpg`和`cyl`。

```R
input <- mtcars[,c('mpg','cyl')]
print(head(input))
```



```R
#以下脚本将为mpg（英里/加仑）和cyl（气缸数）之间的关系创建箱线图。
# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, xlab = "Number of Cylinders",
   ylab = "Miles Per Gallon", main = "Mileage Data")
```

#### 练习： 带槽的箱线图
我们可以绘制带槽的箱线图，以了解不同数据组的中值如何相互匹配。

```R
# Plot the chart.
boxplot(mpg ~ cyl, data = mtcars, 
   xlab = "Number of Cylinders",
   ylab = "Miles Per Gallon", 
   main = "Mileage Data",
   notch = TRUE, 
   varwidth = TRUE, 
   col = c("green","yellow","purple"),
   names = c("High","Medium","Low")
)
```

## 直方图

直方图表示被存储到范围中的变量的值的频率。 直方图类似于条形图，但不同之处在于将值分组为连续范围。 直方图中的每个柱表示该范围中存在的值的数量的高度。

R语言使用`hist()`函数创建直方图。 此函数使用向量作为输入，并使用一些更多的参数来绘制直方图。

### 语法

使用R语言创建直方图的基本语法是:`hist(v,main,xlab,xlim,ylim,breaks,col,border)`

以下是所使用的参数的描述 - 

- **v**是包含直方图中使用的数值的向量。
- **main**表示图表的标题。
- **col**用于设置条的颜色。
- **border**用于设置每个条的边框颜色。
- **xlab**用于给出x轴的描述。
- **xlim**用于指定x轴上的值的范围。
- **ylim**用于指定y轴上的值的范围。
- **break**用于提及每个条的宽度。

#### 练习: 绘制直方图
使用输入`vector`，`label`，`col`和边界参数创建一个简单的直方图。
下面给出的脚本将创建并保存当前R语言工作目录中的直方图。

```R
# Create data for the graph.
v <-  c(9,13,21,8,36,22,12,41,31,33,19)

# Create the histogram.
hist(v,xlab = "Weight",col = "yellow",border = "blue")
```
#### 练习：X和Y值的范围
要指定X轴和Y轴允许的值的范围，我们可以使用`xlim`和`ylim`参数。
每个条的宽度可以通过使用间隔来确定。

```R
# Create data for the graph.
v <- c(9,13,21,8,36,22,12,41,31,33,19)

# Create the histogram.
hist(v,xlab = "Weight",col = "green",border = "red", xlim = c(0,40), ylim = c(0,5),
   breaks = 5)
```

## 折线图
折线图是通过在它们之间绘制线段来连接一系列点的图。 这些点在它们的坐标（通常是x坐标）值之一中排序。 折线图通常用于识别数据中的趋势。

R语言中的`plot()`函数用于创建折线图。

### 语法

在R语言中创建折线图的基本语法是：`plot(v,type,col,xlab,ylab)`

以下是所使用的参数的描述 - 

- **v**是包含数值的向量。
- 类型采用值“p”仅绘制点，“l”仅绘制线和“o”绘制点和线。
- **xlab**是x轴的标签。
- **ylab**是y轴的标签。
- **main**是图表的标题。
- **col**用于给点和线的颜色。

#### 练习：折线图

使用输入向量和类型参数“O”创建简单的折线图。 以下脚本将在当前R工作目录中创建并保存折线图。
```R
# Create the data for the chart.
v <- c(7,12,28,3,41)

# Plot the bar chart. 
plot(v,type = "o")
```
### 折线图标题，颜色和标签
线图的特征可以通过使用附加参数来扩展。 我们向点和线添加颜色，为图表添加标题，并向轴添加标签。

#### 练习：自定义折线图标题，颜色和标签

```R
# Create the data for the chart.
v <- c(7,12,28,3,41)

# Plot the bar chart.
plot(v,type = "o", col = "red", xlab = "Month", ylab = "Rain fall",
   main = "Rain fall chart")
```
### 多线型折线图
通过使用`lines()`函数，可以在同一个图表上绘制多条线。

在绘制第一行之后，`lines()`函数可以使用一个额外的向量作为输入来绘制图表中的第二行。

#### 练习：多线型折线图
```R
# Create the data for the chart.
v <- c(7,12,28,3,41)
t <- c(14,7,6,19,3)

# Plot the bar chart.
plot(v,type = "o",col = "red", xlab = "Month", ylab = "Rain fall", 
   main = "Rain fall chart")

lines(t, type = "o", col = "blue")
```

## 散点图

散点图显示在笛卡尔平面中绘制的许多点。 每个点表示两个变量的值。 在水平轴上选择一个变量，在垂直轴上选择另一个变量。

使用`plot()`函数创建简单散点图。

### 语法

在R语言中创建散点图的基本语法是 -

`plot(x, y, main, xlab, ylab, xlim, ylim, axes)`

以下是所使用的参数的描述 - 

- **x**是其值为水平坐标的数据集。
- **y**是其值是垂直坐标的数据集。
- **main**要是图形的图块。
- **xlab**是水平轴上的标签。
- **ylab**是垂直轴上的标签。
- **xlim**是用于绘图的x的值的极限。
- **ylim**是用于绘图的y的值的极限。
- **axes**指示是否应在绘图上绘制两个轴。

#### 练习：创建散点图

我们使用R语言环境中可用的数据集`mtcars`来创建基本散点图。 让我们使用`mtcars`中的`wt`和`mpg`列。

```R
input <- mtcars[,c('wt','mpg')]
print(head(input))
```

以下脚本将为wt（重量）和mpg（英里/加仑）之间的关系创建一个散点图。

```R
# Get the input values.
input <- mtcars[,c('wt','mpg')]

# Plot the chart for cars with weight between 2.5 to 5 and mileage between 15 and 30.
plot(x = input$wt,y = input$mpg,
   xlab = "Weight",
   ylab = "Milage",
   xlim = c(2.5,5),
   ylim = c(15,30),		 
   main = "Weight vs Milage"
)
```

### 散点图矩阵

当我们有两个以上的变量，我们想找到一个变量和其余变量之间的相关性，我们使用散点图矩阵。 我们使用`pairs()`函数创建散点图的矩阵。

语法: 在R中创建散点图矩阵的基本语法是:`pairs(formula, data)`

以下是所使用的参数的描述 - 

- **formula**表示成对使用的一系列变量。
- **data**表示将从其获取变量的数据集。

#### 练习:绘制散点图

每个变量与每个剩余变量配对。 为每对绘制散点图。

```R
# Plot the matrices between 4 variables giving 12 plots.

# One variable with 3 others and total 4 variables.

pairs(~wt+mpg+disp+cyl,data = mtcars,
   main = "Scatterplot Matrix")
```
## 饼状图

R编程语言有许多库来创建图表和图表。 饼图是将值表示为具有不同颜色的圆的切片。 切片被标记，并且对应于每个片的数字也在图表中表示。

在R语言中，饼图是使用`pie()`函数创建的，它使用正数作为向量输入。 附加参数用于控制标签，颜色，标题等。

## 语法:
使用R语言创建饼图的基本语法是:`pie(x, labels, radius, main, col, clockwise)`

以下是所使用的参数的描述 - 

- **x**是包含饼图中使用的数值的向量。
- **labels**用于给出切片的描述。
- **radius**表示饼图圆的半径（值-1和+1之间）。
- **main**表示图表的标题。
- **col**表示调色板。
- **clockwise**是指示片段是顺时针还是逆时针绘制的逻辑值。

#### 练习：绘制饼状图

使用输入向量和标签创建一个非常简单的饼图。 以下脚本将创建并保存当前R语言工作目录中的饼图。

```R
# Create data for the graph.
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai")


# Plot the chart.
pie(x,labels)
```

#### 练习：饼图标题和颜色
我们可以通过向函数中添加更多参数来扩展图表的功能。 我们将使用参数**main**向图表添加标题，另一个参数是**col**，它将在绘制图表时使用彩虹色板。 托盘的长度应与图表中的值的数量相同。 因此，我们使用**length(x)**。

以下脚本将创建并保存当前R语言工作目录中的饼图。

```R
# Create data for the graph.
x <- c(21, 62, 10, 53)
labels <- c("London", "New York", "Singapore", "Mumbai")

# Plot the chart with title and rainbow color pallet.
pie(x, labels, main = "City pie chart", col = rainbow(length(x)))
```

#### 练习：切片百分比和图表图例

我们可以通过创建其他图表变量来添加切片百分比和图表图例。

```R
# Create data for the graph.
x <-  c(21, 62, 10,53)
labels <-  c("London","New York","Singapore","Mumbai")

piepercent<- round(100*x/sum(x), 1)

# Plot the chart.
pie(x, labels = piepercent, main = "City pie chart",col = rainbow(length(x)))
legend("topright", c("London","New York","Singapore","Mumbai"), cex = 0.8,
   fill = rainbow(length(x)))
```

#### 练习：3D饼图

可以使用其他软件包绘制具有3个维度的饼图。 软件包`plotrix`有一个名为`pie3D()`的函数，用于此。

```R
# Get the library.
library(plotrix)

# Create data for the graph.
x <-  c(21, 62, 10,53)
lbl <-  c("London","New York","Singapore","Mumbai")

# Plot the chart.
pie3D(x,labels = lbl,explode = 0.1, main = "Pie Chart of Countries ")
```


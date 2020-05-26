# R语言 数据类型(datatype)

通常，在使用任何编程语言进行编程时，您需要使用各种变量来存储各种信息。 变量只是保留值的存储位置。 这意味着，当你创建一个变量，你必须在内存中保留一些空间来存储它们。

您可能想存储各种数据类型的信息，如字符，宽字符，整数，浮点，双浮点，布尔等。基于变量的数据类型，操作系统分配内存并决定什么可以存储在保留内存中。

与其他编程语言（如C中的C和java）相反，变量不会声明为某种数据类型。 变量分配有R对象，R对象的数据类型变为变量的数据类型。尽管有很多类型的R对象，但经常使用的是：

- 矢量
- 列表
- 矩阵
- 数组
- 因子
- 数据帧

这些对象中最简单的是向量对象，并且这些原子向量有六种数据类型，也称为六类向量。 其他R对象建立在原子向量之上。

|数据类型|	示例	|结果|
|:--|:--|:--|
|Logical（逻辑型）	TRUE, FALSE	| `v <- TRUE;print(class(v))` | [1] "logical"|
|Numeric（数字）	12.3，5，999	|`v <- 23.5;print(class(v))`|[1] "numeric"|
|Integer（整型）	2L，34L，0L	|`v <- 2L;print(class(v))`|[1] "integer"|
|Complex（复合型）	3 + 2i	|`v <- 2+5i;print(class(v))`|[1] "complex"|
|Character（字符）	'a',"god","TRUE",'23.4';|`v <- "TRUE";print(class(v))`|[1] "character"|
|Raw(原型)"Hello"被存储为 48 65 6c 6c 6f|`v <- charToRaw("Hello");print(class(v))`|[1] "raw"|


在R编程中，非常基本的数据类型是称为向量的R对象，其保存如上所示的不同类的元素。 请注意，在R中，类的数量不仅限于上述六种类型。

 例如，我们可以使用许多原子向量并创建一个数组，其类将成为数组。

## Vectors 向量
当你想用多个元素创建向量时，你应该使用c()函数，这意味着将元素组合成一个向量。

```R
# Create a vector.
apple <- c('red','green',"yellow")
print(apple)

# Get the class of the vector.
print(class(apple))
```

## Lists 列表
列表是一个R对象，它可以在其中包含许多不同类型的元素，如向量，函数甚至其中的另一个列表。
```R
# Create a list.
list1 <- list(c(2,5,3),21.3,sin)

# Print the list.
print(list1)
```
## Matrices 矩阵
矩阵是二维矩形数据集。 它可以使用矩阵函数的向量输入创建。
```R
# Create a matrix.
M = matrix( c('a','a','b','c','b','a'), nrow = 2, ncol = 3, byrow = TRUE)
print(M)
```
## Arrays 数组
虽然矩阵被限制为二维，但阵列可以具有任何数量的维度。 数组函数使用一个dim属性创建所需的维数。 在下面的例子中，我们创建了一个包含两个元素的数组，每个元素为3x3个矩阵。
```R
# Create an array.
a <- array(c('green','yellow'),dim = c(3,3,2))
print(a)
```

## Factors 因子
因子是使用向量创建的r对象。 它将向量与向量中元素的不同值一起存储为标签。 标签总是字符，不管它在输入向量中是数字还是字符或布尔等。 它们在统计建模中非常有用。 使用`factor()`函数创建因子。`nlevels()`函数给出级别计数。
```R
# Create a vector.
apple_colors <- c('green','green','yellow','red','red','red','green')

# Create a factor object.
factor_apple <- factor(apple_colors)

# Print the factor.
print(factor_apple)
print(nlevels(factor_apple))
```
## Data Frames 数据帧
数据帧是表格数据对象。 与数据帧中的矩阵不同，每列可以包含不同的数据模式。 第一列可以是数字，而第二列可以是字符，第三列可以是逻辑的。 它是等长度的向量的列表。 使用`data.frame()`函数创建数据帧。
```R
# Create the data frame.
BMI <-  data.frame(
   gender = c("Male", "Male","Female"),
   height = c(152, 171.5, 165),
   weight = c(81,93, 78),
   Age = c(42,38,26)
)
print(BMI)
```
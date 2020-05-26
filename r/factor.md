# R语言 因子(factor)

因子是用于对数据进行分类并将其存储为级别的数据对象。 它们可以存储字符串和整数。 它们在具有有限数量的唯一值的列中很有用。 像“男性”，“女性”和True，False等。它们在统计建模的数据分析中很有用。

#### 练习：使用`factor()`函数通过将向量作为输入创建因子

```R
# Create a vector as input.
data <- c("East","West","East","North","North","East","West","West","West","East","North")

print(data)
print(is.factor(data))

# Apply the factor function.
factor_data <- factor(data)

print(factor_data)
print(is.factor(factor_data))
```

#### 练习： 数据帧上创建因子

在创建具有文本数据列的任何数据框时，R语言将文本列视为分类数据并在其上创建因子。

```R
# Create the vectors for data frame.
height <- c(132,151,162,139,166,147,122)
weight <- c(48,49,66,53,67,52,40)
gender <- c("male","male","female","female","male","female","male")

# Create the data frame.
input_data <- data.frame(height,weight,gender)
print(input_data)

# Test if the gender column is a factor.
print(is.factor(input_data$gender))

# Print the gender column so see the levels.
print(input_data$gender)
```

#### 练习： 更改级别顺序

可以通过使用新的等级次序再次应用因子函数来改变因子中的等级的顺序。

```R
data <- c("East","West","East","North","North","East","West","West","West","East","North")
# Create the factors
factor_data <- factor(data)
print(factor_data)

# Apply the factor function with required order of the level.
new_order_data <- factor(factor_data,levels = c("East","West","North"))
print(new_order_data)
```

## 生成因子级别

我们可以使用`gl()`函数生成因子级别。 它需要两个整数作为输入，指示每个级别有多少级别和多少次。

### 语法
`gl(n, k, labels)`

以下是所使用的参数的说明 -

- **n**是给出级数的整数。
- **k**是给出复制数目的整数。
- **labels**是所得因子水平的标签向量。

#### 练习：生成因子级别
```R
v <- gl(3, 4, labels = c("Tampa", "Seattle","Boston"))
print(v)
```

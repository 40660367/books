# R语言 字符串(string)

在R语言中的单引号或双引号对中写入的任何值都被视为字符串。 R语言存储的每个字符串都在双引号内，即使是使用单引号创建的依旧如此。

## 在字符串构造中应用的规则

- 在字符串的开头和结尾的引号应该是两个双引号或两个单引号。它们不能被混合。
- 双引号可以插入到以单引号开头和结尾的字符串中。
- 单引号可以插入以双引号开头和结尾的字符串。
- 双引号不能插入以双引号开头和结尾的字符串。
- 单引号不能插入以单引号开头和结尾的字符串。

#### 练习：有效字符串

以下示例阐明了在R语言中创建字符串的规则。

```R
a <- 'Start and end with single quote'
print(a)

b <- "Start and end with double quotes"
print(b)

c <- "single quote ' in between double quotes"
print(c)

d <- 'Double quotes " in between single quote'
print(d)
```

#### 练习：无效字符串的示例

```R
e <- 'Mixed quotes" 
print(e)

f <- 'Single quote ' inside single quote'
print(f)

g <- "Double quotes " inside double quotes"
print(g)
```

## 字符串操作

### 连接字符串：`paste()`函数

R语言中的许多字符串使用`paste()`函数组合。 它可以采取任何数量的参数组合在一起。

### 语法

对于粘贴功能的基本语法是:`paste(..., sep = " ", collapse = NULL)`

以下是所使用的参数的说明 -

- ...表示要组合的任意数量的自变量。
- sep表示参数之间的任何分隔符。它是可选的。
- collapse用于消除两个字符串之间的空格。 但不是一个字符串的两个字内的空间。

#### 练习：字符串拼接

```R
a <- "Hello"
b <- 'How'
c <- "are you? "

print(paste(a,b,c))

print(paste(a,b,c, sep = "-"))

print(paste(a,b,c, sep = "", collapse = ""))
```

### 格式化数字和字符串:`format()`函数

可以使用`format()`函数将数字和字符串格式化为特定样式。

### 语法

格式化函数的基本语法是:`format(x, digits, nsmall, scientific, width, justify = c("left", "right", "centre", "none")) `

以下是所使用的参数的描述 - 

- **x**是向量输入。
- **digits**是显示的总位数。
- **nsmall**是小数点右边的最小位数。
- 科学设置为**TRUE**以显示科学记数法。
- **width**指示通过在开始处填充空白来显示的最小宽度。
- **justify**是字符串向左，右或中心的显示。

#### 练习：字符串格式化

```R
# Total number of digits displayed. Last digit rounded off.
result <- format(23.123456789, digits = 9)
print(result)

# Display numbers in scientific notation.
result <- format(c(6, 13.14521), scientific = TRUE)
print(result)

# The minimum number of digits to the right of the decimal point.
result <- format(23.47, nsmall = 5)
print(result)

# Format treats everything as a string.
result <- format(6)
print(result)

# Numbers are padded with blank in the beginning for width.
result <- format(13.7, width = 6)
print(result)

# Left justify strings.
result <- format("Hello", width = 8, justify = "l")
print(result)

# Justfy string with center.
result <- format("Hello", width = 8, justify = "c")
print(result)
```

### 计算字符串中的字符数 - `nchar()`函数

此函数计算字符串中包含空格的字符数。

### 语法

`nchar()`函数的基本语法是 -

`nchar(x)`

以下是所使用的参数的描述 - 

- **x**是向量输入。

#### 练习：计算字符串中的字符数

```R
result <- nchar("Count the number of characters")
print(result)
```

### 更改case - toupper()和tolower()函数

这些函数改变字符串的字符的大小写。

### 语法

`toupper()`和`tolower()`函数的基本语法是:`toupper(x)`,`tolower(x)`

以下是所使用的参数的描述 - 

- **x**是向量输入。

#### 练习：更改字符串大小写
```R
# Changing to Upper case.
result <- toupper("Changing To Upper")
print(result)

# Changing to lower case.
result <- tolower("Changing To Lower")
print(result)
```

### 提取字符串的一部分 - `substring()`函数

此函数提取字符串的部分。

### 语法

`substring()`函数的基本语法是:`substring(x,first,last)`

以下是所使用的参数的描述 - 

- **x**是字符向量输入。
- 首先是要提取的第一个字符的位置。
- **last**是要提取的最后一个字符的位置。

#### 练习：提取字符串

```R
# Extract characters from 5th to 7th position.
result <- substring("Extract", 5, 7)
print(result)
```

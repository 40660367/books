# R语言 数据类型-向量(vector)

向量是最基本的R语言数据对象。

向量，有六种类型的原子向量。 它们是逻辑，整数，双精度，复杂，字符和原始。

## 创建向量

#### 练习：单元素向量

即使在R语言中只写入一个值，它也将成为长度为1的向量，并且属于上述向量类型之一。

```R
# Atomic vector of type character.
print("abc");

# Atomic vector of type double.
print(12.5)

# Atomic vector of type integer.
print(63L)

# Atomic vector of type logical.
print(TRUE)

# Atomic vector of type complex.
print(2+3i)

# Atomic vector of type raw.
print(charToRaw('hello'))
```

#### 练习：多元素向量

对数值数据使用冒号运算符

```R
# Creating a sequence from 5 to 13.
v <- 5:13
print(v)

# Creating a sequence from 6.6 to 12.6.
v <- 6.6:12.6
print(v)

# If the final element specified does not belong to the sequence then it is discarded.
v <- 3.8:11.4
print(v)
```

#### 练习：使用`seq()`序列运算符

```R
# Create vector with elements from 5 to 9 incrementing by 0.4.
print(seq(5, 9, by = 0.4))
```

#### 练习：使用`C()`函数

如果其中一个元素是字符，则非字符值被强制转换为字符类型。

```R
# The logical and numeric values are converted to characters.
s <- c('apple','red',5,TRUE)
print(s)
```

#### 练习：访问向量元素

使用索引访问向量的元素。 []括号用于建立索引。 索引从位置1开始。在索引中给出负值会丢弃来自**result**.**TRUE**，**FALSE**或0和1的元素，也可用于索引。

```R
# Accessing vector elements using position.
t <- c("Sun","Mon","Tue","Wed","Thurs","Fri","Sat")
u <- t[c(2,3,6)]
print(u)

# Accessing vector elements using logical indexing.
v <- t[c(TRUE,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE)]
print(v)

# Accessing vector elements using negative indexing.
x <- t[c(-2,-5)]
print(x)

# Accessing vector elements using 0/1 indexing.
y <- t[c(0,0,0,0,0,0,1)]
print(y)
```

## 向量操作

### 向量运算

可以添加，减去，相乘或相除两个相同长度的向量，将结果作为向量输出。

#### 练习：向量运算
```R
# Create two vectors.
v1 <- c(3,8,4,5,0,11)
v2 <- c(4,11,0,8,1,2)

# Vector addition.
add.result <- v1+v2
print(add.result)

# Vector substraction.
sub.result <- v1-v2
print(sub.result)

# Vector multiplication.
multi.result <- v1*v2
print(multi.result)

# Vector division.
divi.result <- v1/v2
print(divi.result)
```

### 向量元素回收
如果我们对不等长的两个向量应用算术运算，则较短向量的元素被循环以完成操作。

#### 练习： 向量元素回收
```R
v1 <- c(3,8,4,5,0,11)
v2 <- c(4,11)
# V2 becomes c(4,11,4,11,4,11)

add.result <- v1+v2
print(add.result)

sub.result <- v1-v2
print(sub.result)
```

#### 练习： 向量元素排序

向量中的元素可以使用`sort()`函数排序。

```R
v <- c(3,8,4,5,0,11, -9, 304)

# Sort the elements of the vector.
sort.result <- sort(v)
print(sort.result)

# Sort the elements in the reverse order.
revsort.result <- sort(v, decreasing = TRUE)
print(revsort.result)

# Sorting character vectors.
v <- c("Red","Blue","yellow","violet")
sort.result <- sort(v)
print(sort.result)

# Sorting character vectors in reverse order.
revsort.result <- sort(v, decreasing = TRUE)
print(revsort.result)
```

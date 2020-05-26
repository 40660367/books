# R语言 数组(array)

数组是可以在两个以上维度中存储数据的R数据对象。 例如 - 如果我们创建一个维度(2，3，4)的数组，则它创建4个矩形矩阵，每个矩阵具有2行和3列。 数组只能存储数据类型。

使用`array()`函数创建数组。 它使用向量作为输入，并使用`dim()`参数中的值创建数组。

#### 练习：创建一个由两个3x3矩阵组成的数组，每个矩阵具有3行和3列。
```R
# Create two vectors of different lengths.
vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)

# Take these vectors as input to the array.
result <- array(c(vector1,vector2),dim = c(3,3,2))
print(result)
```

#### 练习：命名列和行

我们可以使用`dimnames`参数给数组中的行，列和矩阵命名。

```R
# Create two vectors of different lengths.
vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)
column.names <- c("COL1","COL2","COL3")
row.names <- c("ROW1","ROW2","ROW3")
matrix.names <- c("Matrix1","Matrix2")

# Take these vectors as input to the array.
result <- array(c(vector1,vector2),dim = c(3,3,2),dimnames = list(row.names,column.names,
   matrix.names))
print(result)
```

#### 练习：访问数组元素
```R
# Create two vectors of different lengths.
vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)
column.names <- c("COL1","COL2","COL3")
row.names <- c("ROW1","ROW2","ROW3")
matrix.names <- c("Matrix1","Matrix2")

# Take these vectors as input to the array.
result <- array(c(vector1,vector2),dim = c(3,3,2),dimnames = list(row.names,
   column.names, matrix.names))

# Print the third row of the second matrix of the array.
print(result[3,,2])

# Print the element in the 1st row and 3rd column of the 1st matrix.
print(result[1,3,1])

# Print the 2nd Matrix.
print(result[,,2])
```

#### 练习：操作数组元素
由于数组由多维构成矩阵，所以对数组元素的操作通过访问矩阵的元素来执行。
```R
# Create two vectors of different lengths.
vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)

# Take these vectors as input to the array.
array1 <- array(c(vector1,vector2),dim = c(3,3,2))

# Create two vectors of different lengths.
vector3 <- c(9,1,0)
vector4 <- c(6,0,11,3,14,1,2,6,9)
array2 <- array(c(vector1,vector2),dim = c(3,3,2))

# create matrices from these arrays.
matrix1 <- array1[,,2]
matrix2 <- array2[,,2]

# Add the matrices.
result <- matrix1+matrix2
print(result)
```

#### 练习：跨数组元素的计算

我们可以使用`apply()`函数在数组中的元素上进行计算。

语法:`apply(x, margin, fun)`

以下是所使用的参数的说明 -

- **x**是一个数组。
- **margin**是所使用的数据集的名称。
- **fun**是要应用于数组元素的函数。

我们使用下面的`apply()`函数计算所有矩阵中数组行中元素的总和。

```R
# Create two vectors of different lengths.
vector1 <- c(5,9,3)
vector2 <- c(10,11,12,13,14,15)

# Take these vectors as input to the array.
new.array <- array(c(vector1,vector2),dim = c(3,3,2))
print(new.array)

# Use apply to calculate the sum of the rows across all the matrices.
result <- apply(new.array, c(1), sum)
print(result)
```
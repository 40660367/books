# R语言 矩阵(matrix)

矩阵是其中元素以二维矩形布局布置的R对象。 它们包含相同原子类型的元素。 虽然我们可以创建一个只包含字符或只包含逻辑值的矩阵，但它们没有太多用处。 我们使用包含数字元素的矩阵用于数学计算。

使用`matrix()`函数创建一个矩阵。

## 语法

在R语言中创建矩阵的基本语法是`matrix(data, nrow, ncol, byrow, dimnames)`

以下是所使用的参数的说明 -

- 数据是成为矩阵的数据元素的输入向量。
- **nrow**是要创建的行数。
- **ncol**是要创建的列数。
- **byrow**是一个逻辑线索。 如果为TRUE，则输入向量元素按行排列。
- **dimname**是分配给行和列的名称。

#### 练习：创建一个以数字向量作为输入的矩阵

```R
# Elements are arranged sequentially by row.
M <- matrix(c(3:14), nrow = 4, byrow = TRUE)
print(M)

# Elements are arranged sequentially by column.
N <- matrix(c(3:14), nrow = 4, byrow = FALSE)
print(N)

# Define the column and row names.
rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")

P <- matrix(c(3:14), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))
print(P)
```

#### 练习： 访问矩阵的元素

可以通过使用元素的列和行索引来访问矩阵的元素。 我们考虑上面的矩阵P找到下面的具体元素。

```R
# Define the column and row names.
rownames = c("row1", "row2", "row3", "row4")
colnames = c("col1", "col2", "col3")

# Create the matrix.
P <- matrix(c(3:14), nrow = 4, byrow = TRUE, dimnames = list(rownames, colnames))

# Access the element at 3rd column and 1st row.
print(P[1,3])

# Access the element at 2nd column and 4th row.
print(P[4,2])

# Access only the  2nd row.
print(P[2,])

# Access only the 3rd column.
print(P[,3])
```

## 矩阵计算

使用R运算符对矩阵执行各种数学运算。 操作的结果也是一个矩阵。

对于操作中涉及的矩阵，维度（行数和列数）应该相同。
#### 练习：矩阵加法和减法
```R
# Create two 2x3 matrices.
matrix1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2)
print(matrix1)

matrix2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2)
print(matrix2)

# Add the matrices.
result <- matrix1 + matrix2
cat("Result of addition","
")
print(result)

# Subtract the matrices
result <- matrix1 - matrix2
cat("Result of subtraction","
")
print(result)
```

#### 练习：矩阵乘法和除法

```R
# Create two 2x3 matrices.
matrix1 <- matrix(c(3, 9, -1, 4, 2, 6), nrow = 2)
print(matrix1)

matrix2 <- matrix(c(5, 2, 0, 9, 3, 4), nrow = 2)
print(matrix2)

# Multiply the matrices.
result <- matrix1 * matrix2
cat("Result of multiplication","
")
print(result)

# Divide the matrices
result <- matrix1 / matrix2
cat("Result of division","
")
print(result)
```
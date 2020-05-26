# R语言 列表(list)

列表是R语言对象，它包含不同类型的元素，如数字，字符串，向量和其中的另一个列表。 列表还可以包含矩阵或函数作为其元素。 

列表是使用`list()`函数创建的。

#### 练习：创建列表
以下是创建包含字符串，数字，向量和逻辑值的列表的示例

```R
# Create a list containing strings, numbers, vectors and a logical values.
list_data <- list("Red", "Green", c(21,32,11), TRUE, 51.23, 119.1)
print(list_data)
```

#### 练习：命名列表元素

列表元素可以给出名称，并且可以使用这些名称访问它们。

```R
# Create a list containing a vector, a matrix and a list.
list_data <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
   list("green",12.3))

# Give names to the elements in the list.
names(list_data) <- c("1st Quarter", "A_Matrix", "A Inner list")

# Show the list.
print(list_data)
```

#### 练习：访问列表元素

列表的元素可以通过列表中元素的索引访问。 在命名列表的情况下，它也可以使用名称来访问。我们继续使用在上面的例子列表

```R
# Create a list containing a vector, a matrix and a list.
list_data <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
   list("green",12.3))

# Give names to the elements in the list.
names(list_data) <- c("1st Quarter", "A_Matrix", "A Inner list")

# Access the first element of the list.
print(list_data[1])

# Access the thrid element. As it is also a list, all its elements will be printed.
print(list_data[3])

# Access the list element using the name of the element.
print(list_data$A_Matrix)
```

#### 练习：操控列表元素

我们可以添加，删除和更新列表元素，如下所示。 我们只能在列表的末尾添加和删除元素。 但我们可以更新任何元素。

```R
# Create a list containing a vector, a matrix and a list.
list_data <- list(c("Jan","Feb","Mar"), matrix(c(3,9,5,1,-2,8), nrow = 2),
   list("green",12.3))

# Give names to the elements in the list.
names(list_data) <- c("1st Quarter", "A_Matrix", "A Inner list")

# Add element at the end of the list.
list_data[4] <- "New element"
print(list_data[4])

# Remove the last element.
list_data[4] <- NULL

# Print the 4th Element.
print(list_data[4])

# Update the 3rd Element.
list_data[3] <- "updated element"
print(list_data[3])
```
#### 练习：合并列表

通过将所有列表放在一个`list()`函数中，您可以将许多列表合并到一个列表中。

```R
# Create two lists.
list1 <- list(1,2,3)
list2 <- list("Sun","Mon","Tue")

# Merge the two lists.
merged.list <- c(list1,list2)

# Print the merged list.
print(merged.list)
```

#### 练习： 将列表转换为向量

列表可以转换为向量，使得向量的元素可以用于进一步的操作。 可以在将列表转换为向量之后应用对向量的所有算术运算。 要做这个转换，我们使用`unlist()`函数。 它将列表作为输入并生成向量。
```r
# Create lists.
list1 <- list(1:5)
print(list1)

list2 <-list(10:14)
print(list2)

# Convert the lists to vectors.
v1 <- unlist(list1)
v2 <- unlist(list2)

print(v1)
print(v2)

# Now add the vectors
result <- v1+v2
print(result)
```


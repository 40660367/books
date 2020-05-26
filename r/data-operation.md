# R语言 数据重塑(reshape)

R语言中的数据重塑是关于改变数据被组织成行和列的方式。 大多数时间R语言中的数据处理是通过将输入数据作为数据帧来完成的。 很容易从数据帧的行和列中提取数据，但是在某些情况下，我们需要的数据帧格式与我们接收数据帧的格式不同。

R语言具有许多功能，在数据帧中拆分，合并和将行更改为列，反之亦然。

#### 练习：于数据帧中加入列和行

我们可以使用`cbind()`函数连接多个向量来创建数据帧。 此外，我们可以使用`rbind()`函数合并两个数据帧。

```R
# Create vector objects.
city <- c("Tampa","Seattle","Hartford","Denver")
state <- c("FL","WA","CT","CO")
zipcode <- c(33602,98104,06161,80294)

# Combine above three vectors into one data frame.
addresses <- cbind(city,state,zipcode)

# Print a header.
cat("# # # # The First data frame
") 

# Print the data frame.
print(addresses)

# Create another data frame with similar columns
new.address <- data.frame(
   city = c("Lowry","Charlotte"),
   state = c("CO","FL"),
   zipcode = c("80230","33949"),
   stringsAsFactors = FALSE
)

# Print a header.
cat("# # # The Second data frame
") 

# Print the data frame.
print(new.address)

# Combine rows form both the data frames.
all.addresses <- rbind(addresses,new.address)

# Print a header.
cat("# # # The combined data frame
") 

# Print the result.
print(all.addresses)
```

#### 练习：合并数据帧

我们可以使用`merge()`函数合并两个数据帧。 数据帧必须具有相同的列名称，在其上进行合并。

在下面的例子中，我们考虑图书馆名称“MASS”中有关Pima Indian Women的糖尿病的数据集。 我们基于血压（“bp”）和体重指数（“bmi”）的值合并两个数据集。 在选择这两列用于合并时，其中这两个变量的值在两个数据集中匹配的记录被组合在一起以形成单个数据帧。

```R
library(MASS)
merged.Pima <- merge(x = Pima.te, y = Pima.tr,
   by.x = c("bp", "bmi"),
   by.y = c("bp", "bmi")
)
print(merged.Pima)
nrow(merged.Pima)
```

`melt()`拆分数据和`cast()`数据重构

R语言编程的一个最有趣的方面是关于在多个步骤中改变数据的形状以获得期望的形状。 用于执行此操作的函数称为`melt()`和`cast()`。

我们考虑称为船舶的数据集称为“MASS”。

```R
library(MASS)
print(ships)
```

 `melt()`拆分数据,现在我们拆分数据进行重组，将除类型和年份以外的所有列转换为多行展示。

```R
molten.ships <- melt(ships, id = c("type","year"))
print(molten.ships)
```

`cast()`重构数据,我们可以将被拆分的数据转换为一种新形式，使用cast()函数创建每年每种类型的船的总和。

```R
recasted.ship <- cast(molten.ships, type+year~variable,sum)
print(recasted.ship)
```

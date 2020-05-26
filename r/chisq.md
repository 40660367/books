# R语言 卡方检验(chisq test)

**卡方检验**是一种确定两个分类变量之间是否存在显着相关性的统计方法。 这两个变量应该来自相同的人口，他们应该是类似 - 是/否，男/女，红/绿等。

例如，我们可以建立一个观察人们的冰淇淋购买模式的数据集，并尝试将一个人的性别与他们喜欢的冰淇淋的味道相关联。 如果发现相关性，我们可以通过了解访问的人的性别的数量来计划适当的味道库存。

## 语法

用于执行卡方检验的函数是:`chisq.test()`

在R语言中创建卡方检验的基本语法是 `chisq.test(data)`

以下是所使用的参数的描述 

- **data**是以包含观察中变量的计数值的表的形式的数据。

#### 练习：:卡方检验

我们将在`MASS`库中获取`Cars93`数据，该图书馆代表1993年不同型号汽车的销售额。

```R
library("MASS")
print(str(Cars93))
```

上述结果表明数据集有很多因素变量，可以被认为是分类变量。 对于我们的模型，我们将考虑变量“AirBags”和“Type”。 在这里，我们的目标是找出所售的汽车类型和安全气囊类型之间的任何显着的相关性。 如果观察到相关性，我们可以估计哪种类型的汽车可以更好地卖什么类型的气囊。

```R
# Load the library.
library("MASS")

# Create a data frame from the main data set.
car.data <- data.frame(Cars93$AirBags, Cars93$Type)

# Create a table with the needed variables.
car.data = table(Cars93$AirBags, Cars93$Type) 
print(car.data)

# Perform the Chi-Square test.
print(chisq.test(car.data))
```

### 结论
结果显示$p$值小于$0.05$，这表明相关。
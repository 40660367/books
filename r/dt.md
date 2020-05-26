# R语言 决策树(decision tree)

决策树是以树的形式表示选择及其结果的图。图中的节点表示事件或选择，并且图的边缘表示决策规则或条件。它主要用于使用R的机器学习和数据挖掘应用程序。

决策树的使用的例子是 - 预测电子邮件是垃圾邮件或非垃圾邮件，预测肿瘤癌变，或者基于这些因素预测贷款的信用风险。通常，使用观测数据（也称为训练数据）来创建模型。然后使用一组验证数据来验证和改进模型。 R具有用于创建和可视化决策树的包。对于新的预测变量集合，我们使用此模型来确定R包`party`用于创建决策树。

## 安装R语言包

在R语言控制台中使用以下命令安装软件包。您还必须安装相关软件包（如果有）。

`install.packages("party")`,`party`包具有用于创建和分析决策树的函数`ctree()`。

## 语法

在R中创建决策树的基本语法是 -

`
ctree(formula, data)
`

以下是所使用的参数的描述 - 

- **formula**是描述预测变量和响应变量的公式。
- **data**是所使用的数据集的名称。

#### 练习：

输入数据：

我们将使用名为`readingSkills`的R内置数据集来创建决策树。 它描述了某人的readingSkills的分数，如果我们知道变量`年龄`，`shoesize`，`分数`，以及该人是否为母语者。

这里是示例数据。

```R
install.packages("party")
# Load the party package. It will automatically load other dependent packages.
library(party)

# Print some records from data set readingSkills.
print(head(readingSkills))
```
我们将使用`ctree()`函数创建决策树并查看其图形。

```R
# Load the party package. It will automatically load other dependent packages.
library(party)

# Create the input data frame.
input.dat <- readingSkills[c(1:105),]


# Create the tree.
output.tree <- ctree(
nativeSpeaker ~ age + shoeSize + score, 
data = input.dat)

# Plot the tree.
plot(output.tree)
```

### 结论
从上面显示的决策树，我们可以得出结论，其readingSkills分数低于38.3和年龄超过6的人不是一个母语者。
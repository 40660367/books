# R语言 随机森林算法(random forest)

在随机森林方法中，创建大量的决策树。 每个观察被馈入每个决策树。 每个观察的最常见的结果被用作最终输出。 新的观察结果被馈入所有的树并且对每个分类模型取多数投票。

对构建树时未使用的情况进行错误估计。 这称为**OOB（袋外）**误差估计，其被提及为百分比。

R语言包`randomForest`用于创建随机森林。

## 安装R包

在R语言控制台中使用以下命令安装软件包。 您还必须安装相关软件包（如果有）。

```R
install.packages("randomForest)
```

包`randomForest`具有函数`randomForest()`，用于创建和分析随机森林。

### 语法

在R语言中创建随机森林的基本语法是 `randomForest(formula, data)`

以下是所使用的参数的描述 - 

- **formula**是描述预测变量和响应变量的公式。
- **data**是所使用的数据集的名称。

### 输入数据

我们将使用名为`readingSkills`的R语言内置数据集来创建决策树。 它描述了某人的`readingSkills`的分数，如果我们知道变量`age`，`shoesize`，`score`，以及该人是否是母语。

以下是示例数据。

```R
# Load the party package. It will automatically load other required packages.
library(party)

# Print some records from data set readingSkills.
print(head(readingSkills))
```

#### 练习:创建决策树并查看它的图

我们将使用`randomForest()`函数来创建决策树并查看它的图。

```R
# Load the party package. It will automatically load other required packages.
library(party)
library(randomForest)

# Create the forest.
output.forest <- randomForest(nativeSpeaker ~ age + shoeSize + score, 
           data = readingSkills)

# View the forest results.
print(output.forest) 

# Importance of each predictor.
print(importance(fit,type = 2)) 
```

结论:

从上面显示的随机森林，我们可以得出结论，鞋码和成绩是决定如果某人是母语者或不是母语的重要因素。 此外，该模型只有1%的误差，这意味着我们可以预测精度为99%。
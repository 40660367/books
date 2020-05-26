# R语言 协方差分析(ancova)

我们使用回归分析创建模型，描述变量在预测变量对响应变量的影响。 有时，如果我们有一个类别变量，如Yes / No或Male/Female等。简单的回归分析为分类变量的每个值提供多个结果。 在这种情况下，我们可以通过将分类变量与预测变量一起使用并比较分类变量的每个级别的回归线来研究分类变量的效果。 这样的分析被称为**协方差分析**，也称为**ANCOVA**。

#### 练习：协方差分析

考虑在R语言内置的数据集`mtcars`。 在其中我们观察到字段`am”`表示传输的类型（自动或手动）。 它是值为0和1的分类变量。汽车的每加仑英里数`mpg`也可以取决于马力`hp`的值。

我们研究`am`的值对`mpg`和`hp`之间回归的影响。 它是通过使用`aov()`函数，然后使用`anova()`函数来比较多个回归来完成的。

输入数据

从数据集`mtcars`创建一个包含字段`mpg`，`hp`和`am`的数据框。 这里我们取`mpg`作为响应变量，`hp`作为预测变量，`am`作为分类变量。

```R
input <- mtcars[,c("am","mpg","hp")]
print(head(input))
```

我们创建一个回归模型，以`hp`作为预测变量，`mpg`作为响应变量，考虑`am`和`hp`之间的相互作用。

- 模型与分类变量和预测变量之间的相互作用

```R
# Get the dataset.
input <- mtcars

# Create the regression model.
result <- aov(mpg~hp*am,data = input)
print(summary(result))
```

这个结果表明，马力和传输类型对每加仑的英里有显着的影响，因为两种情况下的$p$值都小于$0.05$。 但是这两个变量之间的相互作用不显着，因为$p$值大于$0.05$。

- 没有分类变量和预测变量之间相互作用的模型

```R
# Get the dataset.
input <- mtcars

# Create the regression model.
result <- aov(mpg~hp+am,data = input)
print(summary(result))
```

这个结果表明，马力和传输类型对每加仑的英里有显着的影响，因为两种情况下的$p$值都小于$0.05$。

- 比较两个模型

现在我们可以比较两个模型来得出结论，变量的相互作用是否真正重要。 为此，我们使用**anova()**函数。

```R
# Get the dataset.
input <- mtcars

# Create the regression models.
result1 <- aov(mpg~hp*am,data = input)
result2 <- aov(mpg~hp+am,data = input)

# Compare the two models.
print(anova(result1,result2))
```
由于$p$值大于$0.05$，我们得出结论，马力和传播类型之间的相互作用不显着。 因此，在汽车和手动变速器模式下，每加仑的里程将以类似的方式取决于汽车的马力。
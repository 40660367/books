# R语言 生存分析(survival)

生存分析处理预测特定事件将要发生的时间。 它也被称为故障时间分析或分析死亡时间。 例如，预测患有癌症的人将存活的天数或预测机械系统将失败的时间。

命名为`survival`的R语言包用于进行生存分析。 此包包含函数`surv()`，它将输入数据作为R语言公式，并在选择的变量中创建一个生存对象用于分析。 然后我们使用函数`survfit()`创建一个分析图。

## 安装软件包

```R
install.packages("survival")
```

### 语法

在R语言中创建生存分析的基本语法是:
```
surv(time,event)
survfit(formula)
```

以下是所使用的参数的描述 -

- **time**是直到事件发生的跟踪时间。
- **event**指示预期事件的发生的状态。
- **formula**是预测变量之间的关系。

#### 练习：

我们将考虑在上面安装的生存包中存在的名为`pbc`的数据集。 它描述了关于受肝原发性胆汁性肝硬化（PBC）影响的人的生存数据点。 在数据集中存在的许多列中，我们主要关注字段`time`和`status`。 时间表示在接受肝移植或患者死亡的患者的登记和事件的较早之间的天数。

```R
# Load the library.
library("survival")

# Print first few rows.
print(head(pbc))
```

从上述数据，我们正在考虑分析的时间和状态。
应用`surv()`和`survfit()`函数
现在我们继续应用`surv()`函数到上面的数据集，并创建一个将显示趋势图。

```R
# Load the library.
library("survival")

# Create the survival object. 
survfit(Surv(pbc$time,pbc$status == 2)~1)

# Give the chart file a name.
png(file = "survival.png")

# Plot the graph. 
plot(survfit(Surv(pbc$time,pbc$status == 2)~1))

# Save the file.
dev.off()
```
上图中的趋势有助于我们预测在特定天数结束时的生存概率。
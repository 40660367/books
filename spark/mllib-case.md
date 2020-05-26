# Spark 案例:使用mllib实现基本统计功能

[环境准备](./setup.html)

给定一个数据集，数据分析师一般会先观察一下数据集的基本情况，称之为汇总统计或者概要性统计。一般的概要性统计用于概括一系列观测值，包括位置或集中趋势（比如算术平均值、中位数、众数和四分位均值），展型（比如四分位间距、绝对偏差和绝对距离偏差、各阶矩等），统计离差，分布的形状，依赖性等。除此之外，spark.mllib库也提供了一些其他的基本的统计分析工具，包括相关性、分层抽样、假设检验，随机数生成等。在本章，我们将从以下几个方面进行介绍：

- 概括统计 summary statistics
- 相关性 correlations
- 分层抽样 Stratified sampling
- 假设检验 hypothesis testing
- 随机数生成 random data generation
- 核密度估计 Kernel density estimation

```bash
cat /share/datasets/iris.data
```

Iris数据集也称鸢尾花卉数据集，是一类多重变量分析的数据集，是常用的分类实验数据集，由Fisher于1936收集整理。数据集包含150个数据集，分为3类，每类50个数据，每个数据包含4个属性。可通过花萼长度，花萼宽度，花瓣长度，花瓣宽度4个属性预测鸢尾花卉属于（Setosa，Versicolour，Virginica）三个种类中的哪一类。大家可以到这个链接下载该数据集：https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data。其基本的数据样子是：

## 摘要统计 Summary statistics

 对于RDD[Vector]类型的变量，Spark MLlib提供了一种叫colStats()的统计方法，调用该方法会返回一个类型为MultivariateStatisticalSummary的实例。通过这个实例看，我们可以获得每一列的最大值，最小值，均值、方差、总数等。具体操作如下所示：

 首先，我们导入必要的包：

```scala
import org.apache.spark.mllib.linalg.Vector
import org.apache.spark.mllib.stat.{MultivariateStatisticalSummary, Statistics}
```

接下来读取要分析的数据，把数据转变成RDD[Vector]类型：

```scala
val observations=sc.textFile("/share/datasets/iris.data").map(_.split(",")).map(p => Vectors.dense(p(0).toDouble, p(1).toDouble, p(2).toDouble, p(3).toDouble))
```

上面我们就把莺尾花的四个属性，即萼片长度，萼片宽度，花瓣长度和花瓣宽度存储在observations中，类型为RDD[Vector]。

 然后，我们调用colStats()方法，得到一个MultivariateStatisticalSummary类型的变量：

```scala
val summary: MultivariateStatisticalSummary = Statistics.colStats(observations)
```

 最后，依次调用统计方法，得到相应统计结果：

```scala
println(summary.count)150println(summary.mean)
println(summary.variance)
println(summary.min)
println(summary.normL1)
println(summary.normL2)
println(summary.numNonzeros)
```

 其中，主要方法的含义与返回值类型如下：

| 方法名      | 方法含义           | 返回值类型 |
| :---------- | :----------------- | :--------- |
| count       | 列的大小           | long       |
| mean        | 每列的均值         | vector     |
| variance    | 每列的方差         | vector     |
| max         | 每列的最大值       | vector     |
| min         | 每列的最小值       | vector     |
| normL1      | 每列的L1范数       | vector     |
| normL2      | 每列的L2范数       | vector     |
| numNonzeros | 每列非零向量的个数 | vector     |

## 随机数生成 Random data generation

 RandomRDDs 是一个工具集，用来生成含有随机数的RDD，可以按各种给定的分布模式生成数据集，Random RDDs包下现支持正态分布、泊松分布和均匀分布三种分布方式。

RandomRDDs提供随机double RDDS或vector RDDS。

下面的例子中生成一个随机double RDD，其值是标准正态分布
$$
N \sim (0,1)
$$


然后将其映射到
$$
N \sim (1,4)
$$


 首先，导入必要的包：

```scala
import org.apache.spark.SparkContextimport org.apache.spark.mllib.random.RandomRDDs._
```

 生成1000000个服从正态分配N(0,1)的RDD[Double]，并且分布在 10 个分区中：

```scala
val u = normalRDD(sc, 10000000L, 10)
```

把生成的随机数转化成N(1,4) 正态分布：

```scala
val v = u.map(x => 1.0 + 2.0 * x)
```

## 核密度估计 Kernel density estimation

Spark ML 提供了一个工具类 KernelDensity 用于核密度估算，核密度估算的意思是根据已知的样本估计未知的密度，属於非参数检验方法之一。核密度估计的原理是。观察某一事物的已知分布，如果某一个数在观察中出现了，可认为这个数的概率密度很大，和这个数比较近的数的概率密度也会比较大，而那些离这个数远的数的概率密度会比较小。

 首先，导入必要的包：

```scala
import org.apache.spark.mllib.stat.KernelDensityimport org.apache.spark.rdd.RDD
```

 同时留意到已经导入的数据：

```scala
val test = sc.textFile("/share/datasets/iris.data").map(_.split(",")).map(p => p(0).toDouble)
```

用样本数据构建核函数，这里用假设检验中得到的iris的第一个属性的数据作为样本数据进行估计：

```scala
val kd = new KernelDensity().setSample(test).setBandwidth(3.0)
```

其中setBandwidth表示高斯核的宽度，为一个平滑参数，可以看做是高斯核的标准差。

构造了核密度估计kd，就可以对给定数据数据进行核估计：

```scala
val densities = kd.estimate(Array(-1.0, 2.0, 5.0, 5.8))
```

在样本-1.0, 2.0, 5.0, 5.8等样本点上，其估算的概率密度函数值分别是：0.011372003554433524, 0.059925911357198915, 0.12365409462424519, 0.12816280708978114。

## 假设检验 Hypothesis testing

Spark支持皮尔森卡方检测（Pearson’s chi-squared tests），包括“适配度检定”（Goodness of fit）以及“独立性检定”（independence）。

首先，我们导入必要的包

```scala
import org.apache.spark.SparkContext
import org.apache.spark.mllib.linalg._
import org.apache.spark.mllib.regression.LabeledPoint
import org.apache.spark.mllib.stat.Statistics._
```

 接下来，我们从数据集中选择要分析的数据，比如说我们取出iris数据集中的前两条数据v1和v2。不同的输入类型决定了是做拟合度检验还是独立性检验。拟合度检验要求输入为Vector, 独立性检验要求输入是Matrix。

```scala
val v1: Vector = sc.textFile("/share/datasets/iris.data").map(_.split(",")).map(p => Vectors.dense(p(0).toDouble, p(1).toDouble, p(2).toDouble, p(3).toDouble)).first
```

```scala
val v2: Vector = sc.textFile("/share/datasets/iris.data").map(_.split(",")).map(p => Vectors.dense(p(0).toDouble, p(1).toDouble, p(2).toDouble, p(3).toDouble)).take(2).last
```

### 适合度检验 Goodness fo fit

Goodness fo fit（适合度检验）：验证一组观察值的次数分配是否异于理论上的分配。其 H0假设（虚无假设，null hypothesis）为一个样本中已发生事件的次数分配会服从某个特定的理论分配。实际执行多项式试验而得到的观察次数，与虚无假设的期望次数相比较，检验二者接近的程度，利用样本数据以检验总体分布是否为某一特定分布的统计方法。

通常情况下这个特定的理论分配指的是均匀分配，目前Spark默认的是均匀分配。以下是代码：

```scala
val goodnessOfFitTestResult = Statistics.chiSqTest(v1)
```

可以看到P值，自由度，检验统计量，所使用的方法，以及零假设等信息。我们先简单介绍下每个输出的意义：

method: 方法。这里采用pearson方法。

statistic： 检验统计量。简单来说就是用来决定是否可以拒绝原假设的证据。检验统计量的值是利用样本数据计算得到的，它代表了样本中的信息。检验统计量的绝对值越大，拒绝原假设的理由越充分，反之，不拒绝原假设的理由越充分。

degrees of freedom：自由度。表示可自由变动的样本观测值的数目，

pValue：统计学根据显著性检验方法所得到的P 值。一般以P < 0.05 为显著， P<0.01 为非常显著，其含义是样本间的差异由抽样误差所致的概率小于0.05 或0.01。

一般来说，假设检验主要看P值就够了。在本例中pValue =0.133，说明两组的差别无显著意义。通过V1的观测值[5.1, 3.5, 1.4, 0.2]，无法拒绝其服从于期望分配（这里默认是均匀分配）的假设。

### 独立性检验 Indenpendence

卡方独立性检验是用来检验两个属性间是否独立。其中一个属性做为行，另外一个做为列，通过貌似相关的关系考察其是否真实存在相关性。比如天气温变化和肺炎发病率。

首先，我们通过v1、v2构造一个举证Matrix，然后进行独立性检验：

```scala
val mat: Matrix =Matrices.dense(2,2,Array(v1(0),v1(1),v2(0),v2(1)))

val a =Statistics.chiSqTest(mat)
```

 这里所要检验是否独立的两个属性，一个是样本的序号，另一个是样本的数据值。在本例中pValue =0.91，说明无法拒绝“样本序号与数据值无关”的假设。这也符合数据集的实际情况，因为v1和v2是从同一个样本抽取的两条数据，样本的序号与数据的取值应该是没有关系的。

我们也可以把v1作为样本，把v2作为期望值，进行卡方检验：

```scala
val c1 = Statistics.chiSqTest(v1, v2)
```

本例中pValue =0.998，说明样本v1与期望值等于V2的数据分布并无显著差异。事实上，v1=[5.1,3.5,1.4,0.2]与v2= [4.9,3.0,1.4,0.2]很像，v1可以看做是从期望值为v2的数据分布中抽样出来的的。

同样的，键值对也可以进行独立性检验，这里我们取iris的数据组成键值对：

```scala
val data=sc.textFile("/share/datasets/iris.data")

val obs = data.map{ line =>
     |       val parts = line.split(',')
     |       LabeledPoint(if(parts(4)=="Iris-setosa") 0.toDouble else if (parts(4)=="Iris-versicolor") 1.toDouble else
     |       2.toDouble, Vectors.dense(parts(0).toDouble,parts(1).toDouble,parts
(2).toDouble,parts(3).toDouble))}
```

 进行独立性检验，返回一个包含每个特征对于标签的卡方检验的数组：

```scala
scala> val featureTestResults= Statistics.chiSqTest(obs)
```

 这里实际上是把特征数据中的每一列都与标签进行独立性检验。可以看出，P值都非常小，说明可以拒绝“某列与标签列无关”的假设。也就是说，可以认为每一列的数据都与最后的标签有相关性。我们用foreach把完整结果打印出来：

```scala
var i = 1
i: Int = 1

featureTestResults.foreach { result =>
     |   println(s"Column $i:\n$result")
     |   i += 1
     | }
```

spark也支持Kolmogorov-Smirnov 检验，下面将展示具体的步骤：

```scala
val test = sc.textFile("/share/datasets/iris.data").map(_.split(",")).map(p => p(0).toDouble)

// run a KS test for the sample versus a standard normal distribution

val testResult = Statistics.kolmogorovSmirnovTest(test, "norm", 0, 1)

val myCDF: Double => Double = (p=>p*2)

val testResult2 = Statistics.kolmogorovSmirnovTest(test, myCDF)
```


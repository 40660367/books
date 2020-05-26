# Spark 工作流(Pipelines)示例

本节以逻辑斯蒂回归为例，构建一个典型的机器学习过程，来具体介绍一下工作流是如何应用的。我们的目的是查找出所有包含”spark”的句子，即将包含”spark”的句子的标签设为1，没有”spark”的句子的标签设为0。Spark2.0起，`SQLContext`、`HiveContext`已经不再推荐使用，改以`SparkSession`代之，故本文中不再使用`SQLContext`来进行相关的操作，关于`SparkSession`的具体详情，这里不再赘述，可以参看Spark2.0的[官方文档](http://spark.apache.org/docs/latest/sql-programming-guide.html)。

## 环境准备

[环境准备](./setup.html)

## 示例 

Spark2.0以上版本的`spark-shell`在启动时会自动创建一个名为`spark`的`SparkSession`对象，当需要手工创建时，`SparkSession`可以由其伴生对象的`builder()`方法创建出来，如下代码段所示：

```scala
import org.apache.spark.sql.SparkSession
val spark = SparkSession.builder().
            master("local").
            appName("my App Name").
            getOrCreate()
```

和`SQLContext`一样，也可以开启`RDD`的隐式转换：

```scala
import spark.implicits._ 
```

下文中，我们默认名为`spark`的`SparkSession`已经创建。

然后，我们引入要包含的包并构建训练数据集。

```scala
import org.apache.spark.ml.feature._
import org.apache.spark.ml.classification.LogisticRegression
import org.apache.spark.ml.{Pipeline,PipelineModel}
import org.apache.spark.ml.linalg.Vector
import org.apache.spark.sql.Row
 
 
val training = spark.createDataFrame(Seq(
     |       (0L, "a b c d e spark", 1.0),
     |       (1L, "b d", 0.0),
     |       (2L, "spark f g h", 1.0),
     |       (3L, "hadoop mapreduce", 0.0)
     |     )).toDF("id", "text", "label")
training: org.apache.spark.sql.DataFrame = [id: bigint, text: string, label: double]
```

在这一步中我们要定义 Pipeline 中的各个工作流阶段PipelineStage，包括转换器和评估器，具体的，包含tokenizer, hashingTF和lr三个步骤。

```scala
val tokenizer = new Tokenizer().
     |       setInputCol("text").
     |       setOutputCol("words")
 
val hashingTF = new HashingTF().
     |       setNumFeatures(1000).
     |       setInputCol(tokenizer.getOutputCol).
     |       setOutputCol("features")
 
val lr = new LogisticRegression().
     |       setMaxIter(10).
     |       setRegParam(0.01)
```

有了这些处理特定问题的转换器和评估器，接下来就可以按照具体的处理逻辑有序的组织PipelineStages 并创建一个Pipeline。

```scala
val pipeline = new Pipeline().
     |       setStages(Array(tokenizer, hashingTF, lr))
```

现在构建的Pipeline本质上是一个Estimator，在它的fit（）方法运行之后，它将产生一个PipelineModel，它是一个Transformer。

```scala
val model = pipeline.fit(training)
```

我们可以看到，model的类型是一个PipelineModel，这个管道模型将在测试数据的时候使用。所以接下来，我们先构建测试数据。

```scala
val test = spark.createDataFrame(Seq(
     |       (4L, "spark i j k"),
     |       (5L, "l m n"),
     |       (6L, "spark a"),
     |       (7L, "apache hadoop")
     |     )).toDF("id", "text")
test: org.apache.spark.sql.DataFrame = [id: bigint, text: string]
```

然后，我们调用我们训练好的PipelineModel的transform()方法，让测试数据按顺序通过拟合的工作流，生成我们所需要的预测结果。

```scala
model.transform(test).
     |       select("id", "text", "probability", "prediction").
     |       collect().
     |       foreach { case Row(id: Long, text: String, prob: Vector, prediction: Double) =>
     |         println(s"($id, $text) --> prob=$prob, prediction=$prediction")
     |       }
```

通过上述结果，我们可以看到，第4句和第6句中都包含”spark”，其中第六句的预测是1，与我们希望的相符；而第4句虽然预测的依然是0，但是通过概率我们可以看到，第4句有46%的概率预测是1，而第5句、第7句分别只有7%和2%的概率预测为1，这是由于训练数据集较少，如果有更多的测试数据进行学习，预测的准确率将会有显著提升。
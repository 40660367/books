#  Spark PySpark读取HDFS数据分析示例

## MovieLens 100k数据集介绍

MovieLens 100k数据集包含表示多个用户对多部电影的10万次评级数据,也包含电影元数据和用户属性信息。

该数据集不大,方便下载和用Spark程序快速处理,故适合做讲解示例。

## Hadoop及Spark环境准备

[Hadoop环境准备](/hadoop/setup.html)，[Spark环境准备](/spark/setup.html)

## 将数据上传至HDFS

```bash
hadoop fs -mkdir -p /pyspark/ml-100k/ 
fs -put /share/datasets/ml-100k/* /pyspark/ml-100k/
```

## 安装pyspark库

```bash
pip install pyspark -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

## Python源文件

```python
from pyspark import SparkContext,SparkConf  
import numpy as np  
import os  
os.environ['PYSPARK_PYTHON']='/usr/bin/python3'  
os.environ['JAVA_HOME'] = '/usr/local/java'  
conf=SparkConf().setMaster("local[2]").setAppName("movie_info_analyse")  
sc=SparkContext(conf=conf)  

# 加载HDFS上面的用户数据  
user_data = sc.textFile("hdfs://localhost:9000/pyspark/ml-100k/u.user")  
# 用"|"分割符分割每一行的数据，然后将数据返回到user_fields  
user_fields = user_data.map(lambda line: line.split("|"))  
# 统计总的用户数  
num_users = user_fields.map(lambda fields: fields[0]).count()  
#从HDFS中加载u.item数据  
movie_data = sc.textFile("hdfs://localhost:9000/pyspark/ml-100k/u.item")  
#统计电影总数  
num_movies = movie_data.count()  
#从HDFS上面加载用户评分数据  
rating_data = sc.textFile("hdfs://localhost:9000/pyspark/ml-100k/u.data")  
print(rating_data.first())  
#统计评分记录总数

num_ratings = rating_data.count()  
print("Ratings: %d" % num_ratings)  
#使用"\t"符分割每行数据  
rating_data = rating_data.map(lambda line: line.split("\t"))  
#获取每条数据中的用户评分数集合  
ratings = rating_data.map(lambda fields: int(fields[2]))  
#获取最大评分数  
max_rating = ratings.reduce(lambda x, y: max(x, y))  
#获取最小评分数  
min_rating = ratings.reduce(lambda x, y: min(x, y))  
#获取平均评分数  
mean_rating = ratings.reduce(lambda x, y: x + y) / num_ratings  
#获取评分中位数  
median_rating = np.median(ratings.collect())  
#每位用户平均评分  
ratings_per_user = num_ratings / num_users  
#每位用户评了几场电影  
ratings_per_movie = num_ratings / num_movies  
#打印上面这些信息  
print("Min rating: %d" % min_rating)  
print("Max rating: %d" % max_rating)  
print("Average rating: %2.2f" % mean_rating)  
print("Median rating: %d" % median_rating)  
print("Average # of ratings per user: %2.2f" % ratings_per_user)  
print("Average # of ratings per movie: %2.2f" % ratings_per_movie)  
#获取评分数据  
count_by_rating = ratings.countByValue()  
#x轴的显示每个评分（1-5）  
x_axis = count_by_rating.keys()  
#y轴显示每个评分所占概率，总概率和为1  
y_axis = np.array([float(c) for c in count_by_rating.values()])  
y_axis_normed = y_axis / y_axis.sum()  
pos = np.arange(len(x_axis))  
width = 1.0  
#使用matplotlib生成柱状图  
from matplotlib import pyplot as plt2  
ax = plt2.axes()  
ax.set_xticks(pos + (width / 2))  
ax.set_xticklabels(list(x_axis))  
plt2.bar(pos, y_axis_normed, width, color='lightblue')  
plt2.xticks(rotation=30)  
fig = plt2.gcf()  
fig.set_size_inches(16, 10)  
plt2.show()  
```


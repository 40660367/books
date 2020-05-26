# Hadoop YARN配置及提交任务示例

Yarn的配置及启动请参见[Hadoop安装](./setup.html)中的Hadoop配置部分。

## 提交任务至Yarn示例

向 YARN 以 jar 包的方式提交作业，假设 jar 包为 `example.jar` 格式为：

```
hadoop jar jar包名 应用名 输入路径 输出路径
```

例如：

```bash
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-examples-2.9.2.jar wc
```

## 查看当前jobs

```bash
hadoop jobs
```


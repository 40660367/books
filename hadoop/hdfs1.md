# Hadoop HDFS示例1:读取 HDFS文件内容

[环境准备](./setup.html)

## 准备相关文件

文件名:FileSystemCat.java

```java
import java.io.InputStream;

import java.net.URI;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.*;
import org.apache.hadoop.io.IOUtils;

public class FileSystemCat {
    public static void main(String[] args) throws Exception {
        String uri = args[0];
        Configuration conf = new Configuration();
        FileSystem fs = FileSystem. get(URI.create (uri), conf);
        InputStream in = null;
        try {
            in = fs.open( new Path(uri));
            IOUtils.copyBytes(in, System.out, 4096, false);
        } finally {
            IOUtils.closeStream(in);
        }
    }
}
```

文件名:quangle.txt
```txt
On the top of the Crumpetty Tree
The Quangle Wangle sat,
But his face you could not see,
On account of his Beaver Hat.
```

### 创建任务目录，并复制相关文件

```bash
mkdir ~/hdfs1 && cd ~/hdfs1
cp /share/lesson/hadoop/FileSystemCat.java .
cp /share/lesson/hadoop/quangle.txt .
cp /share/lesson/hadoop/hadoop-core-1.2.1.jar .
```

### 编译java文件

```bash
cd ~/hdfs1
javac -classpath hadoop-core-1.1.2.jar FileSystemCat.java
```

## 上传文件至HDFS文件系统

```bash
cd ~/hdfs1
hadoop fs -mkdir -p /hdfs1
hadoop fs -copyFromLocal quangle.txt /hdfs1/quangle.txt
hadoop fs -ls /hdfs1
```

## 验证:

使用如下命令读取 HDFS 中 `/hdfs1/quangle.txt` 内容：

```bash
hadoop FileSystemCat /hdfs1/quangle.txt
```

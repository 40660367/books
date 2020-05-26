# Hadoop HDFS示例2:写入内容至HDFS文件

[环境准备](./setup.html)

在本地文件系统生成一个大约 100 字节的文本文件，写一段程序读入这个文件并将其第 101-120 字节的内容写入 HDFS 成为一个新文件。

## 准备相关文件

文件名:LocalFile2Hdfs.java

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.OutputStream;
import java.net.URI;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FSDataInputStream;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IOUtils;
import org.apache.hadoop.util.Progressable;

public class LocalFile2Hdfs {
    public static void main(String[] args) throws Exception {

        // 获取读取源文件和目标文件位置参数
        String local = args[0];
        String uri = args[1];

        FileInputStream in = null;
        OutputStream out = null;
        Configuration conf = new Configuration();
        try {
            // 获取读入文件数据
            in = new FileInputStream(new File(local));

            // 获取目标文件信息
            FileSystem fs = FileSystem.get(URI.create(uri), conf);
            out = fs.create(new Path(uri), new Progressable() {
                @Override
                public void progress() {
                    System.out.println("*");
                }
            });

            // 跳过前100个字符
            in.skip(100);
            byte[] buffer = new byte[20];

            // 从101的位置读取20个字符到buffer中
            int bytesRead = in.read(buffer);
            if (bytesRead >= 0) {
                out.write(buffer, 0, bytesRead);
            }
        } finally {
            IOUtils.closeStream(in);
            IOUtils.closeStream(out);
        }
    }
}
```

文件名:local2hdfs.txt

```txt
Washington (CNN) -- Twitter is suing the U.S. government in an effort to loosen restrictions on what the social media giant can say publicly about the national security-related requests it receives for user data.
The company filed a lawsuit against the Justice Department on Monday in a federal court in northern California, arguing that its First Amendment rights are being violated by restrictions that forbid the disclosure of how many national security letters and Foreign Intelligence Surveillance Act court orders it receives -- even if that number is zero.
Twitter vice president Ben Lee wrote in a blog post that it's suing in an effort to publish the full version of a "transparency report" prepared this year that includes those details.
The San Francisco-based firm was unsatisfied with the Justice Department's move in January to allow technological firms to disclose the number of national security-related requests they receive in broad ranges.
```

### 创建任务目录，并复制相关文件

```bash
mkdir ~/hdfs2 && cd ~/hdfs2
cp /share/lesson/hadoop/LocalFile2Hdfs.java .
cp /share/lesson/hadoop/local2hdfs.txt .
cp /share/lesson/hadoop/hadoop-core-1.2.1.jar .
```

### 编译java文件

```bash
cd ~/hdfs2
javac -classpath hadoop-core-1.1.2.jar LocalFile2Hdfs.java
```

## 使用java程序上传文件内容到 HDFS

```bash
hadoop fs -mkdir -p /hdfs2
cd ~/hdfs2
hadoop LocalFile2Hdfs local2hdfs.txt /hdfs2/local2hdfs_part.txt
hadoop fs -ls /hdfs2
```

## 验证是否成功

使用如下命令读取 HDFS 中 `/hdfs2/local2hdfs_part.txt` 内容：

```bash
hadoop fs -cat /hdfs2/local2hdfs_part.txt
```

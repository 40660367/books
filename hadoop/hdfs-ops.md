# Hadoop HDFS Shell操作

## HDFS操作实验：

[环境准备](./setup.html)。

### 将数据插入到HDFS

假设在本地系统，这是所谓的file.txt文件中的数据,应当保存在HDFS文件系统。按照下面给出插入在Hadoop的文件系统所需要的文件的步骤。

先创建一个输入目录。

```
hadoop fs -mkdir -p /usr/input
```

传输并使用本地系统put命令，Hadoop文件系统中存储的数据文件。

```
hadoop fs -put /etc/passwd /usr/input
```

可以使用ls命令验证文件。

```
hadoop fs -ls /usr/input
```

### 从HDFS中检索数据

**使用上一节中已经存入HDFS文件系统/usr/input/路径下passwd文件。**

下面给出的是一个简单的演示用于检索从Hadoop文件系统所需的文件。

最初，使用cat命令来查看来自HDFS的数据。

```
hadoop fs -cat /usr/input/passwd
```

从HDFS复制文件到本地文件系统，使用get命令

```
hadoop fs -get /usr/input/passwd ~/
```

验证

```bash
cat ~/passwd
```

### HDFS的文件列表

加载服务器信息后，使用'ls' 可以找出文件列表中的目录，文件状态。下面给出的是ls，可以传递一个目录或文件名作为参数的语法。

```
hadoop fs -ls /
```

### 关闭HDFS

可以使用下面的命令关闭HDFS。

```
stop-dfs.sh
```



## 常用HDFS命令参考

**1. -help：显示帮助信息**

```
hadoop fs -help rm
```

 **2. -ls：显示目录信息**

```
hadoop fs -ls /
```

 **3. -mkdir：在HDFS上创建目录**

```
hadoop fs -mkdir -p /user/test
```

 **4. -moveFromLocal：从本地剪切粘贴到HDFS**

```
hadoop fs -moveFromLocal ~/test.txt /home/root/
```

 **5. -appendToFile：追加一个文件到已经存在的文件末尾**

```
hadoop fs -appendToFile /a.txt /b.txt
```

 **6. -cat：显示文件内容**

```
hadoop fs -cat /user/root/a.txt
```

 **7. -chmod、-chown：修改文件权限、所有者**

```
hadoop fs -chmod 777 /a.txt
hadoop fs -chown admin:root /a.txt
```

 **8. -copyFromLocal：从本地文件系统中拷贝文件到HDFS中**

```
hadoop fs -copyFromLocal a.txt /
```

 **9. copyToLocal：从HDFS拷贝到本地**

```
hadoop fs -copyToLocal /a.txt ~/
```

 **10. -cp：在HDFS中拷贝文件**

```
hadoop fs -cp /aaa/a.txt /bbb/
```

 **11. -mv：在HDFS目录中移动文件**

```
hadoop fs -mv /aaa/a.txt /bbb/ 
```

 **12. -get：从HDFS中拷贝到本地，等同于copyToLocal**

```
hadoop fs -get /aaa/a.txt
```

 **13. -getmerge：合并下载多个文件**

```
hadoop fs -getmerge /logs/* ~/logs.log # 将HDFS上/logs/路径下的所有文件合并下载到本地~/logs.log文件中
```

 **14. -put：将本地文件上传到HDFS，等同于copyFromLocal**

```
hadoop fs -put ~/a.txt /
```

 **15. -tail：显示文件末尾的内容** 

```
hadoop fs -tail /a.txt
```

 **16. -rm：删除文件夹或者文件**

```
hadoop fs -rm /user/root/a.txt
```

 **17. -rmdir：删除空目录**

```
hadoop fs -mkdir /temp
```

 **18. -du：统计文件夹的大小信息**

```
hadoop fs -du -s -h /temp
```

 **19. -setrep：设置HDFS文件中的副本数量**

```
hadoop fs -setrep 5 /a.txt
```

**hadoop fsck**

**hadoop dfsadmin**

运行一个 HDFS 的 dfsadmin 客户端。

```bash
# 报告文件系统的基本信息和统计信息
hadoop dfsadmin -report

hadoop dfsadmin -safemode enter | leave | get | wait
# 安全模式维护命令。安全模式是 Namenode 的一个状态，这种状态下，Namenode
# 1. 不接受对名字空间的更改(只读)
# 2. 不复制或删除块
# Namenode 会在启动时自动进入安全模式，当配置的块最小百分比数满足最小的副本数条件时，会自动离开安全模式。安全模式可以手动进入，但是这样的话也必须手动关闭安全模式。
```

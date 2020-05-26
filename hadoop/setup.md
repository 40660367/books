# Hadoop 环境安装及配置

## 本课程在线环境的安装-模拟分布式安装

### 配置SSH免密登陆

首先执行以下命令，生成公钥和私钥对

```bash
ssh-keygen -t rsa 
```

此时会有多处提醒输入在冒号后输入文本，这里主要是要求输入ssh密码以及密码的放置位置。在这里，只需要使用默认值，按四次回车即可。公钥和私钥已经生成后放置在~/.ssh目录下。

将存储公钥文件的id_rsa.pub里的内容，追加到authorized_keys中。

```bash
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
```

执行ssh 0.0.0.0测试ssh配置连接本机的配置

```bash
ssh 0.0.0.0
```

第一次使用ssh访问，会提醒是否继续连接，输入“yes"继续进行，执行完以后**一定要使用**`exit`命令退出。后续再执行`ssh 0.0.0.0`时，就不用输入密码了。

### 安装JDK和Hadoop

**安装JDK**

```bash
cp /share/tar/jdk-8u241-linux-x64.tar.gz  /usr/local/
#tar -xzvf 对文件进行解压缩，-C 指定解压后，将文件放到/usr/local目录下。
tar -xzvf /usr/local/jdk-8u241-linux-x64.tar.gz -C /usr/local/
mv /usr/local/jdk1.8.0_241 /usr/local/java
```

下面来修改环境变量：系统环境变量或用户环境变量。

```bash
echo 'export JAVA_HOME=/usr/local/java' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc  #生效环境变量
#验证java安装，测试环境变量是否配置正确。如果出现正确的版本信息提示，则安装成功
java -version
```

**安装Hadoop**

```bash
cp /share/tar/hadoop-2.9.2.tar.gz  /usr/local/
tar -xzvf /usr/local/hadoop-2.9.2.tar.gz -C /usr/local/
mv /usr/local/hadoop-2.9.2 /usr/local/hadoop
```

修改用户环境变量，将hadoop的路径添加到path中。

```bash
echo 'export HADOOP_HOME=/usr/local/hadoop' >> ~/.bashrc
echo 'export PATH=$HADOOP_HOME/bin:$PATH' >> ~/.bashrc
echo 'export PATH=$HADOOP_HOME/sbin:$PATH' >> ~/.bashrc
echo 'export HADOOP_MAPRED_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_COMMON_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_HDFS_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export YARN_HOME=$HADOOP_HOME' >> ~/.bashrc
echo 'export HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native' >> ~/.bashrc
echo 'export PATH=$PATH:$HADOOP_HOME/sbin:$HADOOP_HOME/bin' >> ~/.bashrc
echo 'export HADOOP_INSTALL=$HADOOP_HOME' >> ~/.bashrc
source ~/.bashrc  #生效环境变量

cd $HADOOP_HOME/etc/hadoop 
echo 'export JAVA_HOME=/usr/local/java' >> hadoop-env.sh

#验证hadoop环境变量配置是否正常，如果出现正确的版本信息提示，则安装成功。
hadoop version 
```

### 配置Hadoop

修改hadoop相关的配置。首先切换到hadoop配置目录`$HADOOP_HOME`。

####　**修改core-site.xml**

core-site.xml文件中包含如读/写缓冲器用于Hadoop的实例的端口号的信息，分配给文件系统存储，用于存储所述数据存储器的限制和大小。

```bash
#打开core-site.xml配置文件
vim $HADOOP_HOME/etc/hadoop/core-site.xml
```
打开core-site.xml文件，在<configuration></configuration>标签之间添加以下属性。

```xml
<property> 
<name>hadoop.tmp.dir</name> 
<value>/data/tmp/hadoop/tmp</value> 
</property> 

<property> 
<name>fs.defaultFS</name> 
<value>hdfs://localhost:9000</value> 
</property> 
```

####　**修改hdfs-site.xml**

hdfs-site.xml 文件中包含如复制数据的值，NameNode路径的信息，，本地文件系统的数据节点的路径。这意味着是存储Hadoop基础工具的地方。

```bash
vim $HADOOP_HOME/etc/hadoop/hdfs-site.xml
```

打开hdfs-site.xml文件，在<configuration></configuration>标签之间添加以下属性。

```xml
<property>
  <name>dfs.replication</name>
  <value>1</value>
</property>

<property>
  <name>dfs.name.dir</name>
  <value>file:///home/hadoop/hadoopinfra/hdfs/namenode </value>
</property>

<property>
  <name>dfs.data.dir</name> 
  <value>file:///home/hadoop/hadoopinfra/hdfs/datanode </value> 
</property>
```

配置项说明：

```
dfs.namenode.name.dir，配置元数据信息存储位置；
dfs.datanode.data.dir，配置具体数据存储位置；
dfs.replication，配置每个数据库备份数，由于目前我们使用1台节点，所以设置为1，如果设置为2的话，运行会报错。
dfs.permissions.enabled，配置hdfs是否启用权限认证
```

####　**修改mapred-site.xml**

此文件用于指定正在使用MapReduce框架。缺省情况下，包含Hadoop的模板yarn-site.xml。

首先，它需要从mapred-site.xml复制。获得mapred-site.xml模板文件，并编辑这个文件。

```bash
cd $HADOOP_HOME/etc/hadoop
cp mapred-site.xml.template mapred-site.xml 
vim mapred-site.xml 
```

打开mapred-site.xml文件，添加下面配置到<configuration>与</configuration>标签之间。

```xml
<property> 
  <name>mapreduce.framework.name</name>
  <value>yarn</value>
</property>
```

####　**修改yarn-site.xml**

```bash
vim $HADOOP_HOME/etc/hadoop/yarn-site.xml
```

打开 yarn-site.xml文件，在<configuration></configuration>标签之间添加以下属性。

```xml
<property>
  <name>yarn.nodemanager.aux-services</name>
  <value>mapreduce_shuffle</value> 
</property>
```

### 验证Hadoop模拟分布集群
#### 启动HDFSS(耗时两分钟左右)

格式化配置HDFS文件系统，打开NameNode(HDFS服务器)，然后执行以下命令。

```bash
hdfs namenode -format 
```
格式化HDFS后，启动分布式文件系统。以下命令将启动名称节点和数据节点的集群。

```bash
start-dfs.sh
```

将实验区窗口切换为VNC模式，打开FireFox浏览器，

在地址栏输入`localhost:50070`进入HDFS的web界面

#### 启动Yarn

```bash
start-yarn.sh
```
验证所有应用程序的集群:访问{url},集群中的所有应用程序的默认端口号为8088

将实验窗口切换为VNC模式，打开FireFox浏览器，

在地址栏输入`localhost：8088`进入yarn集群任务管理界面

#### 命令jps命令进行验证

 ```bash
jps
 ```

当有后台运行的相关进程提示时，即证明您已经在您当前的云环境中安装成功，您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**
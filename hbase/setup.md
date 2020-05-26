# HBase 环境安装配置 			

## 本课程在线环境的安装-单机模式
### 安装JDK
**安装JDK**

```bash
cp /share/tar/jdk-8u241-linux-x64.tar.gz  /usr/local/
#tar -xzvf 对文件进行解压缩，-C 指定解压后，将文件放到/usr/local目录下。
tar -xzvf /usr/local/jdk-8u241-linux-x64.tar.gz -C /usr/local/
mv /usr/local/jdk1.8.0_241 /usr/local/java
```

下面来修改环境变量：系统环境变量或用户环境变量。我们在这里修改用户环境变量。

```bash
echo 'export JAVA_HOME=/usr/local/java' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc  #生效环境变量
#验证java安装，测试环境变量是否配置正确。如果出现正确的版本信息提示，则安装成功
java -version
```

### 安装HBase

**准备HBase安装文件**

```bash
cp /share/tar/hbase-2.2.4-bin.tar.gz  /usr/local/
tar -xzvf /usr/local/hbase-2.2.4-bin.tar.gz -C /usr/local/
mv /usr/local/hbase-2.2.4 /usr/local/hbase
```

**配置HBase**

```bash
echo 'export HABASE_HOME=/usr/local/hbase' >> ~/.bashrc
echo 'export PATH=$PATH:$HABASE_HOME/bin:$HABASE_HOME/sbin' >> ~/.bashrc
source ~/.bashrc  #生效环境变量
```

**hbase-env.sh**

为HBase设置Java目录，并从conf文件夹打开hbase-env.sh文件。编辑JAVA_HOME环境变量，改变路径到当前JAVA_HOME变量，如下图所示。

```bash
cd $HABASE_HOME/conf
echo 'export JAVA_HOME=/usr/local/java' >> hbase-env.sh
```

### 启动HBase

```bash
#启动HBase
start-hbase.sh
```

启动后使用`jps`命令查看，当出现`HMaster`进程时，代表Hbase已经启动成功

您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**

### 使用HBasse

**使用HBase Shell**

```bash
#启动HBase Shell需要耐心等待两分钟左右
hbase shell
```

看到`hbase(main):001:0> `提示符，就代表可正常使用HBase了。

**使用HBase Web UI**

在右侧vnc界面中打开浏览器，在地址栏中输入`localhost:16030`
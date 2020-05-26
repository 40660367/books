# Scala 环境安装及配置

## 本课程在线环境的安装

### 安装JDK

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

### 安装Scala

```bash
cp /share/tar/scala-2.12.11.tgz /usr/local/
tar -xzvf /usr/local/scala-2.12.11.tgz -C /usr/local/
mv /usr/local/scala-2.12.11 /usr/local/scala
```

```bash
echo 'export PATH=/usr/local/scala/bin:$PATH' >> ~/.bashrc
echo 'export SCALA_HOME=/usr/local/scala' >> ~/.bashrc
source ~/.bashrc  #生效环境变量
scala -version
```

当有版本提示时，即证明您已经在您当前的云环境中安装成功，您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**




# Hive 安装及环境配置

## 本课程在线环境的安装

### Hadoop安装配置

请先进行[Hadoop安装及环境配置](/hadoop/setup.html)

### MySQL配置
请先进行[MySQL安装配置](/mysql/setup.html)

安装并成功启动MySQL之后 ，需要创建hive用到的数据库`hive`，用户名`hive`及密码`hive123`，并对用户进行赋权并刷新生效，以创建Hive的MetaStore数据库。

```mysql
CREATE DATABASE hive;
CREATE USER hive identified by 'hive123';
GRANT ALL PRIVILEGES ON *.* TO 'hive'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

### 安装Hive

**下载Hive**

我们在本教程中使用hive-0.14.0。可以通过访问以下链接下载 [http://apache.petsads.us/hive/hive-0.14.0/.](http://apache.petsads.us/hive/hive-0.14.0/) 假设它下载到/Downloads目录。在这里，我们下载一个名为“apache-hive-0.14.0-bin.tar.gz”的Hive存档。下面的命令用来验证的下载：

```bash
cp /share/tar/apache-hive-3.1.2-bin.tar.gz /usr/local
tar -xzvf /usr/local/apache-hive-3.1.2-bin.tar.gz -C /usr/local/
mv /usr/local/apache-hive-3.1.2-bin/ /usr/local/hive
```

**设置Hive环境**

可以设置Hive环境，通过附加以下行到〜/.bashrc文件中：

```bash
echo 'export HIVE_HOME=/usr/local/hive' >> ~/.bashrc
echo 'export PATH=$PATH:$HIVE_HOME/bin' >> ~/.bashrc
echo 'export CLASSPATH=$CLASSPATH:/usr/local/hadoop/lib/*:.' >> ~/.bashrc
echo 'export CLASSPATH=$CLASSPATH:/usr/local/hive/lib/*:.' >> ~/.bashrc

source ~/.bashrc

#配置Hive用于Hadoop环境中
cd $HIVE_HOME/conf && cp hive-env.sh.template hive-env.sh
echo 'export HADOOP_HOME=/usr/local/hadoop' >> hive-env.sh
```

### 外部数据库服务器配置Metastore。

**创建hive-site.xml**

```bash
cat > $HIVE_HOME/conf/hive-site.xml  << EOF
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
<configuration>
<property>
    <name>javax.jdo.option.ConnectionURL</name>
    <value>jdbc:mysql://localhost/hive?useSSL=false</value>
</property>
<property>
    <name>javax.jdo.option.ConnectionDriverName</name>
    <value>com.mysql.cj.jdbc.Driver</value>
</property>
<property>
    <name>javax.jdo.option.ConnectionUserName</name>
    <value>hive</value>
</property>
<property>
    <name>javax.jdo.option.ConnectionPassword</name>
    <value>hive123</value>
</property>
</configuration>
EOF
```

**复制MySQL驱动文件**

```bash
cp /share/jar/mysql-connector-java-6.0.6.jar $HIVE_HOME/lib/
```

**初始化数据库**

```bash
$HIVE_HOME/bin/schematool -initSchema --dbType mysql --verbose
```

等到终端提示`schemaTool completed`时，说明Hive数据库已经初始化完成

## 进入hive环境

在Linux下输入

```bash
hive
```

即进入hive环境，在`hive>`后面即可输入命令。

到此，环境配置完成，您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**
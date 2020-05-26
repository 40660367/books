# elasticsearch 环境安装及配置 			

## 本课程在线环境的安装

### 创建专用用户并设置密码

```bash
mkdir /home/es && useradd es -d /home/es
chown -R es:es /home/es && chmod 760 /home/es
#切换至elasticsearch专用用户es
su es
```

### 安装ElasticSearch

```bash
cd /home/es/
cp /share/tar/elasticsearch-7.6.2-linux-x86_64.tar.gz /home/es
#对文件进行解压缩，-C 指定解压后，将文件放到/usr/local目录下。
tar -xzvf elasticsearch-7.6.2-linux-x86_64.tar.gz 
mv elasticsearch-7.6.2 /home/es/elasticsearch

#开户elasticsearch服务
/home/es/elasticsearch/bin/elasticsearch &
#切换回root用户
exit
```

```bash
#耐心等待约两分钟左右的启动时间后
#使用如下命令验证es服务是否正常开启
curl localhost:9200
```

当看到有json格式的类似信息返回时，即证明您已经在您当前的云环境中安装成功，您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**
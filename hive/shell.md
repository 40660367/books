# Hive Shell的基本操作

## Hive CIi(Hive Shell)

1、上面的 hive 命令相当于在启动的时候执行：**hive --service cli**
2、使用 **hive --help**，可以查看 hive 命令可以启动那些服务
3、通过 **hive --service serviceName --help** 可以查看某个具体命令的使用方式

## 变量和属性

### set命令
用来显示和修改变量。

**显示单个变量。**

```hql
set system:user.dir;
```

会出现`system:user.dir=/root`的提示。

显示全部变量和属性: 只使用set命令，显示所有变量和属性，包括varconf，env，system和hiveconf。

```bash
set;
```


### hivevar 用户自定义变量

```bash
hive --define testkey=testvalue
```

```
set hivevar:testkey;
```

```
set hivevar:testkey2=testvalue2;
```

### hiveconf hive相关的配置属性

用于对hive相关的配置。
**方法1：**
Hive启动时，通过--hiveconf配置。比如配置显示当前所在的数据库，该值默认为false。

```bash
hive --hiveconf hive.cli.print.current.db=true
```

进入Hive Shell后，`hive`提示后跟有当前正在操作的数据库

**方法2：**
Hive启动后，通过set设置。

```hql
set hive.cli.print.current.db=true;
```

## HQL执行方式
方法1：启动Hive CLI运行交互式Hive Shell
方法2：通过添加-e的参数执行一次HQL语句。-S参数用来去掉输出中的执行时间“Time taken: seconds”和“OK”，下面的语句将显示show databases的结果。

```bash
hive -S -e "show databases" 
```

方法3:在shell内通过hql脚本文件执行

```bash
echo "show databases" > ~/test.hql
hive
```

```hql
source ./test.hql;
```

## Hive shell的其他用法

直接在hive shell中执行一些操作系统命令，只要在命令前加上`!`。有点像是Jupyter Notebook的魔法函数。

```
!pwd;
```

直接在Hive shell中操作hdfs。只要去掉命令前面的hdfs即可。

```
dfs -ls /user/hive/warehouse/;
```
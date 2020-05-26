# R语言 包(library)

R语言的包是R函数，编译代码和样本数据的集合。 它们存储在R语言环境中名为library的目录下。 默认情况下，R语言在安装期间安装一组软件包。 随后添加更多包，当它们用于某些特定目的时。 当我们启动R语言控制台时，默认情况下只有默认包可用。 已经安装的其他软件包必须显式加载以供将要使用它们的R语言程序使用。

所有可用的R语言包都列在R语言的包。

下面是用于检查，验证和使用R包的命令列表。

## 检查可用R语言的包

获取包含R包的库位置

```R
.libPaths()
```

当我们执行上面的代码，它产生结果可能会根据您的电脑的本地设置而有所不同。

## 获取已安装的所有软件包列表

```R
library()
```

当我们执行上面的代码，它产生结果可能会根据您的电脑的本地设置而有所不同。


获取当前在R环境中加载的所有包

```R
search()
```

当我们执行上面的代码，它产生结果可能会根据您的电脑的本地设置而有所不同。

## 安装一个新的软件包

有两种方法来添加新的R包。 一个是直接从CRAN目录安装，另一个是将软件包下载到本地系统并手动安装它。

### 直接从CRAN安装

以下命令直接从CRAN网页获取软件包，并将软件包安装在R环境中。 可能会提示您选择最近的镜像。 根据您的位置选择一个。

```R
install.packages("Package Name")

# Install the package named "XML".
install.packages("XML")
```

### 手动安装包

转到链接

下载所需的包。 将包作为.zip文件保存在本地系统中的适当位置。

现在您可以运行以下命令在R环境中安装此软件包。

```R
install.packages(file_name_with_path, repos = NULL, type = "source")

# Install the package named "XML"
install.packages("E:/XML_3.98-1.3.zip", repos = NULL, type = "source")
```

## 装载包到库中

在包可以在代码中使用之前，必须将其加载到当前R环境中。 您还需要加载先前已安装但在当前环境中不可用的软件包。

使用以下命令加载包：

```R
library("package Name", lib.loc = "path to library")

# Load the package named "XML"
install.packages("/a.zip", repos = NULL, type = "source")
```
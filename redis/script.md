# Redis 脚本

Redis脚本用于使用Lua解释器来执行脚本。从`Redis 2.6.0`版开始内置到Redis中。使用脚本的命令是**EVAL**命令。

## 语法

以下是`EVAL`命令的基本语法。

```
EVAL script numkeys key [key ...] arg [arg ...]
```

## Redis事务命令

下表列出了与Redis脚本相关的一些基本命令。

| 序号 | 命令                                          | 说明                              |
| ---- | --------------------------------------------- | --------------------------------- |
| 1    | EVAL script numkeys key [key …\] arg [arg …]  | 执行一个Lua脚本。                 |
| 2    | EVALSHA sha1 numkeys key [key …\] arg [arg …] | 执行一个Lua脚本。                 |
| 3    | SCRIPT EXISTS script [script …\]              | 检查脚本缓存中是否存在脚本。      |
| 4    | SCRIPT FLUSH                                  | 从脚本缓存中删除所有脚本。        |
| 5    | SCRIPT KILL                                   | 杀死当前正在执行的脚本。          |
| 6    | SCRIPT LOAD script                            | 将指定的Lua脚本加载到脚本缓存中。 |

## 动手试一下

**[环境准备](./setup.html)**

**示例**

以下示例说明了Redis脚本的工作原理。

```bash
EVAL "return {KEYS[1],KEYS[2],ARGV[1],ARGV[2]}" 2 key1 key2 first second  
```

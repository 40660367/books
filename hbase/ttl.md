# HBase 生存时间（TTL）

ColumnFamilies 可以以秒为单位来设置 TTL（Time To Live）长度，一旦达到到期时间，HBase 将自动删除行。这适用于所有版本的行 - 即使是当前版本。在该 HBase 行的中编码的TTL时间以UTC指定。

仅在小型压缩时删除包含过期行的存储文件。设置 hbase.store.delete.expired.storefile 为 false 将禁用此功能。将最小版本数设置为 0 以外的值也会禁用此功能。

最近的 HBase 版本也支持设置时间以每个单元为基础生存。单元 TTL 是使用突变 ＃setTTL 作为突变请求（例如：Appends、Increments、Puts）的属性提交的。如果设置了 TTL 属性，则该操作将应用于服务器上更新的所有单元。单元 TTL 处理和 ColumnFamily TTL 之间有两个显着的区别：

- 单元 TTL 以毫秒为单位而不是秒。
- 单元 TTL 不能将一个单元的有效生命周期延长超过 ColumnFamily 级 TTL 设置。
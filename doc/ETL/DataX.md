

## DataX

> DataX 是阿里巴巴集团内被广泛使用的`离线数据同步工具`/平台，实现包括 MySQL、Oracle、SqlServer、Postgre、HDFS、Hive、ADS、HBase、TableStore(OTS)、MaxCompute(ODPS)、DRDS 等各种`异构数据源`之间高效的数据同步功能。

## Sqoop

> Sqoop(发音: skup)是一款开源的工具，主要用于在Hadoop(Hive)与`传统的数据库`(mysql、postgresql...)间进行数据的传递，可以将一个关系型数据库（例如 ： MySQL ,Oracle ,Postgres等）中的数据导进到Hadoop的`HDFS`中，也可以将HDFS的数据导进到关系型数据库中。
*  Sqoop是一个用来将Hadoop和RDB中的数据相互转移的工具, RDB <--> HDFS.
*  Sqoop专为大数据`批量传输`设计，能够`分割数据集`并创建Hadoop任务来处理每个区块。

## Refer

* [DataX3.0](https://blog.csdn.net/zsj777/article/details/80632959)
* [alibaba/DataX](https://github.com/alibaba/DataX)
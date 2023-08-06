# log.client

一款Python日志客户端，支持直接写入Elasticsearch。

* * * 
# v1.2.2:

## 新功能

1、支持通过环境变设置日志组件配置

# v1.2.1:

## 新功能

1、支持ElasticSearch最小安全性设置。


# v1.1.1:
## 功能优化：

1、支持批量写入Elasticsearch（依赖Elasticsearch包）。

2、增加日志队列慢的异常处理。

* * *
## Usage:
### 1、创建配置文件config.ini:
```ini
[log]
app_name = YOUR-APPNAME
es_urls = http://es-ip:9200
es_index_name = applog-20221228
# 1.2.1版本新增配置
es_username = elastic
es_password = search
```
app_name: 应用名称  
es_urls: Elasticsearch 地址。填写多个时，用,分隔。  
es_index_name: Elasticsearch 索引名称  

1.2.2 支持同名的环境变量替换config.ini. 

```
优先使用环境变量的设置.
linux:
export app_name=testapp
export es_urls=http://es-ip:9200
```

### 2、创建配置文件logging.ini:

```ini
[loggers]
keys=root

[handlers]
keys=consoleHandler,qHandler

[formatters]
keys=simpleFmt,detailFmt

[logger_root]
level=DEBUG
handlers=consoleHandler,qHandler

[handler_consoleHandler]
class=StreamHandler
level=DEBUG
formatter=detailFmt
args=(sys.stdout,)

[handler_qHandler]
class=qlog.logger.QlogHandler
level=INFO
formatter=simpleFmt
args=()

[formatter_detailFmt]
format="%(asctime)-15s %(levelname)s %(filename)s %(funcName)s lineNo: %(lineno)d details: %(message)s"

[formatter_simpleFmt]
format="%(message)s"
```

### 3、日志写入测试

```python
import logging
import logging.config
from time import sleep

logging.config.fileConfig('logging.ini')
logger = logging.getLogger('root')
logger.info('这是一条中文字符测试日志')
logger.info('this is a info log.')
logger.warning('this is a warning log.')
sleep(30)
```

### 4、查看Elasticsearch日志

![img.png](img.png)
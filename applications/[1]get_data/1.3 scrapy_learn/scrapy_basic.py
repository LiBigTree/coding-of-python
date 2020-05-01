# scrapy爬虫步骤：
# 1、建立一个scrapy爬虫工程 startproject 创建一个新工程
# 2、在工程中创建一个爬虫模板 genspider

# scrapy_demo/ >>>外层目录
# - scrapy.cfg >>> 部署scrapy爬虫的配置文件（部署这个概念对应的是服务器）
# - scrapy_demo/ >>> 用户自定义代码
#   -- __init__.py >>> 初始化脚本
#   -- items.py >>> Items代码模板（继承类）
#   -- middlewares.py >>> middlewares模板（继承类）
#   -- pipelines.py >>> pipelines模板 （继承类）
#   -- settings.py >>> 爬虫配置文件
#   -- spiders/ >>> 爬虫代码模板目录
#      -- __init__.py >>> 初始文件，无需修改
#      -- __pycache__/ >>> 缓存目录，无需修改
#
# 3、配置产生的spider爬虫（修改文件）
# - 编写Item Pipeline
# - 优化配置策略
# 4、运行爬虫，获取网页

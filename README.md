# 说明
FofaGather.py可以快速批量获取指定关键词的搜索结果url

非web服务搜索需要修改fofa_spider.py中的xpath解析

<h>使用</h>

1.在fofa_spider.py中修改搜索关键字

2.相关的库
queue
lxml
pip install -r requestment.txt

3.运行python FofaGather.py

<h>提示</h>
cookie请使用burp抓包获取refresh_token（两天内会失效）


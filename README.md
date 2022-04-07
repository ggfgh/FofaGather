# 说明
FofaGather.py可以快速批量获取指定关键词的搜索结果url

非web服务搜索需要修改fofa_spider.py中的xpath解析

1.在fofa_spider.py中添加搜索关键字

2.requirement
queue
lxml
pip install -r requestment.txt

3.运行python FofaGather.py
cookie请使用burp抓包获取refresh_token（两天内会失效）


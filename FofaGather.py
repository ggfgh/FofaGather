import queue
import fofa_spider
import time
import random
import threading

#爬取获得页面--生产者
def do_craw(url_queue:queue.Queue,html_queue:queue.Queue):
    while True:
        url = url_queue.get() #从队列中获取数据
        html = fofa_spider.craw(url)
        html_queue.put(html)

        url_queue.task_done()  #完成一个任务
        print(threading.currentThread().name,f"craw {url}",
             "url_queue.size=",url_queue.qsize())
        time.sleep(random.randint(1, 2))

#解析--消费者
def do_parse(html_queue:queue.Queue,fout):
    while True:
        html = html_queue.get()
        results = fofa_spider.parse(html)

        #print(str(results))
        for result in results:
            print(result)
            fout.write(str(result) + '\n')
        
        html_queue.task_done()
        print(threading.currentThread().name,f"results.size:",len(results),
            "url_queue.size=",url_queue.qsize())

        time.sleep(random.randint(1, 2))

if __name__ == "__main__":

    start = time.time()
    url_queue = queue.Queue()
    html_queue = queue.Queue()

    for url in fofa_spider.urls:
        url_queue.put(url)

    for idx in range(6):
        t = threading.Thread(target=do_craw,args=(url_queue,html_queue),daemon=True,
                            name=f"craw{idx}")
        t.start()

    fout = open(".\\FofaGather.txt","w",encoding="utf-8")

    for idx in range(6):
        t = threading.Thread(target=do_parse,args=(html_queue,fout),daemon=True,
                            name=f"parse{idx}")
        t.start()

    url_queue.join()
    html_queue.join()

    end = time.time()
    print('---------------- end cost time:%ds ---------------' %(end-start))
        

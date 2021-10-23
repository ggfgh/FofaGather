import requests
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64
import time

url = 'https://fofa.so/result'     
search = 'port="3389"'       #搜索关键词
search_base64 = str(base64.b64encode(search.encode('utf-8')),"utf-8")   #编码: str->byte 解码：byte -> str

urls = [
    url + '?qbase64=' + search_base64 + '&page=' + str(page)
    for page in range(1,6)     #爬取的页数 5
]

headers = {
        #cookie两天失效需要burp抓包重新填写
        'Cookie': 'refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTIyMjY4LCJtaWQiOjEwMDA3MjkwNywidXNlcm5hbWUiOiJhcm9vdCIsImV4cCI6MTYzNTEzOTEzOCwiaXNzIjoicmVmcmVzaCJ9.FVVQZQ9DXuMAtImS2TOiBBALaSPFipC9dYXva_H05vzdziNAmTAqwhd-_BehUj1-1yTl_1dAMPMbuUuFdT9e5w',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',
    }

def craw(url):
    #https不进行提示
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.get(url,headers=headers,verify=False)
    print(r.url)
    r.encoding='utf-8'
    return r.text

def parse(html):
    content = etree.HTML(html)
    divs = content.xpath('/html/body/div[1]/div/div/div[2]/div[1]/div[2]/div[2]/div[2]/div')
    return [(''.join(div.xpath("./div[1]/div[1]/span[2]/a/@href"))) for div in divs][0:-1] #web资产
    #return [(''.join(div.xpath("./div[1]/div[1]/span[2]/text()"))) for div in divs][0:-1] #非web资产

if __name__ == '__main__':
    
    start = time.time()
    print(parse(craw(urls[1])))
    end = time.time()
    print('----------- cost time : %ds ------------' %(end-start))
       


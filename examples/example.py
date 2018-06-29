import os
import sys
import threading
import time

import requests
from bs4 import BeautifulSoup
import lxml
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Before run this example, Please run 'run.py'.!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def get_proxy():
    r = requests.get('http://127.0.0.1:8888/get')
    proxy = BeautifulSoup(r.text, "lxml").get_text()
    return proxy


def crawl(url, proxy):
    proxies = {'http': 'http://{}'.format(proxy)}
    r = requests.get(url, proxies=proxies)
    return r.text


def main():
    proxy = get_proxy()
    t = int(time.time())*1000-10000+543

    # url = 'https://mytoken.io/api/ticker/search?category=currency&keyword=ONE&timestamp={}&code=eb8f978b648e58b65134d9abcf35e937&platform=m&v=1.0.0&language=zh_CN&legal_currency=CNY'.format(t)
    url = 'https://mytoken.io/api/ticker/search?category=currency&keyword=one&timestamp=1530259096094&code=aa1fd57793bb33a212379760b1962457&platform=m&v=1.0.0&language=zh_CN&legal_currency=CNY'
    # html = crawl('https://mytoken.io/api/ticker/search?category=currency&keyword=ONE&timestamp={}&code=eb8f978b648e58b65134d9abcf35e937&platform=m&v=1.0.0&language=zh_CN&legal_currency=CNY'.format(int(time.time())*1000), proxy)
    print(t)
    html = crawl(url, proxy)
    print(html)

if __name__ == '__main__':
    import random

    def getRequest():
        while True:
            main()
            time.sleep(random.randint(1, 5))

    # 创建数组存放线程
    threads = []
    # 创建100个线程
    for i in range(100):
        # 针对函数创建线程
        t = threading.Thread(target=getRequest, args=())
        # 把创建的线程加入线程组
        threads.append(t)

    if __name__ == '__main__':
        # 启动线程
        for i in threads:
            i.start()
            # keep thread
        for i in threads:
            i.join()

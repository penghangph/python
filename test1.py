# coding=utf-8
# 爬虫抓学校官网首页
import requests
import re
import urllib.request
from bs4 import BeautifulSoup
import os
import lxml

# 保存文件
def file_save(data, path):
    if not os.path.exists(os.path.split(path)[0]):
        os.makedirs(os.path.split(path)[0])
    try:
        with open(path, 'wb') as f:
            f.write(data.encode('utf-8'))
        print('保存完毕')
    except Exception as ex:
        print('保存失败', ex)


def url_open(url):
    # 伪造头部信息
    headers = {
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }
    r = requests.get(url, headers)
    _data = r.text
    return _data


url = "http://www.yvtc.edu.cn"
data = url_open(url)
soup = BeautifulSoup(data, "lxml")
tag = soup.select('a[href^="/news/show"]')
s = ""
for item in tag:
    s += item.get("href") + "," + item.get("title") + "\n"
print(s)

file_save(s, r"d:\1.txt")
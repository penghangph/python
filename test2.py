# coding=utf-8
import requests
import re
import urllib.request
from bs4 import BeautifulSoup
import os
import lxml
import test1

#读取文件拼接
def read_file(path):
    re=[]
    try:
        with open(path, 'r',encoding='utf-8') as fs:
            data=fs.read().split("\n")
            for line in data:
                row=line.split(',')
               #print(row)
                re.append(row[0])

            return re
    except Exception as ex:
        print('读取失败', ex)

path = r"d:\1.txt"
arr = read_file(path)

for cur_url in arr:
    #组装url
    print("------------------------------------------")
    url="http://www.yvtc.edu.cn"+cur_url
    print(url)
    print("------------------------------------------")

    data=test1.url_open(url)

    soup = BeautifulSoup(data, "lxml")
    article = soup.select('div[class="detail"]>p')
    print(article)

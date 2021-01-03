# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file PyQuery.py
# @description PyQuery
# @author WcJun
# @date 2020/07/06
# ---------------------------------------------


import requests
from pyquery import PyQuery as pq
import src.main.python.spider.SpiderUtils as SpiderUtils


def main():
    http_headers = SpiderUtils.populate_headers()
    url = "https://www.qidian.com/rank/yuepiao"

    response = requests.get(url, headers=http_headers)
    doc = pq(response.text)
    names = doc('.book-mid-info h4 a')
    authors = doc('.book-mid-info .author .name')
    for index in range(0, len(names)):
        name = names.eq(index).text()
        author = authors.eq(index).text()
        print(name, ":", author)

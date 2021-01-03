# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file XPath.py
# @description XPath
# @author WcJun
# @date 2020/07/06
# ---------------------------------------------


from lxml import etree
import requests
import src.main.python.spider.SpiderUtils as SpiderUtils


def main():
    http_headers = SpiderUtils.populate_headers()

    url = "https://www.qidian.com/rank/yuepiao?chn=21"

    response = requests.get(url, headers=http_headers)

    document = etree.HTML(response.text)

    names = document.xpath('//h4/a/text()')
    authors = document.xpath('//p[@class="author"]/a[1]/text()')

    for name, author in zip(names, authors):
        print(name, ":", author)

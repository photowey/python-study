# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file SsL.py
# @description SsL
# @author WcJun
# @date 2020/06/30
# ---------------------------------------------


import ssl
import src.main.python.spider.SpiderUtils as SpiderUtils

url = 'https://www.12306.cn/mormhweb/'
headers = {
    "User-Agent": SpiderUtils.UserAgent().chrome
}
request = SpiderUtils.Request(url, headers=headers)
# 忽略验证证书
context = ssl._create_unverified_context()
response = SpiderUtils.urlopen(request, context=context)
info = response.read().decode()
print(info)

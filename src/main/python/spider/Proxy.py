# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Proxy.py
# @description Proxy
# @author WcJun
# @date 2020/06/30
# ---------------------------------------------


import src.main.python.spider.SpiderUtils as SpiderUtils
from urllib.request import ProxyHandler
from urllib.request import build_opener

url = 'http://httpbin.org/get'
headers = {
    "User-Agent": SpiderUtils.UserAgent().chrome
}
request = SpiderUtils.Request(url, headers=headers)
# 1.
# proxy = ProxyHandler({"https":"60.179.201.207:3000"})
# 2.
# proxy = ProxyHandler({"https":"60.188.1.27:3000"})
proxy = ProxyHandler({"http":"220.249.149.32:9999"})
opener = build_opener(proxy)

response = opener.open(request)
info = response.read().decode()
"""
## 代码返回
# 1.
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/24.0.1295.0 Safari/537.15", 
    "X-Amzn-Trace-Id": "Root=1-5efb4b4b-9a879874db1db3ce4ffb7967"
  }, 
  "origin": "125.82.191.23", 
  "url": "http://httpbin.org/get"
}
# 2.
{
  "args": {}, 
  "headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1467.0 Safari/537.36", 
    "X-Amzn-Trace-Id": "Root=1-5efb4bdd-fd827b7024db9a6aa8e396f6"
  }, 
  "origin": "125.82.191.23", 
  "url": "http://httpbin.org/get"
}
## 浏览器返回
{
"args": {},
"headers": {
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"Accept-Encoding": "gzip, deflate",
"Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7",
"Host": "httpbin.org",
"Upgrade-Insecure-Requests": "1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
"X-Amzn-Trace-Id": "Root=1-5efb4a82-7b52fbc6586f4fc0ecca71e6"
},
"origin": "125.82.191.23",
"url": "http://httpbin.org/get"
}
"""
print(info)

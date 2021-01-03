# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Request.py
# @description Request
# @author WcJun
# @date 2020/06/29
# ---------------------------------------------


from urllib.request import urlopen
from urllib.request import Request
from random import choice


url = "http://www.baidu.com"

user_agents = [
    "Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0",
    "Opera/9.80(WindowsNT6.1;U;en)Presto/2.8.131Version/11.11",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"
]

headers = {
    "User-Agent": choice(user_agents)
}

request = Request(url, headers=headers)

response = urlopen(request)
body = response.read()
print(body.decode())
print(response.geturl())
print(response.getcode())
print(response.info())

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Hello.py
# @description Hello
# @author WcJun
# @date 2020/06/29
# ---------------------------------------------


from urllib.request import urlopen

url = "http://www.baidu.com"

response = urlopen(url)
# byte
body = response.read()
# 解码
print(body.decode())
# 请求地址
print(response.geturl())
# http status
print(response.getcode())
# headers
print(response.info())

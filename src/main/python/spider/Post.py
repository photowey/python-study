# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Post.py
# @description Post
# @author WcJun
# @date 2020/06/29
# ---------------------------------------------


from urllib.parse import urlencode
import src.main.python.spider.SpiderUtils as SpiderUtils

url = "http://www.sxt.cn/index/login/login.html"

form_data = {
    "user": "17703181473",
    "password": "12346"
}
headers = {
    "User-Agent": SpiderUtils.UserAgent().chrome
}


def main():
    f_data = urlencode(form_data)
    request = SpiderUtils.Request(url, data=f_data.encode(), headers=headers)
    response = SpiderUtils.urlopen(request)
    print(response.read().decode())

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Requests.py
# @description Requests
# @author WcJun
# @date 2020/07/05
# ---------------------------------------------


import src.main.python.spider.SpiderUtils as SpiderUtils
import requests


def main():
    http_headers = SpiderUtils.populate_headers()

    hello_url = "http://192.168.0.5:939/hello/greet"
    user_url = "http://192.168.0.5:939/hello-users/users"

    # 禁用安全请求警告
    requests.packages.urllib3.disable_warnings()

    hello_response = requests.get(hello_url, verify=False, headers=http_headers)
    print("the hello response is:", hello_response.text)

    user_response = requests.get(user_url, verify=False, headers=http_headers)
    print("the user response is:", user_response.json())

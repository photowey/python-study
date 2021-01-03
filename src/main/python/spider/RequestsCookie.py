# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Requests.py
# @description RequestsCookie
# @author WcJun
# @date 2020/07/05
# ---------------------------------------------


import src.main.python.spider.SpiderUtils as SpiderUtils
import requests


def main():
    http_headers = SpiderUtils.populate_headers()

    hello_url = "http://192.168.0.5:939/hello/greet"
    cookie_url = "http://192.168.0.5:939/hello/cookie"

    session = requests.Session()
    hello_response = session.get(hello_url, verify=False, headers=http_headers)
    print("the hello response is:", hello_response.text)
    
    cookie_response = session.get(cookie_url, verify=False, headers=http_headers)
    print("the user response is:", cookie_response.text)

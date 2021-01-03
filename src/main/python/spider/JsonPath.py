# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file JsonPath.py
# @description JsonPath
# @author WcJun
# @date 2020/07/06
# ---------------------------------------------


import json
from jsonpath import jsonpath
import requests
import src.main.python.spider.SpiderUtils as SpiderUtils


def main():
    http_headers = SpiderUtils.populate_headers()

    url = "https://www.lagou.com/lbs/getAllCitySearchLabels.json"

    response = requests.get(url, headers=http_headers)
    # to JSON
    json_obj = SpiderUtils.to_json(response.text)
    names = jsonpath(json_obj, '$..name')

    codes = jsonpath(response.json(), '$..code')

    print(names)
    print(codes)

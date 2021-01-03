# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Qiushibaike.py
# @description Qiushibaike
# @author WcJun
# @date 2020/07/05
# ---------------------------------------------


import src.main.python.spider.SpiderUtils as SpiderUtils
import requests
import re

# GLOBAL VARS
RESOURCE_FILE = "../../resources/html"


def main():
    http_headers = SpiderUtils.populate_headers()
    url = "https://www.qiushibaike.com/text/page/1/"

    response = requests.get(url, headers=http_headers)
    response.encoding = "utf-8"
    html = response.text
    qiu_shi_content = re.findall(r'<div class="content">\s*<span>\s*(.+)\s*</span>', html)
    qiu_shi_file_name = "qiu_shi.txt"
    for context in qiu_shi_content:
        target = "\n" + re.sub("<br/>","\n",context) + "\n"
        SpiderUtils.save_text(RESOURCE_FILE + "/" + qiu_shi_file_name, target)

    # file_name = "qiushibaike.html"
    # SpiderUtils.save_html(RESOURCE_FILE + "/" + file_name, response.content)

    # gpp_url = "https://www.ccgp-chongqing.gov.cn/"
    # gpp_response = requests.get(gpp_url, headers=http_headers)
    # gpp_file_name = "gpp.html"
    # SpiderUtils.save_html(RESOURCE_FILE + "/" + gpp_file_name, gpp_response.content)

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Get.py
# @description Get
# @author WcJun
# @date 2020/06/29
# ---------------------------------------------


from urllib.parse import urlencode
import src.main.python.spider.SpiderUtils as SpiderUtils

# GLOBAL VARS
RESOURCE_FILE = "../../resources/html"


def main():
    keywords = input("请输入:要下载的内容: ")
    total_pages = int(input("请输入:要下载的页数: "))
    base_url = "https://tieba.baidu.com/f?ie=utf-8&{}"
    for page_no in range(total_pages):
        args = {
            "pn": page_no * 50,
            "kw": keywords,
        }
        file_name = "第" + str(page_no + 1) + "页.html"
        args = urlencode(args)
        print("正在下载: " + file_name)
        url = SpiderUtils.text_format(base_url, args)
        body = SpiderUtils.request_html(url)
        html = body.read()
        SpiderUtils.save_html(RESOURCE_FILE + "/" + file_name, html)

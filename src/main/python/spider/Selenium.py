# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Selenium.py
# @description Selenium
# @author WcJun
# @date 2020/07/11
# ---------------------------------------------


from selenium import webdriver

# GLOBAL VARS
RESOURCE_FILE = "../../resources/picture/"


def main():
    chrome = webdriver.Chrome()
    chrome.get('http://www.baidu.com')
    chrome.save_screenshot(RESOURCE_FILE + "baidu.png")

    html = chrome.page_source
    print(html)
    chrome.quit()


def search():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')

    chrome = webdriver.Chrome()

    chrome.get('https://cn.bing.com/')
    chrome.find_element_by_id('sb_form_q').send_keys('python')
    chrome.find_element_by_id('sb_form_go').click()

    html = chrome.page_source
    print(html)
    chrome.quit()

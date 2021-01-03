# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file JsonPath.py
# @description JsonPath
# @author WcJun
# @date 2020/07/06
# ---------------------------------------------


import json

# GLOBAL VARS
RESOURCE_FILE = "../../resources/movie/"


def json_operate():
    json_str = '{"name":"盗梦空间"}'
    # <class 'str'>
    print(type(str))
    # to JSON
    json_obj = json.loads(json_str)
    # <class 'dict'>
    print(type(json_obj))
    # to String
    json_str2 = json.dumps(json_obj, ensure_ascii=False)
    print(type(json_str2), ":", json_str2)

    # to File
    json.dump(json_obj, open(RESOURCE_FILE + 'movie.txt', 'w', encoding='utf-8'), ensure_ascii=False)

    json_str3 = json.load(open(RESOURCE_FILE + 'movie.txt', encoding='utf-8'))
    print(json_str3)


def main():
    json_operate()

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Regex.py
# @description Regex
# @author WcJun
# @date 2020/07/05
# ---------------------------------------------


import re

str1 = "I Study Python3.6 Everyday"
print("-------------match()-----------------")
# 匹配 I 字符
m1 = re.match(r'I', str1)
m2 = re.match(r'\w', str1)
m3 = re.match(r'.', str1)
m4 = re.match(r'\D', str1)
m5 = re.match(r'i', str1, re.I)
m6 = re.match(r'\S', str1)
print(m6.group())
print("-------------search()-----------------")
# 匹配 Study
s1 = re.search(r'Study', str1)
print(s1.group())
s2 = re.search(r'S\w+', str1)
print(s2.group())
# 匹配 Python3.6
s3 = re.search(r'P\w+.\d', str1)
print(s3.group())
print("-------------findall()-----------------")
# 查找 所有 y
f1 = re.findall(r'y', str1)
print(f1)
print("-------------test()-----------------")
str2 = '<div><a href="http://www.bjsxt.com">bjsxt尚学堂</a></div>'
# 提取 a 标签的内容
t1 = re.findall(r'[\u4e00-\u9fa5]\w+', str2)
print("t1:", t1)
t2 = re.findall(r'<a href="http://www.bjsxt.com">(.+)</a>', str2)
print("t2:", t2)
# 提取 herf
t3 = re.findall(r'<a href="(.+)">', str2)
print("t3:", t3)
print("-------------sub()-----------------")
# 将str2的div换成span
su1 = re.sub(r'<div>(.+)</div>', r'<span>\1</span>', str2)
print(su1)

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Dictionary.py
# @description Dictionary
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


user = {
    "name": "LiLei",
    "age": 18,
    "Address": "YuBei"
}
# {'name': 'LiLei', 'age': 18}
print(user)
# 18
print(user["age"])
user["Hobby"] = "打篮球"
# {'name': 'LiLei', 'age': 18, 'Address': 'YuBei', 'Hobby': '打篮球'}
print(user)

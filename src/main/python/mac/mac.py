# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file mac.py
# @description mac
# @author WcJun
# @date 2022/05/26
# ---------------------------------------------


def mac():
    mac_int = int('A4:C3:F0:C1:7A:4C'.replace(':', ''), 16)
    print(mac_int)


if __name__ == '__main__':
    mac()

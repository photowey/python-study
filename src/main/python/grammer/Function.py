# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Function.py
# @description Function
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


# 求两个数 n 加到 m 的和
def add(n, m):
    s = 0
    while n <= m:
        s += n
        n += 1
    return s


# 求和
add = add(1, 100)
print(add)

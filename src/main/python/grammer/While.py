# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file While.py
# @description While
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


# while
n = 1
while n < 10:
    print(n)
    n = n + 1
else:
    print("循环结束")

# while 乘法口诀表
m = 1
while m < 10:
    k = 1
    while k <= m:
        print(f"{k}*{m}={k * m}", end=" ")
        k = k + 1
    m = m + 1
    print()

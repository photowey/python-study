# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file For.py
# @description For
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


# for i
for i in range(5):
    print(i)
for i in range(1, 5):
    print(i)
for i in range(1, 5, 2):
    print(i)

print("======================================")

# for 乘法口诀表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}", end=" ")
    print()

# continue - 结束 当次循环
for char in "python":
    if char == "y":
        continue
    print(char)

array = [1, 2, 3, 4, 5, 6, 7]
for item in array:
    if item == 4:
        continue
    print(item)

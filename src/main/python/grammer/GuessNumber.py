# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file GuessNumber.py
# @description GuessNumber
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


"""
在 1~100 产生一个随机数，
让用户反复得猜
只提示 “猜大了”后者 “猜小了”
猜对则结束游戏
"""

import random

# 产生一个随机数
target = random.randint(1, 100)
# 允许猜的最大次数
total = 5
# 猜的次数，默认为: 0
count = 0
while True:
    # 获取从控制台输入的一个数
    guess = int(input("请猜一个1~100的整数\n"))
    if guess > target:
        print("猜大了")
    elif guess < target:
        print("猜小了")
    else:
        print("恭喜您,猜对了,真是料事如神~")
        break
    count += 1
    if count == total:
        print(f"已经猜了{total}了,游戏介绍~")
        break

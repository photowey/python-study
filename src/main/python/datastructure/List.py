# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file List.py
# @description 测试 append() 和 insert() 的性能
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


from timeit import Timer


# append
def append_test():
    target = []
    for i in range(10000):
        target.append(i)


# insert
def insert_test():
    target = []
    for i in range(10000):
        target.insert(0, i)


if __name__ == "__main__":
    timer1 = Timer("append_test()", "from __main__ import append_test")
    print("append_test:", timer1.timeit(1000), " s")

    timer2 = Timer("insert_test()", "from __main__ import insert_test")
    print("insert_test:", timer2.timeit(1000), " s")

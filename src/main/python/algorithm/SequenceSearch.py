# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file SequenceSearch.py
# @description Sequence Search
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


# sequence search
def sequence_search(origin_list, expect_value):
    length = len(origin_list)
    for i in range(length):
        if origin_list[i] == expect_value:
            return i
    return -1


if __name__ == "__main__":
    array_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    expect = 100
    index = sequence_search(array_list, expect)
    if index != -1:
        print(f"找到了，索引值为{index}")
    else:
        print(f"没找到期望的值{expect}")

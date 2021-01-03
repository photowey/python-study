# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file BinarySearch.py
# @description Binary Search
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


# binary search -> 非递归查找
def binary_search(origin_list, expect_value):
    length = len(origin_list)
    start = 0
    end = length - 1
    while start <= end:
        middle = (start + end) // 2
        if origin_list[middle] == expect_value:
            return True
        elif origin_list[middle] < expect_value:
            # 右边
            start = middle + 1
        else:
            # 左边
            end = middle - 1

    return False


# binary search -> 递归查找
def binary_search2(origin_list, expect_value):
    length = len(origin_list)
    if length == 0:
        return False
    start = 0
    end = length - 1
    middle = (start + end) // 2
    if origin_list[middle] == expect_value:
        return middle
    elif origin_list[middle] < expect_value:
        return binary_search2(origin_list[middle + 1:], expect_value)
    else:
        return binary_search2(origin_list[:middle], expect_value)


if __name__ == "__main__":
    array_list = [3, 6, 11, 22, 44, 75, 99]
    expect = 75
    findSucceed = binary_search2(array_list, expect)
    if findSucceed:
        print(f"找到了")
    else:
        print(f"没找到期望的值{expect}")

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file QuickSort.py
# @description Quick Sort
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

# 时间复杂度: 最好:O(n*log-n)  最坏:(n^2)
# 稳定性: 不稳定


sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]


# 基准数 54(sort_list[0]) -- 比 54 小的 放左边, 大的 放右边
# low = 1
# high = n - 1


# quick_sort
def quick_sort(origin_list, start, end):
    if start >= end:
        return
    middle = origin_list[start]
    low = start
    high = end
    while low < high:
        # 从 右 至 左  low < high && origin_list[high] > middle -> high--
        while low < high and origin_list[high] >= middle:
            high -= 1
        origin_list[low] = origin_list[high]
        # 从 左 至 右  low < high && origin_list[low] < middle -> low++
        while low < high and origin_list[low] < middle:
            low += 1
        origin_list[low] = origin_list[high]
    # 将基准数 放在对应的位置
    origin_list[low] = middle
    # 比基准数小的 -> 左边的数据
    quick_sort(origin_list, start, low - 1)
    # 比基准数大的 -> 右边的数据
    quick_sort(origin_list, low + 1, end)


array_sort = sort_list
print("原数组")
print(array_sort)
quick_sort(array_sort, 0, len(array_sort) - 1)
print("排序后数组")
print(array_sort)

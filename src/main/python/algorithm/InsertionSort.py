# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file InsertionSort.py
# @description Insertion Sort
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

# 时间复杂度: 最好:O(n)  最坏:(n^2)
# 稳定性: 稳定


# insertion sort
def insertion_sort(origin_list):
    length = len(origin_list)
    for k in range(1, length - 1):  # O(n)
        i = k
        while i > 0:    # O(n)
            if origin_list[i] < origin_list[i - 1]:
                origin_list[i], origin_list[i - 1] = origin_list[i - 1], origin_list[i]
            else:
                break
            i -= 1


array_sort = [75, 3, 6, 44, 22, 99, 11]
print("原数组")
print(array_sort)
insertion_sort(array_sort)
print("排序后数组")
print(array_sort)

# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file BubbleSort.py
# @description Bubble Sort
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

# 时间复杂度: 最好:O(n)  最坏:(n^2)
# 稳定性: 稳定


# bubble_sort
def bubble_sort(origin_list):
    length = len(origin_list)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
                print(f"--------------------------------------{i}")


array_sort = [75, 3, 6, 44, 22, 99, 11]
print("原数组")
print(array_sort)
bubble_sort(array_sort)
print("排序后数组")
print(array_sort)


# bubble_sort
def bubble_sort2(origin_list):
    for i in range(len(origin_list) - 1, 0, -1):
        for j in range(i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
                print(f"==============================={i}")


array_sort2 = [75, 3, 6, 44, 22, 99, 11]
print("原数组")
print(array_sort2)
bubble_sort2(array_sort2)
print("排序后数组")
print(array_sort2)


# bubble_sort
def bubble_sort3(origin_list):
    for i in range(len(origin_list) - 1, 0, -1):
        swap_count = 0
        for j in range(i):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]
                swap_count += 1
                print(f"==============================={i}")
        if swap_count == 0:
            break


array_sort3 = [3, 6, 11, 22, 44, 75, 99]
print("原数组")
print(array_sort3)
bubble_sort3(array_sort3)
print("排序后数组")
print(array_sort3)

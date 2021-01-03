# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file SelectionSort.py
# @description Selection Sort
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

# 时间复杂度: 最好:O(n^2)  最坏:(n^2)
# 稳定性: 不稳定


# selection sort
def selection_sort(origin_list):
    length = len(origin_list)
    for i in range(length - 1):  # O(n)
        min_index = i
        for j in range(i + 1, length):  # O(n)
            if origin_list[min_index] > origin_list[j]:
                min_index = j
        origin_list[i], origin_list[min_index] = origin_list[min_index], origin_list[i]
        print(f"--------------------------------------{i}")


array_sort = [75, 3, 6, 44, 22, 99, 11]
print("原数组")
print(array_sort)
selection_sort(array_sort)
print("排序后数组")
print(array_sort)


def selection_sort2(origin_list):
    length = len(origin_list)
    for i in range(length - 1):
        min_index = i
        for j in range(i + 1, length):
            if origin_list[min_index] > origin_list[j]:
                # 只记录索引位置
                min_index = j
        # 最小索引有变化--需要交换
        if min_index != i:
            origin_list[i], origin_list[min_index] = origin_list[min_index], origin_list[i]
            print(f"--------------------------------------{i}")


array_sort2 = [75, 3, 6, 44, 22, 99, 11]
print("原数组")
print(array_sort2)
selection_sort2(array_sort2)
print("排序后数组")
print(array_sort2)

array_sort3 = [3, 6, 11, 22, 44, 75, 99]
print("原数组")
print(array_sort3)
selection_sort2(array_sort3)
print("排序后数组")
print(array_sort3)

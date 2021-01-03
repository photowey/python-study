# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file MergeSort.py
# @description Merge Sort
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

# 时间复杂度: 最好:O(n*log-n)  最坏:(n*log-n)
# 稳定性: 稳定


# merge sort
def merge_sort(origin_list):
    length = len(origin_list)
    if length <= 1:
        return origin_list
    middle = length // 2

    # 分解
    left_list = merge_sort(origin_list[:middle])
    right_list = merge_sort(origin_list[middle:])   # O(1)

    # 合并
    # 最终合并结果的 列表 容器
    merge_list = []

    # 左右指针
    left_pointer, right_pointer = 0, 0
    while left_pointer < len(left_list) and right_pointer < len(right_list):    # O(n)
        if left_list[left_pointer] <= right_list[right_pointer]:
            merge_list.append(left_list[left_pointer])
            left_pointer += 1
        else:
            merge_list.append(right_list[right_pointer])
            right_pointer += 1
    # 退出循环后, 将不为空的列表剩余元素 加到 merge_list
    merge_list.extend(left_list[left_pointer:])
    merge_list.extend(right_list[right_pointer:])

    return merge_list


sort_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
array_sort = sort_list
print("原数组")
print(array_sort)
result_list = merge_sort(array_sort)
print("排序后数组")
print(result_list)

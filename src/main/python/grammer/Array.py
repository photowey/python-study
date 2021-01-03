# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Array.py
# @description Array
# @author WcJun
# @date 2020/06/20
# ---------------------------------------------


array = [1, 2, 3, 4, 5]
print(array[0])
print(array[1])
print(array[2])
print(array[3])
print(array[4])
# 越界
# print(array[5])
print(array[-0])
print(array[-1])
print(array[-2])
print(array[-3])
print(array[-4])

# 追加元素 append()
array.append("python")
print(array)

# extend()
array.extend("python")
print(array)
# extend() 必须是列表
# array.extend(1)

array.extend([11, 22, "grammer"])
# [1, 2, 3, 4, 5, 'python', 'p', 'y', 't', 'h', 'o', 'n', 11, 22, 'grammer']
print(array)

# 删除元素
# pop() 删除最后一个
pop = array.pop()
print(pop)
# [1, 2, 3, 4, 5, 'python', 'p', 'y', 't', 'h', 'o', 'n', 11, 22]
print(array)

# pop(index) 删除指定元素
pop = array.pop(2)
print(pop)
# [1, 2, 4, 5, 'python', 'p', 'y', 't', 'h', 'o', 'n', 11, 22]
print(array)

# remove(target) 直接移除
array.remove(4)
# [1, 2, 5, 'python', 'p', 'y', 't', 'h', 'o', 'n', 11, 22]
print(array)
array.remove("python")
# [1, 2, 5, 'p', 'y', 't', 'h', 'o', 'n', 11, 22]
print(array)

# 赋值
array[2] = "dcc"
# [1, 2, 'dcc', 'p', 'y', 't', 'h', 'o', 'n', 11, 22]
print(array)

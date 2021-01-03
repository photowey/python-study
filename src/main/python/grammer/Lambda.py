# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Lambda.py
# @description Lambda
# @author WcJun
# @date 2020/06/25
# ---------------------------------------------


print((lambda a, b: a + b)(10, 20))
print("===============================")
origin_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(list(filter(lambda i: i % 3 == 0, origin_list)))

print("===============================")

print(list(map(lambda i: i + 1, origin_list)))

print("===============================")

origin_list_sort = [4, 5, 6, 1, "2", 3, "7", 8, 9]
# 操作的是原始序列
origin_list_sort.sort(key=int)
print(origin_list_sort)

print("===============================")

origin_list_sorted = [4, 5, 6, 1, "2", 3, "7", 8, 9]
print(origin_list_sorted)
# 返回一个新的排好序的 序列
origin_list_sorted_return = sorted(origin_list_sorted, key=int)
print(origin_list_sorted_return)
print(origin_list_sorted)
print("===============================")


def fx():
    def inner_fx():
        print("I am inner fx")

    return inner_fx


print(fx())
fx()()

print("===============================")


# 闭包
# --------------------------------------
# 1.函数嵌套
# 2.将内部函数作为返回值返回
# 3.内部函数必须使用到外部函数的变量
# --------------------------------------
def make_average():
    num_list = []

    def inner_average(n: int) -> float:
        num_list.append(n)
        print("invoke inner_average")
        return sum(num_list) / len(num_list)

    return inner_average


average = make_average()

print(average(10))
print(average(20))
print(average(30))
print(average(40))

print("===============================")


def fx_decorator(target):
    # 判断一个参数 是不是 函数
    print(type(target))
    print(callable(target))
    if callable(target):
        print("============target============")

    # 装包
    def inner_function(*args, **kwargs):
        print("======start======")
        # 拆包
        result = target(*args, **kwargs)
        print("======end======")
        return result

    return inner_function


new_func = fx_decorator(fx())
new_func()

print("===============================")

new_func_average = fx_decorator(average)
new_func_average(111)

print("===============================")


@fx_decorator
def say_hello():
    print("say hello")


say_hello()

print("===============================")

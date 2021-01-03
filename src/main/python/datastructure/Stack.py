# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Stack.py
# @description 
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


# stack
class Stack(object):
    def __init__(self):
        # 初始化一个空列表
        self.__list = []

    # 压栈
    def push(self, item):
        self.__list.append(item)
        return

    # 弹出 元素
    def pop(self):
        return self.__list.pop()

    # 返回 栈顶 元素
    def peek(self):
        return self.__list[len(self.__list) - 1]

    # 判断 栈是否为空
    def is_empty(self):
        return self.__list == []

    # 计算 栈的长度
    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    stack = Stack()
    print("是否为空栈:", stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print("是否为空栈:", stack.is_empty())
    print(stack.peek())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

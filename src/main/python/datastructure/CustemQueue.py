# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file CustemQueue.py
# @description Queue
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------

# TODO 奇怪的是 如果文件名 命名为 Queue.py 就会报错


# queue
class Queue(object):
    def __init__(self):
        # 初始化一个空列表
        self.__list = []

    # 入队
    def enqueue(self, item):
        # self.__list.append(item)
        self.__list.insert(0, item)
        return

    # 出队
    def dequeue(self):
        # return self.__list.pop(0)
        return self.__list.pop()

    # 判断队列是否为空
    def is_empty(self):
        return self.__list == []

    # 计算队列的长度
    def size(self):
        return len(self.__list)


if __name__ == "__main__":
    queue = Queue()
    print("队列是否位空:", queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

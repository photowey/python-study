# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file SingleLinkedList.py
# @description Linked List
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


# 节点
class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None


# 单向链表
class SingleLinkedList:
    # 初始化 函数
    def __init__(self, node=None):
        if node is not None:
            head = Node(node)
            self.__head = head
        else:
            self.__head = node

    # 在 头部添加元素
    def add(self, item):
        node = Node(item)
        # 将 新节点 的 链接域 next 指向头节点
        node.next = self.__head
        # 将 链表的头节点 指向 新节点
        self.__head = node
        return

    # 在 单向链表的尾部 追加元素
    def append(self, item):
        node = Node(item)
        # 链表为空的场景
        if self.is_empty():
            self.__head = node
        else:
            current_node = self.__head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = node
        return

    # 在 指定位置添加元素
    def insert(self, position, item):
        if position <= 0:
            # 头部插入
            self.add(item)
        elif position > (self.length() - 1):
            # 大于列表的长度 - 尾部插入
            self.append(item)
        else:
            count = 0
            pre_node = self.__head
            node = Node(item)
            while count <= (position - 1):
                count += 1
                pre_node = pre_node.next

            node.next = pre_node.next
            pre_node.next = node
        return

    # 删除 节点
    def remove(self, item):
        current_node = self.__head
        pre_node = None
        while current_node is not None:
            if current_node.element == item:
                # 判断 pre_node 是不是 头节点
                if pre_node is None:
                    self.__head = current_node.next
                else:
                    pre_node.next = current_node.next
                break
            else:
                pre_node = current_node
                current_node = current_node.next
        return

    # 搜索 节点
    def search(self, item):
        current_node = self.__head
        while current_node is not None:
            if current_node.element == item:
                return True
            current_node = current_node.next
        return False

    # 判断 链表是否为空
    def is_empty(self):
        # 判断 __head 是否指向的 None
        return self.__head is None

    # 计算 链表的长度
    def length(self):
        node_count = 0
        current_node = self.__head
        while current_node is not None:
            node_count += 1
            current_node = current_node.next
        return node_count

    # 遍历
    def travel(self):
        current_node = self.__head
        while current_node is not None:
            print(current_node.element, end="\t")
            current_node = current_node.next
        print()


if __name__ == "__main__":
    single_linked_list1 = SingleLinkedList(20)
    single_linked_list2 = SingleLinkedList()
    print("single_linked_list1: 是否为空", single_linked_list1.is_empty())
    print("single_linked_list2: 是否为空", single_linked_list2.is_empty())

    print("single_linked_list1: 长度", single_linked_list1.length())
    print("single_linked_list2: 长度", single_linked_list2.length())

    single_linked_list1.travel()
    single_linked_list2.travel()

    find_succeed1 = single_linked_list1.search(20)
    find_succeed2 = single_linked_list2.search(20)
    print(find_succeed1)
    print(find_succeed2)

    single_linked_list1.add(1)
    single_linked_list1.add(2)
    single_linked_list2.add(1)
    single_linked_list2.add(2)

    single_linked_list1.travel()
    single_linked_list2.travel()

    single_linked_list1.append(100)
    single_linked_list1.append(200)
    single_linked_list2.append(100)
    single_linked_list2.append(200)

    single_linked_list1.travel()
    single_linked_list2.travel()

    single_linked_list3 = SingleLinkedList()
    single_linked_list3.append(200)
    single_linked_list3.travel()

    single_linked_list1.insert(2, 1111)
    single_linked_list1.travel()

    single_linked_list1.insert(-2, 1111)
    single_linked_list1.travel()

    single_linked_list1.insert(111, 1111)
    # 1111	2	1	20	1111	100	200	1111
    single_linked_list1.travel()
    single_linked_list1.remove(1111)
    single_linked_list1.travel()

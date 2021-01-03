# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file DoubleLinkedList.py.py
# @description Double Linked List
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


# 节点
class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None
        self.prev = None


# 双向链表
class DoubleLinkedList:
    def __init__(self, node=None):
        if node is not None:
            head = Node(node)
            self.__head = head
        else:
            self.__head = node

    # 在 头部添加元素
    def add(self, item):
        node = Node(item)
        # 1.将 新节点 的 链接域 next 指向头节点
        node.next = self.__head
        # 2.将 __head 头节点的 prev 指向 新的节点
        if self.is_empty():
            self.__head = node
        else:
            self.__head.prev = node
            # 3.将 链表的头节点__head 指向 新节点
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
            # 将 node 节点的前驱节点 指向 当前节点
            node.prev = current_node
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
            current_node = self.__head
            node = Node(item)
            while count <= (position - 1):
                count += 1
                current_node = current_node.next
            # 将 新 node 节点 的前驱 指向当前节点
            node.prev = current_node
            # 将 新 node 节点的后继 指向 当前节点的下一个节点
            node.next = current_node.next
            # 将 当前节点的下一个节点的前驱 指向 新 node 节点
            current_node.next.prev = node
            # 将 当前节点的后继 指向 新 node 节点
            current_node.next = node
        return

    # 删除 节点
    def remove(self, item):
        current_node = self.__head
        while current_node is not None:
            if current_node.element == item:
                # 判断 current_node 是不是 头节点
                if current_node == self.__head:
                    self.__head = current_node.next
                    # 判断当前节点是否只有一个节点,如果只有一个节点,则不需要移动下一个节点前驱
                    if current_node.next is not None:
                        current_node.next.prev = None
                else:
                    current_node.prev.next = current_node.next
                    # 判断当前节点 是不是 最后一个节点,如果是最后一个节点,最后一个节点的下一个节点指向 None
                    if current_node.next is not None:
                        current_node.next.prev = current_node.prev
                break
            else:
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
    double_linked_list1 = DoubleLinkedList()
    double_linked_list1.add(10)
    double_linked_list1.add(11)
    double_linked_list1.travel()
    double_linked_list1.append(111)
    double_linked_list1.append(222)
    double_linked_list1.append(333)
    # 11	10	111	222	333
    double_linked_list1.travel()

    print("length:", double_linked_list1.length())
    double_linked_list1.insert(2, 444)
    double_linked_list1.travel()

    double_linked_list1.insert(-2, 555)
    double_linked_list1.travel()

    double_linked_list1.insert(100, 1000)
    # 555	11	10	111	444	222	333	1000
    double_linked_list1.travel()

    double_linked_list1.remove(222)
    double_linked_list1.remove(555)
    double_linked_list1.remove(1000)
    # 11	10	111	444	333
    double_linked_list1.travel()

    find_succeed_true = double_linked_list1.search(111)
    find_succeed_false = double_linked_list1.search(1111)
    print("find_succeed_true:", find_succeed_true)
    print("find_succeed_false:", find_succeed_false)

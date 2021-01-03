# -*- coding:utf-8 -*-

# ---------------------------------------------
# @file Tree.py
# @description Tree
# @author WcJun
# @date 2020/06/21
# ---------------------------------------------


# 树-数据结构的特点
# 1.每个节点有零个或者多个子节点
# 2.没有父节点的节点称为根节点
# 3.每个非根节点有且只有一个父节点
# 4.除了根节点,每个子节点可以分为多个不相交的子树


# 树-术语
# 1.节点的度: 一个节点含有的子树的个数称为该节点的度
# 2.树的度: 一棵树中, 最大节点的度称为树的度
# 3.叶子节点或者终端节点: 度为0的节点
# 4.父亲节点或者父节点: 若一个节点含有子节点,这这个节点称为其子节点的父节点
# 5.孩子节点或者子节点: 一个节点含有的子树的根节点称为该节点的子节点
# 6.兄弟节点: 具有相同父节点的节点称为兄弟节点
# 7.节点的层次: 从根开始定义起,根为第一层,根的子节点为第二层,以此类推
# 8.树的高度或深度: 树中节点的最大层次
# 9.堂兄弟节点: 父节点在同一层的节点陈伟堂兄弟节点
# 10.节点的祖先: 从根到该节点所经分支上的所有节点
# 11.子孙: 以某节点为根节点的子树中任一节点都称为该节点的子孙
# 12.森林: 由m(m >= 0)颗互不相交的树的集合称为森林


# 树的种类
# 1.无序树(自由树)
# 2.有序树
# 2.1.二叉树: 每个节点最好含有两个子树的树称为二叉树
# 2.1.1.完全二叉树
# 2.1.1.1.满二叉树
# 2.1.2.平衡二叉树
# 2.1.3.排序二叉树
# 2.2.霍夫曼树
# 2.2.B树

# tree node
class Node(object):
    def __init__(self, item):
        self.element = item
        self.left_child = None
        self.right_child = None


# tree
class Tree(object):
    def __init__(self):
        self.root = None

    # 添加元素
    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            while queue:
                current_node = queue.pop(0)
                if current_node.left_child is None:
                    current_node.left_child = node
                    return
                else:
                    queue.append(current_node.left_child)
                if current_node.right_child is None:
                    current_node.right_child = node
                    return
                else:
                    queue.append(current_node.right_child)

    # 广度优先遍历 -- 0	1	2	3	4	5	6	7	8	9
    def travel(self):
        queue = []
        if self.root is None:
            return
        else:
            queue.append(self.root)
        while queue:
            current_node = queue.pop(0)
            print(current_node.element, end="\t")
            if current_node.left_child is not None:
                queue.append(current_node.left_child)
            if current_node.right_child is not None:
                queue.append(current_node.right_child)
        print()

    # 先序遍历 根-左-右 -- 0	1	3	7	8	4	9	2	5	6
    def pre_order(self, root):
        if root is None:
            return
        else:
            print(root.element, end="\t")
            self.pre_order(root.left_child)
            self.pre_order(root.right_child)

    # 中序遍历 左-根-右 -- 7	3	8	1	9	4	0	5	2	6
    def in_order(self, root):
        if root is None:
            return
        else:
            self.in_order(root.left_child)
            print(root.element, end="\t")
            self.in_order(root.right_child)

    # 后序遍历 左-根-右 -- 7	8	3	9	4	1	5	6	2	0
    def post_order(self, root):
        if root is None:
            return
        else:
            self.post_order(root.left_child)
            self.post_order(root.right_child)
            print(root.element, end="\t")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print("--- 广度优先遍历 ---")
    tree.travel()
    print("--- 先序遍历 ---")
    tree.pre_order(tree.root)
    print()
    print("--- 中序遍历 ---")
    tree.in_order(tree.root)
    print()
    print("--- 后序遍历 ---")
    tree.post_order(tree.root)

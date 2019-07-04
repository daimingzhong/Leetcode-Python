""" Created by daimingzhong on 1/29/18. LeetCode:

Problem: 


Example:

         5

      /    \

    3        8

  /   \        \

1      4        11

In-order traversal is [1, 3, 4, 5, 8, 11]

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

Solution:


"""

from typing import List
from leetcode.class0.tree_node import TreeNode, construct_bst


class InOrderTraverse:
    def in_order_recur(self, root, res : List[TreeNode]):
        if root == None:
            return
        else:
            self.in_order_recur(root.left, res)
            res.append(root.val)
            self.in_order_recur(root.right, res)


def test():
    root = construct_bst()
    inorder = InOrderTraverse()  # res = list<TreeNode>{}  # 使用list<TreeNode> 类型，但不必写出来
    res = []
    inorder.in_order_recur(root, res)
    print(res)
    i = 4
    i += 1


if __name__ == '__main__':
    test()
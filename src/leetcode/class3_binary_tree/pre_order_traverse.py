""" Created by daimingzhong on 1/30/18. LeetCode:  

Problem:

         5

      /    \

    3        8

  /   \        \

1      4        11

In-order traversal is [5, 3, 1, 4, 8, 11]

Example:


Solution:


"""
from leetcode.class0.tree_node import construct_bst


class PreOrderTraverse:

    @staticmethod
    def pre_order_traverse(root, res) -> None:
        if not root:
            return
        else:
            res.append(root.val)
            PreOrderTraverse.pre_order_traverse(root.left, res)
            PreOrderTraverse.pre_order_traverse(root.right, res)



def test():
    root = construct_bst()
    res = []
    PreOrderTraverse().pre_order_traverse(root, res)
    PreOrderTraverse.pre_order_traverse(root, res)
    print(res)


if __name__ == '__main__':
    test()

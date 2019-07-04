"""
         5

      /    \

    3        8

  /   \        \

1      4        11
In-order traversal is [1, 3, 4, 5, 8, 11]

"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bst():
    t1 = TreeNode(5)
    t2 = TreeNode(3)
    t3 = TreeNode(8)
    t4 = TreeNode(1)
    t5 = TreeNode(4)
    t7 = TreeNode(11)

    t1.left, t1.right = t2, t3
    t2.left, t2.right = t4, t5
    t3.left, t3.right = None, t7

    root = t1
    return root

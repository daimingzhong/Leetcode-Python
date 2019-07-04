"""

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Return:

[
   [5,4,11,2],
   [5,8,4,5]
]

"""

from leetcode.class0.tree_node import TreeNode


class PathSumII_113(object):
    def pathSum(self, root, sum):
        ans = []
        self.pathSumDFS(root, sum, ans, [])
        return ans

    def pathSumDFS(self, node, Sum, ans, rec):
        if node != None:
            Sum -= node.val
            rec.append(node.val)
            if Sum == 0 and node.right == None and node.left == None:  # if it is leaf
                ans.append(list(rec))

            print("ans", ans)
            self.pathSumDFS(node.left, Sum, ans, rec)
            self.pathSumDFS(node.right, Sum, ans, rec)
            rec.pop()


if __name__ == "__main__":
    t1 = TreeNode(5)
    t2 = TreeNode(4)
    t3 = TreeNode(8)
    t4 = TreeNode(11)
    t5 = TreeNode(13)
    t6 = TreeNode(4)
    t7 = TreeNode(7)
    t8 = TreeNode(2)
    t9 = TreeNode(5)
    t10 = TreeNode(1)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t3.left = t5
    t3.right = t6

    t4.left = t7
    t4.right = t8
    t6.left = t9
    t6.right = t10

    sol = PathSumII_113()
    sol.pathSum(t1, 22)

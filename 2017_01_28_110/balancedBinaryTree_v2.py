# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.checkBalance(root) != -1

    def checkBalance(self, node):
        if node == None:
            return 0
        left = self.checkBalance(node.left)
        right = self.checkBalance(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        return 1 + max(left, right)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.robHelper(root)[1]
    def robHelper(self, node):
        if not node:
            return (0,0)
        leftSub = self.robHelper(node.left)
        rightSub = self.robHelper(node.right)
        return (leftSub[1]+rightSub[1], max(leftSub[1]+rightSub[1], node.val+leftSub[0]+rightSub[0]))

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        # (currentNode, currentSum, currentRstList)
        rst = []
        queue = [(root, root.val, [root.val])]
        while queue:
            curNode, curSum, curRstList = queue.pop(0)
            if not curNode.left and not curNode.right and curSum == sum:
                rst.append(curRstList)
            if curNode.left:
                queue.append((curNode.left, curSum+curNode.left.val, curRstList+[curNode.left.val]))
            if curNode.right:
                queue.append((curNode.right, curSum+curNode.right.val, curRstList+[curNode.right.val]))
        return rst

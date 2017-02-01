# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        rst = []
        self.helper(root, sum, [], rst)
        return rst

    def helper(self, node, target, templist, rst):
        if node.val == target and not node.left and not node.right:
            templist.append(node.val)
            rst.append(templist)
        if node.left:
            self.helper(node.left, target-node.val, templist+[node.val], rst)
        if node.right:
            self.helper(node.right, target-node.val, templist+[node.val], rst)

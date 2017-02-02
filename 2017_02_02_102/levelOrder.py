# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []

        def helper(node, levelNo):
            if node:
                if levelNo == len(rst):
                   rst.append([node.val])
                else:
                    rst[levelNo].append(node.val)
                helper(node.left, levelNo+1)
                helper(node.right, levelNo+1)

        helper(root,0)
        return rst

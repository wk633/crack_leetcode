class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def addLeft(node, addable):
            if node == None:
                return 0
            if node.left == None and node.right == None and addable:
                return node.val
            return addLeft(node.left, True) + addLeft(node.right, False)

        return addLeft(root, False)

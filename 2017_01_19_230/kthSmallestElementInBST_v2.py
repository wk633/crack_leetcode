class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.vals = []
        self.inorder(root)
        return self.vals[k-1]

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            self.vals.append(root.val)
            self.inorder(root.right)

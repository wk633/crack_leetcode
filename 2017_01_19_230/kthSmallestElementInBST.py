class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root == None:
            return 0
        leftNum = 1 + self.calcNode(root.left)

        if leftNum == k:
            return root.val
        elif leftNum > k:
            return self.kthSmallest(root.left, k)
        else:
            return self.kthSmallest(root.right, k - leftNum)
    def calcNode(self, root):
        if root == None:
            return 0
        left,right = self.calcNode(root.left), self.calcNode(root.right)
        return 1+left+right

# recursive version
class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        if root.val == sum and not root.left and not root.right:
            return [[root.val]]
        tmplist = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val]+item for item in tmplist]

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def collect(node, depth):
            if node:
                if depth == len(vals):
                    vals.append(node.val)
                collect(node.right, depth+1)
                collect(node.left, depth+1)

        vals = []
        collect(root, 0)
        return vals

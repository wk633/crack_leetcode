# using deque to rebuild tree
#
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        vals = []
        def preorder(root):
            if root:
                vals.append(root.val)
                preorder(root.left)
                preorder(root.right)
        preorder(root)
        return " ".join(map(str, vals))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        vals = collections.deque(map(int, data.split()))
        def build(minVal, maxVal):
            if vals and minVal < vals[0] < maxVal:
                val0 = vals.popleft()
                root = TreeNode(val0)
                root.left = build(minVal, val0)
                root.right = build(val0,maxVal)
                return root

        return build(float("-infinity"), float("infinity"))

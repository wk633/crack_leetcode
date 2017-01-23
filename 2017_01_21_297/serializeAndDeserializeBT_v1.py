class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                vals.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                vals.append("#")
        vals = []
        preorder(root)
        return " ".join(vals)


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def dePreorder():
            val = vals.pop(0)
            if val == "#":
                return None
            root = TreeNode(val)
            root.left = dePreorder()
            root.right = dePreorder()
            return root
        print data
        vals = data.split()
        return dePreorder()



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

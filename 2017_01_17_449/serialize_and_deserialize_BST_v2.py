class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(root):
            if root:
                vals.append(root.val)
                preorder(root.left)
                preorder(root.right)
        vals = []
        preorder(root)
        return " ".join(map(str, vals))


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dataList = list(map(int, data.split()))
        inorder = sorted(dataList)
        return self.buildTree(dataList, inorder)

    def buildTree(self, preorder, inorder):
        if inorder:
            idx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[idx])
            root.left = self.buildTree(preorder, inorder[:idx])
            root.right = self.buildTree(preorder, inorder[idx+1:])
            return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

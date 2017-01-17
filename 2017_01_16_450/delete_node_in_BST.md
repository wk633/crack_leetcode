Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).

Example:
```
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7
```

### 背景
BST: binary search trees, keep keys in sorted order

### 思路
首先需要一个帮助函数用于查找树中值最小的节点

deleteNode函数 同时完成查找和删除两个任务，返回值是一个树
如果key < root.val, 那个root.left = deleteNode(root.left, key)
如果key > root.val, 那个root.right = deleteNode(root.right, key)
找到时 key = root.val后进行这样的操作：
  如果 root.left 为空，返回root.right (不需要判断right是否为空，因为即使为空，返回的值也是对的)
  如果 root.right为空，返回root.left
  如果 均不为空，查找节点的右子树中最小的值，并赋给节点，然后对节点的的右子树调用deleteNode函数，要删除的key变为刚才找到的最小值

有价值的参考： http://www.algolist.net/Data_structures/Binary_search_tree/Removal

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

### idea:
calcNode function just to calc the numbers of nodes in the left subtree plus the node itself, denoted as n
if n == k, this node is the kth smallest node
if n > k, the kth smallest node must in the left subtree,
if n < k, so the kth smallest must be found in the right subtree

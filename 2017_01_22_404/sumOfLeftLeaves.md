Find the sum of all left leaves in a given binary tree.

Example:
```
    3
   / \
  9  20
    /  \
   15   7
```
There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.

### solutions
use a flag to determine whether this node is addable.
If a node is addable, it should be a left subtree and it should not have childrens.

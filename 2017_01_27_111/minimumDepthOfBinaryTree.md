recursive solution

if node is none, return 0
if don't have left subtree and have right subtree, go to find the minimum depth of right subtree
if don't have right subtree and have left subtree, vice versa.
else
return 1 + min(leftSubTree minimum depth, rightSubTree minimum depth)

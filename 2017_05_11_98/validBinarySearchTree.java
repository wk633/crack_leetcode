/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public boolean isValidBST(TreeNode root) {
        return checkValid(root, null, null);
        
    }
    public boolean checkValid(TreeNode root, Integer min, Integer max){
        if(root == null){
            return true;
        }
        return (min == null || min < root.val) && (max == null || max > root.val) && checkValid(root.left, min, root.val) && checkValid(root.right, root.val, max);
        
    }
}
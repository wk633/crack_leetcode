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
    private int preIndex = 0;
    
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        return buildHelper(preorder, inorder, 0, preorder.length - 1);
    }
    
    private TreeNode buildHelper(int[] preorder, int[] inorder, int inStart, int inEnd){
        if(inStart > inEnd){
            return null;
        }
        
        TreeNode t = new TreeNode(preorder[preIndex]);
        preIndex++;
        
        if(inStart == inEnd){
            return t;
        }
        
        int inIndex = searchIdx(inorder, inStart, inEnd, preorder[preIndex-1]); // bad practice
        
        t.left = buildHelper(preorder, inorder, inStart, inIndex-1);
        t.right = buildHelper(preorder, inorder, inIndex+1, inEnd);
        return t;
    }
    
    private int searchIdx(int[] inorder, int start, int end, int target){
        int i;
        for(i = start; i <= end; i++){
            if(inorder[i] == target){
                return i;
            }
        }
        return i;
    }
}
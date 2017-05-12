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
    private int postIdx;
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        postIdx = postorder.length-1;
        
        return buildHelper(inorder, postorder, 0, inorder.length-1);
    }
    private TreeNode buildHelper(int[] inorder, int[] postorder, int inStart, int inEnd){
        if(postIdx < 0 || inStart > inEnd){
            return null;
        }
        
        TreeNode t = new TreeNode(postorder[postIdx]);
        postIdx -= 1;
        
        int idx;
        for(idx = inStart; idx <= inEnd; idx++){
            if(inorder[idx] == t.val){
                break;
            }
        }
    
        t.right = buildHelper(inorder, postorder, idx+1, inEnd);
        t.left = buildHelper(inorder, postorder, inStart, idx-1);
        
        return t;
    }
}
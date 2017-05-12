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
    
    public List<TreeNode> generateTrees(int n) {
        
        return n > 0 ? buildHelper(1, n) : new ArrayList<TreeNode>();
    }
    public List<TreeNode> buildHelper(int start, int end){
        List<TreeNode> result = new ArrayList<TreeNode>();
        
        if(start > end){
            result.add(null);
            return result;
        }
        
        for(int i = start; i <= end; i++){
            List<TreeNode> left = buildHelper(start, i-1);
            List<TreeNode> right = buildHelper(i+1, end);
            for(TreeNode l : left){
                for(TreeNode r : right){
                    TreeNode t = new TreeNode(i);
                    t.left = l;
                    t.right = r;
                    result.add(t);
                }
            }
        }
        
        return result;
    }
}
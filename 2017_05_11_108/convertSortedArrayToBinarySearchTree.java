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
    public TreeNode sortedArrayToBST(int[] nums) {
        return buildHelper(nums, 0, nums.length-1);
    }
    private TreeNode buildHelper(int[] nums, int startIdx, int endIdx){
        if(endIdx < startIdx){
            return null;
        }
        int idx = (startIdx+endIdx) / 2;
        TreeNode t = new TreeNode(nums[idx]);
        t.left = buildHelper(nums, startIdx, idx-1);
        t.right = buildHelper(nums, idx+1, endIdx);
        return t;
    }
}
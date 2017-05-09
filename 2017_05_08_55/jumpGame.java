public class Solution {
    public boolean canJump(int[] nums) {
        int currentFurthest = 0;
        for(int i = 0, length = nums.length; i< length; i++){
            if(currentFurthest < i){
                return false;
            }
            currentFurthest = Math.max(currentFurthest, i+nums[i]);
        }
        return true;
    }
}
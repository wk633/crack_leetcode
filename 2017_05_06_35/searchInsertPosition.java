public class Solution {
    public int searchInsert(int[] nums, int target) {
        if(nums.length == 0){
            return 0;
        }
        if(nums.length ==1){
            if(nums[0] >= target){
                return 0;
            }else{
                return 1;
            }
        }
        int low = 0;
        int high = nums.length-1;
        while(low < high){
            int mid = (low+high)/2;
            if(nums[mid] == target){
                return mid;
            }else if(nums[mid] < target){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return target>nums[low]?low+1:low;
    }
}
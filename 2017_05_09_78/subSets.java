public class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        
        if(nums.length == 0){
            return result;
        }
        
        Arrays.sort(nums);
        subSetsHelper(nums, 0, new ArrayList<Integer>(), result);
        return result;
    }
    public void subSetsHelper(int[] nums, int startIdx, List<Integer> list, List<List<Integer>> result){
        result.add(new ArrayList<Integer>(list));
        for(int i = startIdx; i < nums.length; i++){
            list.add(nums[i]);
            subSetsHelper(nums, i+1, list, result);
            list.remove(list.size() - 1);
        }
    }

}

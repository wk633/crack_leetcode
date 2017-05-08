public class Solution {
    public int maxArea(int[] height) {
        int startIdx = 0, endIdx = height.length-1;
        int maxArea = 0;
        while(startIdx < endIdx){
            maxArea = Math.max(maxArea, (endIdx-startIdx)*Math.min(height[startIdx], height[endIdx]));
            if(height[startIdx] > height[endIdx]){
                endIdx--;
            }else{
                startIdx++;
            }
        }
        return maxArea;
    }
}
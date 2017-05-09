public class Solution {
    public int maxProfit(int[] prices) {
        int total = 0;
        for(int i = 0, length = prices.length-1; i < length; i++){
            if(prices[i+1] - prices[i] > 0) {
                total += prices[i+1] - prices[i];
            }
        }
        return total;
    }
}
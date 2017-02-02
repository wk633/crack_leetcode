class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        result = len(nums)+1
        leftIdx = 0
        for rightIdx, num in enumerate(nums):
            total += num
            while total >= s:
                result = min(result, rightIdx-leftIdx+1)
                total -= nums[leftIdx]
                leftIdx += 1
        if result <= len(nums):
            return result
        else:
            return 0

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            return [nums]
        uniqueSet = set(nums)
        for uni in uniqueSet:
            idx = nums.index(uni)
            for item in self.permuteUnique(nums[:idx] + nums[idx+1:]):
                result.append([uni] + item)
        return result

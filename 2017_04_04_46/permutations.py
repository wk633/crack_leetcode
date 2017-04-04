class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) == 1:
            return [nums]
        for i in range(len(nums)):
            for item in self.permute(nums[:i]+nums[i+1:]):
                result.append([nums[i]] + item)
        return result
